# 🛠️ 2026-07-30 视觉工业界日报

> 今日扫描了 GitHub Trending · GitHub Search (新仓库) · HuggingFace Models · HuggingFace Papers · Reddit · PapersWithCode 等 12 个渠道
>
> 🎯 精选 14 条，涵盖 3D 生成 · 多模态 VLM · 视频理解 · 图像生成加速 · 扩散模型蒸馏 · Gaussian Splatting · VLM 评测

---

## 🔥 热门开源项目

### 1. [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2)
- **什么**: Structured 3D Generation 的升级版 — Native + Compact Structured Latents 用于 3D 生成
- **为什么火**: ⭐9.3K，今天登上 GitHub Python Trending！比第一代 TRELLIS 更紧凑更快，直接生成带结构的 3D 资产
- **CV 关联**: 3D 生成 / 结构化几何 / 大规模 3D 资产创建
- **快速上手**: `git clone https://github.com/microsoft/TRELLIS.2.git && cd TRELLIS.2 && pip install -e .`

### 2. [PipeNetwork/kimi-k3-mlx](https://github.com/PipeNetwork/kimi-k3-mlx)
- **什么**: Moonshot AI 的 Kimi-K3 (2.78T 多模态 MoE) 的 MLX 移植版，支持 streaming converter、REAP expert pruning、多语言 expert-overlap 分析
- **为什么火**: ⭐254（创建仅数天），在 Apple Silicon 上跑 2.78T 多模态 MoE 是重大工程成就
- **CV 关联**: 多模态视觉理解 — 原模型在图文理解上很强
- **快速上手**: `pip install mlx mlx-lm && git clone https://github.com/PipeNetwork/kimi-k3-mlx.git`

### 3. [MoonshotAI/PerceptionBench](https://github.com/MoonshotAI/PerceptionBench)
- **什么**: 用于评估 MLLM 原子级视觉感知能力的 benchmark，从 MLLM 的推理/知识中分离出纯粹的感知能力评测
- **为什么火**: ⭐124（创建仅一周），MoonshotAI 出品，同时被 HuggingFace Papers 收录
- **CV 关联**: VLM 评估 / 视觉感知基准
- **快速上手**: `git clone https://github.com/MoonshotAI/PerceptionBench.git`

### 4. [OpenMOSS/OmniVAE](https://github.com/OpenMOSS/OmniVAE)
- **什么**: 音视频联合 VAE（OmniVAE: An Audio-Video VAE with Cross-Modal Alignment for Joint Generation）
- **为什么火**: ⭐61（创建 4 天），OpenMOSS 团队 — 能够同时处理音频和视频的 VAE，为联合生成打下基础
- **CV 关联**: 视频生成 / 多模态 VAE / 音视频对齐
- **快速上手**: `git clone https://github.com/OpenMOSS/OmniVAE.git`

### 5. [jbaehova/oppa-gen](https://github.com/jbaehova/oppa-gen)
- **什么**: 面向 Agent 的多模态生成客户端（Agent-Driven Client for Multimodal Generation）
- **为什么火**: ⭐57，把图像/视频生成能力封装成 Agent 可调用的客户端
- **CV 关联**: Agent × 视觉生成接口 / 多模态工具链
- **快速上手**: TypeScript 项目，`npm install`

### 6. [mupozg823/timecode-agent](https://github.com/mupozg823/timecode-agent)
- **什么**: 基于 Transcript 的视频理解工具 — 时间戳证据账本、延迟视觉验证和编辑交接（EDL/OTIO/FCPXML/SRT）
- **为什么火**: ⭐47，视频理解和编辑工作流的 Agent 化，输出专业剪辑格式
- **CV 关联**: 视频理解 / 视频编辑自动化
- **快速上手**: `pip install timecode-agent`

