# Rule Eval Report: sft_1000_teacher_reference_quality

- records: 1000
- generations: `training/outputs/eval/sft_1000_teacher_reference_quality/generations.jsonl`
- records_path: `training/data/planner/sft/records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 1000 | 1000 | 100.00% |
| attraction_budget_consistent | 1000 | 1000 | 100.00% |
| attraction_budget_party_relation_ok | 1000 | 1000 | 100.00% |
| attraction_count_ok | 1000 | 1000 | 100.00% |
| attraction_diversity_ok | 994 | 1000 | 99.40% |
| attraction_grounding_ok | 1000 | 1000 | 100.00% |
| attraction_repeat_limit_ok | 994 | 1000 | 99.40% |
| budget_arithmetic_consistent | 1000 | 1000 | 100.00% |
| budget_consistent | 1000 | 1000 | 100.00% |
| budget_level_aligned | 947 | 1000 | 94.70% |
| budget_preference_aligned | 947 | 1000 | 94.70% |
| budget_relationship_ok | 511 | 1000 | 51.10% |
| budget_selection_ok | 947 | 1000 | 94.70% |
| budget_user_constraint_ok | 1000 | 1000 | 100.00% |
| budget_within_user_budget | 1000 | 1000 | 100.00% |
| city_ok | 1000 | 1000 | 100.00% |
| date_range_ok | 1000 | 1000 | 100.00% |
| day_dates_ok | 1000 | 1000 | 100.00% |
| day_index_ok | 1000 | 1000 | 100.00% |
| days_len_ok | 1000 | 1000 | 100.00% |
| dpo_soft_pass | 915 | 1000 | 91.50% |
| dpo_soft_recomputed_budget_pass | 915 | 1000 | 91.50% |
| hard_pass | 997 | 1000 | 99.70% |
| hotel_budget_covers_nights | 1000 | 1000 | 100.00% |
| hotel_budget_relation_ok | 1000 | 1000 | 100.00% |
| hotel_distance_placeholder_ok | 1000 | 1000 | 100.00% |
| hotel_grounding_ok | 1000 | 1000 | 100.00% |
| invalid_hotel_name_ok | 1000 | 1000 | 100.00% |
| json_extract_ok | 1000 | 1000 | 100.00% |
| legacy_hard_pass | 969 | 1000 | 96.90% |
| location_object_ok | 1000 | 1000 | 100.00% |
| meal_budget_consistent | 1000 | 1000 | 100.00% |
| meal_complete | 1000 | 1000 | 100.00% |
| meal_cost_scale_ok | 511 | 1000 | 51.10% |
| meal_diversity_ok | 972 | 1000 | 97.20% |
| meal_grounding_ok | 997 | 1000 | 99.70% |
| meal_lunch_dinner_same_day_ok | 988 | 1000 | 98.80% |
| meal_repeat_limit_ok | 981 | 1000 | 98.10% |
| meal_specific_ok | 1000 | 1000 | 100.00% |
| meal_valid_semantics_ok | 997 | 1000 | 99.70% |
| middle_hotel_ok | 1000 | 1000 | 100.00% |
| recomputed_budget_fit_ok | 947 | 1000 | 94.70% |
| recomputed_budget_hard_ok | 1000 | 1000 | 100.00% |
| recomputed_budget_level_aligned | 947 | 1000 | 94.70% |
| recomputed_budget_preference_aligned | 947 | 1000 | 94.70% |
| recomputed_budget_user_constraint_ok | 1000 | 1000 | 100.00% |
| recomputed_budget_within_user_budget | 1000 | 1000 | 100.00% |
| schema_ok | 1000 | 1000 | 100.00% |
| sft_budget_semantic_hard_pass | 508 | 1000 | 50.80% |
| sft_hard_pass | 997 | 1000 | 99.70% |
| sft_no_budget_sum_hard_pass | 997 | 1000 | 99.70% |
| sft_strict_hard_pass | 997 | 1000 | 99.70% |
| transportation_budget_nonnegative | 1000 | 1000 | 100.00% |
| weather_dates_ok | 1000 | 1000 | 100.00% |
| weather_match | 1000 | 1000 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 0.9994,
    "p50": 1.0,
    "p90": 1.0
  },
  "attraction_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "hotel_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_diversity_unique_rate": {
    "avg": 0.9551,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 0.9997,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 0.9997,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 0.9997,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 567.5916,
    "p50": 500.0,
    "p90": 889.11
  },
  "recomputed_budget_total": {
    "avg": 5021.901,
    "p50": 4020.0,
    "p90": 9948.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 823,
  "budget_relationship_mismatch": 489,
  "meal_cost_scale_too_low": 489,
  "budget_preference_mismatch": 53,
  "meal_repeat_too_many": 19,
  "meal_same_day_lunch_dinner_repeat": 12,
  "attraction_repeat_too_many": 6,
  "meal_invalid_name": 3
}
```

