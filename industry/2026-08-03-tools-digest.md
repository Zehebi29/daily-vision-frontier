# 🛠️ 2026-08-03 视觉工业界日报

> 今日扫描了 GitHub Trending · GitHub Search (新 repo) · HuggingFace Models (8 个 pipeline 趋势榜) · HuggingFace Daily Papers · Hacker News 等 7 个渠道（Reddit 全站 403、PapersWithCode API 结构变动，见文末说明）

---

## 🔥 热门开源项目

### 1. [alexiglad/XM — Explorative Modeling](https://github.com/alexiglad/XM)
- **什么**: **Explorative Modeling: Unlocking a Third Pretraining Axis and End-to-End Generation** 官方 PyTorch 实现（⭐138，7-28 新建）— 在"数据规模、模型规模"之外提出第三条预训练轴（explorative modeling），并打通端到端生成
- **为什么火**: 今天 GitHub 新 repo 里 stars 增长最快的视觉相关项目；HF Daily Papers 13 upvotes。把"探索式建模"作为一个**独立预训练范式**提出，对自监督/世界模型一族（JEPA、V-JEPA）是直接的方法论冲击
- **CV 关联**: 自监督预训练 · 世界模型 · 生成式视觉
- **快速上手**: `git clone https://github.com/alexiglad/XM`

### 2. [zju3dv/INTACT-JEPA](https://github.com/zju3dv/INTACT-JEPA)
- **什么**: **INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models**（⭐77，7-28 新建，HF 13 upvotes）— 浙大 3DV 组（NeRF/world model 老牌 lab）的 JEPA 系世界模型，用"意图-动作同构学习"免去动作搜索
- **为什么火**: zju3dv 出品基本等于质量背书；world model + JEPA 是当下最热的两条线合流，且主打 search-free（推理时不做动作搜索，快）
- **CV 关联**: 世界模型 · 视频预测 · JEPA · 具身智能
- **快速上手**: `git clone https://github.com/zju3dv/INTACT-JEPA`

### 3. [micky-li-hd/VideoCoCo](https://github.com/micky-li-hd/VideoCoCo)
- **什么**: **Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System**（⭐75，7-29 新建）— 用"代码作为思维链"给视频生成加物理一致性约束，双引擎 agent 系统
- **为什么火**: 物理一致（不违反重力/碰撞）是视频生成从"好看"到"可用"的关键瓶颈；Code-as-CoT 把约束写成可执行代码、由 agent 编排，思路新鲜且工程可复现
- **CV 关联**: 视频生成 · 物理仿真 · Agentic pipeline
- **快速上手**: `git clone https://github.com/micky-li-hd/VideoCoCo`

