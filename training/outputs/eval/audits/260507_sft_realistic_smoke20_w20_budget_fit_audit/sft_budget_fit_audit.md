# Planner SFT 预算贴合审计

- records: `training/data/planner/sft_realistic_smoke20_w20/records.jsonl`
- audit_rows: `training/outputs/eval/v3_sft_realistic_smoke20_w20_budget_fit_audit/audit_rows.jsonl`
- 样本数：23

## 总览

| 项 | 结果 |
|---|---:|
| 请求预算落在新分档范围 | 100.0% (23) |
| teacher budget 落在请求目标区间 | 87.0% (20) |
| 候选池高配可达请求预算 | 100.0% (23/23) |
| food_pois=0 | 0 |

## 按预算档位

| 档位 | n | amount p50 | teacher p50 | 请求预算OK | teacher预算OK | 候选可达p50 | food_pois=0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable | 4 | 10100 | 9247 | 100.0% (4) | 100.0% (4) | 1.45 | 0 |
| limited | 12 | 2500 | 2185 | 100.0% (12) | 91.7% (11) | 1.34 | 0 |
| premium | 2 | 10450 | 9177 | 100.0% (2) | 50.0% (1) | 1.44 | 0 |
| standard | 5 | 7700 | 7661 | 100.0% (5) | 80.0% (4) | 1.11 | 0 |

## 按档位和约束

| 分组 | n | amount p50 | teacher p50 | 请求预算OK | teacher预算OK | 候选可达p50 | food_pois=0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| comfortable/soft | 4 | 10100 | 9247 | 100.0% (4) | 100.0% (4) | 1.45 | 0 |
| limited/hard | 1 | 2000 | 1656 | 100.0% (1) | 100.0% (1) | 1.58 | 0 |
| limited/none | 1 | 2600 | 1916 | 100.0% (1) | 0.0% (0) | 1.24 | 0 |
| limited/soft | 10 | 2800 | 2626 | 100.0% (10) | 100.0% (10) | 1.34 | 0 |
| premium/none | 1 | 10900 | 10674 | 100.0% (1) | 0.0% (0) | 1.41 | 0 |
| premium/soft | 1 | 10000 | 7681 | 100.0% (1) | 100.0% (1) | 1.48 | 0 |
| standard/soft | 5 | 7700 | 7661 | 100.0% (5) | 80.0% (4) | 1.11 | 0 |

## 优先复查样本

| record_id | level | strict | amount | recommended | teacher_total | request_status | teacher_status | high_ratio | food |
|---|---|---|---:|---:|---:|---|---|---:|---:|
| v3_request_310017 | premium | none | 10900 | 10900-15500 | 10674 | ok | no_budget_policy | 1.41 | 36 |
| v3_request_311019 | standard | soft | 2500 | 2200-2800 | 1427 | ok | below | 2.24 | 24 |
| v3_request_310012 | limited | none | 2600 | 2300-2800 | 1916 | ok | no_budget_policy | 1.24 | 28 |
| v3_request_310008 | comfortable | soft | 18600 | 18600-24900 | 16850 | ok | ok | 1.49 | 37 |
| v3_request_310000 | standard | soft | 13900 | 13900-18000 | 10892 | ok | ok | 1.17 | 33 |
| v3_request_310029 | comfortable | soft | 10900 | 10900-14100 | 9218 | ok | ok | 1.41 | 32 |
| v3_request_310015 | standard | soft | 10800 | 8300-10800 | 8115 | ok | ok | 1.07 | 30 |
| v3_request_310013 | standard | soft | 7700 | 6000-7700 | 7661 | ok | ok | 1.04 | 31 |
| v3_request_310010 | comfortable | soft | 4900 | 3500-4900 | 3426 | ok | ok | 1.33 | 40 |
| v3_request_310001 | limited | soft | 3200 | 3200-4000 | 3104 | ok | ok | 1.48 | 24 |
| v3_request_310005 | limited | soft | 4500 | 3600-4500 | 4542 | ok | ok | 1.35 | 27 |
| v3_request_310014 | limited | soft | 3300 | 3300-3900 | 3132 | ok | ok | 1.14 | 27 |
| v3_request_310022 | limited | hard | 2000 | 2000-2300 | 1656 | ok | ok | 1.58 | 26 |
| v3_request_310027 | limited | soft | 1500 | 1500-2000 | 1450 | ok | ok | 1.79 | 25 |
| v3_request_311034 | limited | soft | 2400 | 2400-2900 | 2324 | ok | ok | 2.30 | 25 |
| v3_request_310033 | limited | soft | 2200 | 2200-2500 | 2047 | ok | ok | 1.61 | 28 |
| v3_request_310016 | comfortable | soft | 9300 | 8000-10700 | 9276 | ok | ok | 2.07 | 40 |
| v3_request_310011 | limited | soft | 1500 | 1400-1700 | 1196 | ok | ok | 1.33 | 26 |
| v3_request_310009 | limited | soft | 5900 | 5200-6500 | 5892 | ok | ok | 1.24 | 23 |
| v3_request_310021 | premium | soft | 10000 | 8300-11700 | 7681 | ok | ok | 1.47 | 40 |
| v3_request_310023 | limited | soft | 1800 | 1700-1900 | 1572 | ok | ok | 1.22 | 26 |
| v3_request_310026 | limited | soft | 3600 | 3200-4000 | 2929 | ok | ok | 1.16 | 28 |
| v3_request_310024 | standard | soft | 2100 | 1900-2400 | 1361 | ok | ok | 1.11 | 23 |

## 解释

- `请求预算OK`：用户预算金额是否落在新预算表按人数、天数、住宿、城市推导出的推荐区间内。
- `teacher预算OK`：SFT teacher 的 `trip_plan.budget.total` 是否落在该请求的 `budget_fit_policy` 目标区间内。
- `候选可达p50`：当前候选池粗估高配预算 / 用户预算；低于 1 表示候选供给可能不足。