## Failure Examples

### v3_request_000018
- request: 天津 2026-07-05->2026-07-06 days=2 transport=打车 hotel=舒适型酒店 prefs=['老人友好', '夜市夜景', '艺术', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 130, "expected_total_attractions": 390, "reported_total_attractions": 390, "meal_per_person_cost_sum": 336, "expected_total_meals": 1008, "reported_total_meals": 1008, "reported_total_transportation": 400}}]`

### v3_request_000008
- request: 大理 2026-05-10->2026-05-12 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['休闲慢游', '城市地标', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 75, "expected_total_attractions": 150, "reported_total_attractions": 150, "meal_per_person_cost_sum": 407, "expected_total_meals": 814, "reported_total_meals": 814, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 150, "reported_total_attractions": 150, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-05-12", "type": "breakfast", "name": "九孃豌豆粉店", "estimated_cost": 9, "min_expected_cost": 14}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-05-12", "type": "breakfast", "name": "九孃豌豆粉店", "estimated_cost": 9, "min_expected_cost": 14}]}}]`

### v3_request_000007
- request: 成都 2026-05-10->2026-05-12 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 165, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_per_person_cost_sum": 548, "expected_total_meals": 1096, "reported_total_meals": 1096, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 900, "reported_total_hotels": 900, "expected_total_attractions": 330, "reported_total_attractions": 330, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 9, "checked_count": 7, "failure_count": 1, "failures": [{"date": "2026-05-10", "type": "lunch", "name": "纯阳馆鱼香排骨面(吉祥街店)", "estimated_cost": 17, "min_expected_cost": 35}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 9, "checked_count": 7, "failure_count": 1, "failures": [{"date": "2026-05-10", "type": "lunch", "name": "纯阳馆鱼香排骨面(吉祥街店)", "estimated_cost": 17, "min_expected_cost": 35}]}}]`

### v3_request_000015
- request: 南京 2026-04-06->2026-04-07 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 125, "expected_total_attractions": 375, "reported_total_attractions": 375, "meal_per_person_cost_sum": 301, "expected_total_meals": 903, "reported_total_meals": 903, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 500, "reported_total_hotels": 500, "expected_total_attractions": 375, "reported_total_attractions": 375, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 6, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-04-06", "type": "lunch", "name": "刘长兴(鼓楼店)", "estimated_cost": 28, "min_expected_cost": 35}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 3, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 6, "checked_count": 6, "failure_count": 1, "failures": [{"date": "2026-04-06", "type": "lunch", "name": "刘长兴(鼓楼店)", "estimated_cost": 28, "min_expected_cost": 35}]}}]`

### v3_request_000011
- request: 福州 2026-06-20->2026-06-23 days=4 transport=打车 hotel=经济型酒店 prefs=['第一次来', '城市漫步']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 253, "expected_total_attractions": 506, "reported_total_attractions": 506, "meal_per_person_cost_sum": 826, "expected_total_meals": 1652, "reported_total_meals": 1652, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 600, "reported_total_hotels": 600, "expected_total_attractions": 506, "reported_total_attractions": 506, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 12, "failure_count": 1, "failures": [{"date": "2026-06-20", "type": "lunch", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 12, "failure_count": 1, "failures": [{"date": "2026-06-20", "type": "lunch", "name": "后街捞化", "estimated_cost": 27, "min_expected_cost": 35}]}}]`

### v3_request_000014
- request: 成都 2026-06-05->2026-06-06 days=2 transport=打车 hotel=经济型酒店 prefs=['小众展览', '美食', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 115, "expected_total_attractions": 460, "reported_total_attractions": 460, "meal_per_person_cost_sum": 381, "expected_total_meals": 1524, "reported_total_meals": 1524, "reported_total_transportation": 400}}]`

