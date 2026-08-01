# 🛠️ 2026-08-01 视觉工业界日报

> 今日扫描了 GitHub Trending · GitHub Search (新 repo) · HuggingFace Models · HuggingFace Daily Papers · PapersWithCode 等 7 个渠道

---

## 🔥 热门开源项目

### 1. [H-EmbodVis/TurboVLA](https://github.com/H-EmbodVis/TurboVLA)
- **什么**: 实时 Vision-Language-Action (VLA) 模型，在 RTX 4090 上以 32Hz 运行、显存占用 <1GB（昨天刚上 HF Papers 首页，今天正式 repo 落地，⭐167 / 创建于 7-28）
- **为什么火**: 把 VLA 的实时性门槛直接打穿 — 这是机器人控制从"研究 demo"走向"边缘部署"的关键一步；repo 活跃（7-31 还在更新），已成为本周新 repo 中 star 增长最快的 CV 项目
- **CV 关联**: 视觉-语言-动作 · Embodied AI · 模型压缩
- **快速上手**: `git clone https://github.com/H-EmbodVis/TurboVLA`

### 2. [neoteai/N0-VTLA](https://github.com/neoteai/N0-VTLA)
- **什么**: Scaling Vision-Tactile-Language-Action Model with Latent Tactile Tokens — 用**隐式触觉 token** 扩展 VLA 到视觉+触觉双模态
- **为什么火**: ⭐27，创建于 7-25。触觉是机器人操作里最难建模的一路模态，把它 token 化后与视觉对齐，是 VLA 从"看"到"摸"的重要探索方向
- **CV 关联**: 多模态 · 触觉感知 · Embodied AI
- **快速上手**: `git clone https://github.com/neoteai/N0-VTLA`

### 3. [alvin528/WorldByCode](https://github.com/alvin528/WorldByCode)
- **什么**: 把一张图片变成**可编辑、可检视的 3D 物理世界** — 用 VLM 生成 procedural 代码 (Three.js/Rapier)，零 3D 生成模型
- **为什么火**: 思路清奇：不训练 3D 生成器，而是让 VLM 直接"写代码造世界"，生成的结果天然可编辑、可交互（real2sim 方向的新范式）
- **CV 关联**: Image-to-3D · World Model · VLM + Procedural Generation
- **快速上手**: `git clone https://github.com/alvin528/WorldByCode`

### 4. [fla-org/flash-linear-attention](https://github.com/fla-org/flash-linear-attention)
- **什么**: 新一代高效 attention 实现的统一工具箱（Mamba/线性注意力等新兴架构的 CUDA kernel）
- **为什么火**: ⭐5,490，本周 Python 周趋势榜。虽然主力是 LLM，但其高效 token-mixing kernel 同样被视觉架构（ViT 变体、视频 transformer）复用
- **CV 关联**: Efficient Attention · ViT · Video Transformers
- **快速上手**: `pip install flash-linear-attention`

---

## 🤗 值得关注的新模型

### [krea/Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo) + [Krea-2-Raw](https://huggingface.co/krea/Krea-2-Raw)
- **类型**: text-to-image（Krea 自家扩散架构，Diffusers `Krea2Pipeline`）
- **下载量**: Turbo 15.3 万次 ❤️769 / Raw 15.0 万次 ❤️418 — 当前 HF text-to-image **趋势榜第 1**
- **特色**: 一直做图像工具 UI 的 Krea 终于开源自研模型，Raw 为基础版、Turbo 为蒸馏加速版（Turbo 以 Raw 为 base）。社区已涌现大量 Krea2 LoRA（Kroma 等），生态正在快速形成
- **可用性**: ⚠️ **gated 访问**（需登录授权）、license: other — 非完全开放，商用需确认条款；适合先在 HF 上申请试用

