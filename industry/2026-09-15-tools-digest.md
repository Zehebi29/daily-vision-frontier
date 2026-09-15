# 🛠️ 2026-09-15 视觉工业界日报

> 扫描 GitHub Trending · GitHub Search（近 7 天新仓库）· HF Models（14 pipeline）· HF 新建模型 · HF Daily Papers · HF Blog · HN · Reddit ×2 · TechCrunch 等 **10 类渠道**，精选 8 条

---

## 🔥 今日主线：多模态基座换血 + 「实时可编辑视频」成新战场

**一**，DeepSeek-V4.1-Flash 5 天 32.6 万下载，trending score **2267 vs 第二名 91**（差 25 倍）——主打 KV Cache 压缩却是 image-text-to-text，**上下文效率已成视觉 LLM 主战场**。**二**，HF Papers 榜首 **Vidu S2**（213 赞）与 **PhysBrain 1.5**（165 赞）都指向「实时交互 / 物理世界」，而非静态出图。**三**，OpenAI 3 亿美元收购计算摄影公司 Glass Imaging——**神经 ISP 进入大厂并购阶段**。

---

## 🔥 热门开源项目

### 1. [roboflow/supervision](https://github.com/roboflow/supervision) ⭐50,174 · MIT · 今日 +163★
- **什么**: 「We write your reusable computer vision tools」——检测/分割/跟踪/标注转换通用库
- **为什么火**: 2022 年老库今日杀回 Python Trending，50K★ 已是 CV 工程事实标准；覆盖 detection/segmentation/tracking/视频后处理
- **上手**: `pip install supervision`

### 2. [LynnReal-AI/LynnReal-Omni](https://github.com/LynnReal-AI/LynnReal-Omni) ⭐83 · 2 天新建
- **什么**: 统一视频生成框架——T2V/I2V + 人体/手部姿态引导 + 结构控制 + 全参考生成 + 风格迁移 + 视频修复
- **为什么火**: 9-13 创建、9-15 仍在推；把散落的可控视频生成能力收进一个 repo，配套 HF paper 40 赞

### 3. [ivanmikhnenkov/tinydit](https://github.com/ivanmikhnenkov/tinydit) ⭐9 · [HF 长文](https://huggingface.co/blog/ivanmikhnenkov/tinydit-text-to-image-from-scratch-one-gpu)
- **什么**: 210M 参数 T2I DiT，**单张 RTX PRO 6000、3.5 天、4.2M 图 @256²** 从零训成（rectified flow + 冻结预训练 VAE/文本编码器）
- **为什么火**: 不刷 SOTA，而是公开「数据决定结果 > 架构」的完整可复现配方

---

## 🤗 值得关注的新模型

### [deepseek-ai/DeepSeek-V4.1-Flash](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) · MIT ✅
- **类型**: image-text-to-text 多模态，FP8 权重；README 标题即「Pushing the Limits of KV Cache Compression」
- **热度**: 9-10 发布，**5 天 325,712 下载 / 2,586 likes**，HF 多模态趋势榜断层第一
- **判断**: 真·基座迭代。上下文压缩做深后，直接抬高长视频 / 高分辨率多图推理的性价比
- **可用性**: MIT 可商用；`transformers` 直载

### [huawei-bayerlab/marigold-v2-0](https://huggingface.co/huawei-bayerlab/marigold-v2-0) · Apache-2.0 ✅
- **类型**: depth-estimation——**单模型同时出 depth + surface normal + albedo**（[arXiv 2609.08084](https://huggingface.co/papers/2609.08084)，69 赞）
- **特色**: 从原版 Marigold 的 SD/UNet 换到 **Qwen-Image-Edit-2509 的 DiT + LoRA**，「重访 diffusion transformer 做单目深度」
- **判断**: 深度估计骨干预训练换代样本，对 OOD 泛化与边缘锐度是实打实的改进

### [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)
- **类型**: image-to-video / 音视频统一（text·image·audio ↔ video·audio）
- **热度**: **1,580,077 下载 / 3,932 likes**，视频趋势榜常驻前列
- **判断**: 开源音视频联合生成最强之一；license "other"，商用需查证

---

## 📰 社区热点

### [OpenAI 逾 3 亿美元收购手机相机公司 Glass Imaging](https://techcrunch.com/2026/09/14/openai-buys-smartphone-camera-maker-glass-imaging-for-300-million-report-says/)（HN 09-14）
- **讨论方向**: Glass Imaging 看家本领是**用神经网络校正镜头/传感器光学像差**（计算摄影 / neural ISP）。买它不是为端侧拍照，而是为采集前端与数据入口布局
- **判断**: 视觉团队估值锚点正从「模型」上移到「成像链路」——做 ISP / 去噪 / HDR 的团队值得重新关注

### r/computervision 双热帖：[浏览器版 COLMAP 摄影测量工作台](https://www.reddit.com/r/computervision/comments/1wgwo6z/i_built_a_fully_browserbased_colmap/) · [DINO + Blender 合成数据停车检测](https://www.reddit.com/r/computervision/comments/1wg6of9/trained_a_multispot_parking_occupancy_detector/)
- **核心观点**: 小样本场景靠「**合成数据 + 强 backbone（DINO）**」而非标更多真图——社区共识高度一致，正是 CV 落地当下主流打法；另有 HN [MultiMatte](https://usefeyn.com/blog/multimatte/)（57 分）promptable 抠图，视频 matting 方向可关注

---

## 📚 HF Daily Papers 精选

- **[Vidu S2：实时交互、可编辑、空间化视频生成](https://huggingface.co/papers/2609.11638)**（**213 赞 · 榜首**）— S2-Avatar **实时 720p 数字人**，S2-Editing 实时视频编辑；视频生成从「等渲染」转向「可交互」
- **[PhysBrain 1.5：从 VLM 走向物理基础模型](https://huggingface.co/papers/2609.14973)**（165 赞）— 统一「理解环境 / 生成动作 / 预测未来状态」，VLM→物理世界的关键一跳，机器人 VLA 上游
- **[Kaininja](https://huggingface.co/papers/2609.15659)**（15 赞）+ **[SNAP3D](https://huggingface.co/papers/2609.13146)** — 同解一题：TRELLIS.2 类模型只给**一个融合 mesh**，而编辑/绑定/仿真要**分离且物理合法**的部件；SNAP3D 更约束「不互穿、能连接、重力下不塌」。**与 CAD 装配视觉直接同题，值得精读**
- **[AlayaVista：全景状态 → 透视视频的流式世界模型](https://huggingface.co/papers/2609.14462)**（18 赞）— 用全景表征解决透视模型长 roll-out 丢失屏外内容的老问题

---

## 🛠️ 工具 & 库更新

### [ShadowPEFT 并入 🤗 PEFT 库](https://huggingface.co/blog/shadow-llm/shadowpeft-peft)（约 10 小时前）
- **功能**: 「适配即模型」——带持久隐藏状态的小影子模型（s⁰→s¹→…→sᴸ），而非 LoRA 那样散落各层的独立低秩增量
- **判断**: 对 DiT / 视频模型微调比 LoRA 更具全局协调性，值得实测

### [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) ⭐59,246 · AGPL-3.0 · 今日 +823★
- **功能**: 开源 agentic 视频生产系统——12 条产线、100+ 工具、700+ skill 文件，串起 FLUX/SD/TTS/ffmpeg/Remotion
- **判断**: 视频生产正被 agent skill 化封装，与生成模型互补

---

*Reddit r/StableDiffusion 与 PapersWithCode API 持续受限（403 / 非 JSON），社区数据以 r/computervision、HN、HF 为准。*
