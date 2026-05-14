# 260514 后训练指标贡献报告包

这个目录把 `training/docs/旅行助手后训练指标贡献补充.md` 里提到的主要评估版本集中到一个 GitHub 友好的报告包里。

收录边界：只放 Markdown 报告和小体积指标 JSON；不放 `generations.jsonl`、服务日志、训练 checkpoint、完整训练目录和本地草稿内容。

## 怎么看

| 补充文档段落 | 对应报告 |
| --- | --- |
| Prompt 阶段：餐饮槽位、上下文、预算 prompt、self-check、A/C/D 消融 | `prompt/Prompt消融阶段总结.md` |
| Clean SFT：base vs main-clean lr8e-5 | `clean_sft/base/`、`clean_sft/main_clean_lr8e5/` |
| 高端 POI 上下文主线 | `260511_high_end_context_mainline/` |
| usage700 replay 与 patch700-only | `usage700_patch_comparison/mainline_comparison.md`、`260511_usage700_followup_w10/` |
| Best-of-N 600 replay | `260512_bestofn_replay_extended_w10/` |
| Best-of-N 1200 retry checkpoint | `260513_bestofn1200_retry_checkpoints_w10/` |
| Best-of-N 1200 vs old600final | `260513_bestofn1200_vs_600final_w10/` |
| rerank：ckpt104、final1200、old600final | `rerank/` |

## 版本覆盖

- Prompt 消融：`harder_w8`、`no_route_w8`、`food_bucket_no_route`、`food_bucket_return_dinner`、`hard_full`、`hard_compact`、`hard_topk`、`balanced_compact`、`budget_fewshot`、`budget_symbolic`、`budget_ledger`、`meal_rotation_symbolic`、`self_check_300`、`A_C` 等。
- SFT 主线：`base`、`main_clean_lr8e5`、`usage700 replay`、`patch700-only`、`Best-of-N 600 final`、`Best-of-N 1200 ckpt52/ckpt104/ckpt156/final`。
- 推理时选择：`ckpt104 + rerank`、`final1200 + rerank`、`old600final + rerank`。

## 目录说明

- `clean_sft/`：从 `by_model` 中复制的 base 与 main-clean lr8e-5 standard/hard 规则评估 Markdown。
- `usage700_patch_comparison/`：从 comparison 目录复制的 usage700 replay 与 patch700-only 横向对比，含 standard/hard 切片。
- `rerank/`：从 `by_model` 中复制的三条 rerank 主线 standard/hard 规则评估 Markdown。
- 其他 `2605xx_*` 目录：已有公开报告包的集中副本。

更完整的来源路径见 `MANIFEST.md`。