### [lvladikov/SeedVR2-1.4B](https://huggingface.co/lvladikov/SeedVR2-1.4B)
- **类型**: super-resolution / image-upscaling（one-step diffusion，蒸馏自 ByteDance SeedVR2-7B sharp 分支）
- **新鲜度**: 7-29 刚发布 🔥（3 天）
- **特色**: 6 层蒸馏版，体积小 **5.7×**，推理显存 **~4.6GB vs 7B 的 14-16GB**；带 MLX (Apple Silicon) 权重，M 系列 Mac 也能跑超分
- **注意**: 与标准 SeedVR2 架构（36 层）不兼容，需用配套 ComfyUI 节点/加载器，直接套用原 workflow 会报 ~930 个 missing keys
- **可用性**: Apache-2.0 ✅ 可商用

### [Sparknight/sam3.1-int8-int4-convrot](https://huggingface.co/Sparknight/sam3.1-int8-int4-convrot)
- **类型**: image-segmentation（Meta **SAM 3.1 Multiplex** 的 ConvRot INT8/INT4 量化版）
- **特色**: 采用 ConvRot 权重+激活量化，CLIP 与质量敏感层保留 FP16；**ComfyUI 标准 checkpoint 加载器直接加载**，无需自定义量化节点 — 把"文本描述即可分割"的 SAM 3.1 塞进了消费级工作流
- **可用性**: SAM License（非商用，需按 Meta 条款）；同系列还有 [sam3.1-int8-int4 其他社区版本](https://huggingface.co/muntedslunt/sam3.1-int8-int4-convrot)

### [Ultralytics/YOLO26](https://huggingface.co/Ultralytics/YOLO26)
- **类型**: object-detection（+ instance-seg / pose / OBB / tracking，一套架构全任务）
- **下载量**: 8.1K 次 ❤️119；Ultralytics 主 repo ⭐60,090，8-01 仍在推送
- **特色**: YOLO 家族最新一代（v8 → v11 → v26），保留"一库全任务"的设计哲学，FP16/INT8 导出链路成熟，是工业落地最稳的目标检测基座之一
- **可用性**: AGPL-3.0（商用需注意许可证条款）

### [PaddlePaddle/PP-DocLayoutV3](https://huggingface.co/PaddlePaddle/PP-DocLayoutV3)
- **类型**: image-segmentation / 文档版面分析（PaddleOCR 生态）
- **下载量**: 3.9 万次（另有 safetensors 版 82.5 万次）
- **特色**: 新版版面检测模型，支持中英多语言、表格/标题/图片区域结构化输出，直接对接 RAG 文档解析管线 — 多模态 RAG 的"版面前处理"是刚需
- **可用性**: Apache-2.0 ✅ 可商用

---

## 📰 社区热点

### Chimera: 混合视觉扩散 Transformer 的 Chinchilla 式缩放研究
- **论文**: [Chimera: Designing and Chinchilla-Scaling Hybrid Visual Diffusion Transformers](https://huggingface.co/papers/2607.28611)
- **核心**: 系统研究 hybrid 视觉 DiT（卷积 + attention 混合）的 scaling law，给出类 Chinchilla 的参数量/数据量配比结论 — 对下一代图像生成架构设计有直接指导意义

### ShadowDancer: 视频世界模型统一动力学学习
- **论文**: [ShadowDancer: Teaching Video World Models Any Action...](https://huggingface.co/papers/2607.28362)
- **核心**: 从"视频 + 其阴影/重投影"学习统一的动作-动力学表征，让视频世界模型学会任意动作条件生成 — 视频生成与物理仿真交叉的前沿方向

### Beacon: 何时做 agentic 视觉推理
- **论文**: [Beacon: Knowing When and How to Perform Agentic Visual Reasoning](https://huggingface.co/papers/2607.28595)
- **核心**: 给多模态 agent 加"该不该多步推理"的决策模块，避免简单视觉任务被 over-reasoning 拖慢 — 工程上很有价值的效率优化思路

### MPIE-Bench: 多人交互编辑基准
- **论文**: [MPIE-Bench: Benchmarking Anatomically Plausible Multi-Person Interaction Editing](https://huggingface.co/papers/2607.27616)
- **核心**: 首个关注**多人交互场景下解剖合理性**的图像编辑 benchmark — 现有编辑模型在多人姿态/接触点一致性上普遍翻车，这个评测会推动一波修 bug

### Qwen-UI-Agent: 新一代 GUI Agent 技术报告
- **论文**: [Qwen-UI-Agent Technical Report](https://huggingface.co/papers/2607.28227)
- **核心**: 面向真实世界的 GUI 智能体基础模型技术报告 — 屏幕理解（OCR + 布局 + 图标识别）是它的视觉底座，也是多模态落地最热的赛道之一

---

## 🛠️ 实用工具 & 库

### [vietanhdev/segment-anything-3-onnx-models](https://huggingface.co/vietanhdev/segment-anything-3-onnx-models)
- Meta **SAM 3**（open-vocabulary，自然语言描述即可分割）的 ONNX 导出包，专为 [AnyLabeling](https://github.com/vietanhdev/anylabeling) 标注工具与边缘部署设计
- ONNX Runtime 即可跑（Python/C++/JS），无需完整 PyTorch 栈 — 数据标注管线接入 SAM3 的最短路径
- Apache-2.0 ✅

### [unsloth/FLUX.2-klein-9B-GGUF](https://huggingface.co/unsloth/FLUX.2-klein-9B-GGUF)
- FLUX.2 klein 9B 的 GGUF 量化版（86K 下载），配合 llama.cpp 系工具链把图像生成也带进了 GGUF 生态 — 显存不足的本地部署玩家值得关注

---

## 📦 值得关注的版本更新

### [Qwen/Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)
- **更新亮点**: Qwen 图像编辑系列最新版（对比 2509 版），改用 `QwenImageEditPlusPipeline`，Apache-2.0，下载量已超 22.8 万
- 中文/英文双语文案驱动编辑，社区衍生（face-swap LoRA、Lightning 蒸馏版）活跃

### [FLUX.2-klein 系列周边](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B)
- **更新亮点**: klein-4B 39.2 万下载 / klein-9B 33.8 万下载，且已出现 **FP8**（4.5 万）、**GGUF**（8.6 万）等社区量化版本 — 消费级 GPU 跑 FLUX.2 的生态正在快速补全

---

## 📊 今日扫描总结

| 渠道 | 覆盖情况 |
|------|---------|
| GitHub Trending (Python, daily+weekly) | ✅ 18 + 17 repos scanned |
| GitHub Search (新 repo, 过去 10 天) | ✅ 4 组关键词 ≈ 2,800 repos，精选 top items |
| HuggingFace Models (downloads + trendingScore) | ✅ 8 pipelines ≈ 60 models |
| HuggingFace Daily Papers | ✅ 38 papers scanned |
| PapersWithCode | ⚠️ 页面加载成功但内容为 JS 渲染，无法静态提取 |
| Reddit (r/computervision, r/StableDiffusion) | ❌ Blocked (403)，与昨日相同 |
| GitHub API (repo/模型元数据核验) | ✅ 15+ repos/models verified |

**精选条目**: 15 条 | **主要方向**: VLA 实时化 (TurboVLA, N0-VTLA) · Krea 自研模型开源 · SAM 3/3.1 边缘化与量化 · SeedVR2 蒸馏 · 视频世界模型 (ShadowDancer, Chimera)

---

> 🎯 **编辑注**: 今日三个信号值得跟踪 —— ① **Krea-2** 作为头部图像工具公司转向开源自研模型（虽然 gated），可能带动新一轮 t2i 竞争；② **SAM 3.1 量化 + SAM3 ONNX** 说明"文本提示分割"正在进入标注与边缘部署的实用阶段；③ **TurboVLA / N0-VTLA / WorldByCode** 三个新 repo 同日出现，Embodied AI 的"实时 + 多模态 + 代码化世界"三条路线都在加速。Reddit 连续第二日被墙，建议后续给社区热点渠道配置备用源（如 pullpush 镜像或 HN）。
