# Rule Eval Report: sft_smoke50_legacy_c_budget_supplement_teacher_quality

- records: 22
- generations: `training/outputs/eval/sft_smoke50_legacy_c_budget_supplement_teacher_quality/generations.jsonl`
- records_path: `training/data/planner/sft/smoke50_legacy_c_budget_supplement_records.jsonl`

## Boolean Metrics

| Metric | Pass | Total | Rate |
| --- | ---: | ---: | ---: |
| accommodation_type_ok | 22 | 22 | 100.00% |
| attraction_budget_consistent | 22 | 22 | 100.00% |
| attraction_budget_party_relation_ok | 22 | 22 | 100.00% |
| attraction_count_ok | 22 | 22 | 100.00% |
| attraction_diversity_ok | 22 | 22 | 100.00% |
| attraction_grounding_ok | 22 | 22 | 100.00% |
| attraction_repeat_limit_ok | 22 | 22 | 100.00% |
| budget_arithmetic_consistent | 22 | 22 | 100.00% |
| budget_consistent | 22 | 22 | 100.00% |
| budget_level_aligned | 21 | 22 | 95.45% |
| budget_preference_aligned | 21 | 22 | 95.45% |
| budget_relationship_ok | 11 | 22 | 50.00% |
| budget_selection_ok | 21 | 22 | 95.45% |
| budget_user_constraint_ok | 22 | 22 | 100.00% |
| budget_within_user_budget | 22 | 22 | 100.00% |
| city_ok | 22 | 22 | 100.00% |
| date_range_ok | 22 | 22 | 100.00% |
| day_dates_ok | 22 | 22 | 100.00% |
| day_index_ok | 22 | 22 | 100.00% |
| days_len_ok | 22 | 22 | 100.00% |
| dpo_soft_pass | 20 | 22 | 90.91% |
| dpo_soft_recomputed_budget_pass | 20 | 22 | 90.91% |
| hard_pass | 22 | 22 | 100.00% |
| hotel_budget_covers_nights | 22 | 22 | 100.00% |
| hotel_budget_relation_ok | 22 | 22 | 100.00% |
| hotel_distance_placeholder_ok | 22 | 22 | 100.00% |
| hotel_grounding_ok | 22 | 22 | 100.00% |
| invalid_hotel_name_ok | 22 | 22 | 100.00% |
| json_extract_ok | 22 | 22 | 100.00% |
| legacy_hard_pass | 21 | 22 | 95.45% |
| location_object_ok | 22 | 22 | 100.00% |
| meal_budget_consistent | 22 | 22 | 100.00% |
| meal_complete | 22 | 22 | 100.00% |
| meal_cost_scale_ok | 11 | 22 | 50.00% |
| meal_diversity_ok | 21 | 22 | 95.45% |
| meal_grounding_ok | 22 | 22 | 100.00% |
| meal_lunch_dinner_same_day_ok | 21 | 22 | 95.45% |
| meal_repeat_limit_ok | 22 | 22 | 100.00% |
| meal_specific_ok | 22 | 22 | 100.00% |
| meal_valid_semantics_ok | 22 | 22 | 100.00% |
| middle_hotel_ok | 22 | 22 | 100.00% |
| recomputed_budget_fit_ok | 21 | 22 | 95.45% |
| recomputed_budget_hard_ok | 22 | 22 | 100.00% |
| recomputed_budget_level_aligned | 21 | 22 | 95.45% |
| recomputed_budget_preference_aligned | 21 | 22 | 95.45% |
| recomputed_budget_user_constraint_ok | 22 | 22 | 100.00% |
| recomputed_budget_within_user_budget | 22 | 22 | 100.00% |
| schema_ok | 22 | 22 | 100.00% |
| sft_budget_semantic_hard_pass | 11 | 22 | 50.00% |
| sft_hard_pass | 22 | 22 | 100.00% |
| sft_no_budget_sum_hard_pass | 22 | 22 | 100.00% |
| sft_strict_hard_pass | 22 | 22 | 100.00% |
| transportation_budget_nonnegative | 22 | 22 | 100.00% |
| weather_dates_ok | 22 | 22 | 100.00% |
| weather_match | 22 | 22 | 100.00% |

## Numeric Metrics

