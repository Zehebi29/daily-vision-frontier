# 🛠️ 2026-08-09 视觉工业界日报

> 今日扫描了 GitHub Trending · GitHub Search API（过去一周新仓库 2 组关键词）· HuggingFace Models（7 个 pipeline 趋势榜 + 下载榜）· HF Daily Papers · Hacker News（Reddit 连续多日 403）等 5 类数据源，共精选 15 条

---

## 🔥 今日主线：视频生成进入「实时编辑」时代，Agent 视觉与 text-to-CAD 双线爆发

本周最拥挤的赛道从「生成一段视频」转向「**实时、可交互地编辑一段视频**」——JD 开源了 autoregressive diffusion 的实时视频编辑模型，SandAI 放出了视频生成高效扩展的 preview，社区里 code-as-CoT 的物理一致性管线也同周出现。与此同时，text-to-CAD（Multi-Agent-CAD）和「给纯文本 agent 装眼睛」的工具链（agent-vision-toolkit、Qwen-MM-Plugins）成为两个快速增长的新方向。

---

## 🔥 热门开源项目

### 1. [jd-opensource/JoyAI-Video-Edit](https://github.com/jd-opensource/JoyAI-Video-Edit)
- **什么**: 京东 AI 官方开源的**实时开放式视频编辑**模型 —— autoregressive diffusion 架构，视频进、编辑后的视频实时出，支持开放式（open-ended）编辑指令
- **为什么火**: ⭐517（8-04 创建，5 天），Apache-2.0。[论文 2608.03974](https://arxiv.org/pdf/2608.03974) + [HF checkpoint](https://huggingface.co/jdopensource/JoyAI-Video-Edit)（video-to-video）+ [streaming V2V 在线 Demo](https://joyai-labs.jd.com/v2v/) 全套放出；延续 JoyAI-Echo（长视频生成）系列，社区已有 [ComfyUI_JoyAI_Echo](https://github.com/smthemex/ComfyUI_JoyAI_Echo)（⭐57）等节点
- **CV 关联**: Video Editing · Autoregressive Diffusion · 流式视频理解与生成
- **快速上手**: `git clone https://github.com/jd-opensource/JoyAI-Video-Edit && pip install -r requirements.txt`

### 2. [Pan-Chera/Multi-Agent-CAD](https://github.com/Pan-Chera/Multi-Agent-CAD)
- **什么**: 清华 IEI Lab 的 **MAC（Multi-Agent CAD）** —— 4 个 agent 协作的解耦式 text-to-CAD 框架，用受限 test-time compute 把自然语言直接转成可打印 3D 模型
- **为什么火**: ⭐483（7-30 创建），MIT。卖点非常硬：**116× fewer tokens、13× lower cost、99.3% feature pass rate** —— 不是又一个 LLM 生成 STEP 的玩具，而是把「多智能体 + 程序化建模（build123d）」组合成工程可用的降本方案
- **CV 关联**: Text-to-CAD · 3D Modeling · 程序化几何生成 —— 与 B-Rep 理解的 CAD 视觉赛道直接相关
- **快速上手**: `git clone https://github.com/Pan-Chera/Multi-Agent-CAD && pip install -e .`

### 3. [SandAI-org/MAGI-2-preview](https://github.com/SandAI-org/MAGI-2-preview)
- **什么**: SandAI 的 **MAGI-2 preview** —— 高效扩展视频生成模型的公开版本（MAGI-1 的续作，主打 scaling efficiency）
- **为什么火**: ⭐425（8-04 创建），Apache-2.0。视频生成拼「更大」的时代正在转向拼「更省」，preview 版提前释放权重让社区先跑起来
- **CV 关联**: Video Generation · Efficient Scaling · 长视频
- **快速上手**: `git clone https://github.com/SandAI-org/MAGI-2-preview`

### 4. [Anionex/agent-vision-toolkit](https://github.com/Anionex/agent-vision-toolkit)
- **什么**: 为**纯文本 LLM**（DeepSeek/GPT 等无视觉接口的模型）设计的视觉工具箱：多图理解、图片问答、长截图 OCR、前端 UI 还原、GUI 自动化，可无缝接入 Claude Code / Codex 等主流 agent
- **为什么火**: ⭐361（8-01 创建），MIT，符合 Agent Skills 标准。上周「Computer Use」主线（8-08 日报）的延续：**视觉能力正在被标准化成 agent 的 skill**，这个仓库是中文社区里最完整的实现之一
- **CV 关联**: Screen Understanding · OCR · GUI Grounding · Agentic Vision
- **快速上手**: `git clone https://github.com/Anionex/agent-vision-toolkit && pip install -e .`

### 5. [PipeNetwork/kimi-k3-mlx](https://github.com/PipeNetwork/kimi-k3-mlx)
- **什么**: **Kimi-K3（2.78T 总参 / 104B 激活的原生多模态 MoE，1M context）的 Apple Silicon MLX 移植**，含 streaming converter（K3 bf16 全量 5.6TB，无法用 mlx_lm convert 物化）、REAP 专家剪枝
- **为什么火**: ⭐326（7-27 创建）。罕见地诚实：README 开篇「Reality check」——最小档也要 ~870GB，**任何单台 Mac 都跑不动**。作为「超大规模多模态 MoE 本地化」的极限实验非常有参考价值
- **CV 关联**: Multimodal MoE · Vision Tower · 本地推理
- **快速上手**: `git clone https://github.com/PipeNetwork/kimi-k3-mlx && pip install -r requirements.txt`

### 6. [alexiglad/XM](https://github.com/alexiglad/XM)
- **什么**: **Explorative Modeling（XM）** —— 提出生成式建模的「第三个预训练轴」：每步探索 K 个「生成 vs 数据」的候选匹配、只训练最好的那个，可叠加在现有生成模型上，也支持端到端生成
- **为什么火**: ⭐208（7-28 创建），Apache-2.0。[论文 2607.27372](https://arxiv.org/abs/2607.27372) + [项目主页](https://explorative-modeling.github.io/)。V-JEPA 一脉的研究新范式（作者与 LeCun 实验室合作紧密），理论新意足，不是换皮
- **CV 关联**: Self-Supervised Learning · Generative Pretraining · JEPA
- **快速上手**: `git clone https://github.com/alexiglad/XM && cd XM && conda env create -f environment.yml`

### 7. [QwenLM/Qwen-MM-Plugins](https://github.com/QwenLM/Qwen-MM-Plugins)
- **什么**: Qwen 官方开源的**多模态 agent 插件体系** —— 每个能力 = 一个 skill（让模型知道工具存在）+ 一个可选 MCP server（工具本身）；core 能力覆盖动态分辨率读图/视频/文档/3D 模型、OCR、grounding、分割、ASR、视觉对话
- **为什么火**: ⭐137（7-29 创建），Apache-2.0。**Qwen 官方下场定义「agent 怎么用视觉」的接口标准**，`qwen-mm-plugins-core` 可直接装进任意 agent harness
- **CV 关联**: Multimodal Agent · Grounding · Segmentation · OCR
- **快速上手**: `pip install qwen-mm-plugins-core`

### 8. [magicrew/doc7](https://github.com/magicrew/doc7)
- **什么**: **「Any document in. AI-ready Markdown out.」** —— 把 PDF/Office/扫描件/截图/图表/公式/示意图转成 AI 可检索可引用的 Markdown（带视觉理解），Go 写的本地优先工具
- **为什么火**: ⭐728（8-02 创建，今日新仓库搜索榜首），MIT。Document AI 是 RAG 落地的刚需，本地化 + 视觉理解（图表/公式）是它和纯文本解析器的差异点
- **CV 关联**: Document Understanding · OCR · Layout Analysis
- **快速上手**: 见 [Releases](https://github.com/magicrew/doc7/releases) 下载二进制，或 `git clone https://github.com/magicrew/doc7`

---

## 🤗 值得关注的新模型

### [mistralai/Shieldstral-1.0-3B](https://huggingface.co/mistralai/Shieldstral-1.0-3B)
- **类型**: 多模态安全审查（moderation）模型
- **热度**: 4.9k 下载 / ❤️201，Apache-2.0，7-16 发布；社区已出现 GGUF / MLX 移植
- **特色**: 3B 开放权重做**图像+文本**的多模态内容审核，面向 vLLM 部署（tags 带 vllm/mistral3/mistral-common），支持多语言
- **可用性**: ✅ Apache-2.0 可商用；3B 参数量，消费级 GPU 可推理

### [nvidia/Qwen-Image-Flash](https://huggingface.co/nvidia/Qwen-Image-Flash)
- **类型**: text-to-image / few-step 蒸馏
- **热度**: 8-04 更新，trending 中（926 下载，新权重）
- **特色**: NVIDIA 用 **DMD2 把 Qwen-Image 压成 few-step 快速版** —— 生成式扩散模型的「推理提速」赛道，NVIDIA 在把开源生态的 SOTA 底座批量蒸馏成实时可用版本
- **可用性**: diffusers `Qwen2Pipeline` 兼容；few-step 推理，单卡可跑

### [pixai-labs/pixai-tagger-v0.9](https://huggingface.co/pixai-labs/pixai-tagger-v0.9)
- **类型**: image-classification / multi-label 打标
- **热度**: ❤️190（8 月 trending 榜，下载量刚起步）
- **特色**: 动漫/Danbooru 风格 **multi-label tagger v0.9** —— 训练 LoRA/微调时的自动打标基建，Apache-2.0 且 endpoints 兼容，属于「生成生态的隐形刚需」
- **可用性**: ✅ Apache-2.0

> 📊 **下载榜观察**: [DA3METRIC-LARGE](https://huggingface.co/depth-anything/DA3METRIC-LARGE)（Depth Anything 3 度量版，62.7 万下载）与 [BiRefNet](https://huggingface.co/ZhengPeng7/BiRefNet)（68.8 万下载，抠图/分割）仍是单目深度与高分辨率分割两个赛道的下载常青树 —— 说明工业界对「度量深度」和「精细抠图」的调用量持续高位。

---

## 📰 社区热点

### [HN: Mistral 开源 3B 多模态审查模型 Shieldstral](https://news.ycombinator.com/item?id=49201970)（score 481 / 133 评论）
- **讨论方向**: 开放权重做内容审核是「监管工具民主化」还是「审查基础设施扩散」？评论区围绕 3B 小模型的误报率、vLLM 部署、以及开源审查模型能否真正替代闭源 moderation API 展开 —— 也间接说明**多模态安全审查正在成为视觉模型的独立产品赛道**

### 「视频实时编辑」三连发：生成模型的下一站是编辑
- **讨论方向**: JoyAI-Video-Edit（实时 V2V 编辑）+ MAGI-2-preview（高效扩展）+ VideoCoCo（code-as-CoT 物理一致编辑）同周出现，加上 HF 论文 [ContextMaster](https://huggingface.co/papers/2608.04956)（多镜头视频创作）。信号明确：**视频生成模型从「一次生成」走向「持续可编辑、多镜头可编排」**，编辑能力（而非生成质量）正在成为 2026 下半年的差异化战场

---

## 🛠️ 实用工具 & 库

### [micky-li-hd/VideoCoCo](https://github.com/micky-li-hd/VideoCoCo)
- **功能**: **Code-as-CoT 的物理一致性视频生成** —— 先用 code agent 写物理模拟代码、在沙箱里渲染成中性白模草稿，再让生成模型照着草稿出像素，物理规律（碰撞/落体/遮挡）由模拟器保证
- **使用**: [🤗 权重](https://huggingface.co/mickyhimself/VideoCoCo) + `git clone https://github.com/micky-li-hd/VideoCoCo`；双引擎（模拟器 + 生成器）agentic 管线，值得复现

### [zouyuanqing/vision-primitives-mcp](https://github.com/zouyuanqing/vision-primitives-mcp)
- **功能**: **单文件 MCP server 给纯文本 LLM 装眼睛** —— describe / locate（坐标定位）/ OCR with bbox / annotate / crop / zoom / 自动异常扫描，基于小米 MiMo V2.5，适配 DeepSeek 等无视觉模型 + computer-use
- **使用**: `git clone https://github.com/zouyuanqing/vision-primitives-mcp`（⭐6 虽小，但「primitive 级视觉原子操作」的思路是 agent-vision 工具链的正确分层方向）

---

## 📦 值得关注的版本更新

### [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI/releases) v0.31.0（8-08）
- **更新亮点**: ① 组织正式迁移到 **Comfy-Org**（原 comfyanonymous/ComfyUI）；② **Flux 3 视频模型支持**（BFL partner nodes）—— 视频生成进入 ComfyUI 官方节点；③ MiniMax-H3 `int8_convrot` VAE 支持（kijai 提交）；④ **LTX 与 Wan 推理加速**；⑤ 无 swap 分区 Linux 内存占用修复；⑥ 前端升至 1.48.6
- **为什么重要**: Flux 3 视频 + MiniMax H3 + LTX/Wan 加速同版落地，ComfyUI 事实上已成为**开源视频生成的事实标准前端**，版本节奏明显加快（8-03 v0.30.0 → 8-08 v0.31.0）

---

## 📚 HF Daily Papers 精选

- **[GaussianSelector: Lightweight Human-Guided Object Selection in 3D Gaussian Splatting with Graph Optimization](https://huggingface.co/papers/2608.01492)** — 从 3DGS 场景里**用图优化做轻量人机目标选择**，不用重训、不建密集多视角 SAM 观测；3D 场景编辑/具身交互的实用弹药
- **[FactorJEPA: Factorizing Monolithic Futures into Layout-Agent-Interaction Channels](https://huggingface.co/papers/2608.01049)** — JEPA 家族继续扩张：把拥挤城市场景的「整体未来」分解成 layout-agent-interaction 通道，直指世界模型在复杂动态场景的建模效率
- **[MASS: Multiplayer World Models with Authoritative Shared State](https://huggingface.co/papers/2608.06257)** — 多人/多视角视频世界模型把 world state 与视角相关 latent **解耦成权威共享状态**，消除冗余计算与视角不一致 —— 游戏与仿真世界模型的可扩展性解法
- **[ContextMaster: Interactive Multi-Shot Video Creation via Fixed-Budget Sparse Context Routing](https://huggingface.co/papers/2608.04956)** — 把「文本生成/参考跟随/编辑」统一进**多镜头创作流程**，固定预算稀疏上下文路由；与今日「视频编辑实时化」主线呼应
- **[World-to-Wrist: Task-Conditioned Future Wrist Modeling for Fine-Grained Robot Manipulation](https://huggingface.co/papers/2608.05369)** — VLA 模型不再把主视角/腕部视角当平行输入，而是**预测腕部视角的未来交互**；精细操作（夹取/装配）具身智能的关键改进
- **[EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic RL](https://huggingface.co/papers/2608.06197)** — agentic RL 里用 **world rehearsal 把环境动力学内化进模型**，绕开昂贵的外部模拟器/可执行环境构造 —— 长时程 tool-use agent 训练成本问题的直接回应

---

*Reddit API 仍全站 403（连续多日），社区热点继续用 Hacker News 作为主要备用源。渠道：GitHub Trending · GitHub Search API（2 组新仓库查询）· HuggingFace Models（7 个 pipeline 趋势榜 + 下载榜）· HF Daily Papers · Hacker News = 5 类数据源，共 15 条精选。*