### 4. [AlayaLab/ShadowDancer](https://github.com/AlayaLab/ShadowDancer)
- **什么**: **Teaching Video World Models Any Action by Learning Unified Dynamics Representation** 代码发布（⭐36，7-31 新建，[项目主页](https://shadowdancer-1.github.io/)，HF 16 upvotes）
- **为什么火**: 视频世界模型通常只能"看"（预测），ShadowDancer 教它"任何动作"——通过统一动力学表示把 action 注入世界模型，是 world model → policy 方向的代表性工作
- **CV 关联**: 视频世界模型 · 统一动力学 · 决策/控制
- **快速上手**: `git clone https://github.com/AlayaLab/ShadowDancer`

### 5. [cvg/DVPSFormer](https://github.com/cvg/DVPSFormer)
- **什么**: **DVPSFormer: Explicit Scene Discretization for Efficient Online Depth-aware Video Panoptic Segmentation**（⭐2，7-28 新建）— ETH cvg 组的深度感知视频全景分割
- **为什么火**: cvg 出品 + 聚焦 **online**（流式/实时）深度感知全景分割，显式场景离散化换效率；对自动驾驶感知落地有直接参考价值
- **CV 关联**: 视频全景分割 · depth-aware · 自动驾驶
- **快速上手**: `git clone https://github.com/cvg/DVPSFormer`

### 6. [JoHnneyWang/AnyID](https://github.com/JoHnneyWang/AnyID)
- **什么**: **AnyID: Ultra-Fidelity Universal Identity-Preserving Video Generation from Any Visual References**（CVPR 2026 官方代码，7-29 新建）
- **为什么火**: 身份保持视频生成（换脸/换身份）从"单参考图"走向"任意视觉参考"，CVPR 中稿 + 官方代码即出；数字人/影视预演赛道高频引用的新基线
- **CV 关联**: 视频生成 · identity-preserving · face reenactment
- **快速上手**: `git clone https://github.com/JoHnneyWang/AnyID`

---

## 🤗 值得关注的新模型

### [lvladikov/SeedVR2-1.4B](https://huggingface.co/lvladikov/SeedVR2-1.4B)
- **类型**: image-to-image / **一步扩散**超分 + 复原（super-resolution · restoration）
- **热度**: 7-29 发布 ❤️32，含 ComfyUI 工作流（tinyvae 版本）
- **特色**: SeedVR 系第二代 — 用 knowledge distillation 把多步扩散复原压成 **one-step**，1.4B 参数兼顾质量与速度；对比传统 GAN 超分（如 Real-ESRGAN），生成式先验对真实退化更鲁棒
- **可用性**: Apache-2.0 ✅ 可商用

### [microsoft/Mage-VL](https://huggingface.co/microsoft/Mage-VL)
- **类型**: image-text-to-text（多模态 LLM）
- **下载量**: **27.2 万次** ❤️186，7-25 发布（arxiv:2607.24904）
- **特色**: 微软新开源的视觉语言模型，Apache-2.0；在多模态 LLM 里它主打视觉 token 效率（Mage 系列延续），27 万下载说明社区对"微软系开源 VLM"的认可度
- **可用性**: Apache-2.0 ✅

### [nvidia/Cosmos-H-Dreams](https://huggingface.co/nvidia/Cosmos-H-Dreams)
- **类型**: image-to-video（**手术机器人仿真**，实时交互式视频生成）
- **热度**: 7-21 发布 ❤️12（NVIDIA 医疗技术线 nv-medtech）
- **特色**: 把 Cosmos 世界模型能力下沉到**外科手术**场景——实时、可交互、自回归生成手术视频，直接服务手术机器人训练数据合成（合成数据缓解真实手术视频稀缺）
- **可用性**: ⚠️ license: other（NVIDIA 医疗条款，需确认）

### [bench-labs/PixelModel-v5](https://huggingface.co/bench-labs/PixelModel-v5)
- **类型**: text-to-image（**tiny rectified-flow DiT**）
- **下载量**: 5,501 次 ❤️25，7-28 发布（MIT）
- **特色**: 小尺寸 rectified flow + DiT 文生图模型，主打"小而能跑"——在 8-1B 大模型刷榜的今天，PixelModel 走的是**边缘/低显存部署**路线，5 天 5.5k 下载说明"轻量 T2I"仍有真实需求
- **可用性**: MIT ✅ 可商用

### [Sparknight/sam3.1-int8-int4-convrot](https://huggingface.co/Sparknight/sam3.1-int8-int4-convrot) + [CornLogic/10EROS-INT8](https://huggingface.co/CornLogic/10EROS-INT8)
- **类型**: 量化部署（segmentation / image-to-video）
- **热度**: 均 7-31 发布；SAM 3.1 int8/int4（含 **convrot** 旋转卷积优化）走 ComfyUI 路线，10EROS-INT8 已 1.4 万下载
- **特色**: 一天内两个**旗舰模型的 INT8/INT4 量化版**上线——SAM 3.1 与 10EROS（视频生成）都在抢"本地可跑"生态位；量化（尤其 convrot 这类算子级技巧）是开源社区把 20B+ 模型塞进消费级显卡的主要手段
- **可用性**: SAM3.1 版 license: other（跟随原模型）；10EROS-INT8 需确认

### [qz-wei/GeoStereo](https://huggingface.co/qz-wei/GeoStereo)
- **类型**: depth-estimation（**扩散式立体匹配**，arxiv:2607.24024）
- **热度**: 7-17 发布 ❤️3，Apache-2.0
- **特色**: 用 diffusion 做 stereo matching，同时输出深度 + surface normal + 几何；与 DepthAnything 这类单目估计互补——需要**绝对尺度**的机器人/自动驾驶任务更吃这一路线
- **可用性**: Apache-2.0 ✅

### [UWGZQ/ConCor-1](https://huggingface.co/UWGZQ/ConCor-1)
- **类型**: image-segmentation（**vision-language grounding** / referring expression segmentation）
- **热度**: 7-26 发布 ❤️2，Apache-2.0
- **特色**: 概念对应（concept correspondence）路线——把"指代分割/开放词表分割"统一到一个 feature extraction 框架，transformer 架构直接可微调；对"按描述找物体"的落地场景（文档、电商、机器人抓取）有用
- **可用性**: Apache-2.0 ✅

---

## 📰 社区热点

### Qwen-UI-Agent Technical Report — HF Daily Papers 今日最高票（285 upvotes）
- **论文**: [Qwen-UI-Agent Technical Report](https://huggingface.co/papers/2607.28227)（arxiv:2607.28227）
- **核心**: 通义团队发布**面向真实世界的 GUI Agent 基座**技术报告——把"看屏幕 → 理解 UI → 执行操作"做成下一代会话级 foundation model。社区关注点：GUI Agent 从 demo 走向"real-world centric"基座化，和 8-02 日报里的 Amadeus（桌面交互 Agent）形成呼应，说明**屏幕理解赛道正在标准化**

### MPIE-Bench: 多人交互编辑有了正规评测（37 upvotes）
- **论文**: [MPIE-Bench](https://huggingface.co/papers/2607.27616) + [代码](https://github.com/AnnLin0628/mpie-bench)（⭐5）
- **核心**: 首个**多人交互（接触场景）角色一致性图像编辑 benchmark**，六轴评测协议。此前这类能力全靠主观目测，现在有标准可量化——图像编辑评测体系的又一次补全

### See2Think: 多模态模型真的用中间视觉状态吗？（22 upvotes）
- **论文**: [See2Think](https://huggingface.co/papers/2607.26769) + [代码](https://github.com/CSU-JPG/See2Think)（⭐5）
- **核心**: 质疑多模态模型"思考时是否真的依赖中间视觉表征"——用探针实验区分"看"与"想"的耦合程度。对 VLM 架构设计（是否该显式插入视觉推理状态）有直接启发，属于**反直觉的评测型工作**

### HN: Meshdiff — 浏览器端 STL 对比（176 pts / 19 评论）
- **链接**: [meshdiff.com](https://meshdiff.com/)
- **核心**: 纯客户端对比两个 STL 版本，3D 打印迭代工作流的好工具；讨论聚焦"本地优先"3D 工具在 AI 生成 mesh（如 TRELLIS 系）流行后的增量价值

---

## 🛠️ 实用工具 & 库

### [BeatAPI/awesome-seedance-2-5-prompts](https://github.com/BeatAPI/awesome-seedance-2-5-prompts)
- **功能**: Seedance 2.5 视频生成 prompt 精选集（电影感/动漫/UGC/广告/叙事分类），含可播放示例
- **CV 关联**: Seedance 2.5 发布（见 8-02 日报）后社区生态快速成形——prompt 库是"闭源模型 + 开源玩法"生态的标准先头部队
- **使用**: `git clone https://github.com/BeatAPI/awesome-seedance-2-5-prompts`

---

## 📦 值得关注的版本更新

### [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR)
- **更新亮点**: 持续霸榜 HF 视觉模型下载前列（**253.6 万次** ❤️3778，MIT）——百度"无限类目 OCR"把文档/票据/自然场景识别收进一个模型，当前开源 OCR 领域事实上的热度第一；有实际 OCR/文档理解需求可优先评估

---

## 📊 今日扫描总结

| 渠道 | 覆盖情况 |
|------|---------|
| GitHub Trending (daily) | ✅ 15 repos scanned（今日多为 agent/安全/系统类，CV 相关占比低） |
| GitHub Search (新 repo, 7-27 后) | ✅ 按 q=image generation / video generation / diffusion / segmentation 检索，stars 排序取 top |
| HuggingFace Models (8 个 pipeline 趋势榜) | ✅ text-to-image · image-to-image · segmentation · detection · depth · video-gen · i2v · video-classification |
| HuggingFace Daily Papers | ✅ 30 篇，按 upvotes 筛选出 CV/多模态相关（今日 VLM/GUI-Agent 议题权重高） |
| Hacker News (front page 40) | ✅ 命中 Meshdiff（STL 对比工具）等视觉/3D 相关 |
| PapersWithCode | ⚠️ API 返回非 JSON（结构变动），仅作交叉验证 |
| Reddit (r/computervision, r/MachineLearning, r/StableDiffusion) | ❌ 全渠道 403（www/old/api 及多 UA 均被拦截），社区信号改用 HN + HF 替代 |

**精选条目**: 15 条 | **主要方向**: 世界模型家族爆发 (XM / INTACT-JEPA / ShadowDancer / VideoCoCo) · 量化部署 (SAM3.1 INT8/INT4, 10EROS-INT8) · GUI Agent 基座化 (Qwen-UI-Agent) · 一步扩散低层视觉 (SeedVR2) · 医疗/具身垂类 (Cosmos-H-Dreams)

---

*今日核心观察: "世界模型"成为本周开源最热关键词——Explorative Modeling (XM)、INTACT-JEPA、ShadowDancer、VideoCoCo 四个方向同周开源，加上 Qwen-UI-Agent 高票刷屏，说明视觉研究重心正从"生成好看"转向"理解物理 + 驱动行动"。另一条线是部署侧：SAM 3.1 与 10EROS 同日出 INT8/INT4 量化版，20B+ 模型进消费级显卡的社区工程战已全面开打。*
