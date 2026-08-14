# 🛠️ 2026-08-14 视觉工业界日报

> 今日扫描了 GitHub Trending · GitHub Search API（3 组关键词，近一周新仓库）· HuggingFace Models（8 个 pipeline 趋势榜/下载榜 + trendingScore）· HF Daily Papers · Hacker News · Reddit（连续第 7 天 403）· PapersWithCode（API 仍异常）等 7 类渠道，共精选 15 条

---

## 🔥 今日主线：图像→3D 桌面化 + Krea 2 生态成型 + 视频模型量化加速 + Agent「视觉插件」继续爆发

四股暗流拼出今日图景：**第一**，`lightningpixel/modly`（⭐5434）杀回 GitHub Trending —— 纯本地 GPU 的「图片→3D 模型」桌面应用，image-to-3D 正式进入端侧消费级赛道；**第二**，Krea 2 的开源生态开始成型 —— 社区已出现 Kroma v0.2 全量微调（trendingScore 127），Krea-2-Turbo 在 HF 累计 8.7 万下载；**第三**，视频生成量化加速成为显学 —— MiniMax-H3 的 GGUF 量化版 11 天拿下 60.6 万下载；**第四**，DeepSeek Harness 发布 developer preview（HN 555 分），一天之内 GitHub 上就冒出 dsh-vision-router / dsh-plugin-deepeye 等视觉插件 —— 「给 agent 补眼睛」正在变成独立生态位。

---

## 🔥 热门开源项目

### 1. [lightningpixel/modly](https://github.com/lightningpixel/modly)
- **什么**: 纯本地 GPU 运行的桌面应用 —— 从图片生成 3D 模型（image-to-3D），TypeScript 写的桌面客户端
- **为什么火**: ⭐5434（今日 GitHub Trending All 榜在列，8-13 仍在推送）。self-hosted、完全离线、一次买断的 3D AIGC 工具 —— 「AI 建模进本地桌面」的标杆
- **CV 关联**: Image-to-3D · Neural Rendering · 消费级 3D 重建
- **快速上手**: `git clone https://github.com/lightningpixel/modly`（桌面 app，需 GPU）

### 2. [a2307588073-arch/zynq-yolov3-tiny-accelerator](https://github.com/a2307588073-arch/zynq-yolov3-tiny-accelerator)
- **什么**: Xilinx Zynq-7000（XC7Z100）FPGA 上的 **INT8 单类 YOLOv3-Tiny 硬件加速器**，含 OV5640 摄像头→HDMI 的 bare-metal demo，配套 PyTorch 训练与参数导出工具
- **为什么火**: ⭐44（8-13 创建，一天内）—— Verilog + Vivado/Vitis 全流程，把 YOLO 推理做进可编程逻辑；边缘 CV 硬件加速方向冷门但硬核
- **CV 关联**: Edge CV · FPGA 加速 · INT8 量化部署（端侧低延迟检测的教科书案例）
- **快速上手**: `git clone https://github.com/a2307588073-arch/zynq-yolov3-tiny-accelerator`

### 3. [Bujiazi/HPSD](https://github.com/Bujiazi/HPSD)
- **什么**: 论文 **HPSD: Hybrid-Policy Self-Distillation for Text-Image-to-Video Diffusion Models** 的官方实现（8-13 发布）
- **为什么火**: 新鲜官方代码（8-13 创建，8-14 仍在更新）。把「文本+图」双条件视频扩散做混合策略自蒸馏 —— 图像可控视频生成蒸馏路线的又一补充
- **CV 关联**: Video Generation · Diffusion Distillation · Text-Image-to-Video
- **快速上手**: `git clone https://github.com/Bujiazi/HPSD`

### 4. [ReyChiaro/StyleController](https://github.com/ReyChiaro/StyleController)
- **什么**: 论文 *Staying True to the Origin: Continuous Image Stylization with Smooth Transitions* 的官方实现 —— **连续风格化**：风格强度可连续调节、风格间平滑过渡，代码 + 数据集全开源
- **为什么火**: ⭐4（8-08 创建，MIT）。基于 diffusers / FLUX / Qwen 生态的 style transfer 新范式 —— 不是「一张图一种风格」，而是风格空间里的连续插值
- **CV 关联**: Style Transfer · Diffusion · Flow Matching
- **快速上手**: `git clone https://github.com/ReyChiaro/StyleController`

---

## 🤗 值得关注的新模型

