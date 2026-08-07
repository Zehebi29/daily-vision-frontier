# 🛠️ 2026-08-07 视觉工业界日报

> 今日扫描了 GitHub Trending · GitHub Search（过去一周新仓库，多组关键词）· HuggingFace Models（全站 trending + 6 个 pipeline 趋势榜）· HF Daily Papers · Hacker News（Reddit 全站仍 403 拦截，继续用 HN 作社区源）等 5 类数据源

---

## 🔥 热门开源项目

### 1. [firecrawl/anydoc](https://github.com/firecrawl/anydoc)
- **什么**: 用 Rust 把 Word / PowerPoint / Excel / OpenDocument / RTF / EPUB / CSV / PDF 全部转成**干净 Markdown**，带 Node.js 和 Python 绑定 — firecrawl 继 pdf-inspector 之后把文档管线吃得更全
- **为什么火**: ⭐8,506（8-03 创建，4 天冲到本周新仓库第一梯队），MIT。firecrawl 是 RAG/文档 AI 的头部基建商，anydoc 直接补齐了"非 PDF 办公文档"进 RAG 的最后一公里
- **CV 关联**: Document AI · Layout Understanding · 扫描件/图文混排文档的结构化（视觉信息不进 Markdown 就丢了）
- **快速上手**: `pip install firecrawl-anydoc`（或 `cargo add anydoc`，见 [README](https://github.com/firecrawl/anydoc)）

### 2. [SandAI-org/MAGI-2-preview](https://github.com/SandAI-org/MAGI-2-preview)
- **什么**: Sand.ai 开源的 **114B 统一音视频生成 MoE 模型，每 token 只激活 6B 参数**（MagiMoE），T2V / I2V + **同步生成声音**并 mux 进视频，两阶段生成（低分辨率去噪 + refiner 升到 1080p），10 秒片段
- **为什么火**: ⭐383（8-04 创建）/ Apache-2.0，权重在 [HF sand-ai/MAGI-2-preview](https://huggingface.co/sand-ai/MAGI-2-preview)，配套 [tech blog](https://sand.ai/blog/magi-2-preview)。"用 MoE 稀疏激活把视频生成的算力成本砍下来"是继 MiniMax-H3 之后开源阵营的又一条 scaling 路线，两个模型撞在同一周发布，视频生成进入"效率军备竞赛"
- **CV 关联**: Video Generation · Audio-Visual Generation · MoE Scaling
- **快速上手**: `docker pull sandai/magi-2-preview && docker run --gpus all -it -v /path/to/ckpt:/workspace/ckpt sandai/magi-2-preview:latest`（注意需 8× Hopper）

### 3. [inspatio/querysplat](https://github.com/inspatio/querysplat)
- **什么**: **QuerySplat: Decoupling Geometry and Appearance Representations in 3DGS Prediction** 官方实现（arXiv 2608.01186）— 从单张图预测 3D Gaussian，把几何和外观表示解耦，配套 VGGT-Omega 相机/深度预测 + 可选 test-time optimization
- **为什么火**: ⭐233 / Apache-2.0（8-02 创建），[项目主页](https://inspatio.github.io/querysplat/)。单图 → 3DGS 是 2026 年 3D 视觉最卷的赛道（VGGT 系全家桶），QuerySplat 的"解耦几何/外观"思路直指多视角一致性和编辑可控性两个老痛点
- **CV 关联**: 3D Gaussian Splatting · 单图重建 · Camera Pose 估计
- **快速上手**: `git clone https://github.com/inspatio/querysplat && cd querysplat && pip install torch==2.11.0 --index-url https://download.pytorch.org/whl/cu128 && pip install -r requirements.txt`

### 4. [thebuggeddev/anatomy](https://github.com/thebuggeddev/anatomy)
- **什么**: threejs 写的**可交互 3D 人体解剖浏览器**（GPT 5.6 Sol 辅助生成），浏览器里直接旋转/剖切查看人体结构
- **为什么火**: ⭐1,867（8-02 创建），本周增长最快的 3D 可视化项目之一。虽然是"非典型 CV"，但它把医学图谱变成可交互 3D 资产，对医学影像可视化、手术规划工具的前端参考价值不小
- **CV 关联**: 3D Visualization · Medical Imaging 前端 · 交互渲染
- **注意**: ⚠️ 仓库**无 LICENSE**（默认保留版权），商用前需联系作者
- **快速上手**: `git clone https://github.com/thebuggeddev/anatomy && npm install && npm run dev`

### 5. "照片 → 抽象海报" 生成式技能潮 🔥
- **代表仓库**: [ZzzLc0405/photo-abstract-editorial](https://github.com/ZzzLc0405/photo-abstract-editorial)（⭐998，8-04）· [Evianis/travel-photo-abstraction](https://github.com/Evianis/travel-photo-abstraction)（⭐133）· [yangcodingmaster/photo-distill](https://github.com/yangcodingmaster/photo-distill)（⭐34，纯 HTML/CSS/SVG 手写实现，不用生成模型）
- **什么**: 一组"把照片蒸馏成极简编辑插画/海报"的 agent skill，输入一张照片，输出风格化抽象图形（杂志编辑风、旅行手绘风、极简 poster）
- **为什么火**: 一周内连出多个高 star 同款，说明 **image-to-image 生成 + agent skill 封装**成为新的爆款应用模板 — 不再是"换个脸"，而是"换一种视觉语言"。对做 style transfer / image abstraction 的团队是现成的产品化参考
- **CV 关联**: Style Transfer · Image Abstraction · Agentic Image Workflow

---

## 🤗 值得关注的新模型

### [thinkingmachines/Inkling-Small](https://huggingface.co/thinkingmachines/Inkling-Small) — 今日 HF 趋势榜黑马（trending 190）
- **类型**: image-text-to-text 原生多模态 MoE（**text + image + audio 输入 → text 输出**），276B 总参 / **12B active**，42 层 decoder，6/256 experts + 2 shared
- **热度**: ❤️321 / 2.2 万下载（7-27 发布，这两天冲上趋势榜），Thinking Machines Lab（Mira Murati 等前 OpenAI 核心团队）出品，另有 [NVFP4 量化版](https://huggingface.co/thinkingmachines/Inkling-Small-NVFP4) 与官方 [HF blog](https://huggingface.co/blog/thinkingmachines-inkling)
- **特色**: 图像用分层 patch encoder、音频用离散 token 编码，所有模态投影到共享空间由 decoder 统一处理；SWEBench Verified 80.2%（同列最强，超过 Qwen3.5 397B 的 76.4%）、Terminal Bench 64.7% 也是开源组第一 — **12B active 打平 300B+ 闭源梯队**，Apache-2.0 可商用
- **可用性**: Apache-2.0 ✅；SGLang / vLLM / Unsloth / llama.cpp 全支持，NVFP4/MXFP8 量化，单节点多卡可跑

### MiniMax-H3 开源生态一周爆发（模型本体 8-06 已介绍，这里是生态跟进）
- **GGUF 量化落地**: [Abiray/MiniMax-H3-GGUF](https://huggingface.co/Abiray/MiniMax-H3-GGUF) 发布 4 天 **15.5 万下载**（8-03），另有 [molbal](https://huggingface.co/molbal/MiniMax-H3-GGUF) / [leejet](https://huggingface.co/leejet/MiniMax-H3-GGUF) 多版本 — 视频生成模型开始像 LLM 一样"本地化"
- **Turbo 蒸馏**: [larryvrh/MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)（trending 289）+ [ComfyUI 工作流节点](https://huggingface.co/Comfy-Org/MiniMax-H3)，社区在快速补全"提速 + 可编排"的最后一公里
- **判断**: 一个开源视频模型火不火，看它 GGUF 化的速度 — H3 这个速度是 Sora 级热度才有的待遇；下一步盯 llama.cpp/MLX 的本地跑通

### [thedeoxen/Krea-2-pose-controlnet](https://huggingface.co/thedeoxen/Krea-2-pose-controlnet)
- **类型**: image-to-image / ControlNet（Krea 2 的姿态控制）
- **热度**: 8-04 发布，Krea 2 生态新增的 pose 控制件（配套社区已有 depth controlnet）
- **特色**: 给 Krea 2 补上人体姿态控制 — 此前 Krea 2 强在风格/编辑，姿态可控性弱是社区共识；这是开源社区给闭源基座"补能力"的典型路径（参考 SD 时代的 controlnet 生态）
- **可用性**: 需 Krea 2 基座（gated）；ControlNet 权重本身社区可用

---

## 📰 社区热点

### [Anthropic: Our position on open-weights models](https://news.ycombinator.com/item?id=49076057)（HN）
- 讨论方向: Anthropic 官方首次系统阐述对开源权重模型的态度（1179 分 / 386 评论，本周 HN 最大 AI 话题）。核心张力：开放权重的安全风险 vs 生态价值，直接关系到 FLUX、Qwen-VL、SAM、V-JEPA 这些开源视觉模型未来的"自由度"
- 热度: score 1,179 / 386 条评论。对 CV 从业者: 视觉开源生态（diffusers、safetensors、LoRA 文化）是这个争论最大的受益方之一，值得通读原文 [anthropic.com/news/position-open-weights-models](https://www.anthropic.com/news/position-open-weights-models)

### [Flock 车牌识别相机 71% 误读率之争](https://news.ycombinator.com/item?id=49199088)（HN）
- 讨论方向: 加州一镇称 Flock 自动车牌识别（ALPR）相机**误读率高达 71%**；同话题还有 [Flock 相机被大量剪断偷走](https://news.ycombinator.com/item?id=49171656)（391 分/248 评论）等系列贴 — 从 CV 精度到隐私政治的全链条争论
- 热度: 46 分（误读贴）/ 391 分（破坏事件贴），多贴同热。对 CV 从业者的信号: **ALPR/监控识别的精度评估、误报成本、部署伦理**是 2026 年最"出圈"的 CV 议题，也催生了对 fair/robust 车牌识别评估基准的需求

### [AMD 收购 Taalas：把模型"蚀刻"进硅片](https://news.ycombinator.com/item?id=49201970)（HN）
- 讨论方向: AMD 收购 Taalas，后者用"把模型权重直接硬件化"（etching models in silicon）的思路做推理加速；对 CV 的意义在于 **vision 模型推理（YOLO 系、ViT、扩散模型）是这类专用加速器最典型的目标负载**
- 热度: score 349 / 279 条评论

---

## 🛠️ 实用工具 & 库

### [alexw5702-afk/krea2-anypaint](https://github.com/alexw5702-afk/krea2-anypaint)
- **功能**: 原生 ComfyUI 节点，封装 Krea 2 AnyPaint — 任意 mask 的 inpainting / outpainting / 混合图像编辑
- **使用**: `git clone https://github.com/alexw5702-afk/krea2-anypaint` 后放入 ComfyUI `custom_nodes/`，需 Krea 2 基座权重（gated）

### [uulong950/qingming-z-image-turbo](https://github.com/uulong950/qingming-z-image-turbo)
- **功能**: **AMD 原生** HIP/C++ 实现的 Z-Image-Turbo 推理，为 RX 7900 XTX（gfx1100, WMMA）优化 — 目前 Z-Image 系大多只照顾 CUDA，这是少见的 AMD 原生移植，对 A 卡用户的本地生图是实打实的补缺
- **使用**: `git clone https://github.com/uulong950/qingming-z-image-turbo`（需要 ROCm/HIP 环境）

### [Sparknight/sam3.1-int8-int4-convrot](https://huggingface.co/Sparknight/sam3.1-int8-int4-convrot)
- **功能**: Meta **SAM 3.1 Multiplex** 的原生 ComfyUI 量化版 — ConvRot W8A8（1.19 GiB）和 W4A4（0.98 GiB），质量敏感层保持 FP16，官方 checkpoint loader 直接加载，无需自定义量化节点
- **使用**: ComfyUI v0.27+ 直接下载加载；SAM 3.1 的主打升级是 Object Multiplex 快速多目标视频跟踪

---

## 📦 值得关注的版本更新

### [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics/releases) v8.4.115（8-01）
- **更新亮点**: 全面迁移到 **Ultralytics Platform** — `yolo login API_KEY` / `yolo logout` 新认证，settings schema 升到 0.0.7，**移除 legacy `ultralytics.hub` 包**。老 HUB API key 会被自动清理，升级前确认自己的训练/导出脚本没有依赖旧 HUB 接口
- **为什么重要**: YOLO 系是 CV 落地使用率最高的工具链，这次是"训练平台化"的一次大重构，CI 脚本和团队文档需要跟着改

---

## 📚 HF Daily Papers 精选

- **[Ego2Robot: Scalable Robot Data Synthesis from Egocentric Human Data](https://huggingface.co/papers/2608.02580)** — 用第一人称人类视频大规模合成机器人训练数据，正面回应"机器人数据不够"的行业瓶颈
- **[DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with Adversarial Patch Attack](https://huggingface.co/papers/2608.03207)** — 对抗 patch 攻击 flow-matching 的视觉语言动作模型（VLA），机器人安全方向的攻防新基线
- **[SIGNPOST-Bench: Benchmarking Text-Vision Conflict Resolution in MLLMs](https://huggingface.co/papers/2608.04244)** — 专门测"文字和视觉打架时模型信谁"的基准，直指多模态幻觉的根源性评估
- **[WorldCycle: Self-Verifiable RL for Long-Horizon Video World Models](https://huggingface.co/papers/2608.04964)** — 视频世界模型 + 自验证强化学习，长程一致性是 world model 进 policy 的关键一步
- **[BridgeVLA++: Data-Efficient, Generalizable VLA Framework for 3D Manipulation](https://huggingface.co/papers/2608.05042)** — 记忆增强 + 数据高效的三维操作 VLA，具身智能落地的工程化代表

---

*Reddit API 全站 403（含 RSS），社区热点继续用 Hacker News 作为主要备用源；PapersWithCode 主页 API 结构变动本次未采到结构化数据，已用 GitHub Search + HF 数据补足。渠道：GitHub Trending · GitHub Search API · HuggingFace Models（含多 pipeline）· HF Daily Papers · Hacker News = 5 类数据源。*