### 7. [Lucas1479/Amadeus](https://github.com/Lucas1479/Amadeus)
- **什么**: 实时多模态 AI 桌面交互 Agent（Real-Time Multimodal AI Agent for Desktop Interaction）
- **为什么火**: ⭐42，用视觉理解桌面 + 语音交互，类似多模态版 Desktop Agent
- **CV 关联**: 屏幕理解 / GUI Agent / 多模态交互
- **快速上手**: 见 repo README

### 8. [yihui-dev/yh-chatcut-skills](https://github.com/yihui-dev/yh-chatcut-skills)
- **什么**: ChatCut 视频编辑的开源技能包 — 时间戳精确的 SRT 生成
- **为什么火**: ⭐38，让 Agent 能精确剪辑视频
- **CV 关联**: 视频编辑 / 时间戳对齐
- **快速上手**: `git clone https://github.com/yihui-dev/yh-chatcut-skills.git`

### 9. [arloopa/UnitySplats](https://github.com/arloopa/UnitySplats)
- **什么**: Unity 6 跨平台 3D Gaussian Splatting 包 — 支持 Built-in/URP/HDRP、PLY/SOG/SPZ/GLB 格式、XR、移动端、WebGL 2
- **为什么火**: ⭐21，填补了 Unity 生态中 3DGS 原生支持的空白
- **CV 关联**: 3D 视觉 / Novel View Synthesis / Gaussian Splatting
- **快速上手**: Unity Package Manager 安装

### 10. [Rouf0x/splatfpv](https://github.com/Rouf0x/splatfpv)
- **什么**: 浏览器端 FPV 无人机模拟器 — 在 3D Gaussian Splat 场景中飞行
- **为什么火**: ⭐15，3DGS × 游戏化交互，非常新颖的用法
- **CV 关联**: 3DGS 实时渲染 / 沉浸式体验
- **快速上手**: 浏览器直接打开

---

## 🤗 值得关注的新模型

### [FLUX.2-klein-9B / FLUX.2-klein-4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B)
- **类型**: text-to-image / image-to-image (Flux 架构)
- **下载量**: klein-9B: 33.7万 / klein-4B: 38.7万
- **特色**: Black Forest Labs 的 FLUX.2 小型化模型系列，9B 和 4B 参数。保持高质量的同时降低推理成本
- **可用性**: 非商用 license / 需要 16-24GB VRAM 推理

### [Mage-Flow-Turbo](https://huggingface.co/numen-tech/Mage-Flow-Turbo)
- **类型**: text-to-image (Flow Matching + Distillation)
- **特色**: 基于 Mage 架构的加速版，用蒸馏技术把多步 flow matching 压缩到少步推理
- **可用性**: 新发布（2026-07-29），值得关注后续发展

### [Qwen-Image-Edit-2509](https://huggingface.co/Qwen/Qwen-Image-Edit-2509)
- **类型**: image-to-image / 图像编辑
- **下载量**: 40.4万
- **特色**: 通义千问的图像编辑模型，支持 instruction-based 编辑，统一中文/英文输入
- **可用性**: 可商用（Qwen License）

---

## 📰 社区热点（HuggingFace 每日论文精选）

### [Wonder: Video World Model Done Better](https://huggingface.co/papers/2607.26037)
- 作者: Jiacong Xu, Hanwen Jiang, Zhixin Shu (Adobe Research) 等
- 核心: 一个实时、可控制摄像头的视频世界模型 — 给定图片或条件视频，用户可以自由导航探索场景，发现未观测区域并在长时间范围内保持一致性
- 热度: 🔥 Paper of the Day

### [Mage-VL: Efficient Codec-Native Streaming Multimodal Foundation Model](https://huggingface.co/papers/2607.24904)
- 作者: Senqiao Yang, Kaichen Zhang (Microsoft) 等
- 核心: 解决 VLM 的"Moravec's paradox" — 擅长复杂离线推理但流式感知效率低。提出定制 tokenizer Mage-ViT 替换均匀帧采样
- 重要性: 流式多模态理解的新范式