### v3_request_000001
- request: 桂林 2026-09-03->2026-09-05 days=3 transport=公共交通 hotel=高端酒店 prefs=['艺术', '美食', '第一次来', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 415, "expected_total_attractions": 830, "reported_total_attractions": 830, "meal_per_person_cost_sum": 413, "expected_total_meals": 826, "reported_total_meals": 826, "reported_total_transportation": 450}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1500, "reported_total_hotels": 1500, "expected_total_attractions": 830, "reported_total_attractions": 830, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 3, "failures": [{"date": "2026-09-03", "type": "breakfast", "name": "海天肠粉", "estimated_cost": 14, "min_expected_cost": 20}, {"date": "2026-09-04", "type": "breakfast", "name": "秋福米粉(桂林市正阳路步行街店)", "estimated_cost": 10, "min_expected_cost": 20}, {"date": "2026-09-05", "type": "breakfast", "name": "碗碗都市香米粉店(铁西店)", "estimated_cost": 10, "min_expected_cost": 20}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 3, "failures": [{"date": "2026-09-03", "type": "breakfast", "name": "海天肠粉", "estimated_cost": 14, "min_expected_cost": 20}, {"date": "2026-09-04", "type": "breakfast", "name": "秋福米粉(桂林市正阳路步行街店)", "estimated_cost": 10, "min_expected_cost": 20}, {"date": "2026-09-05", "type": "breakfast", "name": "碗碗都市香米粉店(铁西店)", "estimated_cost": 10, "min_expected_cost": 20}]}}]`

### v3_request_000017
- request: 苏州 2026-05-08->2026-05-10 days=3 transport=地铁+步行 hotel=亲子酒店 prefs=['亲子', '历史文化', '休闲慢游', '户外轻徒步']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 220, "expected_total_attractions": 660, "reported_total_attractions": 660, "meal_per_person_cost_sum": 514, "expected_total_meals": 1542, "reported_total_meals": 1542, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 5000, "reported_total_hotels": 5000, "expected_total_attractions": 660, "reported_total_attractions": 660, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 2, "failures": [{"date": "2026-05-09", "type": "breakfast", "name": "秋娟馄饨店", "estimated_cost": 14, "min_expected_cost": 20}, {"date": "2026-05-10", "type": "breakfast", "name": "西园寺素食-面馆", "estimated_cost": 16, "min_expected_cost": 20}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 3, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 9, "checked_count": 9, "failure_count": 2, "failures": [{"date": "2026-05-09", "type": "breakfast", "name": "秋娟馄饨店", "estimated_cost": 14, "min_expected_cost": 20}, {"date": "2026-05-10", "type": "breakfast", "name": "西园寺素食-面馆", "estimated_cost": 16, "min_expected_cost": 20}]}}]`

### v3_request_000006
- request: 南京 2026-07-05->2026-07-08 days=4 transport=打车 hotel=经济型酒店 prefs=['老人友好', '美食', '城市公园', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 200, "expected_total_attractions": 600, "reported_total_attractions": 600, "meal_per_person_cost_sum": 1092, "expected_total_meals": 3276, "reported_total_meals": 3276, "reported_total_transportation": 600}}]`

### v3_request_000005
- request: 广州 2026-07-05->2026-07-07 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['博物馆', '城市公园', '城市地标', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 30, "expected_total_attractions": 60, "reported_total_attractions": 60, "meal_per_person_cost_sum": 450, "expected_total_meals": 900, "reported_total_meals": 900, "reported_total_transportation": 180}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 500, "reported_total_hotels": 500, "expected_total_attractions": 60, "reported_total_attractions": 60, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-07-07", "type": "lunch", "name": "银记肠粉(北京路店)", "estimated_cost": 23, "min_expected_cost": 25}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-07-07", "type": "lunch", "name": "银记肠粉(北京路店)", "estimated_cost": 23, "min_expected_cost": 25}]}}]`

