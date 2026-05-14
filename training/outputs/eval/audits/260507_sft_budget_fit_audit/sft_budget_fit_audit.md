# Planner SFT 预算贴合审计

- records: `training/data/planner/sft/records.jsonl`
- audit_rows: `training/outputs/eval/v3_sft_budget_fit_audit_20260507/audit_rows.jsonl`
- 样本数：1138

## 总览

| 项 | 结果 |
|---|---:|
| 请求预算落在新分档范围 | 36.3% (413) |
| teacher budget 落在请求目标区间 | 69.4% (790) |
| 候选池高配可达请求预算 | 64.8% (737/1138) |
| food_pois=0 | 0 |

## 按预算档位

| 档位 | n | amount p50 | teacher p50 | 请求预算OK | teacher预算OK | 候选可达p50 | food_pois=0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable | 286 | 8800 | 6506 | 47.9% (137) | 47.2% (135) | 0.90 | 0 |
| limited | 265 | 3200 | 2832 | 29.8% (79) | 91.3% (242) | 1.63 | 0 |
| luxury | 11 | 18600 | 7673 | 27.3% (3) | 18.2% (2) | 0.39 | 0 |
| premium | 121 | 13000 | 10922 | 29.8% (36) | 65.3% (79) | 1.16 | 0 |
| standard | 455 | 5500 | 3932 | 34.7% (158) | 73.0% (332) | 1.12 | 0 |

## 按档位和约束

| 分组 | n | amount p50 | teacher p50 | 请求预算OK | teacher预算OK | 候选可达p50 | food_pois=0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable/hard | 12 | 12800 | 8323 | 58.3% (7) | 41.7% (5) | 0.81 | 0 |
| comfortable/none | 18 | 15200 | 6295 | 38.9% (7) | 0.0% (0) | 0.66 | 0 |
| comfortable/soft | 256 | 8550 | 6469 | 48.0% (123) | 50.8% (130) | 0.91 | 0 |
| limited/hard | 52 | 3150 | 2860 | 38.5% (20) | 100.0% (52) | 1.64 | 0 |
| limited/none | 23 | 2900 | 2726 | 21.7% (5) | 0.0% (0) | 1.51 | 0 |
| limited/soft | 190 | 3300 | 2813 | 28.4% (54) | 100.0% (190) | 1.64 | 0 |
| luxury/none | 4 | 20100 | 3502 | 0.0% (0) | 0.0% (0) | 0.35 | 0 |
| luxury/soft | 7 | 16600 | 11912 | 42.9% (3) | 28.6% (2) | 0.45 | 0 |
| premium/hard | 1 | 7700 | 6746 | 100.0% (1) | 100.0% (1) | 1.37 | 0 |
| premium/none | 6 | 9400 | 2646 | 66.7% (4) | 0.0% (0) | 0.81 | 0 |
| premium/soft | 114 | 13650 | 11794 | 27.2% (31) | 68.4% (78) | 1.18 | 0 |
| standard/hard | 24 | 6100 | 4130 | 29.2% (7) | 66.7% (16) | 1.24 | 0 |
| standard/none | 37 | 3400 | 2618 | 27.0% (10) | 0.0% (0) | 1.10 | 0 |
| standard/soft | 394 | 5550 | 4061 | 35.8% (141) | 80.2% (316) | 1.11 | 0 |

## 优先复查样本

