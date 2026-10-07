# ⚙️ 2026-10-07 视觉硬件日报

> 扫描 10 渠道（CNX Software · EETimes · NVIDIA · SemiEngineering · Tom's Hardware · SemiAnalysis · Sony Semicon · GitHub · HuggingFace · Reddit），精选 7 条 + 快讯
> 窗口 10-01 ~ 10-07 | 主线：**存算一体打破「边缘跑大模型」的功耗墙**、**内存/封装成为 AI 芯片真正的瓶颈战场**、**ToF 与 RISC-V 相机板进入模块化量产期**
> 注：Reddit 403/429 不可用、SemiAnalysis feed 停在 2025-09、Sony Semicon 最新仍为 9/7 Aramco MoU（本周无传感器新品）

---

## 🎥 传感器与采集

### 1. [XIMEA MU003TG-SY-UC：26mm 微型 ToF 模组，Sony IMX556 + 独立 VCSEL 同步接口](https://www.cnx-software.com/2026/10/06/ximea-mu003tg-sy-uc-a-miniature-modular-0-3mp-usb-3-0-tof-sensor-based-on-sony-imx556/)
- **什么**: 工业 iToF 相机——Sony **IMX556** CMOS ToF 传感器（global shutter，无片上滤光片）+ USB 3.2 Gen1
- **亮点**: **640×480**、像素 **10µm**、1/2″，12-bit；**60/120/240 ToF phases/s**；曝光 0.25–1000µs；**功耗 0.45W 待机 / 1.8W 流式**；**26.4×26.4×28.67mm / 31g**；C-mount
- **视觉关联**: 机器人抓取、UAV、3D 扫描、人脸识别——空间受限的嵌入式深度
- **对比/判断**: 硬件本身是 IMX556 的成熟规格，**真价值在「解耦」**：照明源与 band-pass 滤光片走独立 10-pin Cabline V（5V + LVDS 触发 + I2C 遥测），同一模组可自由适配不同 VCSEL 与量程——**ToF 从「整机方案」变成「可拼装的深度积木」**

## 🖥️ GPU 与算力

### 2. [Axelera Europa：629 TOPS INT8 @35W，「存内计算」把数据中心推理塞进嵌入式功耗包络](https://www.eetimes.com/axelera-ai-data-center-inference-performance-in-the-power-envelope-of-embedded-systems/)
- **什么**: 面向 Physical AI 的推理加速器——**Digital In-Memory Compute（DIMC）**把占推理 ~80% 的矩阵-向量乘放进存储单元内算
- **性能**: **629 TOPS INT8**（8 颗二代 AI 核）· 16 个片上 RISC-V 向量处理器（前后处理）· **LPDDR5 200GB/s** · 硬件 HEVC/H.265 解码 · Kudelski KSE3 安全飞地 · **LLM 推理 35W 典型**
- **形态**: **Edge 232p**（half-height/half-length PCIe 卡）与 **Server 250p**（FHFL，4 个 APU）——标准槽位、现有服务器，免新机架/新散热
- **判断**: CEO 的核心论点是对的——**瓶颈不是算力而是数据搬运**，DIMC 直接砍掉 80% 的数据流动；配套 **Voyager SDK** 直吃 PyTorch（CNN/Transformer VLM/LLM 全支持）+ **Wingman** 自然语言生成流水线，且 RISC-V 开源无锁定。真正的看点是**「数据不能出厂」的行业（制造/医疗/城市）就地推理**这一场景被正面满足

### 3. [NVIDIA DGX Spark 新增 64GB 统一内存 SKU：GB10 Grace Blackwell，本地跑 100B 模型](https://blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/)
- **什么**: 个人 AI 超算桌面机新配置——沿用 **GB10 Grace Blackwell** 超级芯片 + ConnectX-7 + DGX OS 全栈，仅内存档位下探
- **性能**: **64GB 统一内存**（另有 128GB 版），支持 **100B 参数**模型本地推理/微调；两台可经 **Sync Cluster Assistant** 零配置组网
- **获取**: 本月起由 **Acer / ASUS / Dell / Gigabyte / HP / MSI** 厂商渠道独家供 64GB SKU
- **视觉关联**: 本地 VLM/检测/分割模型的边缘开发与 fine-tune 入口
- **判断**: 这是**「边缘视觉大模型」的消费级价格锚点**——把 100B 级模型的私有化部署从机房搬到工位；对研发生态的意义大于对推理 TCO 的意义

### 4. [DEBIX M8391-01：MediaTek Genio 720（9 TOPS NPU）+ 双 ISP，工业级视觉 SBC](https://www.cnx-software.com/2026/10/05/debix-m8391-01-industrial-sbc-features-mediatek-genio-720-soc-with-9-tops-npu-dual-display-support/)
- **什么**: 信用卡大小的工业 SBC——**MT8391 / Genio 720**（2×A78@2.6GHz + 6×A55，Mali-G57 MC2）
- **规格**: **NPU850 9 TOPS** + **2×独立 ISP**；4-lane MIPI CSI **最高 32MP@30fps**；LPDDR4 4/8/16GB，eMMC + M.2 NVMe + microSD；2.5K MIPI DSI / eDP 1.4 4K；2.5GbE PoE、Wi-Fi 6；**-40~+85℃**
- **视觉关联**: 边缘 AI 视觉、机器人、工业 IoT——多目 + 本地推理一体
- **判断**: **「双 ISP + 9 TOPS」是边缘视觉的实用配比**：ISP 独立承接多路传感器数据流，才能让 NPU 专注感知模型；温度范围与 PoE 说明它是**工业现场而非创客**定位

