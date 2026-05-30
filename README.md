# TravelMind：个性化旅行规划 Agent

TravelMind 是一个基于 Hello-Agents 框架二次开发的个性化旅行规划智能体系统。系统围绕“用户需求采集 -> 工具与知识检索 -> 个性化行程生成 -> 质量检查与导出”构建，支持出行城市、天数、预算、兴趣偏好、交通方式、同行结构等约束的综合规划。

## 核心功能

- 多轮需求采集：前端以结构化表单和对话式补充要求收集城市、日期、预算、交通、住宿和偏好信息。
- 城市景点 RAG 知识库：`backend/app/rag/city_attractions.json` 保存景点介绍、开放时间、门票价格、推荐游玩时长和交通建议，并在生成前进行召回增强。
- 用户偏好记忆：`backend/app/memory/preference_memory.py` 使用 JSON 文件记录历史偏好、交通方式、住宿选择和已规划城市，后续请求自动召回。
- 天气工具调用：后端通过高德天气接口获取天气快照，并要求 Agent 只使用真实工具返回或明确标注远期天气未知。
- 预算估算：TravelMindContext 注入门票、酒店、餐饮和交通价格提示，最终输出预算分项和总预算。
- 行程合理性检查：后端对 TripPlan schema、天数、日期、天气、预算、餐饮和 POI grounding 做结构化校验。
- Markdown/PDF 行程导出：前端结果页支持图片和 PDF 导出，便于保存和分享行程。
- 简单评估集：`training/eval/travelmind_eval_set.jsonl` 提供预算、偏好、路线和约束维度的基础评估样例。

## 技术栈

- Python + FastAPI
- Vue 3 + Vite + Ant Design Vue
- Hello-Agents / 自定义 Agent 编排
- JSON 轻量 RAG 知识库，可替换为 FAISS / Chroma
- JSON 偏好记忆，可替换为 SQLite
- Qwen / DeepSeek / OpenAI-compatible API
- 高德地图与天气 API
- html2canvas / jsPDF 导出

## 本地运行

后端配置放在 `backend/.env`：

```env
LLM_MODEL_ID=qwen-plus
LLM_API_KEY=your_dashscope_api_key_here
LLM_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
AMAP_API_KEY=your_amap_web_service_api_key_here
```

启动后端：

```powershell
cd E:\agent\travelmind-agent
.\.venv\Scripts\python.exe backend\run.py
```

启动前端：

```powershell
cd E:\agent\travelmind-agent\frontend
npm run dev
```

访问：

- 前端: http://localhost:5173
- API 文档: http://localhost:7000/docs

## 简历描述

基于 Hello-Agents 框架二次开发 TravelMind 个性化旅行规划 Agent，支持多轮对话式需求采集，整合城市景点 RAG 知识库、用户偏好记忆、天气查询、预算估算和路线合理性检查工具，能够根据城市、天数、预算、兴趣偏好和交通方式生成可执行旅行计划。构建轻量评估集，从预算满足率、偏好匹配度、路线合理性和约束违反率等维度评估 Agent 生成质量，并支持 PDF 行程导出。