```json
{
  "attraction_diversity_unique_rate": {
    "avg": 1.0,
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
    "avg": 0.9695,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_food_pois_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_grounding_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "meal_semantic_valid_rate": {
    "avg": 1.0,
    "p50": 1.0,
    "p90": 1.0
  },
  "recomputed_budget_per_person_day": {
    "avg": 923.06,
    "p50": 764.4,
    "p90": 1580.0
  },
  "recomputed_budget_total": {
    "avg": 12064.1818,
    "p50": 6944.0,
    "p90": 31600.0
  }
}
```

## Failure Types

```json
{
  "meal_budget_inconsistent": 18,
  "budget_relationship_mismatch": 11,
  "meal_cost_scale_too_low": 11,
  "budget_preference_mismatch": 1,
  "meal_same_day_lunch_dinner_repeat": 1
}
```

## Failure Examples

### v3_request_002008
- request: 北京 2026-05-09->2026-05-12 days=4 transport=公共交通 hotel=经济型酒店 prefs=['自然风光', '历史文化', '摄影', '夜市夜景']
- errors: `[{"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 750, "reported_total_hotels": 750, "expected_total_attractions": 140, "reported_total_attractions": 140, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 10, "failure_count": 2, "failures": [{"date": "2026-05-10", "type": "breakfast", "name": "老北京烧饼", "estimated_cost": 8, "min_expected_cost": 14}, {"date": "2026-05-12", "type": "dinner", "name": "牛街洪记小吃店", "estimated_cost": 24, "min_expected_cost": 35}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 1, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 12, "checked_count": 10, "failure_count": 2, "failures": [{"date": "2026-05-10", "type": "breakfast", "name": "老北京烧饼", "estimated_cost": 8, "min_expected_cost": 14}, {"date": "2026-05-12", "type": "dinner", "name": "牛街洪记小吃店", "estimated_cost": 24, "min_expected_cost": 35}]}}]`

### v3_request_002016
- request: 上海 2026-05-08->2026-05-11 days=4 transport=打车 hotel=舒适型酒店 prefs=['亲子', '老人友好', '美食', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 1313, "expected_total_attractions": 6565, "reported_total_attractions": 6565, "meal_per_person_cost_sum": 2216, "expected_total_meals": 11080, "reported_total_meals": 11080, "reported_total_transportation": 1355}}]`

### v3_request_002005
- request: 西安 2025-05-07->2025-05-10 days=4 transport=地铁+步行 hotel=民宿 prefs=['亲子', '自然风光', '休闲慢游', '博物馆']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 257, "expected_total_attractions": 771, "reported_total_attractions": 771, "meal_per_person_cost_sum": 685, "expected_total_meals": 2055, "reported_total_meals": 2055, "reported_total_transportation": 400}}]`

### v3_request_002017
- request: 呼和浩特 2026-05-02->2026-05-05 days=4 transport=自驾 hotel=亲子酒店 prefs=['老人友好', '城市漫步', '历史文化', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 3, "hotel_room_count": 2, "attraction_ticket_sum": 618, "expected_total_attractions": 1854, "reported_total_attractions": 1854, "meal_per_person_cost_sum": 1295, "expected_total_meals": 3885, "reported_total_meals": 3885, "reported_total_transportation": 1800}}]`

### v3_request_002007
- request: 宁波 2026-04-23->2026-04-26 days=4 transport=地铁+步行 hotel=高端酒店 prefs=['亲子', '美食', '休闲慢游']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 366, "expected_total_attractions": 1464, "reported_total_attractions": 1464, "meal_per_person_cost_sum": 1329, "expected_total_meals": 5316, "reported_total_meals": 5316, "reported_total_transportation": 800}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 7200, "reported_total_hotels": 7200, "expected_total_attractions": 1464, "reported_total_attractions": 1464, "meal_scale_eval": {"ok": false, "party_total": 4, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 12, "checked_count": 11, "failure_count": 1, "failures": [{"date": "2026-04-25", "type": "breakfast", "name": "老李蛋饼店(国医双拥小区店)", "estimated_cost": 13, "min_expected_cost": 20}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 4, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 12, "checked_count": 11, "failure_count": 1, "failures": [{"date": "2026-04-25", "type": "breakfast", "name": "老李蛋饼店(国医双拥小区店)", "estimated_cost": 13, "min_expected_cost": 20}]}}]`

