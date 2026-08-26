# ⚙️ 2026-08-26 视觉硬件日报

> 今日扫描 11 渠道（SemiAnalysis · EETimes · NVIDIA · Tom's Hardware · SemiEngineering · Hackaday · Sony · OmniVision · GitHub · Google News(国产) · Reddit），精选 8 条
> ⚠️ Reddit 连续第五日 403；Sony/OmniVision 无新传感器（静默期第五周）；SemiAnalysis 停更；昇腾 910C 供不应求，国产算力缺口仍是主线
> 注: 不重复 8/19（H200 到货、博世×征程6B、ABF 断供）；主线是 **Hot Chips 2026**、**小米 3nm 智驾芯片**、**苹果首款 2nm**

---

## 🎥 传感器与采集

### 1. [智驾摄像头的芯片战争：中国开始进入全球汽车供应链腹地](https://news.google.com/rss/articles/CBMiUkFVX3lxTFA0aEZzSzVKNnY2X2tHQ1R0Y1p6UzhIMlUySUIwc0hhTldSLWd6UEdlTWZSX1VKd0ZFanQ0c2pxb3ljRlNMRlVzNnVPcWxQZ21LZVE?oc=5)
- **什么**: 车载摄像头芯片（CIS/ISP）国产化专题——思特威、韦尔、爱芯元智等进入全球 Tier1 供应链
- **亮点**: 智驾单车摄像头 8-12 颗，CIS 之外 ISP/SoC 成为新卡位点；国产厂商从「替代」转向「全球定点」
- **视觉关联**: 车载视觉采集层直接相关；与 8/19 地平线定点、今日征程6B 新定点互相印证
- **判断**: 国产车载视觉芯片进入放量验证期——能否守住全球定点比参数更重要

## 🖥️ GPU 与算力

### 2. [d-Matrix Raptor：AI 加速器直叠定制 DRAM，单卡 100 TB/s（Hot Chips 2026）](https://www.tomshardware.com/tech-industry/semiconductors/d-matrix-stacks-its-ai-accelerator-directly-on-custom-dram-for-100-tbs-per-card)
- **什么**: 「首个 3D DRAM 推理加速器」——TSMC 4nm 计算 die 与定制 DRAM 面对面键合，36μm pitch
- **性能**: 32GB 定制 DRAM 提供 100 TB/s 带宽/卡；面向生成式推理（LLM/VLM）而非训练
- **视觉关联**: 多模态 VLM 推理「内存墙」解法——省去 HBM 成本，适合视觉大模型批量部署
- **对比**: 带宽达 HBM3e 级别但成本/功耗更低；2026H2 推理新变量

### 3. [NVIDIA Vera Rubin NVL72：为 AI Agent 定义「每瓦 30 倍」效率新标准](https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents/)
- **什么**: Rubin 平台（Blackwell 继任者）效率数据；Groq 3 LPX 全面投产，Vera Rubin 推理版图扩展
- **亮点**: 30x work-per-watt 面向 agentic AI（多轮推理/长上下文），延续 NVLink Fusion 机架互联
- **视觉关联**: 多模态 Agent（视频理解/具身大脑）推理成本随 Rubin 代际显著下降
- **获取**: 2026H2-2027 云实例上线，与 8/17 TPU v10 对位——推理架构竞争白热化

## 🔩 芯片与半导体

### 4. [苹果发布首款 2nm 芯片 M6（Mac mini 首发），M5 Ultra 解锁四晶粒架构](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5DcU1tenpMQ09sMURkYThwbE9sSGJVMjdjd0ZxRlJLVV9nc050UFAxbDhHblZsOGNtSkhtZVlkUWNyMHpMeE5EUmFfNTIySlJ3ZGZv?oc=5)
- **动态**: 苹果首款 2nm SoC M6 落地，AI 性能宣称 4x；M5 Ultra 采用四晶粒（quad-die）架构
- **影响**: 2nm 从「军备竞赛」进入消费级量产；移动端 ISP/神经引擎/视频编解码算力代际跃升
- **判断**: 2nm 良率爬坡验证——为 2027 年智驾/边缘视觉 SoC 采用 2nm 提供参照系

