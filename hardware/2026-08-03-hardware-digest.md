# ⚙️ 2026-08-03 视觉硬件日报

> 今日扫描了 SemiAnalysis · EETimes · NVIDIA · AMD · SemiEngineering · Tom's Hardware · Sony Semiconductor · GitHub · HuggingFace · Reddit 等 10 个渠道，精选 12 条

---

## 🎥 传感器与采集

### [Sony × 三菱电机成立合资公司，做制造场景 AI 视觉传感器](https://www.sony-semicon.com/en/news/2026/2026072201.html)
- **什么**: Sony Semiconductor Solutions 与 Mitsubishi Electric 达成最终协议，成立合资公司 (JV)，面向工厂自动化 (FA) 开发 AI 视觉传感器解决方案
- **亮点**: 核心是把 AI 视觉分析直接做在 image sensor 上（on-sensor edge AI），Sony 出图像传感器 + 边缘 AI 技术，三菱出 FA 控制系统与产线经验；面向 labor-saving / 无人化制造
- **视觉关联**: 工业视觉检测、产线定位、机器人上下料 —— 这是「智能传感器」路线的标志性产业整合
- **对比**: 与一般"相机 + 外挂 AI 盒子"不同，JV 主打 sensor 级 AI，latency 和功耗优势明显；值得关注后续具体产品型号

### [Sony LYTIA 610: 业界首个 RB2×2 OCL 像素结构手机传感器](https://www.sony-semicon.com/en/news/2026/2026062401.html)
- **什么**: 1/2-type 约 64MP 堆叠式 CMOS，面向移动影像，6 月 24 日发布（本期补录）
- **亮点**: 业界首个 RB2×2 On-Chip Lens 像素结构 —— 同一 sensor 上混合 1×1 OCL（保分辨率）与 2×2 OCL（提对焦），配合专用算法，高分辨率与 AF 性能兼得
- **视觉关联**: 手机影像、对焦速度是 AR/扫码/人像等场景关键指标
- **对比**: 传统 2×2 OCL 牺牲分辨率换对焦，LYTIA 610 试图两全；是像素级光学设计的创新点

### [Sony IMX711: 业界最快 X-ray CMOS，26,100 fps](https://www.sony-semicon.com/en/news/2026/2026060901.html)
- **什么**: 直接转换型 charge-integrating X-ray CMOS，用于检测与测量仪器
- **亮点**: 最大 26,100 fps（业界最快，charge-integrating 类目），3.73-type (27.88 × 52.85 mm)，约 28 万有效像素
- **视觉关联**: 电池/半导体内部缺陷检测、材料科学 X 射线成像 —— 与产线视觉质检强相关
- **对比**: 速度是同类竞品的量级领先，直接转换结构免去闪烁体环节

## 🖥️ GPU 与算力

### [AMD 发布 Instinct MI400 系列 + Helios Rackscale，CDNA 5 上 2nm](https://www.amd.com/en/news/aai-2026-mi400-instinct-update/)
- **什么**: AAI 2026 上发布的下一代 AI GPU 旗舰系列，配套 Helios 整机柜方案
- **性能**: MI455X 号称 3200 亿晶体管、最高 40 PFLOPS AI 算力、HBM4 显存（MI400 单卡 144GB HBM4 传闻，Meta 已计划定制使用）；CDNA 5 架构、2nm 制程；同时发布 ROCm.ai 与 "Gorgon Halo"
- **视觉关联**: 训练/推理通用算力，视觉大模型训练的主力备选；HBM4 带宽利好多模态大 batch
- **获取方式**: 云厂商采购为主，Cirrascale 等已开放 Helios 方案

### [AMD Kria AI 机器人开发平台 + Ryzen AI Embedded X100，押注 Physical AI](https://www.amd.com/en/news/aai-2026-kria-robotics-dev-platform/)
- **什么**: 面向 Physical AI 的 turnkey 集成平台（Kria AI 机器人开发板/方案）与 Ryzen AI Embedded X100 异构计算产品线，7 月 23 日发布
- **性能**: 主打 CPU+GPU+NPU 异构，为实时机器人感知/控制提供可落地的边缘算力；配套 Open Robotics Partner Network
- **视觉关联**: 机器视觉、SLAM、抓取、人形机器人边缘推理
- **对比**: 正面回应 NVIDIA Jetson 生态，Kria 的差异化在 FPGA 自适应算力 + 开放伙伴网络

### [NVIDIA Vera Rubin NVL72 量产爬坡：10x 每兆瓦吞吐，Spectrum-6 配套落地](https://blogs.nvidia.com/blog/vera-rubin/)
- **什么**: Vera Rubin NVL72 已在 CoreWeave、Google Cloud、Azure、Oracle、Nebius 等伙伴机架运行；配套 Spectrum-6 以太网 (102.4T 交换 + 1.6T ConnectX-9 SuperNIC) 与业界首个量产 CPO 共封装光模块
- **性能**: CoreWeave DeepSeek-R1 基准显示每 MW 吞吐为 GB200 NVL72 的 10 倍；7 颗芯片 + 5 个机架托盘系统级协同设计；机架内无缆/无风扇/无软管，装配从数小时降到 1 分钟
- **视觉关联**: 大规模视觉模型训练/推理的算力底座，token cost 持续下探利好多模态应用
- **获取方式**: 云实例（CoreWeave、Azure、GCP 等）

