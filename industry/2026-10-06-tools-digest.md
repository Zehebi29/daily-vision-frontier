# 🛠️ 2026-10-06 视觉工业界日报

> 今日扫描 GitHub Trending · GitHub Search API · HF Models（4 类 CV pipeline 趋势榜）· HF Daily Papers · Reddit r/computervision + r/StableDiffusion · HackerNews · ComfyUI Releases 等 **8 类渠道**，精选 10 条

---

## 🔥 今日主线：Agent 反攻 CAD，检测模型「llama.cpp 化」

**一**，**text-to-cad** 冲到 GitHub Trending 头部（⭐17.7k），把 STEP/GLB/STL/3MF 生成、可制造性(DfM)检查、工程图全部交给 coding agent。**二**，**locate-anything.cpp** 把 NVIDIA 开放词表检测模型移植到 ggml——检测也能像 LLM 一样在 CPU 端「gguf 化」跑。**三**，视频生成三连发（MiniMax-H3 / Prism / Kandinsky 6），**音频同生成**成开源视频模型新标配。

---

## 🔥 热门开源项目

### 1. [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad) ⭐17,728 · MIT ✅
- **什么**: 给 coding agent 装上「CAD 超能力」，本地生成 STEP/GLB/STL/3MF
- **为什么火**: 今日 Trending 头部；支持 DfM 检查、自动出工程图，并直连 3D 打印/钣金/CNC 服务；底层 build123d + Open CASCADE，`pip install cadgen`
- **CV 关联**: 打通「工程图生成 → CAD 视觉理解 → 可制造几何」闭环，agent 直接产出可下单的零件

### 2. [mudler/locate-anything.cpp](https://github.com/mudler/locate-anything.cpp) ⭐607 · C++
- **什么**: NVIDIA LocateAnything-3B 的 ggml 移植，开放词表目标检测 / visual grounding
- **为什么火**: 检测模型首次「llama.cpp 化」，GGUF 权重 [`mudler/locate-anything.cpp-gguf`](https://huggingface.co/mudler/locate-anything.cpp-gguf)（下载 1090 万）可在消费级 CPU 跑；配套 web UI [gammahazard/locate-anything](https://github.com/gammahazard/locate-anything) ⭐164
- **判断**: 开放词表检测的「端侧可部署」拐点，改 prompt 即可定位新类别，无需重训

---

## 🤗 值得关注的新模型

### [MiniMaxAI/MiniMax-H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) · 348万下载 / 5,927 赞
- **类型**: image-text-to-video，支持 文/图/视频 → 音画同生（audio+video joint）
- **特色**: 社区 LoRA 生态爆发（角色替换 ⭐315、360° 环绕 ⭐223）；Reddit 实测 1984×1120 / 2K 生成
- **判断**: 开源视频生成第一梯队，音频协同 + 活跃 LoRA 生态是护城河

### [black-forest-labs/FLUX.2-klein-4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B) · Apache-2.0 ✅ · 39.9万下载
- **类型**: text-to-image + 多参考 image editing，统一 4B rectified-flow 架构
- **特色**: 端到端 **<1 秒**、仅需 ~13GB VRAM（RTX 3090/4070 可跑），BFL 迄今最快模型；另有 klein-9B / fp8 变体
- **判断**: 实时图像生成真正落到消费显卡，Apache-2.0 可商用，本地交互式应用最佳底座

### [Qwen/Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1) · 3,023 赞
- 通义 Qwen-Image 迭代版，新增 **RGBA 透明通道**输出，文生图 + 编辑一体；配套 [Qwen-Image-Edit-2511](https://huggingface.co/Qwen/Qwen-Image-Edit-2511)（Apache-2.0，25.8万下载）

### [briaai/VRMBG-3.0](https://huggingface.co/briaai/VRMBG-3.0) · 视频抠像
- **类型**: video background removal / matting，自回归、实时、时序一致
- **判断**: 从单帧 RMBG-2.0（44万下载）延伸到**视频**背景移除，直击 temporal consistency 这一硬伤

### [Prism](https://huggingface.co/papers/2610.05416) · Tencent Hunyuan + Fudan · MIT
- **类型**: 原生 **2K 联合视频+音频**生成，Dynamic Sparse Attention 训练范式
- HF 今日 Papers 在榜，Reddit 已确认代码放出，值得关注训练效率设计

---

## 📰 社区热点

### [极端镜面反射数据集：机器人镜面战衣（425 张 RAW/JPEG）](https://www.reddit.com/r/computervision/comments/1wyslkw/)
- r/computervision：专为**基准测试 CV 与深度估计算法在镜子/高镜面反射下的鲁棒性**而拍，直击当前模型经典失效场景
- **判断**: 镜面/反射是单目深度与 3D 重建的盲区，这类 edge-case 数据集很实用

### [Kandinsky 6.0 Video：音视频同步生成基础模型](https://huggingface.co/papers/2610.05608)
- HF 今日 Papers **榜首**，主打同步音画生成；Reddit 同步热议，与 MiniMax-H3/Prism 形成「视频+音频」三角

### [M-plicits: Neural Implicit Surfaces via Nested Multiscale Residuals (NeurIPS 2026)](https://www.reddit.com/r/computervision/comments/1wy7xnt/)
- 嵌套多尺度残差的神经隐式表面，NeurIPS 2026 论文在 r/computervision 自荐，属 3D 重建方向

---

## 📦 值得关注的版本更新

### [ComfyUI v0.39.0](https://github.com/comfyanonymous/ComfyUI/releases) · 2026-10-05
- 新增 **Minimax-H3 VAE** 支持（LynnReal light）、修复 Qwen-Image 2.1 的 int8/int4 cache 崩溃、默认提升 Save Video 编码质量；生态已全面跟上视频模型

### [well9472/Nanosaur2-670M](https://huggingface.co/well9472/Nanosaur2-670M) · 6.7亿参数
- 极小扩散模型，Reddit 实测 **RTX 5090 上 7 img/s**；适合超低延迟 / 批量生成实验

---

*📅 数据来源: GitHub Trending & Search API · HuggingFace Models & Papers · Reddit RSS · HackerNews · ComfyUI Releases*
