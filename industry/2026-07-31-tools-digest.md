# 🛠️ 2026-07-31 视觉工业界日报

> 今日扫描了 GitHub Trending · HuggingFace Models · HuggingFace Papers · GitHub Search 等 6 个渠道

---

## 🔥 热门开源项目

### 1. [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2)
- **什么**: Microsoft 开源的最新 3D 生成大模型（4B 参数），基于 Native and Compact Structured Latents 实现 high-fidelity image-to-3D
- **为什么火**: ⭐ 9,620 stars，GitHub Python 趋势榜前排。TRELLIS 是当下最火的开源 3D 生成方案之一，v2 版本在 token 效率和生成质量上大幅提升
- **CV 关联**: 3D 生成 · Image-to-3D · Structured Latents
- **快速上手**: `git clone https://github.com/microsoft/TRELLIS.2` — 基于 PyTorch，需 GPU (推荐 A100)

### 2. [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- **什么**: 百度出品的轻量级 OCR 工具包，支持 100+ 语言，可从 PDF/图片中提取结构化数据
- **为什么火**: ⭐ 86,597 stars，今日 Python 趋势榜第 13 位。新增 PaddleOCR-VL 多模态能力、PDF-to-Markdown 管线和 RAG 集成
- **CV 关联**: OCR · Document Parsing · Layout Analysis · Text Detection
- **快速上手**: `pip install paddlepaddle paddleocr` 即可使用

### 3. [deepfakes/faceswap](https://github.com/deepfakes/faceswap)
- **什么**: 老牌开源人脸替换/深度伪造工具，持续活跃
- **为什么火**: ⭐ 56,716 stars，今日再次登上 Python 趋势榜（第 9 位）。社区极其活跃，持续更新训练 pipeline 和推理优化
- **CV 关联**: Face Detection · Face Alignment · GAN-based Face Swapping
- **快速上手**: `git clone https://github.com/deepfakes/faceswap`

### 4. [Fooocus](https://github.com/lllyasviel/Fooocus)
- **什么**: 专注 prompt 和生成体验的 Stable Diffusion 前端界面，lllyasviel 出品
- **为什么火**: ⭐ 51,648 stars，今日 Python 趋势榜。以「无需调参即可出好图」的理念受到大量用户喜爱，内置风格化和精调功能
- **CV 关联**: Text-to-Image · Stable Diffusion · Image Generation UI
- **快速上手**: `git clone https://github.com/lllyasviel/Fooocus && cd Fooocus && pip install -r requirements.txt`

---

## 🤗 值得关注的新模型

### [FLUX.2-dev](https://huggingface.co/black-forest-labs/FLUX.2-dev)
- **类型**: Image-to-Image / 文生图 / 图生图
- **下载量**: 136 万次
- **特色**: Black Forest Labs 的下一代 FLUX 系列。相比 FLUX.1，FLUX.2 在生成质量、编辑能力、结构控制上有显著提升。同期发布的还有 **FLUX.2-klein-9B**（337K 下载）和 **FLUX.2-klein-4B**（391K 下载），提供不同规模的蒸馏版本
- **可用性**: 非商业许可（dev），需通过 bfl.ai 申请商用许可

### [Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)
- **类型**: Text-to-Image
- **下载量**: 114 万次 | ❤️ 5,054
- **特色**: 阿里通义团队出品的高效文生图模型，在速度和质量间取得出色平衡。基于 ZImagePipeline，支持 Diffusers 集成
- **可用性**: 可商用，safetensors 格式，适合消费级 GPU

### [Qwen-Image-Edit-2509](https://huggingface.co/Qwen/Qwen-Image-Edit-2509)
- **类型**: Image-to-Image (编辑)
- **下载量**: 41 万次 | ❤️ 1,222
- **特色**: 通义千问团队的图像编辑模型，支持中英文指令驱动的图像编辑任务，是 Qwen 多模态生态的重要补充
- **可用性**: 可商用，Diffusers 集成

### [RMBG-2.0](https://huggingface.co/briaai/RMBG-2.0)
- **类型**: Image Segmentation (Background Removal)
- **下载量**: 68.7 万次
- **特色**: BRIA AI 的下一代背景去除模型，相比 v1 在边缘细节和多类别物体上表现更好。支持 ONNX 推理，适合生产部署
- **可用性**: 可商用，轻量级（safetensors + ONNX）

