# DPO 分块 Logprob 补丁论证

更新时间：2026-04-29

这份文档说明为什么在 LLaMA-Factory 的 DPO 训练中，把 `logits.log_softmax(-1)` 改成分块计算目标 token log probability 是合理的、等价的，以及它解决了什么显存问题。

## 1. 背景问题

当前旅行规划任务是长上下文 DPO：

```text
模型：Qwen2.5-7B-Instruct
数据：TripPlan 长 prompt + chosen/rejected
cutoff_len: 16384
词表大小：约 152k
训练方式：LoRA + DeepSpeed ZeRO-3
```

即使 `cutoff_len: 16384` 不会截断当前样本，2 卡和 4 卡训练都在第一步 OOM，报错位置一致：

```text
logits.log_softmax(-1)
```

这说明瓶颈不是 LoRA 参数，也不是 optimizer state，而是 DPO 计算 token-level log probability 时 materialize 了巨大的中间张量。

原实现的主要逻辑：

```python
per_token_logps = torch.gather(
    logits.log_softmax(-1),
    dim=2,
    index=labels.unsqueeze(2),
).squeeze(2)
```

其中 `logits` 的形状约为：

```text
[chosen + rejected, seq_len, vocab]
```

在当前场景中粗略是：

```text
batch: 2
seq_len: 接近 16k
vocab: 约 152k
```

一次性计算 `logits.log_softmax(-1)` 会产生 `[2, 16k, 152k]` 级别的全词表 log probability 张量，显存峰值非常高。DeepSpeed ZeRO-3 能切参数、梯度、优化器状态，但不会自动把这个局部 logits/logsoftmax 中间张量切开。

## 2. 数学等价性

语言模型某个位置目标 token `y_t` 的 log probability 是：

```text
log p(y_t | x) = log softmax(logits)_y_t
```

展开 softmax：

```text
softmax(logits)_y_t = exp(logit_y_t) / sum_j exp(logit_j)
```

取 log：

```text
log p(y_t | x) = logit_y_t - log(sum_j exp(logit_j))
```

也就是：

```text
log p(y_t | x) = selected_logit - logsumexp(logits)
```

因此，这两种写法在数学上等价：

```python
torch.gather(logits.log_softmax(-1), dim=2, index=labels.unsqueeze(2))
```

和：

```python
selected_logits = torch.gather(logits, dim=2, index=labels.unsqueeze(2))
log_normalizers = torch.logsumexp(logits, dim=-1)
selected_logits - log_normalizers
```

区别只在实现方式：

- 原实现会保留全词表每个 token 的 log probability。
- 新实现只计算并保留目标 label 对应的 log probability。

DPO 损失只需要 chosen/rejected response 中目标 token 的 log probability 总和或平均值，不需要保存所有 vocabulary token 的 log probability。因此这个替换不改变 DPO 训练目标。

## 3. 为什么分块能省显存

原实现对整个序列一次性做：

```text
[batch, seq_len, vocab]
```

新实现按 sequence 维度分块，例如每次处理 1024 个 token：

```text
[batch, chunk_size, vocab]
```

粗略对比：

```text
原始峰值：2 * 16k  * 152k
分块峰值：2 * 1024 * 152k
```

在 `chunk_size=1024` 时，logprob 相关中间张量峰值约降到原来的 `1/16`。这会增加循环次数和重算开销，但能明显降低显存峰值。

这种方式的本质是：

```text
用计算时间换显存峰值。
```

对于当前任务，这是合理的，因为我们更需要保留真实 16k 长上下文，而不是为了显存把样本截短到 12k。

## 4. 当前补丁内容

修改文件：

```text
LLaMA-Factory/src/llamafactory/train/trainer_utils.py
LLaMA-Factory/src/llamafactory/train/dpo/trainer.py
```

### `get_batch_logps` 改动

将整块：

```python
logits.log_softmax(-1)
```

改成按 sequence chunk 计算：

```python
selected_logits = torch.gather(chunk_logits, dim=2, index=chunk_labels.unsqueeze(2)).squeeze(2)
log_normalizers = torch.logsumexp(chunk_logits, dim=-1)
chunk_logps = selected_logits - log_normalizers
```

并拼回：

```python
per_token_logps = torch.cat(per_token_logps, dim=1)
```

### 去掉整块 logits fp32 拷贝

原 DPO trainer 会执行：

```python
all_logits = model(...).logits.to(torch.float32)
```