## 🇨🇳 国产芯片

### 5. [小米官宣玄戒 D100：国内首款 3nm 智驾高算力芯片，明年商用](https://news.google.com/rss/articles/CBMiTEFVX3lxTFBLQzRrLVZnMHN3UjhDdGxKV1VqWjlDbi02WFZyMWxCcVc1OUltclluaUNXTjE5MjROTTFhel81d1hHVDlKQW4zazMzamQ?oc=5)
- **什么**: 小米「三芯齐发」——玄戒 O3（手机 SoC，10 全大核/CPU+60%/首发长鑫 LPDDR6）+ 玄戒 D100（智驾）+ 大模型加速芯片
- **亮点**: D100 为国内首款 3nm 智驾芯片、160GB 内存，2027 年商用；O3 随小米 18 Fold/平板 9 月首发
- **视觉关联**: 智驾「算力军备竞赛」升级——3nm 上车验证国产智驾 SoC 是否追平英伟达 Thor
- **判断**: 等 2027 上车实测；但「手机+车+端侧」三线自研是国内唯一

### 6. [地平线征程 6B 生态再下一城：neueHCT 方案获德系车企全球平台定点](https://news.google.com/rss/articles/CBMisgFBVV95cUxNSFRERnhoWTFnM25aakRqMi01QUtwdGhjRGpYTVpjU1NPcWpaVjJyRXk4ZVFWLXdFZ0NoSlJYVmJDRXNCaGNOa0lNbzF0ZUtzNGR5Q1owZ2FaZVdvMXFhb29FZmtaZHhhQUdoRmoxS0hQTjVZYVdlSDRqcEVuVTJFaUxyWldRNHNHdkg3eWRpRE9IbTBnWVBZZzA1QkJQTDY1b3lGNzhTbjVyTXIyS2JlXy13?oc=5)
- **什么**: 继 8/19 博世 MPC4 千万套定点后，征程 6B 方案再获德系车企全球平台定点（neueHCT）
- **亮点**: 「国产智驾芯片出海」从单点定点走向平台级放量——德系全球平台意味着海外产线/认证闭环
- **判断**: 地平线拐点确认：征程 6B（~10 TOPS 级中端）是走量主力，视觉感知供应链受益确定

## 📰 产业动态

### 7. [瑞芯微 2026 H1：营收 28.77 亿（+40.6%），端侧 AI 芯片放量](https://news.google.com/rss/articles/CBMiQ0FVX3lxTE83WkZUVVo2UEJjR1dFMk11Q05PczNlQ2J5dlAtRlRSNFBUQWdKbWdVNm16SzhzZGdWRDBpQ3Z0WDdCSUU?oc=5)
- **核心**: 归母净利 8.59 亿（+61.73%）；端侧 AI 芯片（RK3588/RK3576 等）成为增长引擎
- **影响**: 边缘视觉设备（IPC/机器人/平板）主控 SoC 需求回暖的直接财务证据；国产端侧 AI 进入盈利兑现期
- **判断**: 与昇腾 910C 供不应求对照——「端侧放量、云端缺货」的国产算力结构分化

## 📦 开源硬件与工具

### 8. [rpg-esim-python：纯 Python 的事件相机模拟器（RPG ESIM 移植）](https://github.com/lianeheidemann/rpg-esim-python)
- **功能**: 把苏黎世理工 RPG 的 ESIM 事件生成内核移植为纯 Python——用普通视频序列模拟事件相机输出
- **上手**: `pip install` 即可在无硬件条件下开发/调试事件相机算法（SLAM、去模糊、高速检测）
- **视觉关联**: 事件相机硬件仍小众（Sony IMX636/Prophesee），模拟器降低入门门槛——适合算法预研

---

*数据窗口 2026-08-24 ~ 08-26 · SemiAnalysis（停更）/ EETimes / NVIDIA / Tom's Hardware / SemiEngineering / Hackaday / Sony / OmniVision / GitHub / Google News(国产) / Reddit（403）*
