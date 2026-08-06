# 🛠️ 2026-08-06 视觉工业界日报

> 今日扫描了 GitHub Trending · GitHub Search（diffusion / image-generation / multimodal 三组）· HuggingFace Models · HF Daily Papers · Hacker News（Reddit 被 403 拦截，继续用 HN 作备用源）等 6 个渠道

---

## 🔥 热门开源项目

### 1. [HUANGCHIHHUNGLeo/claude-real-video](https://github.com/HUANGCHIHHUNGLeo/claude-real-video)
- **什么**: 让 Claude（或任意 LLM）真正"看"视频 — 从 URL/本地文件做**场景感知抽帧 + 去重 + 字幕转录**，把视频变成带时间轴的图文上下文喂给模型，本地运行，MIT
- **为什么火**: ⭐1,961（6-30 创建，两周涨到近 2k），multimodal 关键词新仓库搜索第一名。痛点非常具体：LLM 读视频最怕"一帧帧全塞"烧 token / "随便抽几帧"丢信息，这个工具用场景切分做智能采样，属于 agent 视频理解的基础设施件
- **CV 关联**: Video Understanding · Keyframe Extraction · Agent 视觉上下文
- **快速上手**: `git clone https://github.com/HUANGCHIHHUNGLeo/claude-real-video`（依赖 ffmpeg + anthropic SDK）

### 2. [nv-tlabs/ardy](https://github.com/nv-tlabs/ardy)
- **什么**: NVIDIA 官方实现 **ARDY: Autoregressive Diffusion with Hybrid Representation**，SIGGRAPH 2026 论文，面向**交互式人体运动生成**
- **为什么火**: ⭐725 / Apache-2.0，NVIDIA Research 出品（nv-tlabs 是业界质量背书）。AR 与 diffusion 的混合表示是 2026 年生成式动画的热点路线：既要自回归的流式可控性，又要 diffusion 的多样性
- **CV 关联**: Human Motion Generation · Autoregressive Diffusion · 数字人/动画
- **快速上手**: `git clone https://github.com/nv-tlabs/ardy && cd ardy && pip install -e .`

### 3. [OpenSenseNova/SenseNova-Vision](https://github.com/OpenSenseNova/SenseNova-Vision)
- **什么**: 商汤开源的 **Vision as Unified Multimodal Generation** — 把检测、分割等传统 CV 任务统一成 MLLM 生成范式，配套 7B MoT 模型 + 50M 语料数据集
- **为什么火**: ⭐573 / Apache-2.0（6-29 发布），arXiv 2607.06560，HF 上有 `sensenova/SenseNova-Vision-7B-MoT` 权重和 demo space。"CV 任务即生成"是继 YOLO 后国产视觉模型重新定义任务边界的代表方向
- **CV 关联**: Unified CV · MLLM for Detection/Segmentation · 通用视觉基座
- **快速上手**: `git clone https://github.com/OpenSenseNova/SenseNova-Vision`；权重 `sensenova/SenseNova-Vision-7B-MoT`

### 4. [magicrew/doc7](https://github.com/magicrew/doc7)
- **什么**: Go 编写的**文档 → AI-ready Markdown** 转换器，核心卖点是用 VLM 做视觉理解（版面、表格、图表都能结构化），而不是纯文本流
- **为什么火**: ⭐456 / MIT，**8-02 创建，4 天涨到 450+**，本周新仓库里涨速最快的文档视觉项目。RAG 管线最缺的正是"把 PDF/扫描件变成 AI 能吃且不丢视觉信息的 Markdown"这一环
- **CV 关联**: Document AI · Layout Understanding · VLM 驱动的结构化
- **快速上手**: `git clone https://github.com/magicrew/doc7 && cd doc7 && go build`

### 5. [Anionex/agent-vision-toolkit](https://github.com/Anionex/agent-vision-toolkit)
- **什么**: 给纯文本 LLM agent 装"眼睛"的视觉工具箱 + skill：图片问答、OCR、截图分析、视觉定位，可无缝接入 Codex / Claude Code / OpenCode
- **为什么火**: ⭐302 / MIT（8-01 创建）。和昨天 browser-use/video-use 同一条主线 — 2026 年 agent 竞争的本质是"谁先获得可靠的视觉感知"，这个项目把视觉能力打包成 agent skill 范式，中文社区热度高
- **CV 关联**: Agent Vision · OCR · Visual Grounding · Screen Understanding
- **快速上手**: `git clone https://github.com/Anionex/agent-vision-toolkit`（按 README 装进 Codex/Claude Code skills）

### 6. [Xingyu-Zheng/MrFlow](https://github.com/Xingyu-Zheng/MrFlow)
- **什么**: **Multi-Resolution Flow Matching** — 通过 staged sampling 实现**训练-free 扩散加速**，不用改权重直接提速
- **为什么火**: ⭐283 / Apache-2.0。扩散推理加速是刚需赛道（LCM、Turbo、蒸馏之外，"训练-free"路线对已有模型零成本），多分辨率阶段采样是 2026 年加速方法里被低估但有效的一支
- **CV 关联**: Diffusion Sampling · Inference Acceleration · Text-to-Image/Video 通用
- **快速上手**: `git clone https://github.com/Xingyu-Zheng/MrFlow`

### 7. [oxbshw/watch-skill](https://github.com/oxbshw/watch-skill)
- **什么**: 面向 AI agent 的**视频理解 + 自验证 skill**：把视频、直播流、agent 录屏变成可检索、带时间戳的证据，再让 agent 基于证据自我校验
- **为什么火**: ⭐258 / MIT（7-05）。录屏→证据→自验证的组合，直接服务于"agent 写完代码自己看回放检查"这类闭环，和 claude-real-video 互补（一个喂给 LLM，一个做 agent 闭环校验）
- **CV 关联**: Video Understanding · Agent Logging · Temporal Grounding
- **快速上手**: `git clone https://github.com/oxbshw/watch-skill`

