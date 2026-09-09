# ⚙️ 2026-09-09 视觉硬件日报

> 今日扫描 12 渠道，精选 8 条 | 窗口 09-03 ~ 09-09
> 主线：**NVIDIA $12.9B 买下模型分发入口**、**Sony 传感器转向「AI 方案商」**（×Aramco）、**TSMC High-NA EUV 定档 2030**
> 注: Reddit 仍 403；OmniVision 新闻页 404；Sony 本周无新品但签工业 AI 大 MoU

---

## 🎥 传感器与采集

### 1. [Sony 半导体 × Aramco 签 MoU：图像传感 + 边缘 AI 进油气工业](https://www.sony-semicon.com/en/news/2026/2026090701.html)
- **什么**: 非约束性 MoU（9/7）——Sony image sensing/edge AI × Aramco 工业数据与 90+ 年运营场景
- **焦点**: 工业感知与态势监控、图像/视频智能接入 Aramco AI 平台做多模态理解；Aramco 做真实试验场
- **视觉关联**: 油气/化工等复杂环境的视觉巡检、安全监控——CIS 巨头从「卖传感器」转向「卖感知方案」
- **判断**: 延续 8/3「Sony×三菱电机」制造 AI 合资逻辑，垂直行业逐个击破；看点是如何应对防爆/高温等非标视觉场景

### 2. [清华发布感-算-存一体全光内存计算芯片：竞速无人机自主导航演示](https://semiengineering.com/chip-industry-week-in-review-154/)
- **什么**: 研究原型（SE 9/4 周报）——sensing + processing + memory 融合的 in-memory photonic computing，7,378 神经元
- **亮点**: 消除计算与外部存储间的数据搬运（光互连）；已用自主竞速无人机导航实测
- **视觉关联**: 仿视网膜「感知即计算」路线——与事件相机/神经形态视觉同赛道，未来超低时延边缘视觉候选
- **判断**: 光计算芯片距量产仍远，但「光感知融合」是 2026 学术界明确信号，值得追踪产业化路径

## 🖥️ GPU 与算力

### 3. [NVIDIA 以 $12.93B 收购 Hugging Face：AI 时代的「微软买 GitHub」](https://blogs.nvidia.com/blog/nvidia-to-acquire-hugging-face/)
- **什么**: 9/3 Jensen 官宣——18M 开发者、3M 模型、500K 数据集、200K 公司的模型分发层并入 NVIDIA
- **关键承诺**: HF 保持开放中立，不强制 NVIDIA compute，多云多加速器照常
- **视觉关联**: 视觉模型（含边缘 VLM/深度估计）的下载-部署-微调入口被算力巨头收编——Jetson/DGX 生态获得天然分发通道
- **判断**: 收购价精确到个位数；反垄断与「平台中立」话术能否兑现，决定开源生态走向——2026 最大生态事件

