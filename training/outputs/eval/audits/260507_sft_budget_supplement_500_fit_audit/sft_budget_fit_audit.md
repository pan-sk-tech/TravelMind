# Planner SFT 预算贴合审计

- records: `training/data/planner/sft_budget_supplement_500_20260507/records.jsonl`
- audit_rows: `training/outputs/eval/v3_sft_budget_supplement_500_20260507_fit_audit/audit_rows.jsonl`
- 样本数：503

## 总览

| 项 | 结果 |
|---|---:|
| 请求预算落在新分档范围 | 34.6% (174) |
| teacher budget 落在请求目标区间 | 100.0% (503) |
| 候选池高配可达请求预算 | 100.0% (503/503) |
| food_pois=0 | 0 |

## 按预算档位

| 档位 | n | amount p50 | teacher p50 | 请求预算OK | teacher预算OK | 候选可达p50 | food_pois=0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable | 264 | 11750 | 11540 | 61.4% (162) | 100.0% (264) | 1.43 | 0 |
| premium | 239 | 14400 | 14256 | 5.0% (12) | 100.0% (239) | 1.44 | 0 |

## 按档位和约束

| 分组 | n | amount p50 | teacher p50 | 请求预算OK | teacher预算OK | 候选可达p50 | food_pois=0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable/soft | 264 | 11750 | 11540 | 61.4% (162) | 100.0% (264) | 1.43 | 0 |
| premium/soft | 239 | 14400 | 14256 | 5.0% (12) | 100.0% (239) | 1.44 | 0 |

## 优先复查样本

| record_id | level | strict | amount | recommended | teacher_total | request_status | teacher_status | high_ratio | food |
|---|---|---|---:|---:|---:|---|---|---:|---:|
| v3_request_009319 | premium | soft | 25200 | 41400-58700 | 24466 | below | ok | 1.78 | 39 |
| v3_request_009714 | premium | soft | 20700 | 35600-51400 | 20780 | below | ok | 1.53 | 39 |
| v3_request_009149 | premium | soft | 23500 | 37800-51600 | 24276 | below | ok | 2.22 | 35 |
| v3_request_009374 | premium | soft | 28800 | 42600-57000 | 27400 | below | ok | 1.21 | 39 |
| v3_request_009115 | premium | soft | 32100 | 43000-60300 | 32248 | below | ok | 1.15 | 34 |
| v3_request_010786 | premium | soft | 20300 | 32600-46400 | 21028 | below | ok | 2.73 | 35 |
| v3_request_010547 | premium | soft | 25000 | 36800-50600 | 25918 | below | ok | 1.30 | 39 |
| v3_request_010811 | premium | soft | 24300 | 35800-50100 | 24670 | below | ok | 1.64 | 39 |
| v3_request_009052 | premium | soft | 26000 | 38000-51100 | 24950 | below | ok | 1.38 | 39 |
| v3_request_010831 | premium | soft | 30400 | 41500-55800 | 31585 | below | ok | 1.55 | 40 |
| v3_request_009105 | premium | soft | 27400 | 38900-52000 | 28570 | below | ok | 1.21 | 36 |
| v3_request_010311 | premium | soft | 27400 | 38900-52000 | 27445 | below | ok | 1.38 | 37 |
| v3_request_010468 | premium | soft | 27900 | 38700-51800 | 27060 | below | ok | 1.29 | 35 |
| v3_request_009247 | premium | soft | 27900 | 37600-51400 | 27898 | below | ok | 1.65 | 40 |
| v3_request_011826 | premium | soft | 22800 | 33200-44700 | 23280 | below | ok | 1.77 | 40 |
| v3_request_009823 | premium | soft | 18600 | 28900-40400 | 18940 | below | ok | 2.17 | 37 |
| v3_request_010828 | premium | soft | 13800 | 24400-34700 | 13494 | below | ok | 1.98 | 37 |
| v3_request_011514 | premium | soft | 20600 | 30500-41900 | 21468 | below | ok | 1.59 | 34 |
| v3_request_011001 | premium | soft | 16300 | 26100-37600 | 16892 | below | ok | 2.33 | 40 |
| v3_request_011312 | premium | soft | 16300 | 26100-37600 | 15756 | below | ok | 1.45 | 40 |
| v3_request_010334 | premium | soft | 26400 | 34800-49000 | 26366 | below | ok | 2.12 | 37 |
| v3_request_011141 | premium | soft | 24100 | 32600-46400 | 24100 | below | ok | 2.44 | 36 |
| v3_request_010649 | premium | soft | 24100 | 32600-46400 | 24640 | below | ok | 1.92 | 37 |
| v3_request_010485 | premium | soft | 21800 | 31400-42900 | 21368 | below | ok | 1.66 | 36 |
| v3_request_009285 | premium | soft | 22900 | 32300-43800 | 23302 | below | ok | 1.58 | 40 |
| v3_request_010631 | premium | soft | 20000 | 28800-40700 | 19075 | below | ok | 1.85 | 33 |
| v3_request_010663 | premium | soft | 17300 | 26300-36800 | 16480 | below | ok | 1.17 | 36 |
| v3_request_011218 | premium | soft | 18600 | 27000-38500 | 18588 | below | ok | 1.95 | 40 |
| v3_request_009331 | premium | soft | 24300 | 31800-44900 | 24360 | below | ok | 1.45 | 37 |
| v3_request_011356 | premium | soft | 18000 | 26800-37100 | 18640 | below | ok | 1.75 | 38 |

## 解释

- `请求预算OK`：用户预算金额是否落在新预算表按人数、天数、住宿、城市推导出的推荐区间内。
- `teacher预算OK`：SFT teacher 的 `trip_plan.budget.total` 是否落在该请求的 `budget_fit_policy` 目标区间内。
- `候选可达p50`：当前候选池粗估高配预算 / 用户预算；低于 1 表示候选供给可能不足。