### 8. [MCG-NJU/TimeLens2](https://github.com/MCG-NJU/TimeLens2)
- **什么**: **TimeLens2: Generalist Video Temporal Grounding with Multimodal LLMs** — 用 MLLM 做通用视频时序定位（"第几秒发生了什么"）
- **为什么火**: ⭐117（7-16 发布），南京大学 MCG 实验室系列续作。视频理解从"能看懂"走向"能定位到秒"，是 RAG-video / agent 视频检索的关键能力
- **CV 关联**: Video Temporal Grounding · MLLM · Video QA
- **快速上手**: `git clone https://github.com/MCG-NJU/TimeLens2`

---

## 🤗 值得关注的新模型

### [MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) — 今日 HF 趋势榜第一
- **类型**: image-text-to-video（omni-modal 生成系统：统一理解 text/image/video/audio，生成**带原生立体声**的视频）
- **热度**: 🔥 HF 全站 trendingScore **2387 排名第一**，❤️2,497；配套 [Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) 工作流节点
- **特色**: 输出 4–15 秒 / 24fps / 32kHz 立体声音频，支持 2K 分辨率（H3-Regenerate-2K）；FL2VA 变体支持首帧+尾帧双图控制；预训练阶段即具备强多模态指令跟随。**同时开源权重 + 上线 API/App（海螺 hailuoai.video）**，是继 H2 之后视频生成开源阵营对闭源 Sora 系的最有力回应
- **可用性**: `minimax-h3-community-license-agreement`（社区协议，商用需以官方条款为准）；权重经 diffusers 加载

### HF 趋势快照（本周已覆盖过的老面孔，趋势仍在）
- [moonshotai/Kimi-K3](https://huggingface.co/moonshotai/Kimi-K3) — 2.78T 多模态 MoE，下载 **113 万** ❤️10,125（7-30 日报已介绍 MLX 移植）
- [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR) — 百度 OCR 模型，下载 **270 万**，MIT（8-03 已介绍）
- [microsoft/Mage-VL](https://huggingface.co/microsoft/Mage-VL) — codec-native 流式多模态，下载 43.6 万（7-29/8-03 已介绍）

---

## 📰 社区热点

### [Meta 投放了含 AI 生成 CSAM 图片的广告](https://news.ycombinator.com/item?id=42401234)（HN）
- 讨论方向: 图像生成模型的安全护栏 vs 平台投放审核的漏洞 — Wired 调查发现 Meta 广告系统投放了 AI 生成的儿童性虐待图像
- 热度: score 245 / 198 条评论。对 CV 从业者的信号: **内容审核（moderation）重新成为图像生成栈的必选项**，Mistral Shieldstral（昨日日报）这类专用审核模型的市场逻辑被进一步验证

### [Painting with Gaussians（用高斯泼溅作画）](https://yogthos.net/posts/2026-08-03-splat-painter.html)（HN）
- 讨论方向: 3D Gaussian Splatting 的创意工具化 — 把 3DGS 当成"会呼吸的画笔"，实时交互式泼溅绘画
- 热度: score 92 / 16 条评论。3DGS 生态从"重建/渲染"向"创作工具"延伸的又一个案例，配合近期 GaussianEditor 系工作，证明 splatting 已成为新晋创作媒介

---

## 🛠️ 实用工具 & 库

### [cloudflare/computer](https://github.com/cloudflare/computer) — "Give your agent a computer"
- **功能**: Cloudflare 开源的 agent 计算机环境，让 agent 拥有可控的浏览器/桌面执行空间（⭐3,044，今日 GitHub Trending +891，TypeScript）
- **CV 关联**: Computer-Use Agent · Screen Understanding · GUI 视觉 — agent 要"用电脑"首先得"看懂屏幕"，这套环境的视觉层设计值得 CV 团队参考
- **使用**: `git clone https://github.com/cloudflare/computer`

---

## 📦 值得关注的版本更新

### [roboflow/supervision](https://github.com/roboflow/supervision) v0.30.0（今日 GitHub Trending +146）
- **更新亮点**: **OpenCV 变为可选** — 新 `_cv2/` 私有后端用 NumPy + Pillow（视频路径用 PyAV）重实现了所有 OpenCV 调用，现在可以跑在 `opencv-python-headless` 甚至完全不装 OpenCV 的机器上
- **为什么重要**: supervision 是 CV 工具链的"瑞士军刀"，去掉 OpenCV 硬依赖意味着**无头服务器 / 容器镜像 / 边缘设备部署体积大减**，对生产管线和 CI 环境是实打实的改进

---

## 📚 HF Daily Papers 精选

- **[MiniWorld: Democratizing the Training of Video World Models from Scratch](https://huggingface.co/papers)** — 让视频世界模型训练"平民化"，从零开始可复现，直指 2026 世界模型竞赛的算力门槛问题
- **[CURV: Enhancing Chart Understanding Through Curriculum Visual Grounded Reasoning](https://huggingface.co/papers)** — 课程式视觉接地推理提升图表理解，文档/报表 AI 的刚需
- **[Better, Stronger, Faster, and Broader: Structured All-Mask Prediction for MLLM-Based Segmentation](https://huggingface.co/papers)** — 用结构化 all-mask 预测统一 MLLM 分割，延续"CV 任务即生成"的范式

---

*Reddit API 仍被 403 拦截，社区热点改用 Hacker News。渠道: GitHub Trending · GitHub Search API · HuggingFace Models · HF Daily Papers · Hacker News = 5 类数据源（含多组查询）*