### v3_request_002010
- request: 苏州 2026-08-05->2026-08-09 days=5 transport=打车 hotel=亲子酒店 prefs=['亲子', '城市漫步', '第一次来', '摄影']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 315, "expected_total_attractions": 1260, "reported_total_attractions": 1260, "meal_per_person_cost_sum": 1000, "expected_total_meals": 4000, "reported_total_meals": 4000, "reported_total_transportation": 2000}}]`

### v3_request_002002
- request: 北京 2026-09-04->2026-09-06 days=3 transport=自驾 hotel=舒适型酒店 prefs=['亲子', '老人友好', '艺术', '美食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 150, "expected_total_attractions": 600, "reported_total_attractions": 600, "meal_per_person_cost_sum": 711, "expected_total_meals": 2844, "reported_total_meals": 2844, "reported_total_transportation": 1500}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 2000, "reported_total_hotels": 2000, "expected_total_attractions": 600, "reported_total_attractions": 600, "meal_scale_eval": {"ok": false, "party_total": 4, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-09-04", "type": "breakfast", "name": "老北京烧饼", "estimated_cost": 8, "min_expected_cost": 14}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 4, "budget_level": "standard", "per_person_lunch_dinner_floor": 35, "per_person_breakfast_floor": 14, "meal_count": 9, "checked_count": 9, "failure_count": 1, "failures": [{"date": "2026-09-04", "type": "breakfast", "name": "老北京烧饼", "estimated_cost": 8, "min_expected_cost": 14}]}}]`

### v3_request_002014
- request: 宁波 2026-05-02->2026-05-05 days=4 transport=自驾 hotel=高端酒店 prefs=['亲子', '老人友好', '美食', '特色餐厅']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 5, "hotel_room_count": 3, "attraction_ticket_sum": 723, "expected_total_attractions": 3615, "reported_total_attractions": 3615, "meal_per_person_cost_sum": 2899, "expected_total_meals": 14495, "reported_total_meals": 14495, "reported_total_transportation": 21990}}]`

### v3_request_002021
- request: 重庆 2026-05-10->2026-05-12 days=3 transport=公共交通 hotel=经济型酒店 prefs=['美食', '海滨度假']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 320, "expected_total_attractions": 1280, "reported_total_attractions": 1280, "meal_per_person_cost_sum": 328, "expected_total_meals": 1312, "reported_total_meals": 1312, "reported_total_transportation": 240}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 1280, "reported_total_attractions": 1280, "meal_scale_eval": {"ok": false, "party_total": 4, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 9, "checked_count": 8, "failure_count": 3, "failures": [{"date": "2026-05-11", "type": "lunch", "name": "面少侠•特色糊辣壳面•彭水米粉", "estimated_cost": 18, "min_expected_cost": 25}, {"date": "2026-05-12", "type": "breakfast", "name": "熨斗糕老烧饼", "estimated_cost": 5, "min_expected_cost": 10}, {"date": "2026-05-12", "type": "lunch", "name": "麦当劳(龙湖重庆时代天街餐厅)", "estimated_cost": 22, "min_expected_cost": 25}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 4, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 9, "checked_count": 8, "failure_count": 3, "failures": [{"date": "2026-05-11", "type": "lunch", "name": "面少侠•特色糊辣壳面•彭水米粉", "estimated_cost": 18, "min_expected_cost": 25}, {"date": "2026-05-12", "type": "breakfast", "name": "熨斗糕老烧饼", "estimated_cost": 5, "min_expected_cost": 10}, {"date": "2026-05-12", "type": "lunch", "name": "麦当劳(龙湖重庆时代天街餐厅)", "estimated_cost": 22, "min_expected_cost": 25}]}}]`

