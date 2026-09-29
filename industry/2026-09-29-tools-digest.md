# 🛠️ 2026-09-29 视觉工业界日报

> 今日扫描 GitHub Trending（全站+Python）· GitHub Search API（8 组 CV 关键词·近 7 天新库）· HF Models（14 个 CV pipeline 趋势榜）· HF Daily Papers · Reddit r/computervision · HN 等 **10 类渠道**，精选 10 条

---

## 🔥 今日主线：「MIT 替代品」刺向 AGPL 护城河

**一**，**LibreYOLO** 用 MIT 授权把 100+ 视觉模型家族（含 YOLO 系、RF-DETR、Depth Anything 3）收进一套 API，训练+导出**内置而非另售**，正面替代 Ultralytics 的 AGPL 商业模式。**二**，**Cognex 5 亿美元收购 RealSense**——工业 2D 视觉巨头用现金买 3D 感知入场券。**三**，**华为 Marigold V2** 证明生成式底座「顺手」做密集预测的路线成立。

---

## 🔥 热门开源项目

### 1. [LibreYOLO/libreyolo](https://github.com/LibreYOLO/libreyolo) ⭐710 · MIT ✅
- **什么**: MIT 授权的一站式 CV 库，20 类任务共用同一套 API
- **为什么火**: Ultralytics 的 YOLO 是 AGPL-3.0，商用要么开源要么买 license；LibreYOLO 收 **100+ 模型家族**（YOLOv9/RF-DETR/RT-DETRv1·v2·v4/D-FINE/DEIM/Depth-Anything-3/Marigold V2/BiRefNet/PP-OCR/Grounding DINO/Qwen3-VL…），训练与导出内置
- **CV 关联**: 检测/分割/姿态/深度/法线/OCR/开放词表全覆盖；**直接读 YOLO 格式数据集**，迁移成本极低
- **上手**: `pip install libreyolo` → `LibreYOLO("LibreYOLO9t.pt")("img.jpg", save=True)`

### 2. [roboflow/rf-detr](https://github.com/roboflow/rf-detr) ⭐9,645 · ICLR 2026
- **什么**: 实时目标检测 / 实例分割架构，COCO SOTA、面向微调
- **为什么火**: 本周发布 **INT8 量化模型**（r/computervision 实测贴），主打边缘/产线部署；Apache-2.0 层级可商用
- **判断**: DETR 系终于在实时场景追上 YOLO，量化版补齐落地最后一环

### 3. [zju3dv/geometry-as-address](https://github.com/zju3dv/geometry-as-address) ⭐19 · 09-28 新建
- 长时**相机轨迹可控**视频生成：把几何当「地址」，将 attention 路由到视觉记忆层
- **判断**: 长视频漂移是当前痛点，用显式几何记忆做「寻址」而非堆上下文，方向正确

---

## 🤗 值得关注的新模型

### [huawei-bayerlab/marigold-v2-0](https://huggingface.co/huawei-bayerlab/marigold-v2-0) · Apache-2.0 ✅
- **类型**: 单目深度 + 表面法线 + 反照率（dense prediction），DiT
- **特色**: 以 **Qwen-Image-Edit-2509 为底座 LoRA 微调**，而非从零训
- **判断**: 生成式基础模型「顺手」做密集预测被验证；几何+材质三合一，合成数据 / 3D 重建可直接吃

### [apple/LensVLM-9B](https://huggingface.co/apple/LensVLM-9B) · apple-amlr
- **类型**: VLM（image-text-to-text），Qwen3.5-9B 底座
- **特色**: 主打**长上下文 + 视觉-文本压缩**（visual-text-compression）
- **判断**: Apple 系统级多模态一步，压缩路线指向端侧长文档 / 长视频理解；**许可非商用友好，商用需查证**

### Qwen-Image-2.1 生态继续统治 T2I
- 主模型 [Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1) 2,633 likes；衍生链：[无审查 GGUF](https://huggingface.co/abenzerps/Qwen-Image-2.1-Uncensored-GGUF)（**115 万下载**）· [Viggle turbo 蒸馏](https://huggingface.co/Viggle/Qwen-Image-2.1-viggle-turbo) · [PrunaAI 量化](https://huggingface.co/PrunaAI/Pruna-Qwen-Image-2.1) · [unsloth GGUF](https://huggingface.co/unsloth/Qwen-Image-2.1-GGUF)
- **判断**: 开源 T2I 事实标准已切到 Qwen 系；社区围绕它的量化/加速/去审查生态**比官方更新更快**

### [inclusionAI/Ming-Image-0.1-Design](https://huggingface.co/inclusionAI/Ming-Image-0.1-Design) · MIT ✅
- 面向**平面设计/海报**的 T2I，强调文字渲染 + 原生 RGBA 透明输出（340 likes，刚上）

---

## 📰 社区热点

### [Cognex 以 5 亿美元收购 RealSense](https://www.reddit.com/r/computervision/comments/1wsy0j7/cognex_agrees_to_buy_realsense_for_500_million/)
- **核心**: 机器视觉龙头 Cognex 从 Intel 手中买下 RealSense，切入**机器人感知 / physical AI / 工厂边缘 AI**
- **判断**: 工业 2D 视觉增长见顶 → 巨头用收购换 3D 感知入场券；传感器+算法一体化竞争加剧

### [GPT-6 Astra 视觉实测：“难视觉，易视觉”](https://huggingface.co/papers/2609.35718) · [Roboflow 评测](https://blog.roboflow.com/gpt-6-astra-vision/)
- 通用大模型正吞掉传统专用 CV 任务，但在**细粒度/几何任务**上仍有明显短板
- **判断**: 对垂直 CV 团队的信号——护城河要建在大模型做不好的「难视觉」上，而非通用识别

### [50 万次车站人脸扫描：0 逮捕、1 误报](https://www.theguardian.com/technology/2026/sep/29/trial-live-facial-recognition-cameras-london-stations-false-positive)（HN 115 分）
- 伦敦车站实时人脸识别试点数据公开，误报率与有效性再引政策争议

### [Qwen3-VL 8B 在 MacBook 上跑 137 份文档](https://www.reddit.com/r/computervision/comments/1wsbuiq/qwen3vl_8b_on_a_macbook_vs_opus_55_sonnet_5_gpt56/)
- 本地 8B VLM 在税务表格上超 GPT-5.6，但**印度日期格式惨败**
- **判断**: 本地文档理解已可用，**格式鲁棒性**才是与前沿模型的分水岭

---

## 📄 HF Daily Papers（视觉相关精选）

- [GeoVerse](https://huggingface.co/papers/2609.35734) — 几何隐空间中的世界一致新视角合成
- [InfiniHand](https://huggingface.co/papers/2609.35743) — 第一人称视频流式世界坐标手部运动估计
- [VGGT-Diff](https://huggingface.co/papers/2609.33253) — 视觉几何（VGGT）遇上扩散，稀疏视角 NVS
- [Structured Residual Connectivity for DiT](https://huggingface.co/papers/2609.33203) — DiT 结构化残差连接
- [How Far from Removing the Visual Encoder?](https://huggingface.co/papers/2609.35457) — 无编码器多模态预训练 scaling law

---

*📅 每日更新 · 数据截至 2026-09-29*