### [NVIDIA Jetson 边缘 AI 推广：67 TOPS 的 Orin Nano Super](https://blogs.nvidia.com/blog/build-ai-with-nvidia-jetson/)
- **什么**: NVIDIA 博客周专题，强调 Jetson 平台在机器人/边缘 AI 的部署能力
- **性能**: Jetson Orin Nano Super 67 TOPS（INT8），桌面级生成式 AI 能力装进开发板；平台覆盖 Orin Nano Super → AGX Orin → AGX Thor
- **视觉关联**: 机器人、CV 教学、边缘原型验证的标准平台
- **获取方式**: 开发者套件零售，第三方载板生态成熟

## 🔩 芯片与半导体

### [CEA-Leti 推进 3D 堆叠路线图：AI 撞上内存与功耗墙](https://www.eetimes.com/cea-leti-pushes-stacking-roadmap-as-ai-runs-into-memory-and-power-limits/)
- **动态**: CEA-Leti（法国研究机构）更新 stacking 路线图，应对 AI 的内存带宽与功耗瓶颈；重点在 3D 集成、混合键合 (hybrid bonding)、chiplet 互连
- **影响**: 对视觉硬件意味着更高带宽的 sensor+ISP 堆叠、HBM 迭代路径、边缘 AI 芯片功耗密度问题；欧洲先进封装话语权信号

### [美国 CHIPS Act 再拨 $874M R&D 激励 + 行业周报：DRAM 短缺、UMC 扩产](https://semiengineering.com/chip-industry-week-in-review-149/)
- **动态**: 美国商务部与 7 家公司签署意向书，最多 $874M CHIPS R&D 激励，覆盖集成光子、先进封装、衬底、新材料、新型内存、计算架构与供应链安全；周报还提到 DRAM 短缺持续、UMC 扩产、中国 immersion DUV 进展
- **影响**: 先进封装与新型内存直接关系传感器堆叠与 AI 加速器；DRAM 短缺会推高边缘设备 BOM 成本，值得关注视觉终端定价

### [首尔大学：NAND+DRAM 混合内存，加快数据传输](https://semiengineering.com/nad-memory-combines-nand-flash-and-dram-for-faster-data-transfer-u-of-seoul/)
- **动态**: 研究级新内存架构，将 NAND 与 DRAM 融合，缩短大容量存储与高速缓存之间的数据通路
- **影响**: 若产业化，可改善边缘视频流/大模型权重加载的带宽瓶颈；距离商用尚远，先标记为技术风向

## 📦 开源硬件与工具

### [HuggingFace 边缘部署热榜：Depth-Anything GGUF + 量化 SAM 3.1](https://huggingface.co/mudler/depth-anything.cpp-gguf)
- 功能描述: `depth-anything.cpp-gguf` 把 Depth Anything 转成 GGUF，可在 CPU/低功耗设备跑单目深度估计；另有 `Sparknight/sam3.1-int8-int4-convrot` 量化版 SAM 3.1（分割一切）适配端侧
- 上手方式: GGUF 直接加载到 llama.cpp 系运行时 / 量化权重替换原模型，适合 Jetson、树莓派类设备
- 视觉关联: 深度估计与分割是机器人/AR 的核心能力，端侧化趋势明显

## 📰 产业动态

### [Qualcomm 约 $40 亿收购 Modular：开源 AI 软件栈背后的异构算力野心](https://www.eetimes.com/why-qualcomm-bought-an-open-ai-software-stack/)
- 核心内容: EE Times 专访 Modular 联创 Tim Davis —— 收购（接近 $40 亿）的逻辑是"AI 计算必然异构"，软件是让非 GPU 硬件（NPU/边缘芯片）跑推理的关键；Qualcomm 从 edge 到 cloud 的硬件版图需要一套 hardware-agnostic 的开放软件栈
- 影响: 边缘 AI 推理部署的软件标准之争升温，Qualcomm 在视觉端侧 NPU 的生态卡位

### [Big Tech AI 基础设施投入破 $1 万亿，2026 年还要再加 $745B](https://www.tomshardware.com/tech-industry/big-tech/big-tech-spends-more-than-usd1-trillion-on-ai-infrastructure-additional-usd745-billion-expected-to-be-added-to-the-figure-in-2026-alone)
- 核心内容: 主要科技巨头累计 AI 基础设施支出超过 $1T，2026 年预计再增 $745B
- 影响: GPU/加速卡、HBM、先进封装、数据中心网络持续紧缺；对视觉行业意味着云算力价格战与硬件迭代加速并存

---