### [lodestones/Kroma](https://huggingface.co/lodestones/Kroma) v0.2
- **类型**: text-to-image（Krea 2 全量微调）
- **热度**: ❤️270 / trendingScore 127（T2I 榜第 2，仅次于 FLUX.1-dev）
- **特色**: **Krea 2 开源生态的第一个社区全量微调** —— ComfyUI 原生可用、提供完整采样配置与 workflow。Krea 2 权重开放后社区衍生层快速生长，这是「商用模型开源 → 微调生态」的标准剧本
- **可用性**: ⚠️ krea-2-community-license（需核对条款）；配套 [krea/Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo)（❤️855，8.7 万下载）

### [LiquidAI/LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B)
- **类型**: vision-language（3B 小模型）
- **热度**: ❤️121 / trend 121（8-11 上架，极新）
- **特色**: Liquid AI 的 **LFM 2.5 视觉版** —— 3B 规模把 VLM 卷到「单卡/端侧可跑」区间，走 Liquid Foundation Model 的液态网络架构路线
- **可用性**: 3B 规模，消费级 GPU 可推理；license 见模型卡

### [CohereLabs/North-Micro-Vision-Instruct](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct)
- **类型**: vision-language-instruct（微型 VLM）
- **热度**: ❤️96 / trend 96（8-10 上架）
- **特色**: Cohere「North」系列的 Micro Vision 指令版 —— 大厂集体下探**微型多模态**：和 LFM2.5-VL-3B 同天窗口发布，端侧 VLM 军备竞赛正酣
- **可用性**: 微型尺寸，适合端侧 / 边缘部署

### [Abiray/MiniMax-H3-GGUF](https://huggingface.co/Abiray/MiniMax-H3-GGUF)
- **类型**: image-to-video（MiniMax-H3 的 GGUF 量化）
- **下载量**: **60.6 万**（8-03 上架，11 天），❤️102
- **特色**: 视频生成模型量化的社区标杆 —— ComfyUI 直连、GGUF 单文件分发让 H3 从「旗舰卡专属」变成「消费级可跑」。H3 生态（量化/ComfyUI 节点/工作流）已是当前开源视频生成最活跃的衍生层
- **可用性**: GGUF 量化版，低 VRAM 可推理

### [realrebelai/Rebels_w4a8s](https://huggingface.co/realrebelai/Rebels_w4a8s)
- **类型**: text-to-image（**W4A8 INT4 量化** T2I 全家桶）
- **热度**: ❤️38 / trend 38（8-07 上架）
- **特色**: 作者明确对比「为什么用 W4A8 而不是 GGUF」—— T2I 量化的权重/激活位宽之争有了社区派系。低显存 ComfyUI 出图的新选项
- **可用性**: ComfyUI 直接加载，低 VRAM 场景

---

## 📰 社区热点

### [HN: Mistral OCR 4.1（252▲ / 99💬）](https://news.ycombinator.com/item?id=49288889)
- **讨论方向**: Mistral 最新 OCR 服务 —— **原生段落级 bounding box 提取 + 结构块标签 + 块级置信度**，驱动其 Document AI 栈。文档视觉理解从「整页转文字」走向「结构化版面解析」；评论区讨论精度与价格（€3.5/千页）的性价比
- **CV 关联**: OCR · Document Understanding · Layout Parsing（商业 API 动向，开源对标：PaddleOCR / DeepSeek-OCR）

