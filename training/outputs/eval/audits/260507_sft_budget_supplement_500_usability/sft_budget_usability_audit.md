# Planner SFT 预算可用性审计

- audit_rows: `training/outputs/eval/v3_sft_budget_supplement_500_20260507_fit_audit/audit_rows.jsonl`
- 样本数：503

## 结论总览

| 类别 | 含义 | 数量 | 建议 |
|---|---|---:|---|
| usable_budget_clean | 预算主集可用 | 34.6% (174) | 直接进入预算主训练子集。 |
| usable_budget_candidate_tight | 预算可用但候选偏紧 | 0.0% (0) | 可进预算控制子集，不建议用于训练“用足预算/高品质”。 |
| repair_request_rebudget | 需重标请求预算 | 65.4% (329) | 重标 amount/free_text/budget_fit_policy 后再考虑。 |
| repair_teacher_regen | 需重生成 teacher | 0.0% (0) | 保留请求和上下文，重生成 teacher。 |
| nonbudget_only | 仅适合非预算 SFT | 0.0% (0) | 只做非预算 schema/grounding 训练。 |
| drop_or_full_regen | 预算训练淘汰或整条重做 | 0.0% (0) | 预算训练淘汰；需要时整条重做。 |

## 按预算档位

| 档位 | n | 主集可用 | 候选偏紧可用 | 需重标请求 | 需重生成teacher | 非预算 | 淘汰/重做 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable | 264 | 61.4% (162) | 0.0% (0) | 38.6% (102) | 0.0% (0) | 0.0% (0) | 0.0% (0) |
| premium | 239 | 5.0% (12) | 0.0% (0) | 95.0% (227) | 0.0% (0) | 0.0% (0) | 0.0% (0) |

## 按档位和约束

| 分组 | n | 主集可用 | 候选偏紧可用 | 需重标请求 | 需重生成teacher | 非预算 | 淘汰/重做 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable/soft | 264 | 61.4% (162) | 0.0% (0) | 38.6% (102) | 0.0% (0) | 0.0% (0) | 0.0% (0) |
| premium/soft | 239 | 5.0% (12) | 0.0% (0) | 95.0% (227) | 0.0% (0) | 0.0% (0) | 0.0% (0) |

## 抽查优先级

### 预算主集可用样本示例

| record_id | city | level | strict | amount | recommended | teacher | high_ratio |
|---|---|---|---|---:|---:|---:|---:|
| v3_request_010005 | 南京 | comfortable | soft | 11600 | 11200-15000 | 11452 | 1.87 |
| v3_request_010015 | 桂林 | comfortable | soft | 16200 | 14100-18900 | 16049 | 1.19 |
| v3_request_011019 | 贵阳 | comfortable | soft | 14900 | 12400-16900 | 15380 | 1.31 |
| v3_request_009022 | 北京 | comfortable | soft | 13100 | 10400-13800 | 13204 | 1.38 |
| v3_request_009024 | 北京 | comfortable | soft | 7000 | 5500-7600 | 6894 | 1.71 |
| v3_request_009030 | 北京 | premium | soft | 12400 | 12400-17600 | 12028 | 2.03 |
| v3_request_009031 | 丽江 | comfortable | soft | 12800 | 11100-14900 | 13220 | 1.23 |
| v3_request_009038 | 哈尔滨 | comfortable | soft | 8700 | 8600-11400 | 8735 | 1.18 |
| v3_request_010043 | 宁波 | comfortable | soft | 14100 | 12800-16300 | 14100 | 1.33 |
| v3_request_010056 | 南京 | comfortable | soft | 9400 | 6900-9400 | 9286 | 1.35 |
| v3_request_010060 | 郑州 | comfortable | soft | 4800 | 4600-5700 | 4603 | 1.63 |
| v3_request_010071 | 南京 | comfortable | soft | 15000 | 14800-18600 | 14598 | 1.48 |
| v3_request_011069 | 南京 | comfortable | soft | 7500 | 6900-9400 | 7136 | 1.83 |
| v3_request_010075 | 青岛 | comfortable | soft | 9700 | 8100-10900 | 9272 | 1.38 |
| v3_request_011073 | 北京 | comfortable | soft | 10200 | 10000-13100 | 10605 | 1.93 |
| v3_request_009083 | 福州 | comfortable | soft | 11300 | 10200-13600 | 10959 | 1.24 |
| v3_request_011079 | 上海 | comfortable | soft | 12000 | 9600-13100 | 11842 | 1.57 |
| v3_request_011078 | 济南 | comfortable | soft | 13100 | 12400-16900 | 12748 | 1.83 |
| v3_request_010090 | 杭州 | comfortable | soft | 10800 | 9600-13100 | 10600 | 1.32 |
| v3_request_010092 | 武汉 | comfortable | soft | 15200 | 15200-20000 | 15212 | 1.31 |

### 预算训练优先淘汰/整条重做示例

| record_id | city | level | strict | amount | recommended | teacher | high_ratio |
|---|---|---|---|---:|---:|---:|---:|

## 文件

- `record_classification.jsonl`：每条样本的分类和原因。
- `record_classification.csv`：便于表格筛选的同内容 CSV。
- `*_ids.txt`：按分类输出的 record_id 名单。

## 口径

- `预算主集可用`：请求预算符合新版分档，teacher budget 落在目标区间，候选池高配预算可达请求金额。
- `预算可用但候选偏紧`：请求和 teacher 都合格，但候选池高配估算低于请求金额；适合预算控制，不适合训练用满预算。
- `需重标请求预算`：teacher 能贴合原目标，但 amount/free_text 和新版分档不一致。
- `需重生成 teacher`：请求预算已经合理，但 teacher budget 明显偏低。
