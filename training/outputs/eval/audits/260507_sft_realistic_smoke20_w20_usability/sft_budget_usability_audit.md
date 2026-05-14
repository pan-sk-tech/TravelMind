# Planner SFT 预算可用性审计

- audit_rows: `training/outputs/eval/v3_sft_realistic_smoke20_w20_budget_fit_audit/audit_rows.jsonl`
- 样本数：23

## 结论总览

| 类别 | 含义 | 数量 | 建议 |
|---|---|---:|---|
| usable_budget_clean | 预算主集可用 | 87.0% (20) | 直接进入预算主训练子集。 |
| usable_budget_candidate_tight | 预算可用但候选偏紧 | 0.0% (0) | 可进预算控制子集，不建议用于训练“用足预算/高品质”。 |
| repair_request_rebudget | 需重标请求预算 | 0.0% (0) | 重标 amount/free_text/budget_fit_policy 后再考虑。 |
| repair_teacher_regen | 需重生成 teacher | 4.3% (1) | 保留请求和上下文，重生成 teacher。 |
| nonbudget_only | 仅适合非预算 SFT | 8.7% (2) | 只做非预算 schema/grounding 训练。 |
| drop_or_full_regen | 预算训练淘汰或整条重做 | 0.0% (0) | 预算训练淘汰；需要时整条重做。 |

## 按预算档位

| 档位 | n | 主集可用 | 候选偏紧可用 | 需重标请求 | 需重生成teacher | 非预算 | 淘汰/重做 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable | 4 | 100.0% (4) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (0) |
| limited | 12 | 91.7% (11) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 8.3% (1) | 0.0% (0) |
| premium | 2 | 50.0% (1) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 50.0% (1) | 0.0% (0) |
| standard | 5 | 80.0% (4) | 0.0% (0) | 0.0% (0) | 20.0% (1) | 0.0% (0) | 0.0% (0) |

## 按档位和约束

| 分组 | n | 主集可用 | 候选偏紧可用 | 需重标请求 | 需重生成teacher | 非预算 | 淘汰/重做 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable/soft | 4 | 100.0% (4) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (0) |
| limited/hard | 1 | 100.0% (1) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (0) |
| limited/none | 1 | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 100.0% (1) | 0.0% (0) |
| limited/soft | 10 | 100.0% (10) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (0) |
| premium/none | 1 | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 100.0% (1) | 0.0% (0) |
| premium/soft | 1 | 100.0% (1) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (0) | 0.0% (0) |
| standard/soft | 5 | 80.0% (4) | 0.0% (0) | 0.0% (0) | 20.0% (1) | 0.0% (0) | 0.0% (0) |

## 抽查优先级

### 预算主集可用样本示例

| record_id | city | level | strict | amount | recommended | teacher | high_ratio |
|---|---|---|---|---:|---:|---:|---:|
| v3_request_310016 | 北京 | comfortable | soft | 9300 | 8000-10700 | 9276 | 2.07 |
| v3_request_310001 | 黄山 | limited | soft | 3200 | 3200-4000 | 3104 | 1.48 |
| v3_request_310011 | 济南 | limited | soft | 1500 | 1400-1700 | 1196 | 1.33 |
| v3_request_310005 | 丽江 | limited | soft | 4500 | 3600-4500 | 4542 | 1.35 |
| v3_request_310008 | 厦门 | comfortable | soft | 18600 | 18600-24900 | 16850 | 1.49 |
| v3_request_310009 | 青岛 | limited | soft | 5900 | 5200-6500 | 5892 | 1.24 |
| v3_request_310015 | 广州 | standard | soft | 10800 | 8300-10800 | 8115 | 1.07 |
| v3_request_310014 | 大理 | limited | soft | 3300 | 3300-3900 | 3132 | 1.14 |
| v3_request_310021 | 杭州 | premium | soft | 10000 | 8300-11700 | 7681 | 1.47 |
| v3_request_310023 | 济南 | limited | soft | 1800 | 1700-1900 | 1572 | 1.22 |
| v3_request_310022 | 三亚 | limited | hard | 2000 | 2000-2300 | 1656 | 1.58 |
| v3_request_310000 | 广州 | standard | soft | 13900 | 13900-18000 | 10892 | 1.17 |
| v3_request_310026 | 呼和浩特 | limited | soft | 3600 | 3200-4000 | 2929 | 1.16 |
| v3_request_310024 | 福州 | standard | soft | 2100 | 1900-2400 | 1361 | 1.11 |
| v3_request_310010 | 广州 | comfortable | soft | 4900 | 3500-4900 | 3426 | 1.33 |
| v3_request_310013 | 三亚 | standard | soft | 7700 | 6000-7700 | 7661 | 1.04 |
| v3_request_310027 | 西安 | limited | soft | 1500 | 1500-2000 | 1450 | 1.79 |
| v3_request_311034 | 呼和浩特 | limited | soft | 2400 | 2400-2900 | 2324 | 2.30 |
| v3_request_310033 | 上海 | limited | soft | 2200 | 2200-2500 | 2047 | 1.61 |
| v3_request_310029 | 南京 | comfortable | soft | 10900 | 10900-14100 | 9218 | 1.41 |

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
