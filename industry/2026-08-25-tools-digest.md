# 🛠️ 2026-08-25 视觉工业界日报

> 今日扫描 GitHub Trending · GitHub Search（近 7 天新仓库）· HuggingFace Models（下载/趋势/新模型）· HF Daily Papers · Reddit（仍 403）· PapersWithCode（API 异常）等 6 类渠道，精选 7 条

---

## 🔥 今日主线：GPT-Image2 提示词工程社区化 + 小型 T2I 部署生态加速 + 世界模型转向「可进入」模拟

**第一**，GitHub 今日头名是 GPT-Image2 提示词库——530+ 逆向案例沉淀成「Prompt as Code」模板，生图工作流的工程化知识开始开源沉淀；**第二**，上周登顶的小型 T2I `Anima-2.9B` 今日迎来 GGUF 量化版，`Krea-2-Turbo` 4-step 蒸馏 LoRA 同步上架——小型生图模型正在复制 LLM 的量化/蒸馏剧本；**第三**，世界模型论文集中发力——`EchoWM` 把生成式媒体做成「可进入」的 720p 音视频世界，`From Generation to Simulation` 则系统评估生成式世界模型离真模拟器还有多远。

---

## 🔥 热门开源项目

### 1. [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2) ⭐16.6K
- **什么**: GPT-Image2 工业级提示词引擎与模板库，530+ 案例逆向工程、20+ 套模板，提炼为 Skills
- **为什么火**: 今日 GitHub Trending 全站第 1（+1,698/day），MIT，8-25 仍在推送
- **CV 关联**: Image Generation · Prompt Engineering · 生图工作流工程化
- **快速上手**: `git clone https://github.com/freestylefly/awesome-gpt-image-2`

---

## 🤗 值得关注的新模型

### [vanes430/Anima-2.9B-GGUF](https://huggingface.co/vanes430/Anima-2.9B-GGUF) + [lvladikov/Krea2-Turbo-Distill-4step-LoRA](https://huggingface.co/lvladikov/Krea2-Turbo-Distill-4step-LoRA)
- **类型**: text-to-image 量化 / 蒸馏加速
- **热度**: Anima-GGUF 今日上架（首发）；Krea2 4-step LoRA 今日更新（3.9K 下载）
- **特色**: Anima-2.9B（08-17 登顶 HF T2I 趋势）GGUF 化，T2I 可走本地 CPU/小显存部署；Krea-2-Turbo 蒸馏到 4 step，推理成本骤降
- **可用性**: 均非商用 license（circlestone-labs-non-commercial / krea other）；量化单文件 ComfyUI 直用

### [PaddlePaddle/PP-DocLayoutV3](https://huggingface.co/PaddlePaddle/PP-DocLayoutV3)
- **类型**: image-segmentation（文档版面分析）
- **热度**: 19K 下载 ❤107，HF 分割趋势榜常客
- **特色**: PaddleOCR-VL 1.5/1.6 与 GLM-OCR 的**统一版面模块**——检测+结构识别一体，工业文档解析事实标准
- **可用性**: Apache-2.0 ✅，PaddleOCR 全家桶直接调用

---

## 🛠️ 实用工具 & 库

### [marin-community/marin](https://github.com/marin-community/marin) ⭐1.9K
- **功能**: 开源 foundation model 研发框架——数据策展/过滤/分词/预训练/评测全流程，主打 open development 过程知识共享
- **使用**: Apache-2.0；视觉基础模型研究者可复用其训练管线基建
- **判断**: 「把训练 LLM 的完整过程知识开源」定位独特，基础模型工程化参考价值高

---

## 📰 社区热点

### [EchoWM: Open and Enterable Omnimodal World Models](https://huggingface.co/papers/2608.23189)
- **讨论方向**: 世界模型从「生成视频」转向「可进入生成媒体」——按相机意图连续导航，同时生成 720p 视频+环境音+音乐+语音
- **判断**: 交互式 omni-modal 世界模型，视频生成与 3D 导航结合的激进尝试，开源将推高世界模型上限

### [From Generation to Simulation: How Far Are World Models from Being True Simulators?](https://huggingface.co/papers/2608.23070)
- **讨论方向**: 用外部标尺系统评测扩散式世界模型离物理引擎/游戏引擎/RL 环境还有多远
- **判断**: 世界模型「能不能当模拟器用」首次被当工程问题量化，与 EchoWM 互补

---

## 📚 HF Daily Papers 精选

- **[EXPL-FR: Explaining Face Recognition Models via Vision-Language Alignment](https://huggingface.co/papers/2608.21486)** — 在冻结 FR 嵌入空间内对齐 VLM 编码器，回答「相似度分数依赖哪些语义属性」；只用 face 图像训练、零文本监督——FR 可解释性新范式
- **[WorldToken: Time-First Sequence Modeling for Robotic Imitation Learning](https://huggingface.co/papers/2608.22591)** — 把多视角图像+本体感觉+任务条件在每个决策步融合成单一 world token，时间优先建模范式——机器人模仿学习序列建模新排序

---

*Reddit 全站仍 403、PapersWithCode API 仍异常；社区热点以 HF + GitHub 数据为主源。*
