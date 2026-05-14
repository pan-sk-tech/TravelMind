# 后训练产物

这个目录是旅行助手后训练阶段的读者版产物归档，按阶段和实验步骤整理配置、脚本口径和评估报告。入口文档对应 `training/docs/教程/旅行助手后训练实战教程.md` 和 `training/docs/教程/旅行助手后训练指标贡献补充.md`。

收录原则：

- `配置/` 放训练 YAML、serve YAML、评估/数据生成脚本等可复现实验口径。
- `报告/` 放 Markdown 评估报告、摘要 JSON、审计报告和小体积指标文件。
- 不放模型权重、`generations.jsonl`、大训练产物、服务日志和私有草稿。

## 目录

| 目录 | 内容 |
| --- | --- |
| `00_总览/` | 后训练教程、指标贡献补充、SFT 阶段总结、踩坑与经验总结。 |
| `01_Prompt阶段/01_Prompt消融/` | Prompt 消融阶段报告，以及构建/刷新 prompt eval 的脚本口径。 |
| `01_Prompt阶段/02_评测集与指标/` | standard/hard 评估集说明、评测指标、预算口径和评估集构建脚本。 |
| `01_Prompt阶段/03_历史Prompt报告/` | 历史 prompt 报告记录，包括 prompt、context ablation、预算 prompt、A/C/D 消融和 self-check。 |
| `02_SFT阶段/00_数据生成与审计/` | SFT 数据生成、清洗、预算审计、分布审计和目标边界。 |
| `02_SFT阶段/01_Clean_SFT训练/` | clean SFT/main-clean lr6e-5/lr8e-5 配置，base 与 main-clean 评估报告。 |
| `02_SFT阶段/02_Usage700_Replay/` | usage700 replay 配置、serve 配置、by-model 评估和横向对比报告。 |
| `02_SFT阶段/03_Patch700_Only诊断/` | patch700-only 配置、serve 配置、by-model 评估和 usage700/patch700 对比。 |
| `02_SFT阶段/04_Best-of-N_600_Replay/` | Best-of-N 600 replay 训练配置、Best-of-N 数据脚本、ckpt96/ckpt192/final 评估。 |
| `02_SFT阶段/05_Best-of-N_1200_Retry/` | Best-of-N 1200 retry 配置、ckpt52/ckpt104/ckpt156/final 评估与 600 final 对比。 |
| `02_SFT阶段/06_历史SFT主线报告/` | 早期主线 SFT 报告记录，包括 cp2/v2a/v2b、realbudget、main-clean step/final 和 valloss 对比。 |
| `03_Rerank阶段/01_多温度候选Rerank/` | 多温度候选 + 规则 rerank 脚本口径，以及 ckpt104/final1200/old600final 评估。 |

## 使用建议

先读 `00_总览/报告/旅行助手后训练实战教程.md` 和 `00_总览/报告/旅行助手后训练指标贡献补充.md`，再按阶段进入子目录看配置和报告。每个步骤的来源路径见 `清单.md`。

本目录集中整理 prompt 报告记录、主线 SFT 报告记录和最新 rerank 报告；不把无关 archive 全量搬入。
