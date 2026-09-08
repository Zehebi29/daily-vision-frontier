# 🛠️ 2026-09-08 视觉工业界日报

> 今日扫描 GitHub Trending（global/python）· GitHub Search（近 7 天新仓库 ×2 查询）· HuggingFace Models（8 个 pipeline × trending/downloads）· HF Daily Papers · Reddit ×3（连续 403）· PapersWithCode API（异常）等 7 类渠道，精选 7 条

---

## 🔥 今日主线：实时视频生成框架开源 + Diffusion-LLM 图像生成入局

**第一**，视频生成进入「框架开源化」阶段——OpenVDN/vdn-minimax-h3 周内 371★，实时 T2V/I2V 生成可从本地起服务；**第二**，LLaDA-Image（inclusionAI，Apache-2.0）把 diffusion LLM 路线带到图像生成，Turbo/FP8 版本 9-03 跟进；**第三**，GitHub Trending 被 agent-skills 霸榜（openai/skills 居首），CV/3D 能力开始以「技能包」形态分发。

---

## 🔥 热门开源项目

### 1. [OpenVDN/vdn-minimax-h3](https://github.com/OpenVDN/vdn-minimax-h3) ⭐371 · Apache-2.0
- **什么**: VideoDeltaNet-H3——基于 MiniMax H3 的 live T2VA/I2VA/FL2VA 实时视频生成框架
- **为什么火**: 9-02 创建、9-08 仍在更新；把视频生成做成本地可部署的 agent 视频服务
- **CV 关联**: video generation · 文/图/首尾帧 → 实时视频
- **快速上手**: `git clone https://github.com/OpenVDN/vdn-minimax-h3`

### 2. [dreamers-laboratory/image-to-3d-pipeline](https://github.com/dreamers-laboratory/image-to-3d-pipeline) ⭐302 · Apache-2.0
- **什么**: 串联多个开源模型做图生 3D mesh，并自动评分「谁重建得最好」
- **为什么火**: 9-02 新建即 302★——把 Trellis/InstantMesh 类模型变成可评测、可对比的统一管线
- **CV 关联**: 3D reconstruction · 单图/多图 mesh 生成工程化
- **快速上手**: `git clone https://github.com/dreamers-laboratory/image-to-3d-pipeline`

### 3. [achimala/dream-loop](https://github.com/achimala/dream-loop) ⭐318 · MIT
- **什么**: agent skill——Blender + image gen + subagent critic 循环迭代 3D 视觉
- **为什么火**: 9-07 新建一天 318★；把 3D 创作拆成「生成-批评-再生成」agent 循环
- **CV 关联**: 3D rendering · agentic generation；与 CAD 视觉工作流同源的 skill 形态

---

## 🤗 值得关注的新模型

### [inclusionAI/LLaDA-Image](https://huggingface.co/inclusionAI/LLaDA-Image) (+ [Turbo](https://huggingface.co/inclusionAI/LLaDA-Image-Turbo) / [FP8](https://huggingface.co/inclusionAI/LLaDA-Image-Turbo-FP8))
- **类型**: text-to-image / image editing（**diffusion LLM** 路线，非自回归）
- **热度**: 8-28 开源，9-03 Turbo/FP8 跟进，本周 HF T2I 趋势榜前列
- **特色**: LLaDA 扩散语言模型架构做图像生成，中英双语；diffusion-LLM 在图像侧的稀缺开源实现
- **可用性**: Apache-2.0 ✅ 可商用；`diffusers` LLaDAImagePipeline 直载

### [krea/Krea-2-Raw](https://huggingface.co/krea/Krea-2-Raw) / [Krea-2-Turbo](https://huggingface.co/krea/Krea-2-Turbo) + 社区生态
- **类型**: text-to-image（Krea2Pipeline）
- **热度**: 本周 HF T2I 趋势榜第 1（ts 69，7 万下载）；[4-step 蒸馏 LoRA](https://huggingface.co/lvladikov/Krea2-Turbo-Distill-4step-LoRA)（2 万下载）+ [Pose ControlNet](https://huggingface.co/thedeoxen/Krea-2-pose-controlnet)（Apache-2.0）跟上
- **特色**: Krea 放权重后社区生态一周内成型——蒸馏加速 + pose 可控，扩散生态复制 FLUX 路径
- **可用性**: license other（商用需查证）；diffusers 直载

---

## 📰 社区热点

### [GitHub Trending：openai/skills 居首，agent-skill 霸榜](https://github.com/trending)
- **观察**: 今日 trending 前 10 过半是 Claude Code/Codex skills；CV/多模态正被封装成「技能包」分发（dream-loop、guizang-yingzao、image-to-css-art 皆属此类），生态从「调 API」转向「装技能」
- **热度**: openai/skills 今日第 1，microsoft/markitdown 等长驻榜

### [heygen-com/hyperframes v0.8.31](https://github.com/heygen-com/hyperframes) ⭐47K · Apache-2.0
- **什么**: 「Write HTML. Render video. Built for agents」——HTML/GSAP → 视频渲染框架，昨日发布 v0.8.31
- **判断**: HeyGen 开源其 agent 视频渲染层，是 agent 生成视频的「最终渲染出口」，与生成模型互补

---

## 🛠️ 实用工具 & 库

### [Blueforcer/ComfyUI-DLSS5-Enhancer](https://github.com/Blueforcer/ComfyUI-DLSS5-Enhancer) ⭐101（同类 [dlss-unlocked](https://github.com/ShyVortex/dlss-unlocked) ⭐138）
- **功能**: NVIDIA DLSS 5 Neural Rendering（NGX feature 18）封装成 ComfyUI 节点——批量图/视频增强 + 帧插值
- **判断**: 游戏显卡的实时神经渲染/补帧反哺 AIGC 工具链，RTX 40/50 系新玩法，新奇可玩

---

## 📚 HF Daily Papers 精选

- **[AdaptVPR: 路由感知难例生成，鲁棒视觉定位](https://huggingface.co/papers/2609.04369)** — 为 VPR 主动构造路线相关 hard positives，机器人/自驾定位实用向
- **[UniMate: 统一模型驱动多样骨骼动画](https://huggingface.co/papers/2609.05415)** — 人形/动物/异形骨架一个模型通吃，动画资产管线降本
- **[ShallowStream: 流式视频理解「先索引后深答」](https://huggingface.co/papers/2609.02780)** — 长视频问答先建浅层索引再按需深挖，token 效率思路

---

*Reddit 连续 403、PapersWithCode API 异常，社区数据以 GitHub + HF 为准。*