### [HN: DeepSeek Harness developer preview（555▲ / 241💬）](https://news.ycombinator.com/item?id=49285244)
- **讨论方向**: DeepSeek 的 agent harness 开发预览高居 HN 前列。**值得注意**：GitHub 上当天就出现配套视觉插件生态 —— [dsh-vision-router](https://github.com/ysr666/dsh-vision-router)、[dsh-plugin-deepeye](https://github.com/Favio8/dsh-plugin-deepeye)（图像描述/OCR/VQA/UI 布局）、[dsh-vision-provider](https://github.com/libinyam/dsh-vision-provider) —— 「agent 框架发布 → 社区视觉插件跟进」的周期已缩短到一天
- **CV 关联**: Multimodal Agents · OCR · UI Understanding

### [HN: Gemini 3.7 Flash（615▲ / 343💬）](https://news.ycombinator.com/item?id=49289112)
- **讨论方向**: Google 发布 Gemini 3.7 Flash，今日 HN 最高分（615）—— 虽为闭源，但作为多模态推理的对照基准值得记录；评论区焦点在延迟/价格与开源模型的差距
- **CV 关联**: 多模态模型竞争的产业坐标

---

## 🛠️ 实用工具 & 库

### [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)
- **功能**: 29 种「编辑级」图表类型模板（自包含 HTML + SVG）给 Claude Code 用 —— 生成**可直接用的图表**而非 Mermaid 占位
- **热度**: ⭐14665，今日 GitHub Trending 双榜在列（8-13 推送）
- **使用**: clone 后作为 agent skill / 参考模板注入 Claude Code 工作流；视觉相关点在于「结构化图表即视觉信息表达」

### [yan-stone-computer/ModelVisionSkill](https://github.com/yan-stone-computer/ModelVisionSkill)
- **功能**: 给**非多模态模型**装眼睛 —— 6 个免费 vision engine 打包成一个 skill，适配各类 agent 平台（12⭐，8-09）
- **使用**: 作为 skill 注入 agent；延续 8-12/8-13 日报追踪的「agent 视觉工具链」主线

### [ilinxa/ilinxa-capture](https://github.com/ilinxa/ilinxa-capture)
- **功能**: 视频抽帧 + 拼图服务 —— FFmpeg 抽帧并合成 1×1 / 2×2 / 4×4 网格图喂给多模态 LLM；REST API + Web UI + **MCP server** 三合一
- **使用**: `docker` 起服务或接 MCP；视频理解管线的标准预处理件

### [vandorena/diffusion.pdf](https://github.com/vandorena/diffusion.pdf)
- **功能**: **在 PDF 文件内部跑一个 diffusion 图像模型**（8-10 创建，GPL-3.0）—— 极客向的「文件格式即运行时」实验
- **使用**: clone 后按 README 在 PDF 内执行；脑洞类项目，适合逆向/格式黑客爱好者

---

## 📦 值得关注的版本更新

### [unslothai/unsloth](https://github.com/unslothai/unsloth) v0.1.702-beta（8-13）
- **更新亮点**: **Unsloth Desktop 正式发布**（首个本地「跑+训」AI 桌面 app，8-11 官宣，8-13 迭代）—— 本地 UI 同时支持 LLM 与 **diffusion 模型**（Qwen3.8 / Kimi K3 / MiniMax-H3 / FLUX 等），新增 tool calling / web search、VRAM 可调、AMD RDNA3/4 优化。⭐71078，Apache-2.0。「本地训练+推理一体化」正在成为工具链标配

### [NVIDIA-NeMo/Automodel](https://github.com/NVIDIA-NeMo/Automodel)
- **更新亮点**: NVIDIA 的 PyTorch 分布式训练库（LLM/VLM，OOTB HF 支持）8-14 仍在活跃推送（⭐825，Apache-2.0）—— 大厂把 VLM 训练基础设施开源化，和 Unsloth Desktop 一「重」一「轻」两头夹击本地训练赛道

### [meta-models/Muse-Glimmer-30B](https://huggingface.co/meta-models/Muse-Glimmer-30B) 持续霸榜
- **更新亮点**: 8-09 开源后趋势不减 —— 今日 ❤️1423 / 12.1 万下载 / trend 1339（多模态榜第 1），官方 + unsloth 双轨 GGUF 均已就位。「本地 30B agentic 多模态」是本周 HF 最确定的趋势线

---

## 📚 HF Daily Papers 精选

- **[Gaze Target Estimation Anywhere with Concepts](https://arxiv.org/abs/2608.11367)** — 抛弃「头框+姿态」多级流水线，用概念化表示做 in-the-wild 视线目标估计 —— 目光追踪走向「单阶段 + 免显式输入」
- **[Learning How the World Evolves: Extrapolative Video World Models via Latent Dynamics Reasoning](https://arxiv.org/abs/2608.09926)** — 视频扩散模型只拟合像素、不建模状态迁移；该文在潜空间显式推理动力学，让世界模型「外推」而非「插值」—— 视频生成向世界模型进化的关键一步
- **[Hand Visibility Detector: Per-Keypoint Visibility Estimation for Hands](https://arxiv.org/abs/2608.11574)** — 手部关键点的逐点可见性估计，为 AR/VR、机器人抓取在遮挡下的置信度评估补上缺失的一环
- **[AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models](https://arxiv.org/abs/2608.06729)** — 单腕相机的 VLA 存在「感知遗忘」（物体出画面即丢）；AtlasVLA 引入持久化 world-ego 状态建模，长程具身任务的记忆问题新解法

---

*Reddit API 连续第 7 天全站 403、PapersWithCode API 仍异常，社区热点继续以 Hacker News + HF 生态数据为主源。渠道：GitHub Trending · GitHub Search API（3 组关键词）· HuggingFace Models（trending/downloads/trendingScore 多维）· HF Daily Papers · Hacker News = 5 类可用数据源，共精选 15 条。*
