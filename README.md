# 📷 Daily Vision Paper

> **每日双线追踪计算机视觉前沿**
>
> 🔬 **学术界** — 每日一篇 CV/多模态/VLM 论文精读（arXiv 精选）
> 🛠️ **工业界** — 每日开源工具/模型/社区热点追踪（GitHub/HF/Reddit）
>
> 从第一性原理出发，用类比讲透晦涩原理，每天 GitHub update

---

## 🏗️ 架构

```
daily-vision-paper/
├── papers/           # 🔬 学术界：每日论文精读（8:00 cron）
│   ├── YYYY-MM-DD-title-slug.md
│   └── ...
├── industry/         # 🛠️ 工业界：每日工具/模型/热点（9:00 cron）
│   ├── YYYY-MM-DD-tools-digest.md
│   └── ...
├── archive/
│   └── index.md     # 论文索引总表
├── scripts/         # 自动化脚本
│   └── ...
└── README.md
```

## 📖 内容导航

| 分区 | 内容 | 更新频率 | Cron |
|------|------|----------|------|
| [📚 论文精读](papers/) | 近半年 CV/VLM 前沿论文深度分析 | 每日 8:00 | `0 8 * * *` |
| [🧰 工业界动态](industry/) | 开源工具/模型/社区热点 | 每日 9:00 | `0 9 * * *` |
| [📇 归档索引](archive/index.md) | 全部论文索引 | 自动更新 | - |

## 📖 论文列表

| 日期 | 论文标题 | 领域 | 核心关键词 |
|------|----------|------|-----------|
| 2026-07-28 | [Rethinking CFG in On-Policy Diffusion Distillation](papers/2026-07-28-rethinking-cfg-on-policy-diffusion-distillation.md) | 扩散模型蒸馏 | CFG, OPD, NBA, PDM, 视频控制 |
| _(每日自动更新)_ | | | |

---

*Powered by Hermes Agent · arXiv API · Daily Cron*
