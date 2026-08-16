# 🛠️ 2026-08-16 视觉工业界日报

> 今日扫描了 GitHub Trending（daily）· GitHub Search API（6 组关键词，近一周新仓库）· HuggingFace Models（9 个 pipeline 的 trendingScore 榜）· HF Daily Papers · Hacker News · Reddit（连续第 9 天 403）· PapersWithCode（API 仍异常）等 7 类渠道，共精选 16 条

---

## 🔥 今日主线：Agent Harness「视觉插件生态」爆发 + AI 拆图杀进设计工作流 + 视频生成的 previz 工程化

今天没有重量级基础模型首发，但三条**生态层**主线非常清晰：**第一**，DeepSeek Harness 发布一周后，视觉插件从 8-14 的 2-3 个膨胀到 5+ 个 —— `Anionex/dsh-vision-toolkit` 三天拿下 437★ 成为近一周新仓库榜首，`dsh-vision-router` 146★ 今天仍在推送，OpenCode 生态也跟进（OpenCode Senses 上 HN）——「给纯文本 agent 装眼睛」已从点子变成独立生态位；**第二**，`50kg/image-to-slice`（259★/5 天）把「图像 → 补齐 → Figma 图层 → HTML/CSS」串成一条链，视觉理解正式成为设计工程的一环；**第三**，视频生成的「先规划再生成」工具化 —— Blender 白模 previz（VLM-Generation-Harness）、隐藏 storyboard 编排（nautilus-studio）、硬件感知的 H3 本地生成 skill（h3lite）—— 在花算力之前先用几何把镜头定下来。

---

## 🔥 热门开源项目