### 4. [NVIDIA 增持 MediaTek：$3.5B 可转债 + NVLink Fusion 平台对外授权](https://semiengineering.com/chip-industry-week-in-review-154/)
- **什么**: SE 9/4 周报：NVIDIA 买入 $3.5B MediaTek 可转债；MediaTek 将把 **NVLink Fusion 平台**作为自定义 AI 加速器客户的设计基础（[背景：NVLink Fusion XPU 生态](https://blogs.nvidia.com/blog/nvlink-fusion-xpu-ai-factory/)）
- **看点**: 双方继续合作 edge 与 automotive——NVIDIA 从「卖整机」延伸到「卖互连 IP 授权」
- **视觉关联**: 智驾/机器人定制芯片若走 NVLink Fusion 授权路线，将绑定 NVIDIA 生态（CUDA/工具链）
- **判断**: 绑紧 MediaTek = 卡位「非 NVIDIA 自研加速器」市场；可转债结构比直接入股更灵活，落地看授权客户名单

## 🔩 芯片与半导体

### 5. [TSMC High-NA EUV 量产导入定档 2030：A10/A11 为首批候选节点](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-to-start-using-high-na-euv-lithography-in-2030-a10-or-a11-technology-prime-candidates-for-use)
- **动态**: 9/8——High-NA EUV（0.55 NA）推进到 2030 年量产；A10/A11 为首批候选
- **影响**: 2030 后制程密度上限由此决定——图像传感器逻辑层、NPU/ISP 等「视觉算力」都吃这波红利；也牵动 ASML 设备出货节奏
- **判断**: 比 Intel（18A 即用 High-NA）保守但稳妥——良率优先策略延续；国产光刻在 High-NA 代际差距恐再拉大

### 6. [Arm CSS for Mobile 2「AI-Native」平台：C2-Ultra/C2-Pro + Mali G2-Ultra NX 神经图形](https://www.cnx-software.com/2026/09/08/arm-css-for-mobile-2-ai-native-platform-arm-c2-ultra-and-c2-pro-cpu-cores-mali-g2-ultra-nx-gpu/)
- **什么**: 9/8 发布——移动计算底座：CPU 带 SME2（Armv9.3-A，最高 14 核），Mali GPU 内置神经加速器
- **亮点**: neural graphics 原生跑在 GPU 上——渲染与神经处理同管；面向「AI 手机」影像/端侧多模态
- **视觉关联**: 移动端 AI 摄影、实时视频增强、端侧 VLM 的算力底座；下一批旗舰手机 SoC（联发科/三星）大概率采用
- **判断**: 把 NPU 塞进 GPU 是架构宣言——「视觉计算」将越来越多由 GPU 神经单元承担，专用 NPU 叙事被稀释

## 📦 开源硬件与工具

### 7. [Boardcon CM311Y3 SoM（Amlogic A311Y3）：8 TOPS 边缘 AI 模组，主打 4K 安防与机器人](https://www.cnx-software.com/2026/09/03/amlogic-a311y3-cortex-a78-a55-edge-ai-system-on-module-delivers-up-to-8-tops/)
- **功能**: 8 核（2×A78@2.4 + 6×A55@2.0 + RISC-V 协核）+ 8 TOPS NPU，210-pin 邮票孔模组
- **规格**: 最高 16GB LPDDR5 / 256GB eMMC；定位 4K 视频监控、边缘 AI、交互终端、自主机器人
- **上手**: Boardcon 提供配套开发板；国产边缘视觉方案的高性价比新选项（对标瑞芯微/海思同档）
- **判断**: 8 TOPS 卡在「轻量 VLM 边缘部署」甜点位；Amlogic 靠安防存量渠道放量，看点是谁家 NVR/机器人先采用

---

## 📰 产业动态

### 8. [Lyte 融资 $165M：为机器人造「定制硅 + 多模态传感器 + 空间软件」](https://semiengineering.com/chip-industry-week-in-review-154/)
- **核心**: SE 9/4 周报收录——机器人感知硬件公司扩产，覆盖自定义芯片、多模态传感器（相机/深度）与 spatial software
- **影响**: 机器人「感知栈自研化」资本升温——与 NVIDIA/MediaTek 抢同一批客户，差异化在传感器侧
- **快讯**: ① SEMI：半导体设备 Q2 出货 $40.53B（+23% YoY）；② NVIDIA RTX Spark Windows PC 十月开卖（联想/Acer，[IFA 2026](https://blogs.nvidia.com/blog/local-ai-ifa-next-gen-agents-nv-pair-rtx-spark/)）

---

*渠道: NVIDIA / EETimes / SemiEngineering / Tom's Hardware / CNX / Embedded / Hackaday / Sony / SemiAnalysis（feed 停 2025，弃用）/ OmniVision（404）/ GitHub / Reddit（403 第 7 日）· 备查: embedded world NA 非视觉；NVIDIA IFA 以软件为主仅记录*