### v3_request_000010
- request: 西安 2026-08-04->2026-08-07 days=4 transport=公共交通 hotel=经济型酒店 prefs=['城市公园', '美食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 319, "expected_total_attractions": 638, "reported_total_attractions": 638, "meal_per_person_cost_sum": 541, "expected_total_meals": 1082, "reported_total_meals": 1082, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 750, "reported_total_hotels": 750, "expected_total_attractions": 638, "reported_total_attractions": 638, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 12, "failure_count": 2, "failures": [{"date": "2026-08-06", "type": "dinner", "name": "马洪小炒泡馍馆", "estimated_cost": 31, "min_expected_cost": 35}, {"date": "2026-08-07", "type": "dinner", "name": "邢老三肉丸糊辣汤腊牛肉夹馍总店", "estimated_cost": 18, "min_expected_cost": 35}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 12, "failure_count": 2, "failures": [{"date": "2026-08-06", "type": "dinner", "name": "马洪小炒泡馍馆", "estimated_cost": 31, "min_expected_cost": 35}, {"date": "2026-08-07", "type": "dinner", "name": "邢老三肉丸糊辣汤腊牛肉夹馍总店", "estimated_cost": 18, "min_expected_cost": 35}]}}]`

### v3_request_000019
- request: 丽江 2026-05-10->2026-05-14 days=5 transport=打车 hotel=经济型酒店 prefs=['亲子', '老人友好', '海滨度假', '美食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 720, "expected_total_attractions": 3600, "reported_total_attractions": 3600, "meal_per_person_cost_sum": 919, "expected_total_meals": 4595, "reported_total_meals": 4595, "reported_total_transportation": 1000}}]`

### v3_request_000004
- request: 张家界 2026-05-10->2026-05-14 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '城市漫步', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 541, "expected_total_attractions": 2164, "reported_total_attractions": 2164, "meal_per_person_cost_sum": 741, "expected_total_meals": 2964, "reported_total_meals": 2964, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 3200, "reported_total_hotels": 3200, "expected_total_attractions": 2164, "reported_total_attractions": 2164, "meal_scale_eval": {"ok": false, "party_total": 4, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 15, "checked_count": 15, "failure_count": 2, "failures": [{"date": "2026-05-14", "type": "breakfast", "name": "家旺小吃(解放路店)", "estimated_cost": 13, "min_expected_cost": 14}, {"date": "2026-05-14", "type": "lunch", "name": "肯德基(张家界回龙路店)", "estimated_cost": 26, "min_expected_cost": 35}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 4, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 15, "checked_count": 15, "failure_count": 2, "failures": [{"date": "2026-05-14", "type": "breakfast", "name": "家旺小吃(解放路店)", "estimated_cost": 13, "min_expected_cost": 14}, {"date": "2026-05-14", "type": "lunch", "name": "肯德基(张家界回龙路店)", "estimated_cost": 26, "min_expected_cost": 35}]}}]`

### v3_request_000022
- request: 桂林 2026-04-06->2026-04-09 days=4 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '自然风光', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 484, "expected_total_attractions": 1452, "reported_total_attractions": 1452, "meal_per_person_cost_sum": 488, "expected_total_meals": 1464, "reported_total_meals": 1464, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 1452, "reported_total_attractions": 1452, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 12, "checked_count": 12, "failure_count": 1, "failures": [{"date": "2026-04-08", "type": "dinner", "name": "仁利米粉(施家园店)", "estimated_cost": 13, "min_expected_cost": 25}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 3, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 12, "checked_count": 12, "failure_count": 1, "failures": [{"date": "2026-04-08", "type": "dinner", "name": "仁利米粉(施家园店)", "estimated_cost": 13, "min_expected_cost": 25}]}}]`

### v3_request_000021
- request: 上海 2026-06-20->2026-06-21 days=2 transport=地铁+步行 hotel=经济型酒店 prefs=['老人友好', '休闲慢游', '城市漫步', '主题乐园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 70, "expected_total_attractions": 140, "reported_total_attractions": 140, "meal_per_person_cost_sum": 518, "expected_total_meals": 1036, "reported_total_meals": 1036, "reported_total_transportation": 50}}]`

### v3_request_000003
- request: 西安 2025-05-06->2025-05-10 days=5 transport=打车 hotel=舒适型酒店 prefs=['亲子', '历史文化', '购物商圈']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 399, "expected_total_attractions": 1197, "reported_total_attractions": 1197, "meal_per_person_cost_sum": 922, "expected_total_meals": 2766, "reported_total_meals": 2766, "reported_total_transportation": 2800}}]`

### v3_request_000020
- request: 杭州 2026-06-20->2026-06-23 days=4 transport=地铁+步行 hotel=高端酒店 prefs=['历史文化', '海滨度假']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 80, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_per_person_cost_sum": 649, "expected_total_meals": 1298, "reported_total_meals": 1298, "reported_total_transportation": 200}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 4200, "reported_total_hotels": 4200, "expected_total_attractions": 160, "reported_total_attractions": 160, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 12, "checked_count": 11, "failure_count": 2, "failures": [{"date": "2026-06-23", "type": "lunch", "name": "柳来原味螺蛳粉(枫香路店)", "estimated_cost": 31, "min_expected_cost": 50}, {"date": "2026-06-23", "type": "dinner", "name": "郑阿公顺德鸡煲饭双皮奶(萧山店)", "estimated_cost": 46, "min_expected_cost": 50}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 12, "checked_count": 11, "failure_count": 2, "failures": [{"date": "2026-06-23", "type": "lunch", "name": "柳来原味螺蛳粉(枫香路店)", "estimated_cost": 31, "min_expected_cost": 50}, {"date": "2026-06-23", "type": "dinner", "name": "郑阿公顺德鸡煲饭双皮奶(萧山店)", "estimated_cost": 46, "min_expected_cost": 50}]}}]`