### v3_request_002027
- request: 广州 2026-04-23->2026-04-27 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '特色餐厅', '休闲慢游', '购物商圈']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1018, "expected_total_attractions": 2036, "reported_total_attractions": 2036, "meal_per_person_cost_sum": 2227, "expected_total_meals": 4454, "reported_total_meals": 4454, "reported_total_transportation": 3000}}]`

### v3_request_002023
- request: 南京 2026-05-01->2026-05-05 days=5 transport=地铁+步行 hotel=舒适型酒店 prefs=['美食', '历史文化', '休闲慢游', '博物馆']
- errors: `[{"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 5000, "reported_total_hotels": 5000, "expected_total_attractions": 280, "reported_total_attractions": 280, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 15, "checked_count": 14, "failure_count": 8, "failures": [{"date": "2026-05-01", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 70}, {"date": "2026-05-01", "type": "dinner", "name": "南京大牌档(1912总统府店)", "estimated_cost": 68, "min_expected_cost": 70}, {"date": "2026-05-02", "type": "breakfast", "name": "许阿姨糕团店(南京总店)", "estimated_cost": 24, "min_expected_cost": 28}, {"date": "2026-05-02", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)", "estimated_cost": 63, "min_expected_cost": 70}, {"date": "2026-05-03", "type": "breakfast", "name": "清真·西北桥头拉面大王(丁家桥店)", "estimated_cost": 27, "min_expected_cost": 28}, {"date": "2026-05-04", "type": "lunch", "name": "刘长兴(鼓楼店)", "estimated_cost": 28, "min_expected_cost": 70}, {"date": "2026-05-05", "type": "breakfast", "name": "夏记早点", "estimated_cost": 15, "min_expected_cost": 28}, {"date": "2026-05-05", "type": "lunch", "name": "李记清真馆(打钉巷店)", "estimated_cost": 26, "min_expected_cost": 70}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 1, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 15, "checked_count": 14, "failure_count": 8, "failures": [{"date": "2026-05-01", "type": "lunch", "name": "小潘记鸭血粉丝汤", "estimated_cost": 34, "min_expected_cost": 70}, {"date": "2026-05-01", "type": "dinner", "name": "南京大牌档(1912总统府店)", "estimated_cost": 68, "min_expected_cost": 70}, {"date": "2026-05-02", "type": "breakfast", "name": "许阿姨糕团店(南京总店)", "estimated_cost": 24, "min_expected_cost": 28}, {"date": "2026-05-02", "type": "lunch", "name": "南京大牌档(中山陵紫金坊店)", "estimated_cost": 63, "min_expected_cost": 70}, {"date": "2026-05-03", "type": "breakfast", "name": "清真·西北桥头拉面大王(丁家桥店)", "estimated_cost": 27, "min_expected_cost": 28}, {"date": "2026-05-04", "type": "lunch", "name": "刘长兴(鼓楼店)", "estimated_cost": 28, "min_expected_cost": 70}, {"date": "2026-05-05", "type": "breakfast", "name": "夏记早点", "estimated_cost": 15, "min_expected_cost": 28}, {"date": "2026-05-05", "type": "lunch", "name": "李记清真馆(打钉巷店)", "estimated_cost": 26, "min_expected_cost": 70}]}}]`

### v3_request_002033
- request: 郑州 2026-06-21->2026-06-24 days=4 transport=公共交通 hotel=经济型酒店 prefs=['小众展览', '美食']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 200, "expected_total_attractions": 400, "reported_total_attractions": 400, "meal_per_person_cost_sum": 654, "expected_total_meals": 1308, "reported_total_meals": 1308, "reported_total_transportation": 200}}]`

### v3_request_002022
- request: 成都 2026-09-04->2026-09-08 days=5 transport=地铁+步行 hotel=民宿 prefs=['美食', '第一次来']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 1160, "expected_total_attractions": 2320, "reported_total_attractions": 2320, "meal_per_person_cost_sum": 1762, "expected_total_meals": 3524, "reported_total_meals": 3524, "reported_total_transportation": 600}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 2320, "reported_total_attractions": 2320, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 15, "checked_count": 15, "failure_count": 1, "failures": [{"date": "2026-09-06", "type": "breakfast", "name": "纯阳馆鱼香排骨面(吉祥街店)", "estimated_cost": 17, "min_expected_cost": 20}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 15, "checked_count": 15, "failure_count": 1, "failures": [{"date": "2026-09-06", "type": "breakfast", "name": "纯阳馆鱼香排骨面(吉祥街店)", "estimated_cost": 17, "min_expected_cost": 20}]}}]`

### v3_request_002036
- request: 丽江 2026-03-08->2026-03-11 days=4 transport=自驾 hotel=亲子酒店 prefs=['美食', '户外轻徒步', '自然风光', '历史文化']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 960, "expected_total_attractions": 1920, "reported_total_attractions": 1920, "meal_per_person_cost_sum": 898, "expected_total_meals": 1796, "reported_total_meals": 1796, "reported_total_transportation": 400}}]`

