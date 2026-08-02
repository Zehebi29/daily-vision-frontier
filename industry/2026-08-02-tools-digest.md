# 🛠️ 2026-08-02 视觉工业界日报

> 今日扫描了 GitHub Trending · GitHub Search (新 repo) · HuggingFace Models (5 个 pipeline 趋势榜) · HuggingFace Daily Papers · PapersWithCode · Hacker News 等 7 个渠道（Reddit 被 403 拦截，见文末说明）

---

## 🔥 热门开源项目

### 1. [OpenImagingLab/RealVDeblur](https://github.com/OpenImagingLab/RealVDeblur)
- **什么**: **一步扩散**真实世界视频去模糊（One-Step Diffusion for Generalizable Real-World Video Deblurring），7-21 新建 repo，附 [项目主页](https://rbjin.github.io/RealVDeblur/)
- **为什么火**: 视频修复领域的主流痛点是"真实模糊 vs 合成模糊的 domain gap"+"多步采样太慢"。一步扩散 + 通用化去模糊正好同时打这两个点，是 video restoration 往实时走的代表性工作
- **CV 关联**: 视频复原 · Diffusion · 低层视觉 (low-level vision)
- **快速上手**: `git clone https://github.com/OpenImagingLab/RealVDeblur`

### 2. [Lucas1479/Amadeus](https://github.com/Lucas1479/Amadeus)
- **什么**: 实时多模态桌面交互 Agent — TALK 可打断实时语音 · EMBODY 表演与语音同帧 · ACT Provider 委派执行 · CONTROL 可恢复可接管（中文项目，附 B 站 10 分钟演示）
- **为什么火**: ⭐53，创建于 7-26。GUI/桌面 Agent 是当下多模态落地最热赛道之一，Amadeus 的亮点是把"屏幕理解"与"低延迟语音/动作"做成一套可运行的 OS 层交互界面
- **CV 关联**: 屏幕理解 (screen understanding) · 多模态 Agent · GUI grounding
- **注意**: license 为 open-source noncommercial（非商用）
- **快速上手**: `git clone https://github.com/Lucas1479/Amadeus`

### 3. [rogerioagjr/PSP](https://github.com/rogerioagjr/PSP)
- **什么**: **Inference-Time Scaling of Diffusion Models via Progressive Seed Pruning**（ECCV 2026）官方实现 — 用"渐进式种子剪枝"给扩散模型做推理时扩展
- **为什么火**: 图像生成的推理时扩展（类比 o1 式 thinking）是 2026 的热点方向，PSP 的思路是不改模型、纯推理侧通过 seed 空间剪枝换取质量提升，工程上非常轻
- **CV 关联**: Diffusion · Inference-time Scaling · 图像生成
- **快速上手**: `git clone https://github.com/rogerioagjr/PSP`

---

## 🤗 值得关注的新模型

### [nvidia/Qwen-Image-Flash](https://huggingface.co/nvidia/Qwen-Image-Flash)
- **类型**: text-to-image（few-step 蒸馏）
- **下载量**: 634 次 ❤️75，7-23 发布
- **特色**: NVIDIA 用自家 **DMD2 + FastGen + Model Optimizer + AutoModel** 把 Qwen-Image 蒸馏成 **4 步**生成（shift-3 轨迹），保留原架构与 scheduler 配置 — "少步生成"正在成为各家模型商的标配赛道
- **可用性**: ⚠️ NVIDIA Open Model License（非 Apache，商用需确认条款）

### [egeorcun/lucida](https://huggingface.co/egeorcun/lucida)
- **类型**: image-segmentation / 抠图 matting（BiRefNet 微调）
- **下载量**: 4,219 次 ❤️48，7-24 更新
- **特色**: 专攻开源模型普遍翻车的场景 — **伪装物体 (camouflage)、透明材质 (玻璃)、文字/logo 保留、插画**；自建 203 图 9 类 benchmark 上 MAE 全面领先，含商业参考模型；有 [在线 demo](https://huggingface.co/spaces/egeorcun/lucida-demo)
- **社区彩蛋**: 7-24 曾发布 v13 实验权重，因社区测试在真实分层插画上回退，一天内**撤回并回滚到 v7** — 这种诚实迭代在 HF 上不多见，值得围观 v14
- **可用性**: MIT ✅ 可商用

### [Alissonerdx/BFS-Best-Face-Swap](https://huggingface.co/Alissonerdx/BFS-Best-Face-Swap)
- **类型**: image-editing（Qwen-Image-Edit 系 face/head swap LoRA）
- **下载量**: **10.9 万次** ❤️730，7-30 更新 — 当前 Qwen-Image-Edit 生态最火的换脸 LoRA 之一
- **特色**: 基于开源编辑模型做可控换脸/换头，ComfyUI 直接可用 — 说明 Qwen-Image-Edit 的社区衍生生态（LoRA 化定制）已经跑通
- **可用性**: 需遵循 Qwen-Image-Edit 的 Apache-2.0 派生条款

### [pixai-labs/pixai-tagger-v0.9](https://huggingface.co/pixai-labs/pixai-tagger-v0.9)
- **类型**: image-classification / 多标签打标（anime · danbooru 体系）
- **下载量**: 新发布 ❤️189（7-07）
- **特色**: 面向**数据集自动打标管线**的新 tagger（WD14-tagger 生态的替代/竞争者），multi-label + danbooru 词表，对训练 LoRA/微调数据的清洗很有用
- **可用性**: Apache-2.0 ✅

---

## 📰 社区热点

### Seedance 2.5 发布引热议 — ByteDance 视频生成再升级
- **讨论**: [HN: Seedance 2.5](https://news.ycombinator.com/item?id=?)（原帖 [ByteDance Seed 博客](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-intro)，热度 **148 pts / 54 评论**）
- **核心**: 单次生成 **30 秒 4K 视频**（告别多片段拼接）、支持**最多 50 个多模态参考输入**、原生音频 — 视频生成的"一键成片"门槛又被拉低；社区讨论焦点是闭源 vs 开源视频模型的差距和 Seed 系列的迭代速度

### Flux-OPD: On-Policy Distillation with Evolving Contexts
- **论文**: [Flux-OPD](https://huggingface.co/papers/2607.28022)（39 upvotes）+ 官方实现 [rethinking-cfg-opd/Rethinking-CFG-OPD](https://github.com/rethinking-cfg-opd/Rethinking-CFG-OPD)（⭐8，7-28 新建）
- **核心**: 在 on-policy 扩散蒸馏中引入**演化上下文**，并重新审视 CFG 的作用 — 少步蒸馏 (OPD) 家族的最新改进，直接关系 FLUX/SD 系 turbo 模型的蒸馏质量

### RefCaptioner: 多参考图像锚定的视频描述
- **论文**: [RefCaptioner](https://huggingface.co/papers/2607.28509)（25 upvotes）+ 代码 [pkucs-Ltf/RefCaptioner](https://github.com/pkucs-Ltf/RefCaptioner)（⭐3）
- **核心**: 用**多张参考图像**锚定视频生成描述，解决纯文本 prompt 对视频内容约束不足的问题 — 对视频理解数据合成 (data synthesis) 管线有直接价值

---

## 🛠️ 实用工具 & 库

### [Microsoft Flint: A Visualization Language for the AI Era](https://microsoft.github.io/flint-chart/)
- **功能**: 微软新发布的**可视化语言**（图表 DSL），让 AI agent 直接"写代码出图"，替代手搓 matplotlib/ECharts — HN 热度 **255 pts / 67 评论**
- **CV 关联**: 严格说是 data-viz 而非 CV，但对"视觉输出"密集的 agent 应用（分析报告、评测展示）很实用，且代表"语言即界面"的 agent 工具趋势
- **使用**: 见项目文档，支持生成图表代码并渲染

---

## 📦 值得关注的版本更新

### [ideogram-ai/ideogram-4-fp8](https://huggingface.co/ideogram-ai/ideogram-4-fp8)
- **更新亮点**: Ideogram 4 的 **FP8 量化版**（4.3 万下载 ❤️729），DiT + flow-matching 架构，Diffusers `Ideogram4Pipeline` 直接可用 — 大厂开始把旗舰文生图模型主动出 FP8 版本，降低本地部署门槛
- **可用性**: ⚠️ license: other（需确认商用条款）

### [lodestones/Kroma](https://huggingface.co/lodestones/Kroma) — Krea2 LoRA 生态继续生长
- **更新亮点**: Krea 2 开源自研模型后（见 8-01 日报），社区 LoRA 一周内爆发 — Kroma 是其中最受关注的风格/能力 LoRA（❤️95，7-31 发布，ComfyUI 可用），说明 Krea2 的微调生态已经起步

---

## 📊 今日扫描总结

| 渠道 | 覆盖情况 |
|------|---------|
| GitHub Trending (daily) | ✅ 15 repos scanned（CV 相关占比低，多为 agent/安全类） |
| GitHub Search (新 repo, 7-20 后) | ✅ diffusion 744 / multimodal 1,825 命中，按 stars 取 top |
| HuggingFace Models (5 个 pipeline 趋势榜) | ✅ text-to-image · image-to-image · segmentation · detection · depth |
| HuggingFace Daily Papers | ✅ 30 篇，筛选出 CV/多模态相关 |
| PapersWithCode | ⚠️ 主页/API 信号弱（页面结构改动），仅作交叉验证 |
| Hacker News (Top 40) | ✅ 命中 Seedance 2.5、Flint 等社区热点 |
| Reddit (r/computervision, r/MachineLearning, r/StableDiffusion) | ❌ 全渠道 403（www/old/api/redlib 镜像均被网络策略拦截），今日社区信号改用 HN + HF 替代 |

**精选条目**: 13 条 | **主要方向**: 视频复原 (RealVDeblur) · 少步蒸馏 (Qwen-Image-Flash, Flux-OPD) · 抠图 (lucida) · GUI Agent (Amadeus) · 视频生成社区热度 (Seedance 2.5)

---

*今日核心观察: 少步/one-step 蒸馏（NVIDIA Qwen-Image-Flash、Flux-OPD、RealVDeblur 的一步扩散）与"抠图/打标这类小而美的垂类模型"（lucida、pixai-tagger）是本周最活跃的两条线。*