### [BiRefNet](https://huggingface.co/ZhengPeng7/BiRefNet)
- **类型**: Image Segmentation / Background Removal
- **下载量**: 76.3 万次
- **特色**: 基于双向参考网络的高质量分割模型，在背景去除和 mask 生成任务上表现优异。目前社区下载量增长迅速
- **可用性**: 可商用，safetensors

---

## 📰 社区热点

### TurboVLA: 在 RTX 4090 上以 32Hz 运行的实时 VLA 模型
- **论文**: [TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090](https://huggingface.co/papers/2607.27205)
- **核心**: 将 VLA (Vision-Language-Action) 模型压缩到 <1GB VRAM，在 RTX 4090 上达到 32Hz 推理速度。这为机器人 + 边缘部署打开了新可能
- **意义**: 实时性一直是 VLA 落地的瓶颈，TurboVLA 通过模型压缩和架构优化大幅降低了门槛
- **热度**: HF Daily Papers 今日首页推荐

### Explicit Layer Modeling: 视频物体插入与图层分解
- **论文**: [Explicit Layer Modeling for Video Object Insertion and Layer Decomposition](https://huggingface.co/papers/2607.25802)
- **核心**: 提出显式图层建模方法，在视频中实现物体插入和前景/背景分解。将视频分解为多个 RGBA 层，支持逐层的编辑和合成
- **意义**: 视频编辑领域的重要进展，特别是在多对象场景下的图层分离

### DistillAlign: 自回归视频蒸馏的协调策略
- **论文**: [DistillAlign: Coordinating Mode Covering and Mode Seeking in Autoregressive Video Distillation](https://huggingface.co/papers/2607.26811)
- **核心**: 在自回归视频生成模型中，协调"模式覆盖"和"模式寻找"两种蒸馏策略
- **热度**: GitHub 48 stars，10 位作者的联合工作

---

## 🛠️ 实用工具 & 库

### [FaceSwap](https://github.com/deepfakes/faceswap)
- 深度伪造的全流程工具包：人脸检测、对齐、训练、合成
- 支持自定义数据集训练、GPU 加速、多种 encoder 架构

### [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- PDF/图片 → LLM-ready 结构化数据的全功能 OCR 管线
- 支持 100+ 语言、表格识别、版面分析、文档翻译
- 特别适合 RAG 场景的 PDF 解析

---

## 📦 值得关注的版本更新

### [FLUX.2 系列](https://huggingface.co/black-forest-labs/FLUX.2-dev)
- **更新亮点**: Black Forest Labs 正式发布 FLUX.2 系列，包括完整版 (dev) 和两个 klein 蒸馏版 (9B/4B)
- 增强的图像编辑能力 (Kontext-style editing)
- 更好的结构控制 (Canny/Depth conditioning)
- klein 版本面向消费级 GPU 做了大幅优化

### [TRELLIS.2](https://github.com/microsoft/TRELLIS.2)
- **更新亮点**: 相比 v1，在结构化 latent 的紧凑性、生成质量和推理速度上均有明显提升
- 4B 参数，支持 text-to-3D 和 image-to-3D

---

## 📊 今日扫描总结

| 渠道 | 覆盖情况 |
|------|---------|
| GitHub Trending (Python) | ✅ 18 repos scanned |
| HuggingFace Models | ✅ 6 pipelines, ~30 models |
| HuggingFace Papers | ✅ ~25 papers scanned |
| GitHub Search (new CV repos) | ✅ 15 repos scanned |
| Reddit | ❌ Blocked (403) |

**精选条目**: 13 条 | **主要方向**: 3D 生成 (TRELLIS.2) · 图像生成 (FLUX.2, Z-Image-Turbo) · OCR (PaddleOCR) · VLA (TurboVLA) · 视频编辑 (Explicit Layer Modeling)

---

> 🎯 **编辑注**: 今日最值得深入关注的是 **FLUX.2 系列**和 **TRELLIS.2**。FLUX.2 的 klein 蒸馏版本（4B/9B）让消费级 GPU 运行高质量文生图成为可能；TRELLIS.2 则代表了 3D 生成领域的新范式。TurboVLA 在 VLA 实时性上的突破也值得追踪。