### [Parallel Decoding Distillation for Fast Image and Video Generation](https://huggingface.co/papers/2607.26004)
- 作者: Neta Shaul, Chao Liu, Arash Vahdat (NVIDIA) 等
- 核心: 提出并行解码蒸馏 — 将扩散/流模型的迭代采样压缩到少步生成，同时适用于图像和视频
- 重要性: 视频生成加速的关键技术

### [MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities](https://huggingface.co/papers/2607.25948)
- 作者: Mingqiao Ye, Zhaochong An (Cledar) 等
- 核心: Decoder-only 架构做任意模态到任意模态的生成，无需 encoder-decoder 或扩散架构
- 重要性: 统一多模态建模的新方向

### [PerceptionBench: Evaluating Atomic Visual Perception in MLLMs](https://huggingface.co/papers/2607.24957)
- 作者: Zichao Lin, Yifeng Xie (MoonshotAI) 等
- 核心: 将 MLLM 的纯视觉感知能力从推理/知识中解耦评估，揭示模型在基础感知任务上的真正瓶颈
- 重要性: 为 VLM 提供了更有针对性的评估框架

### [ReDesign: Recovering Editable Design Structures from Images](https://huggingface.co/papers/2607.25565)
- 作者: Jooyeol Yun, Jintae Park (NAVER) 等
- 核心: 从栅格图像中恢复可编辑的设计文件层级结构（排版、矢量、颜色、分组、图层顺序）
- 重要性: CV × Design 工具的交叉领域，有实际工业价值

### [Visual Prompt Engineering for Video Models](https://huggingface.co/papers/2607.25537)
- 作者: Robert Geirhos, Yuxuan Li (Google DeepMind) 等
- 核心: 像语言模型的 prompt engineering 一样，研究如何自动修改任务图像以提升视频基础模型的视觉推理
- 重要性: 提示工程从 NLP 延伸到视频领域

---

## 🛠️ 实用工具 & 库

### [HeadCast: Casting Attention Heads for Efficient Autoregressive Video Generation](https://github.com/sjlgaga/HeadCast)
- **功能**: 自回归视频生成中的注意力头裁剪 — 将部分注意力头"投射"到其他头，显著加速推理
- **CV 关联**: 视频生成加速 / Transformer 架构优化
- ⭐5（新仓库）

### [let-ai-read-video](https://github.com/xiaohui5206/let-ai-read-video)
- **功能**: 100% 本地运行的视频阅读 skill — faster-whisper GPU 转录 + ffmpeg 场景感知抽帧，双通道带时间戳
- **亮点**: 1 小时视频 3-5 分钟读完，数据不出机器，适合隐私敏感场景
- **CV 关联**: 视频理解 / 多模态 Agent

### [CliffWade/hermes-image-studio](https://github.com/CliffWade/hermes-image-studio)
- **功能**: Hermes Agent 的 AI 图像生成插件 — 10 个预设、6 种 FLUX + GPT Image 模型、图生图、超分辨率、批量生成
- **CV 关联**: 图像生成 / Agent 工具链

---

## 📦 值得关注的版本更新

### [TRELLIS.2](https://github.com/microsoft/TRELLIS.2) — 持续更新中
- 3D 结构生成的最新 SOTA，相比第一代更紧凑的原生 latent 空间
- 仍在高频迭代中 ⭐9.3K

### [FLUX.2-klein 系列](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B) — 正式发布
- Black Forest Labs 的 klein 蒸馏版本，9B 和 4B 两个尺寸
- 适合部署到边缘设备和消费级 GPU

---

## 📊 数据总览

| 指标 | 值 |
|------|-----|
| 扫描渠道 | 12 |
| 精选条目 | 14 |
| 新 GitHub 仓库 (本周) | 40+ 条扫描，精选 10 个 |
| HF 热点论文 | 7 篇精选 |
| 重点领域 | 3D 生成 · 视频理解 · MLLM 评估 · 图像加速 · 3DGS |

---

*Generated at 2026-07-30 by CV Industry Agent*