### v3_request_000023
- request: 大理 2026-09-03->2026-09-05 days=3 transport=地铁+步行 hotel=经济型酒店 prefs=['亲子', '博物馆', '休闲慢游', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 195, "expected_total_attractions": 585, "reported_total_attractions": 585, "meal_per_person_cost_sum": 434, "expected_total_meals": 1302, "reported_total_meals": 1302, "reported_total_transportation": 500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 585, "reported_total_attractions": 585, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-09-05", "type": "breakfast", "name": "九孃豌豆粉店", "estimated_cost": 9, "min_expected_cost": 10}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 3, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-09-05", "type": "breakfast", "name": "九孃豌豆粉店", "estimated_cost": 9, "min_expected_cost": 10}]}}]`

### v3_request_000026
- request: 扬州 2026-05-10->2026-05-12 days=3 transport=公共交通 hotel=舒适型酒店 prefs=['美食', '博物馆', '素食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 500, "expected_total_attractions": 1000, "reported_total_attractions": 1000, "meal_per_person_cost_sum": 364, "expected_total_meals": 728, "reported_total_meals": 728, "reported_total_transportation": 300}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 1000, "reported_total_attractions": 1000, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 9, "checked_count": 8, "failure_count": 3, "failures": [{"date": "2026-05-10", "type": "lunch", "name": "扬州大明寺素食坊餐饮发展有限公司", "estimated_cost": 27, "min_expected_cost": 35}, {"date": "2026-05-11", "type": "lunch", "name": "天缘斋清心素食", "estimated_cost": 23, "min_expected_cost": 35}, {"date": "2026-05-12", "type": "dinner", "name": "共和春(甘泉路店)", "estimated_cost": 27, "min_expected_cost": 35}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 9, "checked_count": 8, "failure_count": 3, "failures": [{"date": "2026-05-10", "type": "lunch", "name": "扬州大明寺素食坊餐饮发展有限公司", "estimated_cost": 27, "min_expected_cost": 35}, {"date": "2026-05-11", "type": "lunch", "name": "天缘斋清心素食", "estimated_cost": 23, "min_expected_cost": 35}, {"date": "2026-05-12", "type": "dinner", "name": "共和春(甘泉路店)", "estimated_cost": 27, "min_expected_cost": 35}]}}]`

### v3_request_000030
- request: 三亚 2026-05-10->2026-05-13 days=4 transport=自驾 hotel=亲子酒店 prefs=['亲子', '自然风光', '休闲慢游', '城市公园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 619, "expected_total_attractions": 1857, "reported_total_attractions": 1857, "meal_per_person_cost_sum": 901, "expected_total_meals": 2703, "reported_total_meals": 2703, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 8400, "reported_total_hotels": 8400, "expected_total_attractions": 1857, "reported_total_attractions": 1857, "meal_scale_eval": {"ok": false, "party_total": 3, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 12, "checked_count": 11, "failure_count": 1, "failures": [{"date": "2026-05-10", "type": "lunch", "name": "老善溜肉段东北菜馆(三亚店)", "estimated_cost": 40, "min_expected_cost": 50}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 3, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 12, "checked_count": 11, "failure_count": 1, "failures": [{"date": "2026-05-10", "type": "lunch", "name": "老善溜肉段东北菜馆(三亚店)", "estimated_cost": 40, "min_expected_cost": 50}]}}]`
