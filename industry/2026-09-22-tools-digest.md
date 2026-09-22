# 🛠️ 2026-09-22 视觉工业界日报

> 扫描 GitHub Trending（全站 + Python）· GitHub Search API（8 组关键词 · 近 7 天新库）· HF Models（14 个 CV pipeline 趋势榜）· HF 新建高赞模型 · HF Daily Papers · HF Blog RSS · Reddit ×2 · HN 等 **10 类渠道**，精选 10 条

---

## 🔥 今日主线：开源 T2I 换代，同时「百 M 小模型」反向突围

**一**，**Qwen-Image-2.1** 一周拿下 HF text-to-image 趋势榜第一（ts **1585**，是第二名量化版的 2 倍）+ GitHub 1,195★，并带出整条量化/加速生态链。**二**，反向路线同周出现：**Supra2-IMG 用 1.04 亿参数从零训出 SOTA 级 T2I**（Apache-2.0）。**三**，**Roboflow 把私有数据 / 权重下载 / 自托管推理全部下放免费层**——CV 平台护城河正从「锁数据」转向「卖算力」。

---

## 🔥 热门开源项目

### 1. [QwenLM/Qwen-Image-2.1](https://github.com/QwenLM/Qwen-Image-2.1) ⭐1,195 · 09-14 新建 · [HF](https://huggingface.co/Qwen/Qwen-Image-2.1) 9 天 **1,654 likes**
- **什么**: 生成 + 编辑统一模型，视觉生成侧 **7B / 32 层 Single-Stream DiT**，混合粒度 attention + prefix KV cache 复用
- **为什么火**: 原生 **RGBA 透明图生成** + 图文生透明图层 + 照片主体抽取三合一；编辑支持 **最多 10 张参考图**、圈选/涂鸦/mask 局部改、人像与商品身份保持
- **判断**: 真换代。这一组合 FLUX.2 / Qwen-Image-Edit-2511 都没有。**qwen-research 许可，非 Apache/MIT，商用需查证**
- **上手**: `git+https://github.com/huggingface/diffusers` → `QwenImage21Pipeline`，2048² 直出 / 40 步

### 2. [zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip) ⭐8,653 · MIT · 今日 **+654★**
- **什么**: AI 视频高光提取与二创剪辑工具
- **判断**: 单日 +654★ 冲上 Python Trending；「长视频 → 爆点片段」这条短视频刚需被做成开箱即用件，视频理解能力的落地封装

### 3. [VAST-AI-Research/Mira-Scene](https://github.com/VAST-AI-Research/Mira-Scene) ⭐18 · 3 天新建 · [paper](https://huggingface.co/papers/2609.23796)
- Pixel-Aligned Layouts 做生成式 3D 场景重建。**判断**: 把**显式布局先验**注入 3D 生成而非纯扩散漫游，对仿真数据合成价值高

### 4. [meshy-dev/meshybench](https://github.com/meshy-dev/meshybench) ⭐10 · Apache-2.0
- image-to-3D 基准，分几何对齐 / 纹理对齐 / mesh 细节三维度打分。**判断**: 图生 3D 长期缺公认评测，官方下场做裁判，直击「demo 好看但 mesh 不能用」

---

## 🤗 值得关注的新模型