### v3_request_002035
- request: 张家界 2026-08-05->2026-08-08 days=4 transport=打车 hotel=舒适型酒店 prefs=['美食', '特色餐厅', '休闲慢游', '城市漫步']
- errors: `[{"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 1200, "reported_total_hotels": 1200, "expected_total_attractions": 1164, "reported_total_attractions": 1164, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 12, "checked_count": 11, "failure_count": 3, "failures": [{"date": "2026-08-06", "type": "dinner", "name": "富正毅三下锅(溪布街店)", "estimated_cost": 47, "min_expected_cost": 50}, {"date": "2026-08-07", "type": "lunch", "name": "老媽下饭菜(张家界中天鹭鸶湾一期店)", "estimated_cost": 45, "min_expected_cost": 50}, {"date": "2026-08-08", "type": "breakfast", "name": "家旺小吃(解放路店)", "estimated_cost": 13, "min_expected_cost": 20}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 1, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 12, "checked_count": 11, "failure_count": 3, "failures": [{"date": "2026-08-06", "type": "dinner", "name": "富正毅三下锅(溪布街店)", "estimated_cost": 47, "min_expected_cost": 50}, {"date": "2026-08-07", "type": "lunch", "name": "老媽下饭菜(张家界中天鹭鸶湾一期店)", "estimated_cost": 45, "min_expected_cost": 50}, {"date": "2026-08-08", "type": "breakfast", "name": "家旺小吃(解放路店)", "estimated_cost": 13, "min_expected_cost": 20}]}}]`

### v3_request_002038
- request: 北京 2025-08-10->2025-08-12 days=3 transport=地铁+步行 hotel=舒适型酒店 prefs=['亲子', '美食', '历史文化', '城市公园']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 4, "hotel_room_count": 2, "attraction_ticket_sum": 409, "expected_total_attractions": 1636, "reported_total_attractions": 1636, "meal_per_person_cost_sum": 615, "expected_total_meals": 2460, "reported_total_meals": 2460, "reported_total_transportation": 200}}]`

### v3_request_002029
- request: 桂林 2026-07-06->2026-07-10 days=5 transport=公共交通 hotel=亲子酒店 prefs=['亲子', '老人友好', '历史文化', '自然风光']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 6, "hotel_room_count": 3, "attraction_ticket_sum": 1314, "expected_total_attractions": 7884, "reported_total_attractions": 7884, "meal_per_person_cost_sum": 733, "expected_total_meals": 4398, "reported_total_meals": 4398, "reported_total_transportation": 9030}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 14400, "reported_total_hotels": 14400, "expected_total_attractions": 7884, "reported_total_attractions": 7884, "meal_scale_eval": {"ok": false, "party_total": 6, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 15, "checked_count": 11, "failure_count": 1, "failures": [{"date": "2026-07-06", "type": "breakfast", "name": "鸿日桂林米粉", "estimated_cost": 10, "min_expected_cost": 20}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 6, "budget_level": "comfortable", "per_person_lunch_dinner_floor": 50, "per_person_breakfast_floor": 20, "meal_count": 15, "checked_count": 11, "failure_count": 1, "failures": [{"date": "2026-07-06", "type": "breakfast", "name": "鸿日桂林米粉", "estimated_cost": 10, "min_expected_cost": 20}]}}]`