| record_id | level | strict | amount | recommended | teacher_total | request_status | teacher_status | high_ratio | food |
|---|---|---|---:|---:|---:|---|---|---:|---:|
| v3_request_000085 | luxury | none | 54700 | 24700-33900 | 13056 | above | no_budget_policy | 0.39 | 24 |
| v3_request_002029 | comfortable | hard | 54500 | 27500-37000 | 35712 | above | below | 0.55 | 38 |
| v3_request_000767 | luxury | none | 21600 | 8400-11900 | 2602 | above | no_budget_policy | 0.25 | 30 |
| v3_request_000921 | luxury | soft | 25700 | 13000-18200 | 18000 | above | below | 0.25 | 32 |
| v3_request_002017 | comfortable | hard | 22600 | 11500-15000 | 14739 | above | below | 0.66 | 38 |
| v3_request_000885 | luxury | none | 18600 | 8300-11400 | 2820 | above | no_budget_policy | 0.31 | 27 |
| v3_request_000515 | comfortable | none | 23700 | 12900-17500 | 6004 | above | no_budget_policy | 0.37 | 30 |
| v3_request_000012 | luxury | soft | 27300 | 17400-23100 | 19398 | above | below | 0.38 | 21 |
| v3_request_000635 | luxury | none | 15200 | 8300-11400 | 4185 | above | no_budget_policy | 0.39 | 25 |
| v3_request_000163 | standard | soft | 18800 | 12000-15400 | 10400 | above | below | 0.58 | 22 |
| v3_request_000905 | standard | soft | 18900 | 12200-15600 | 10544 | above | below | 0.64 | 34 |
| v3_request_000316 | comfortable | soft | 18300 | 11800-15500 | 12086 | above | below | 0.51 | 30 |
| v3_request_000586 | comfortable | soft | 16000 | 9600-13100 | 10450 | above | below | 0.61 | 30 |
| v3_request_000344 | premium | soft | 13000 | 14300-20600 | 9464 | below | below | 0.53 | 30 |
| v3_request_000893 | premium | none | 15800 | 9200-13400 | 2188 | above | no_budget_policy | 0.41 | 38 |
| v3_request_000946 | comfortable | soft | 21100 | 14200-19000 | 13735 | above | below | 0.74 | 27 |
| v3_request_000315 | luxury | soft | 11000 | 5800-7400 | 7673 | above | below | 0.45 | 23 |
| v3_request_000833 | premium | soft | 29600 | 21000-29400 | 20796 | above | below | 0.50 | 37 |
| v3_request_000645 | comfortable | soft | 8300 | 10400-14600 | 5440 | below | below | 0.71 | 22 |
| v3_request_000043 | standard | soft | 16200 | 10600-13600 | 8980 | above | below | 0.66 | 29 |
| v3_request_000226 | comfortable | soft | 8800 | 10900-15000 | 5700 | below | below | 0.74 | 22 |
| v3_request_002010 | comfortable | hard | 26500 | 19200-25500 | 17260 | above | below | 0.95 | 38 |
| v3_request_001066 | comfortable | none | 14400 | 8700-12100 | 3708 | above | no_budget_policy | 0.39 | 23 |
| v3_request_000399 | comfortable | soft | 31800 | 24500-31400 | 21664 | above | below | 0.56 | 29 |
| v3_request_000964 | comfortable | none | 21200 | 14700-19900 | 7220 | above | no_budget_policy | 0.51 | 29 |
| v3_request_001068 | comfortable | soft | 22000 | 15800-20400 | 14620 | above | below | 0.60 | 30 |
| v3_request_000796 | standard | soft | 16000 | 10600-14000 | 9110 | above | below | 0.58 | 25 |
| v3_request_000822 | comfortable | soft | 21000 | 15000-19700 | 13600 | above | below | 0.48 | 31 |
| v3_request_000108 | standard | soft | 19200 | 13800-17600 | 10690 | above | below | 0.74 | 27 |
| v3_request_001046 | comfortable | none | 19400 | 13700-18000 | 9064 | above | no_budget_policy | 0.53 | 39 |

## 解释

- `请求预算OK`：用户预算金额是否落在新预算表按人数、天数、住宿、城市推导出的推荐区间内。
- `teacher预算OK`：SFT teacher 的 `trip_plan.budget.total` 是否落在该请求的 `budget_fit_policy` 目标区间内。
- `候选可达p50`：当前候选池粗估高配预算 / 用户预算；低于 1 表示候选供给可能不足。