### [SupraLabs/Supra2-IMG](https://huggingface.co/SupraLabs/Supra2-IMG) · Apache-2.0 ✅
- **类型**: text-to-image，**104.1M tiny DiT**（D_MODEL 576 / 14 层 / 9 头 / patch 2），256² 输出
- **特色**: 从零训练（frozen **Flan-T5-Base** + **SD-VAE-FT-MSE**），10 epochs 跑完 [FLUX-Reason-6M](https://huggingface.co/datasets/LucasFang/FLUX-Reason-6M)
- **判断**: 继 TinyDiT 后第二例——**数据与配方 > 参数规模**在小尺寸 T2I 上被反复验证；单卡可训可推、Apache-2.0 可商用

### [nvidia/c-foundationstereo-s](https://huggingface.co/nvidia/c-foundationstereo-s) · NVIDIA TAO
- **类型**: 零样本双目深度 / stereo matching（[arXiv 2501.09898](https://arxiv.org/abs/2501.09898)）；直接给 **TensorRT + ONNX** 部署件（320×736 / 576×960 / dynamic）
- **判断**: 少见的「模型即产品」——工业双目深度可量产直用，机器人与产线检测即插即用

---

## 📰 社区热点

### [Roboflow 新定价：免费层拿到私有数据 + 权重下载 + 自托管推理](https://www.reddit.com/r/computervision/comments/1wmix9y/new_roboflow_pricing_free_private_data_weights/)
- **核心**: 私有数据、权重下载与自托管推理、Neural Architecture Search、高级评估全部下放免费层，改纯 credit 消费制；免费额度约 **1 万张 SAM3 自动标注 / 3 万云训任务 / 8 万次云推理每月**
- **判断**: 变现点从锁数据转向卖算力；对自建流水线的团队是**把标注托管出去**的现实窗口（YOLO 系等需商业授权的模型仍要单独买 license）

### Qwen-Image-2.1 社区生态 48 小时爆发（r/StableDiffusion）
- [int8 convrot 实测](https://www.reddit.com/r/StableDiffusion/comments/1wn2sy0/qwen_image_21_int8_convrot_more_tests/) · [2x 加速（质量有损）](https://www.reddit.com/r/StableDiffusion/comments/1wn4j8i/2x_faster_qwen_image_21_for_a_quality_hit/) · [当超分模型用](https://www.reddit.com/r/StableDiffusion/comments/1wmljce/qwen_21_is_very_good_upscaler/) · [输出归你所有](https://www.reddit.com/r/StableDiffusion/comments/1wmbfxz/fyi_you_actually_own_the_outputs_you_generate/)
- **判断**: 开源模型的健康指标不是榜单分，而是**发布后 48 小时内量化/加速/偏门用法的数量**。社区普遍实测其「upscaler / 编辑」副业强于 T2I 主业

### [Divide by depth for instant 3D](https://gabrieloc.com/2026/09/15/perspective.html)（HN **178 分**）
- **讨论方向**: 用「除以深度」做透视正确插值，渲染阶段直接把 2D 图立起来，不需要重建 mesh
- **判断**: 老图形学技巧的新用途——**轻量 3D 伪重建**；产品转台、AR 叠加、立体展示的低成本方案

---

## 📚 HF Daily Papers 精选

- **[WorldCrafter：带隐式 3D-aware 记忆的一致视频世界模型](https://huggingface.co/papers/2609.24984)**（**97 赞 · 榜首**，[repo](https://github.com/TencentARC/WorldCrafter) ⭐185）— **camera-queryable 隐式 3D 记忆** + 历史观测 + 少步蒸馏，支持单图/文本起流的流式长时程探索。世界模型从拼时长转向**拼相机可控 + 长期一致**，本周最值得精读
- **[Transferring the Intelligence of VLMs to Robotic Control](https://huggingface.co/papers/2609.22966)**（95 赞）— 不重训 VLM，而把其表征能力迁移到控制策略，VLA 主流打法的反向思路
- **[Why Do Video Diffusion Models Violate Physics?](https://huggingface.co/papers/2609.23658)**（8 赞）— 把物理不守恒**归因到 attention 机制本身**而非数据，视频生成可信度的必读诊断框架

---

## 🛠️ 工具 & 版本更新

### [abenzerps/Qwen-Image-2.1-GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-GGUF) · 2 天 **182,313 下载 / 881 likes**
- llama.cpp / ComfyUI GGUF 量化件（`comfyui-gguf`），T2I 趋势榜第二。**下载量是原版权重的 11 倍**——「能不能在消费卡上跑」已比原版权重本身更决定传播力

### [FastVideo/FastVideo-FastH3-8-Step-V2](https://huggingface.co/FastVideo/FastVideo-FastH3-8-Step-V2)
- MiniMax-H3 视频生成的**少步蒸馏**版（DMD2），8 步出片，含 text-to-audio-video 联合输出；视频生成成本曲线仍在快速下压

---

*数据说明：GitHub Trending 当日页面仅渲染 8 条，已用 GitHub Search API 按 8 组 CV 关键词补全近 7 天新库；Reddit r/MachineLearning、r/LocalLLaMA 返回 429，社区数据以 r/computervision、r/StableDiffusion、HN 与官方 RSS 为准。*
