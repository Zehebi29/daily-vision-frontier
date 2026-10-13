# 🛠️ 2026-10-13 视觉工业界日报

> 今日扫描 GitHub Trending · GitHub Search API · HF Models（trendingScore 8 类 CV pipeline）· HF Daily Papers · Reddit r/computervision + r/StableDiffusion(RSS) · HN Algolia · GitHub 仓库 API 等 **9 类渠道**，精选 10 条

---

## 🔥 今日主线：Unified Dense 预测升温，「消费/端侧」成关键词

**一**，Google **TIPSv2** 把 depth / 表面法线 / 语义分割塞进同一 backbone（dense-prediction 一体化继续提速）。**二**，端侧军团齐发：**MiniCPM-V-4.7**（35B-A3B MoE + 1B）与 **LiquidAI d1-3B** 同卡「On-Device」赛道。**三**，算力落地侧，ComfyUI 出现**跨双 DGX Spark 分布式生成**节点，DFlash/DGX 生态从 LLM 外溢到影像生成。

---

## 🔥 热门开源项目

### 1. [baidu/Unlimited-OCR](https://github.com/baidu/Unlimited-OCR) ⭐27,235 · MIT ✅
- **什么**: 一句话——「One-shot Long-horizon Parsing」，超长文档/复杂版面一次性解析
- **为什么火**: GitHub Trending Python 榜在榜；HF 镜像 [baidu/Unlimited-OCR](https://huggingface.co/baidu/Unlimited-OCR) 4590 赞 / 117 万下载
- **CV 关联**: 文档理解 + VLM-OCR 融合，直击长文档「截断/重排」痛点，与社区 [r/computervision VLM+OCR 结构化抽取](https://www.reddit.com/r/computervision/comments/1x4v92x/) 讨论同频

### 2. [LINs-lab/UltraText_Bench](https://github.com/LINs-lab/UltraText_Bench) ⭐49 · 新仓（10-08）
- **什么**: 双语（中/英）**图像生成中的文字渲染**评测基准
- **为什么火**: 出生 5 天即登榜；生成模型「画不对字」长期是硬伤，中文尤甚
- **CV 关联**: 补齐 T2I 评测的一块空白，可直接用于中文海报/logo 生成选型

### 3. [Deen-Media/dgx-monarch](https://github.com/Deen-Media/dgx-monarch) ⭐19 · Apache-2.0 ✅
- **什么**: ComfyUI 节点，把图像/视频生成**分布式铺到两台 NVIDIA DGX Spark**
- **为什么火**: 蹭上 DGX Spark（GB10）硬件热；标签含 distributed-inference / diffusion-models
- **判断**: 单机 128GB 统一内存已不够跑大视频模型，「多机 ComfyUI」是务实解法

---

## 🤗 值得关注的新模型

### [Qwen/Qwen-Image-2.1-Turbo](https://huggingface.co/Qwen/Qwen-Image-2.1-Turbo) · trendingScore 640（T2I 榜首）
- **类型**: text-to-image + editing，Qwen-Image-2.1 的**蒸馏加速版**
- **特色**: 10-09 新发，678 赞；生态同步放出 [Viggle-turbo](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo) 与多个 Angle/Scene LoRA
- **判断**: 「基座 + Turbo」双发已是国内厂商标配，少步数推理是落地刚需

### [google/tipsv2-b14-dpt](https://huggingface.co/google/tipsv2-b14-dpt) · dense-prediction 统一模型
- **类型**: **depth + surface-normal + semantic-segmentation 三合一**（arXiv:2604.12012）
- **特色**: 一个 ViT backbone 出三种 dense 输出，b14/g14 双档
- **判断**: 对齐「一个模型多种几何预测」趋势，机器人/3D 感知省一套管线

### [openbmb/MiniCPM-V-4.7-35B-A3B](https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B) · MoE
- **类型**: image-text-to-text，**35B-A3B MoE**，另发 [1B 端侧版](https://huggingface.co/openbmb/MiniCPM-V-4.7-1B)
- **特色**: 「On-Device Model」标签，激活仅 3B；HF 今日 Papers 侧同源讨论活跃
- **判断**: 端侧多模态里少见的 MoE 路线，性价比值得实测

### [speridlabs/iris-3b](https://huggingface.co/speridlabs/iris-3b) · Apache-2.0 ✅
- **类型**: 3B **pixel-space flow-matching「general-vision-learner」**
- **特色**: 一个骨干同时挂 text-to-image / depth-estimation / image-restoration
- **判断**: 把「生成」当通用视觉学习范式的尝试，方向新但需警惕「换皮多任务」

---

## 📰 社区热点

### [Kinematic 0.5.0：65 个本地 ML 模型原生 GPU 运行，开源免费](https://www.reddit.com/r/computervision/comments/1x49zr7/kinematic_050_is_out_65_local_ml_models_running/)
- r/computervision 热帖；一个本地推理工作台塞进 65 个 CV 模型，主打免云、GPU 原生
- **判断**: 本地 CV 工具箱拥挤赛道里的「一站式」打法，适合快速原型

### [Fast non-autoregressive OCR model for manga](https://www.reddit.com/r/computervision/comments/1x4rxy5/)
- 自建**非自回归**日漫 OCR，主打速度；对白气泡 / 竖排日语是通用 OCR 难点
- **判断**: 非自回归 OCR 在专用域追速度，是一条被 VLM-OCR 挤到边缘但仍有价值的路线

---

## 🛠️ 实用工具 & 库

### [gwenn-ha-dev/Siliconed](https://github.com/gwenn-ha-dev/Siliconed) ⭐5 · Apache-2.0
- **功能**: macOS 原生（Swift + Metal, fp32）本地跑 **Z-Image Turbo / Qwen-Image-2.1** 生成与编辑，与 diffusers 对拍
- **判断**: Apple Silicon 上「原生 app 而非 Python」的本地生成尝试，稀缺

---

## 📦 值得关注的版本 / 论文

### [SPLATIFY (arXiv:2610.09116)](https://huggingface.co/papers/2610.09116) · HF Daily Papers 在榜
- **亮点**: 多 agent 框架把 **3DGS 论文自动转成可训练的 gsplat 代码**（Paper→Code）
- **判断**: 3D Gaussian Splatting 复现成本高，paper-to-code 提效工具对 3D 视觉社区是刚需

---

*📅 数据来源: GitHub Trending & Search API · GitHub Repos API · HuggingFace Models & Daily Papers · Reddit RSS · HN Algolia*