这会复制出一个巨大的 fp32 logits tensor。补丁改为：

```python
all_logits = model(...).logits
```

默认不再整块 upcast。若后续发现数值稳定性问题，可以通过环境变量只在 chunk 内 upcast：

```text
LLAMAFACTORY_LOGPS_UPCAST=1
```

这比对全量 logits `.to(torch.float32)` 更省显存。

## 5. 环境变量

补丁提供三个环境变量：

```text
LLAMAFACTORY_LOGPS_CHUNK_SIZE=1024
LLAMAFACTORY_LOGPS_CHECKPOINT=1
LLAMAFACTORY_LOGPS_UPCAST=0
```

含义：

| 变量 | 默认值 | 作用 |
| --- | --- | --- |
| `LLAMAFACTORY_LOGPS_CHUNK_SIZE` | `1024` | sequence 方向每块 token 数 |
| `LLAMAFACTORY_LOGPS_CHECKPOINT` | `1` | 是否对 chunk logprob 开启 checkpoint 重算 |
| `LLAMAFACTORY_LOGPS_UPCAST` | `0` | 是否在 chunk 内把 logits 转 fp32 |

调参建议：

- 如果仍然 OOM：把 `CHUNK_SIZE` 从 `1024` 降到 `512`。
- 如果训练极慢且显存富余：可以把 `CHUNK_SIZE` 提到 `2048`。
- 如果怀疑 bf16 logsumexp 数值不稳：设置 `UPCAST=1`，但显存会上升。
- 如果速度太慢且显存富余：设置 `CHECKPOINT=0`。

## 6. 已做验证

### 语法验证

已对修改文件执行 Python 编译：

```text
python -m py_compile trainer_utils.py trainer.py
```

结果通过。

### 数值等价验证

用小张量对比原始实现和分块实现：

```text
max_abs_diff = 0.0
length_equal = True
grad_ok = True
```

说明：

- 分块版与原始 `log_softmax + gather` 数值一致。
- valid token length 统计一致。
- 反向传播正常。

### 训练现象验证

未打补丁前：

- 2 卡 DPO 在第一步 `logits.log_softmax(-1)` OOM。
- 4 卡 DPO 仍然在同一位置 OOM。

打补丁后：

- 4 卡 `3,5,6,7` 能进入 `***** Running training *****`。
- 显存仍然贴边，但没有像原实现一样立刻 OOM。
- 第一轮 step 会明显变慢，这是 chunk + checkpoint 用时间换显存的预期结果。

## 7. 风险和限制

### 速度会变慢

分块和 checkpoint 都会增加计算开销。尤其第一步可能很慢，这是预期结果。

### 显存并非无限降低

该补丁主要解决 `logits.log_softmax(-1)` 的峰值显存。模型前向、attention、activation、DeepSpeed 通信缓冲等仍然会占显存。

### bf16 数值精度

默认 `LLAMAFACTORY_LOGPS_UPCAST=0` 是为了最大化省显存。通常 bf16 的 `logsumexp` 可以工作，但如果出现 loss 异常、nan 或训练不稳定，可以改成：

```text
LLAMAFACTORY_LOGPS_UPCAST=1
```

这会牺牲一部分显存。

### 框架升级风险

这是对本地 LLaMA-Factory 源码的 patch。后续如果更新 LLaMA-Factory，需要重新检查该文件是否被覆盖。

## 8. 回滚方案

如果补丁导致训练异常，可以回滚两个文件：

```text
LLaMA-Factory/src/llamafactory/train/trainer_utils.py
LLaMA-Factory/src/llamafactory/train/dpo/trainer.py
```

回滚到原逻辑：

```python
per_token_logps = torch.gather(logits.log_softmax(-1), dim=2, index=labels.unsqueeze(2)).squeeze(2)
```

以及：

```python
all_logits = model(...).logits.to(torch.float32)
```

但回滚后，当前 16k DPO 大概率会重新 OOM。

## 9. 结论

这个补丁是一个等价计算重写：

```text
原始：先算全词表 log_softmax，再 gather 目标 token。
现在：只对目标 token 计算 selected_logit - logsumexp。
```

它不改变 DPO 的数学目标，只降低 logprob 计算时的显存峰值。对于当前长上下文旅行规划 DPO，它比直接截断数据或盲目加卡更符合实验目标。

一句话：

```text
这不是为了“跑通”而改变训练目标，而是把同一个目标用更省显存的方式算出来。
```
