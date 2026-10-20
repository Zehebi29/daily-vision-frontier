# 🛠️ 2026-10-20 视觉工业界日报

> 今日扫描 GitHub Trending · GitHub Search API · GitHub Releases · HF Models（8 类 CV pipeline）· HF Daily Papers · Reddit r/computervision · arXiv API，共 **7 类渠道**，精选 9 条

---

## 🔥 今日主线：开源 T2I 从「卷审美」转向「卷排版」

MOSS-Image 用 5B 单流 DiT 把**双语长文本渲染 + bbox 版面控制**当主目标，直指闭源系统最赚钱的信息图/海报场景；另一侧，视觉**工程工具链**集体拥抱 depth（supervision）与边缘 NPU（ultralytics）。

---

## 🔥 热门开源项目

### 1. [OpenMOSS/MOSS-Image](https://github.com/OpenMOSS/MOSS-Image) ⭐1.1k（4 天）· Apache-2.0 ✅
- **什么**: 5B 单流 DiT，从零预训练，主打高保真长文本渲染与 layout-to-image
- **为什么火**: 10-16 放权重，4 天 1.1k★；HF [Base](https://huggingface.co/OpenMOSS-Team/MOSS-Image-Base) 3.5k 下载 / [SFT](https://huggingface.co/OpenMOSS-Team/MOSS-Image-SFT) 470 赞；技术报告 [arXiv:2610.23374](https://arxiv.org/abs/2610.23374) 昨日上线
- **CV 关联**: 补的是开源模型最弱的一环——密集文本与复杂版面；配套 agentic prompt enhancer 输出 `{caption, items[label, bbox]}` 结构化布局
- **生态**: ComfyUI / SGLang / vLLM-Omni day-0 支持；[KohakuMossTrainer](https://github.com/KohakuBlueleaf/KohakuMossTrainer) 声称 **6GB VRAM** 可训 LoRA
- **判断**: 真创新在数据配方与意图解析，不在架构；但它把「可控排版」变成了可复现的开源基线

### 2. [Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth) ⭐3,544 · MIT ✅
- **什么**: 图像地理定位 Agent Skill：给一张照片，返回相机坐标 ± 误差半径、朝向、卫星证据图
- **为什么火**: 4 周 3.5k★/484 fork；EXIF 抹除、无路牌无地标的照片也能解
- **CV 关联**: 不靠 VLM 猜，靠**几何可验证**——桥墩间距当测距尺、阴影反推方位、山脊线匹配 DEM、街景 SIFT 内点校验
- **实测**: 青海戈壁盲测 87 次工具调用 / 32 分钟命中；候选从 14,843 个电力线簇收敛到 1
- **上手**: `git clone` 后把 `SKILL.md` 丢进 Claude Code / Codex / Cursor 即可，纯 Python 脚本

### 3. [speridlabs/iris-3b](https://huggingface.co/speridlabs/iris-3b) · Apache-2.0 ✅
- **什么**: 3B **pixel-space** flow-matching 模型，无 VAE、无 latent，网络直接吐 1024px 像素
- **特色**: 同一套权重微调即得单目深度、修复、超分——作者主张用「生成先验」替代 DINOv2 类判别基座
- **可用性**: 3B 参数，turbo 版 4 步出图约 **0.7s / H100**；HF 319 赞
- **判断**: 「latent 有损、纹理偏置」的论点有意思，但 pixel-space 在高分辨率下的算力账仍不划算

---

## 🤗 值得关注的新模型

### [black-forest-labs/flux-3-image-klein](https://github.com/black-forest-labs/flux-3-image-klein)
- **类型**: FLUX 3 klein 系列官方参考推理代码（10-15 放出，代码 Apache-2.0）
- **热度**: ComfyUI 权重版 [flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy) 43.9 万下载 / 1,035 赞（权重 license 仍是 `other`，非商用需确认）
- **判断**: klein 线走「小参数 + 开放权重 + 官方代码」路线，是 BFL 稳住开源生态的持续投喂；商用请先读 license

---

## 🛠️ 实用工具 & 库

### [roboflow/supervision](https://github.com/roboflow/supervision) v0.31.0 ✅
- **`sv.DepthMap`**: 把深度图直接接到 `Detections` 上，逐目标测距并叠加可视化，不依赖 OpenCV
- **移动镜头修正**: `PolygonZone` / `LineZone` 在相机 pan 时不再错位计数
- **新增**: `KeyPointMeanAveragePrecision`（对齐 pycocotools）、Kosmos-2 / Gemini 3.6/3.7 / MediaPipe hands 直读
- **注意**: **破坏性更新** —— `sv.ByteTrack`、`supervision.keypoint`、`sv.LMM` 已移除，升级前看 Migration guide

### [ultralytics](https://github.com/ultralytics/ultralytics) v8.4.183（今日）
- Axelera Metis 支持 YOLO26 **全任务**（det/seg/depth/pose/OBB/cls），走 NMS-free 路径
- Voyager SDK 1.9 在 COCO128 batch=32 达 **109 img/s**（1.8 为 40 img/s）
- LiteRT 导出新增 Intel CPU/NPU 后端 —— 边缘出货路线又宽了一条

---

## 📰 论文速览（HF Daily Papers）

### [MT Forcing](https://huggingface.co/papers/2610.25404) · 34↑
多轮图像编辑的「漂移」问题：几轮后画质崩、非编辑区被误改。提出 Single-Turn DMD 蒸馏 + 多轮一致性监督，是 unified multimodal model 落地的关键补丁。

### [Text-to-Image Without Language Pretraining](https://huggingface.co/papers/2610.26863) · 2↑
Halcyon 从零预训练 early-fusion AR：0.52B 以 **18.2× 更少算力**超过 LlamaGen-XL/8；对照实验显示 text-only 预训练对 T2I **无增益**。结论很反直觉，值得复现。

### [DeOverlay](https://huggingface.co/papers/2610.26081) · 12↑
视频字幕/logo 去除的 benchmark + source-anchored flow：用 region-weighted flow matching 从源 latent 逐级修正，避免残留与结构扭曲。

---

## 💡 一句话判断

今天没有新架构，只有**三个务实信号**：开源 T2I 开始啃「排版 + 文字」这块硬骨头（MOSS-Image）、视觉 agent 开始用几何而非直觉做验证（geo-sleuth）、工程库开始原生吃 depth（supervision）。闭源在审美上仍领先，但在「可控、可验证、可部署」这三点上，开源的追赶速度比想象中快。