## 🔩 芯片与半导体

### 5. [Kepler：3D 铁电存储器 2027 量产，宣称「每瓦带宽比 HBM 高 5–10×」](https://www.eetimes.com/kepler-aims-to-launch-energy-saving-replacement-for-hbm-in-2027/)
- **动态**: 2018 年成立的 Kepler Computing（创始人多来自 Intel，Intel Capital 投资）计划**明年量产**两类存储器——一个替代 HBM、一个替代 SRAM；已自建 fab，代工伙伴 **GlobalFoundries**
- **参数**: 密度提升 **2–3×**、后端工艺（BEOL）兼容 CMOS；**每瓦带宽 5–10× 于 HBM**；宣称**无需 EUV** 即可冲先进节点，投资仅 1/10；**2027 全部产能已分配**
- **判断**: **叙事极强、验证极少**——铁电材料成分/电极/梯度「绝不公开」（理由是规避对手绕过 EUV），客户除 GF 外一律不具名。若 5–10× 带宽/瓦为真，对视觉大模型推理是**内存墙级**利好；但目前**只有参数声明、没有第三方基准**，建议列入「高关注、待证伪」

### 6. [Everspin：业界首个 CXL 挂载 DDR4 MRAM，做 DRAM 与 NAND 之间的持久层](https://www.eetimes.com/cxl-connected-mram-address-ai-storage-latency/)
- **动态**: SNIA 开发者大会演示——**4×1GB Everspin DDR4 MRAM** 经 **Wolley CXL 3.2 控制器**组成 **4GB 连续持久内存池**；平台为 Supermicro 服务器（AMD EPYC 9355 + Alveo U250 FPGA），已过 MemTester / GSA 验证
- **参数**: 以 CXL.mem 语义访问，**延迟比 NVMe NAND SSD 低约 100×**，断电保持、无需电池/超级电容
- **判断**: 定位是**持久缓存层而非 NAND 替代**——切中 AI 系统里「GPU 等 checkpoint I/O 空转、利用率跌破 50%」的痛点；与上一条 Kepler 同向：**AI 芯片战争已从算力转向存储层级**

## 📦 开源硬件与工具

### 7. [Avaota F2：首款 Allwinner V861 双核 RISC-V SBC，1 TOPS AI-ISP + PTZ，硬件全开源](https://www.cnx-software.com/2026/10/02/avaota-f2-allwinner-v861-risc-v-sbc-targets-ai-cameras-with-ptz-and-audio-support/)
- **什么**: AI 相机主板——Allwinner **V861** 双核 64-bit RISC-V（XuanTie **C907** RVV1.0 + **E907**），片上 **128MB DDR3**
- **规格**: **1 TOPS INT8 NPU**（称 AI-ISP 2.0）；4K@25 H.265 编码；支持 **GC8613（3840×2160@15fps）** 与 GC2083；8× 铸孔**电机控制**（PTZ）＋ 双麦单扬；约 **40×22mm**
- **上手**: 原理图/PCB/Gerber/STEP/BOM 全开放，**CC0 许可**，GitHub 可得
- **判断**: **「1 TOPS + 片上 128MB + RISC-V」是超低成本智能相机的完整底座**，PTZ 电机接口说明它瞄准云台 IPC；短板是**无 WiFi、无 NPU 工具链生态**——适合放进量大面广的视觉产品做二次开发，而非高端感知

---

## 📰 产业动态

- **机器人视觉软件**: [NVIDIA Isaac ROS 5.0](https://blogs.nvidia.com/blog/isaac-ros-5-0-agentic-open-source-robotics/) 于 ROSCon Toronto 发布，支持 ROS Lyrical + Ubuntu 24.04，引入 agentic 开发流——**感知栈开始「AI 写 AI」**
- **边缘立体深度**: HuggingFace 上 [nvidia/c-fast-foundationstereo](https://huggingface.co/nvidia/c-fast-foundationstereo)（zero-shot 立体匹配、ONNX/TAO、EdgeNeXt+ConvGRU、real-time）与 [Depth Anything 3](https://huggingface.co/depth-anything/DA3NESTED-GIANT-LARGE) 同榜——**深度感知继续「软件化 + 边缘 ONNX 化」**
- **工业算力**: [AAEON UP Xtreme PTL Edge Air](https://www.cnx-software.com/2026/10/02/up-xtreme-ptl-edge-air-panther-lake-mini-pc-gets-airjet-solid-state-active-cooling-solution/) 用 **Frore AirJet** 固态散热替代厚散热片，Intel Panther Lake 平台 **CPU+GPU+NPU 合计 180 TOPS**（Arc B390 GPU 122 TOPS + 50 TOPS NPU），**薄 35% / 轻 43% / <21 dBA**
- **传感器静默**: Sony Semiconductor 本周无新品（最新 9/7 Aramco MoU），CIS 板块新品节奏继续让位于**索尼×TSMC 熊本合资产能落地**
- **封装议题**: [EETimes：汽车电子从电气化转向架构](https://www.eetimes.com/from-electrification-to-architecture-the-next-automotive-era/)——软件定义汽车正把**半导体封装与测试**推成新的设计约束

---

*渠道: CNX Software / EETimes / NVIDIA Blog / SemiEngineering / Tom's Hardware / SemiAnalysis / Sony Semicon / GitHub / HuggingFace / Reddit · 失败源: Reddit 403·429、SemiAnalysis feed 停更、Sony Semicon 无新品*