### 1. [Anionex/dsh-vision-toolkit](https://github.com/Anionex/dsh-vision-toolkit)
- **什么**: **DeepSeek Harness 原生视觉插件**（TypeScript，MIT）——带意图的图片问答、长截图 OCR、UI 还原、grounding、pixel diff、Artifacts 输出
- **为什么火**: ⭐437（8-13 创建，三天），近一周「image generation/text-to-image」类新仓库第 1。它是 8-14 报道的 DSH 视觉插件潮的**头部玩家**，同场还有 [dsh-vision-router](https://github.com/ysr666/dsh-vision-router)（146★，今天仍在推送）、[oil-oil/dsh-vision](https://github.com/oil-oil/dsh-vision)（40★）、[Yts1919/dsh-vision-complete](https://github.com/Yts1919/dsh-vision-complete)（23★）、[tonyd2wild 的「给 DeepSeek V4 Flash 装眼睛」shim](https://github.com/tonyd2wild/DeepSeek-v4-Flash-0731-Vision-DSpark-1M-NVFP4-KV-2x-DGX-Spark)（22★，OpenAI 兼容、零依赖）——**一个 agent 框架 → 一撮视觉插件**的周期已稳定在 1-2 天
- **CV 关联**: Agentic Vision · OCR · GUI Automation · Grounding · Screenshot Testing
- **快速上手**: `git clone https://github.com/Anionex/dsh-vision-toolkit`（按 README 装进 DeepSeek Harness）

### 2. [50kg/image-to-slice](https://github.com/50kg/image-to-slice)
- **什么**: **AI 拆图工具**（JavaScript，MIT）——把一张设计图自动拆成图层：被遮挡背景补齐 → 人工校准 → 导入可编辑 Figma 图层 → 导出 HTML/CSS
- **为什么火**: ⭐259（8-10 创建，5 天）。「视觉理解 → 设计工程」闭环的完成度很高，与 UI 还原/Design-to-Code 赛道互相印证
- **CV 关联**: Image Segmentation · Layer Separation · Inpainting · Design-to-Code
- **快速上手**: `git clone https://github.com/50kg/image-to-slice`

### 3. [Rimagination/h3lite](https://github.com/Rimagination/h3lite)
- **什么**: **硬件感知的 Codex skill**——本地用 ComfyUI 跑 MiniMax H3 视频生成，按机器配置自动选最优路径（MIT，8-13）
- **为什么火**: ⭐128（3 天）。H3 生态的「本地部署最后一公里」被工具化 —— 从 ComfyUI 节点、量化、Turbo 蒸馏之后，轮到「skill 化」层
- **CV 关联**: Video Generation · MiniMax H3 · ComfyUI · Agent Skills
- **快速上手**: 按 README 装进 Codex skills

### 4. [TedLentsch/TokenGraph3D](https://github.com/TedLentsch/TokenGraph3D)
- **什么**: **ECCV 2026 论文代码**——Emergent 3D Instance Segmentation，从 2D 分割 token 中「涌现」出 3D 实例分割（Apache-2.0，8-15 创建）
- **为什么火**: 极新（昨天刚建仓）。3D 分割的 emergent 范式值得跟踪——不走显式 3D 监督，而是 token 层面的自组织
- **CV 关联**: 3D Instance Segmentation · Emergent Representation · ECCV 2026
- **快速上手**: `git clone https://github.com/TedLentsch/TokenGraph3D`

### 5. [zhaozhen2333/Turbo-Learning](https://github.com/zhaozhen2333/Turbo-Learning)
- **什么**: **CVIU 2026 官方实现**——「A Turbo-Inference Strategy for Object Detection and Instance Segmentation」：训练-free 的检测/实例分割迭代细化加速（Apache-2.0，8-14）
- **为什么火**: ⭐23。"turbo" 思路从生成模型蔓延到检测推理——训练-free 的迭代细化在 mmdetection 生态里直接可用
- **CV 关联**: Object Detection · Instance Segmentation · Training-free Acceleration · mmdetection
- **快速上手**: `git clone https://github.com/zhaozhen2333/Turbo-Learning`

### 6. [hyulin472-dotcom/yolopoint11-vins-slam](https://github.com/hyulin472-dotcom/yolopoint11-vins-slam)
- **什么**: **YOLOPointv11 + LightGlue 的立体视觉惯性 SLAM**（C++，ROS 2，GPL-3.0，8-12）
- **为什么火**: ⭐28。YOLO 关键点检测 + LightGlue 特征匹配整合进 VIO SLAM 前端的实践——「检测模型进机器人感知栈」的参考实现
- **CV 关联**: Visual SLAM · Keypoint Detection · Visual-Inertial Odometry · ROS 2
- **快速上手**: `git clone https://github.com/hyulin472-dotcom/yolopoint11-vins-slam`

---

## 🤗 值得关注的新模型

### [jimmycarter/krea2-turbo-bbox](https://huggingface.co/jimmycarter/krea2-turbo-bbox)
- **类型**: text-to-image（基于 `krea/Krea-2-Raw` 的蒸馏 bbox 控制 LoRA）
- **热度**: ts 21 居今日 HF T2I 趋势榜前列（7-20 上架，8-16 仍在更新）
- **特色**: Krea 2 生态的「bbox 可控蒸馏」衍生层——延续 8-14 报道的 Krea2 LoRA 生态生长曲线（Kroma v0.2 → Turbo → bbox 控制）
- **可用性**: diffusers 直接加载

### [Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)（趋势追踪，非首发）
- **类型**: image-to-video / text-to-video / video-to-video / audio-video（diffusion single-file）
- **热度**: **ts 779，今日 HF 视频生成趋势榜第 1**；累计 37.8 万下载 ❤941（8-12 首发已报道，4 天数据翻倍）
- **特色**: 一个单文件覆盖 image/video/audio 全模态；gated 访问（申请制）反而带火了下载与讨论——「官方 SDK + 受限权重」的发布策略成为生成模型新常态
- **可用性**: 需 HF 授权申请；官方 [LTX-2.5-Diffusers](https://huggingface.co/Lightricks/LTX-2.5-Diffusers) 推理栈已就位

---

## 📰 社区热点

### [HN: SparrowMap – Cameras that watch government vehicles（▲165 / 💬12）](https://news.ycombinator.com/item?id=49293294)
- **讨论方向**: 公民自发部署相机网络**反向**监控政府车辆 —— 「监控技术扩散」的镜像应用。与上周 Flock ALPR 71% 误读率之争形成完整对照：当 CV 监控能力廉价到人人可部署，监控与被监控的边界开始反转
- **CV 关联**: Surveillance · ALPR · Camera Networks · 隐私伦理

### [HN: Show HN: OpenCode Senses – vision plugin（▲8）](https://news.ycombinator.com/item?id=49289890)
- **讨论方向**: OpenCode 生态的「insanely fast and highly accurate」视觉插件——与 DeepSeek Harness 视觉插件潮同频。「agent 框架 → 视觉插件」正在变成所有 harness 的标配组合拳
- **CV 关联**: Agent Vision · Plugin Ecosystem · Multimodal Agents

### [HN: Diffusion PDF – diffusion image model embedded in a PDF（▲5）](https://news.ycombinator.com/item?id=49285429)
- **讨论方向**: 把扩散图像模型**整个嵌进一个 PDF 文件**——「文件格式即运行时」的创意工程。评论区围绕 PDF 作为便携 AI 载体的可行性展开
- **CV 关联**: Diffusion · 创意工程 · 可移植 AI 载体

---

## 🛠️ 实用工具 & 库

### [Elysia-Beloved/easy-LWE-watermark-](https://github.com/Elysia-Beloved/easy-LWE-watermark-)
- **功能**: Tree-Ring 水印工程 → 潜空间 LWE 环形隐写 + NC 检测，支持 SD 2.1、信号失真/几何攻击、频率/小波能量分析，带 Gradio WebUI（MIT，8-10，⭐23）
- **使用**: `git clone` + `pip install`；本地或 HF 模型加载——AI 内容溯源方向的轻量工具箱

### [7ohnson/VLM-Generation-Harness](https://github.com/7ohnson/VLM-Generation-Harness) + [yeahdongcn/nautilus-studio](https://github.com/yeahdongcn/nautilus-studio)
- **功能**: 视频生成的「先规划再生成」双工具——(1) Blender 白模 previz，用几何控制 AI 视频的机位/空间/切点（「在花钱之前把错误拦下来」）；(2) 隐藏 storyboard 编排的长视频工作室，可插拔生成后端（MiniMax H3 / vllm-omni，Apache-2.0）
- **使用**: 均为 skill/studio 形态，按 README 安装——分镜和镜头语言正在变成视频生成的「第一层控制面」

### [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)（今日 GitHub Trending）
- **功能**: 29 种 editorial diagram 类型给 Claude Code 用，自包含 HTML+SVG——「No shadows, no Mermaid-slop」，把「agent 出图的排版品味」做成规格
- **使用**: 作为 Claude Code skill 引入（⭐18.6K，今日回榜 Trending）——视觉生成的质量竞争从「画得对」进入「排版美」

---

## 📦 值得关注的版本更新

### [ysr666/dsh-vision-router](https://github.com/ysr666/dsh-vision-router)（8-16 仍在推送，146★）
- **更新亮点**: 内置免费视觉链（无需 API key）+ pixel-level 工具全集（Q&A / grounding / crop / pixel diff / 取色 / OCR / SVG trace / cutout / 截图），一条命令接入——DSH 视觉插件「路由层」的标杆实现，8-14 创建后连续更新

### [lightx2v/Minimax-h3-Turbo](https://huggingface.co/lightx2v/Minimax-h3-Turbo) 数据更新
- **更新亮点**: Apache-2.0 的 H3 涡轮版累计 **21.1 万下载** ❤514（8-07 上架，8-13 更新）。H3 生态正沿着「GGUF 量化（60.6 万下载）→ Turbo 蒸馏 → ComfyUI 节点 → Codex skill（h3lite）」全链路工具化推进

---

## 📚 HF Daily Papers 精选

- **[RibAssist 3D: Biplanar Rib-Fracture Detection and Selective 3D Localization](https://huggingface.co/papers/2608.06914)** — 双平面 CT 投影做肋骨骨折检测 + 选择性 3D 定位，医学影像「投影即输入」的降维思路
- **[Context-Matched Distillation: Teacher Causality for Autoregressive Video Distillation](https://huggingface.co/papers/2608.13391)** — 自回归视频蒸馏中 teacher 因果性匹配——视频蒸馏的「上下文对齐」新视角
- **[H2R-Bench: Human-to-Robot Manipulation Video Generation in World Models](https://huggingface.co/papers/2608.13049)** — 人→机器人操作视频生成的 benchmark——给世界模型类方法立了一把「动作可迁移性」的尺子
- **[CW-BASS v2: Saturation-Aware Pseudo-Label Selection for Semi-Supervised Segmentation](https://huggingface.co/papers/2608.12773)** — foundation-model teacher 下的半监督分割：饱和感知伪标签选择，弱监督方向的新技巧
- **[Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence](https://huggingface.co/papers/2608.12743)** — 空间智能的经验记忆——agent 把空间经验程序化存储，做「导航/操作知识」的长期记忆

---

*Reddit API 连续第 9 天全站 403、PapersWithCode API 仍异常，社区热点以 Hacker News + HF 生态数据为主源。渠道：GitHub Trending · GitHub Search API（6 组关键词）· HuggingFace Models（9 pipelines × trendingScore）· HF Daily Papers · Hacker News = 5 类可用数据源，共精选 16 条。*
