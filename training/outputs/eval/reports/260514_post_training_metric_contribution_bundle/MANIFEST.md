# Manifest

来源文档：`training/docs/旅行助手后训练指标贡献补充.md`

## Prompt

| Bundle path | Source path |
| --- | --- |
| `prompt/Prompt消融阶段总结.md` | `training/docs/Prompt消融阶段总结.md` |

## Clean SFT

| Bundle path | Source path |
| --- | --- |
| `clean_sft/base/standard/rule_eval_report.md` | `training/outputs/eval/by_model/base_qwen25_7b/260511_high_end_context_standard_w10/rule_eval_report.md` |
| `clean_sft/base/hard/rule_eval_report.md` | `training/outputs/eval/by_model/base_qwen25_7b/260511_high_end_context_hard_w10/rule_eval_report.md` |
| `clean_sft/main_clean_lr8e5/standard/rule_eval_report.md` | `training/outputs/eval/by_model/sft_qwen25_7b_v3_260509_main_clean_cp2_v2b_valloss_lr8e5/260511_high_end_context_standard_w10/rule_eval_report.md` |
| `clean_sft/main_clean_lr8e5/hard/rule_eval_report.md` | `training/outputs/eval/by_model/sft_qwen25_7b_v3_260509_main_clean_cp2_v2b_valloss_lr8e5/260511_high_end_context_hard_w10/rule_eval_report.md` |

## Public Report Packages

| Bundle path | Source path |
| --- | --- |
| `260511_high_end_context_mainline/` | `training/outputs/eval/reports/260511_high_end_context_mainline/` |
| `260511_usage700_followup_w10/` | `training/outputs/eval/reports/260511_usage700_followup_w10/` |
| `260512_bestofn_replay_extended_w10/` | `training/outputs/eval/reports/260512_bestofn_replay_extended_w10/` |
| `260513_bestofn1200_retry_checkpoints_w10/` | `training/outputs/eval/reports/260513_bestofn1200_retry_checkpoints_w10/` |
| `260513_bestofn1200_vs_600final_w10/` | `training/outputs/eval/reports/260513_bestofn1200_vs_600final_w10/` |

## Usage700 And Patch700

| Bundle path | Source path |
| --- | --- |
| `usage700_patch_comparison/mainline_comparison.*` | `training/outputs/eval/comparisons/260511_usage700_followup_w10/mainline_comparison.*` |
| `usage700_patch_comparison/slice_standard/slice_report.*` | `training/outputs/eval/comparisons/260511_usage700_followup_w10/slice_standard/slice_report.*` |
| `usage700_patch_comparison/slice_hard/slice_report.*` | `training/outputs/eval/comparisons/260511_usage700_followup_w10/slice_hard/slice_report.*` |

## Rerank

| Bundle path | Source path |
| --- | --- |
| `rerank/ckpt104/standard/rule_eval_report.md` | `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_rerank_ckpt104/260513_rerank_ckpt104_standard_w10/rule_eval_report.md` |
| `rerank/ckpt104/hard/rule_eval_report.md` | `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_rerank_ckpt104/260513_rerank_ckpt104_hard_w10/rule_eval_report.md` |
| `rerank/final1200/standard/rule_eval_report.md` | `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_rerank_final1200/260513_rerank_final1200_standard_w10/rule_eval_report.md` |
| `rerank/final1200/hard/rule_eval_report.md` | `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_rerank_final1200/260513_rerank_final1200_hard_w10/rule_eval_report.md` |
| `rerank/old600final/standard/rule_eval_report.md` | `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_rerank_old600final/260513_rerank_old600final_standard_w10/rule_eval_report.md` |
| `rerank/old600final/hard/rule_eval_report.md` | `training/outputs/eval/by_model/sft_qwen25_7b_v3_260513_rerank_old600final/260513_rerank_old600final_hard_w10/rule_eval_report.md` |

## Deliberately Excluded

- `training/outputs/eval/logs/`
- `training/outputs/eval/by_model/**/generations.jsonl`
- `training/outputs/qwen25_7b/`
- 本地草稿目录