### v3_request_002039
- request: 扬州 2025-11-08->2025-11-12 days=5 transport=公共交通 hotel=民宿 prefs=['美食', '特色餐厅', '休闲慢游', '小众展览']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 849, "expected_total_attractions": 1698, "reported_total_attractions": 1698, "meal_per_person_cost_sum": 1658, "expected_total_meals": 3316, "reported_total_meals": 3316, "reported_total_transportation": 2586}}]`

### v3_request_002042
- request: 大连 2025-11-08->2025-11-12 days=5 transport=地铁+步行 hotel=经济型酒店 prefs=['城市漫步', '自然风光', '摄影', '城市地标']
- errors: `[{"stage": "rule", "type": "meal_budget_inconsistent", "details": {"party_total": 2, "hotel_room_count": 1, "attraction_ticket_sum": 160, "expected_total_attractions": 320, "reported_total_attractions": 320, "meal_per_person_cost_sum": 770, "expected_total_meals": 1540, "reported_total_meals": 1540, "reported_total_transportation": 150}}, {"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 800, "reported_total_hotels": 800, "expected_total_attractions": 320, "reported_total_attractions": 320, "meal_scale_eval": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 15, "checked_count": 15, "failure_count": 3, "failures": [{"date": "2025-11-08", "type": "lunch", "name": "孟哥焖子(香洲花园酒店商务楼店)", "estimated_cost": 16, "min_expected_cost": 25}, {"date": "2025-11-08", "type": "dinner", "name": "大羊螺蛳粉", "estimated_cost": 24, "min_expected_cost": 25}, {"date": "2025-11-11", "type": "lunch", "name": "水仙拉面馆(水仙街店)", "estimated_cost": 23, "min_expected_cost": 25}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 2, "budget_level": "limited", "per_person_lunch_dinner_floor": 25, "per_person_breakfast_floor": 10, "meal_count": 15, "checked_count": 15, "failure_count": 3, "failures": [{"date": "2025-11-08", "type": "lunch", "name": "孟哥焖子(香洲花园酒店商务楼店)", "estimated_cost": 16, "min_expected_cost": 25}, {"date": "2025-11-08", "type": "dinner", "name": "大羊螺蛳粉", "estimated_cost": 24, "min_expected_cost": 25}, {"date": "2025-11-11", "type": "lunch", "name": "水仙拉面馆(水仙街店)", "estimated_cost": 23, "min_expected_cost": 25}]}}]`

### v3_request_002040
- request: 丽江 2026-05-09->2026-05-13 days=5 transport=公共交通 hotel=高端酒店 prefs=['美食', '特色餐厅', '休闲慢游', '历史文化']
- errors: `[{"stage": "rule", "type": "budget_relationship_mismatch", "details": {"hotel_budget_relation_ok": true, "attraction_budget_party_relation_ok": true, "meal_cost_scale_ok": false, "budget_relationship_ok": false, "expected_total_hotels": 4800, "reported_total_hotels": 4800, "expected_total_attractions": 1609, "reported_total_attractions": 1609, "meal_scale_eval": {"ok": false, "party_total": 1, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 15, "checked_count": 15, "failure_count": 3, "failures": [{"date": "2026-05-09", "type": "lunch", "name": "渣渣米线(古城店)", "estimated_cost": 59, "min_expected_cost": 70}, {"date": "2026-05-12", "type": "lunch", "name": "阿婆情腊排骨火锅(旗舰店)", "estimated_cost": 60, "min_expected_cost": 70}, {"date": "2026-05-13", "type": "dinner", "name": "阿滇饭店", "estimated_cost": 63, "min_expected_cost": 70}]}}}, {"stage": "rule", "type": "meal_cost_scale_too_low", "details": {"ok": false, "party_total": 1, "budget_level": "premium", "per_person_lunch_dinner_floor": 70, "per_person_breakfast_floor": 28, "meal_count": 15, "checked_count": 15, "failure_count": 3, "failures": [{"date": "2026-05-09", "type": "lunch", "name": "渣渣米线(古城店)", "estimated_cost": 59, "min_expected_cost": 70}, {"date": "2026-05-12", "type": "lunch", "name": "阿婆情腊排骨火锅(旗舰店)", "estimated_cost": 60, "min_expected_cost": 70}, {"date": "2026-05-13", "type": "dinner", "name": "阿滇饭店", "estimated_cost": 63, "min_expected_cost": 70}]}}, {"stage": "rule", "type": "budget_preference_mismatch", "details": {"part_sum": 8712, "total": 8712, "diff": 0, "requested_budget": {"available": true, "amount": 9300, "scope": "total", "party_size": 1, "total": 9300, "source": "budget_constraint", "budget_level": "premium", "strictness": "soft"}, "per_person_day": 1742.4, "budget_level": "premium", "strictness": "soft", "budget_fit_policy": {"enabled": true, "budget_level": "premium", "strictness": "soft", "amount": 9300, "target_min_ratio": 0.95, "target_max_ratio": 1.05, "target_min_total": 8800, "target_max_total": 9800, "instruction": "这是一条预算利用型SFT补充样本；soft预算应尽量落在用户总预算的95%-105%之间，不要做成低配省钱方案。", "validation_min_ratio_margin": 0.02, "validation_max_ratio_margin": 0.02}, "arithmetic_consistent": true, "within_user_budget": true, "user_constraint_ok": true, "level_aligned": false, "preference_aligned": false, "hotel_budget": {"available": true, "lodging_nights": 4, "party_total": 1, "room_count": 1, "priced_nights": 4, "expected_min_total_hotels": 4800, "reported_total_hotels": 4800, "diff": 0, "covers_nights": true}, "hotel_budget_covers_nights": true}}]`
