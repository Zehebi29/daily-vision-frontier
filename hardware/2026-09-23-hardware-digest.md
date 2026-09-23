# ⚙️ 2026-09-23 视觉硬件日报

> 扫描 9 渠道，精选 7 条 + 快讯 | 窗口 09-17 ~ 09-23
> 主线：**车规 SerDes 下放到创客板**、**星上 AI 推理把对地观测从小时压到分钟**、**中国 AI 加速器与 DRAM 双线推进**
> 注: Sony 官网最新仍为 9/7 Aramco MoU（本周无新品）；OmniVision `/news/` 与 `/company/press-releases/` 均 404；SemiAnalysis feed 停 2025-09；Reddit 403 / GitHub Search 限流

---

## 🎥 传感器与采集

### 1. [Raspberry Pi 5 双 GMSL2 相机 HAT：MAX96716A 让 Pi 接 10 米同轴车规相机](https://www.cnx-software.com/2026/09/17/raspberry-pi-5-gets-dual-gmsl2-camera-hat-based-on-max96716a-deserializer/)
- **什么**: BE-IIS（Brechel）BE-IIS-2CAM HAT+——ADI MAX96716A GMSL2 解串器，2× Rosenberger FAKRA 输入，配 MAX96717 相机侧串行器板
- **规格**: 每路 **6 Gbps**、**PoC 同轴供电**、双 CSI-2 lane/相机；实测双 IMX708（2304×1296 RAW10）**10 米同轴线**稳定；相机侧电压跳线 5/9/12/16/24V
- **判断**: GMSL2 此前是车厂/工业专供，现经 HAT+ 直接落到 1.3M 台 Pi 生态——**长距离、低延迟、单线供电**三合一，是立体视觉/机器人/车载原型最省事的采集方案；驱动走 apt 包即可，不用重编内核

### 2. [WLV-01：可换传感器的开源 DIY 相机，M4/3 全光谱 + 单色版](https://www.cnx-software.com/2026/09/18/wlv-01-hackable-diy-digital-camera-features-raspberry-pi-5-interchangeable-sensors/)
- **什么**: 众筹开源相机——RPi 5 (2GB) + 可插拔传感器卡匣 + 手动 Sony E 卡口（C/M/M42/Nikon F/Pentax K/Canon FD/Leica M 转接）
- **规格**: IMX585 1/1.2″ 8.3MP（全光谱/单色）、**IMX294 / IMX492 M4/3 11MP binned / 47MP unbinned**；4″ DSI 屏、18650 供电、3D 打印机身
- **判断**: 价值不在画质而在**传感器可换 + 全光谱/单色可选**——一台机器做 IR、单色低光与 Bayer 对比，是光谱/低光算法的低成本取证平台

### 3. [「超算一号」(S-AIDC-1)：中国首颗星上 AI 推理卫星，对地观测处理从小时压到分钟](https://www.tomshardware.com/tech-industry/space/china-puts-ai-compute-into-orbit-with-supercomputing-1-satellite-onboard-processing-aims-to-cut-earth-observation-data-processing-from-hours-to-minutes)
- **什么**: CAS Space 力箭一号 9/20 一箭九星，S-AIDC 研制的「超算一号」搭载**高分辨率光学载荷 + 星上图像处理 AI 计算机**
- **亮点**: 在轨完成判读，不回传原始影像——绕开**星地下行带宽瓶颈**（遥感的真实瓶颈已不是分辨率而是链路）
- **判断**: 6 月成立的「太空计算产业创新中心」把火箭、卫星、晶圆厂、AI 公司拉到一个盘子；这不是轨道数据中心，而是**边缘 AI 的极限场景**——功耗、散热、抗辐照三约束下的推理栈

## 🖥️ GPU 与算力

### 4. [阿里平头哥 真武 V900：216GB 显存 + 500,000 卡超节点，2027Q1 量产](https://www.tomshardware.com/tech-industry/artificial-intelligence/alibaba-unveils-zhenwu-v900-ai-accelerator-claims-its-the-most-powerful-ai-chip-in-china-accelerator-supports-500-000-chip-supercluster-with-a-10t-parameter-qwen-model-on-the-roadmap)
- **什么**: 训练/推理一体加速器，Apsara 2026 发布，CEO 吴泳铭称「中国最强 AI 芯片」，性能为上一代 M890 的 **3×**
- **规格**: **216GB 显存**、**1,200 GB/s 片间带宽**；超节点从 M890 的 128 卡 → **>1,000 卡单系统、可扩至 50 万卡**；对标昇腾 960PR（192GB / 2.4TB/s，2027Q3）
- **判断**: **未公布 FLOPS、制程、代工厂、功耗**——「3×」无绝对基准，需等实测；真正的信号是**目标 5–10T 参数 Qwen 训练**与年更节奏，国产算力从「能推理」转向「敢训大模型」

### 5. [Brainchip AKD1500：神经形态边缘 AI 卡，800 GOPS @ <300mW，$99 起](https://www.cnx-software.com/2026/09/21/brainchip-akd1500-m-2-and-pcie-edge-ai-cards-brainboard-1500-spi-module/)
- **什么**: Akida Neuron Fabric 协处理器——M.2 B+M Key 开发卡 $129、BrainBoard 1500（SPI，Nicla 尺寸）$99、PCIe 卡 $149
- **规格**: 400MHz 下 **800 GOPS / <300mW**（典型 250mW）；**22nm FD-SOI**；1MB 片上内存；**片上学习、无需上云**；休眠低至 mW、OFF 态 37µW
- **判断**: 能效比传统 NPU 高一个量级，适合**事件相机/常开视觉（always-on）** 与关键词唤醒类前端；M.2 直插 RPi 5 意味着可实测——扣分项是 SNN 模型生态仍窄，工具链是最大风险而非芯片

### 6. [NVIDIA Isaac ROS 5.0：把 AI Agent 拉进机器人开发，ROS Lyrical + Ubuntu 24.04](https://blogs.nvidia.com/blog/isaac-ros-5-0-agentic-open-source-robotics/)
- **什么**: ROSCon Toronto 发布——GPU 加速 ROS 包集合，面向 **Jetson** 的物理 AI 部署；支持 ROS Lyrical / Ubuntu 24.04
- **亮点**: 与 Open Source Robotics Alliance 共同贡献标准化数据接口，并引入 agentic 工作流辅助开发
- **判断**: 覆盖 **~130 万 ROS 用户**——NVIDIA 在机器人视觉栈继续「用开源换默认」；升级收益主要在**平台支持与数据接口标准化**，而非新算子

## 🔩 芯片与半导体

### 7. [CXMT G5 五代 DRAM 量产（11.95nm half-pitch）；DRAM 每 mm² 单价已超 TSMC N2](https://www.tomshardware.com/pc-components/dram/chinas-cxmt-hits-12nm-class-dram-milestone-new-5th-gen-dram-tech-uses-quadruple-patterning-to-boost-die-capacity-by-50-percent)
- **动态**: 长鑫 G5 用**四重曝光**把有源区 half-pitch 压到 **11.95nm**，HKMG 把核心阵列高度降到 6,762nm，电容深宽比 **45:1**；首发 **24Gb LPDDR5X 已量产，容量 +50%**
- **配套读数**: [Kurnal Insights 测算](https://www.tomshardware.com/pc-components/dram/dram-is-now-more-expensive-than-compute-chips-on-per-area-basis-ai-demand-drives-memory-die-value-past-leading-edge-silicon) 1b DRAM ≈ **$0.654/mm²**，已高于 TSMC N2（$0.424）与 N3（$0.283）
- **影响**: SK hynix 称 10nm 以下电容深宽比需 **>100:1**，45:1 说明 CXMT 仍在追赶但已进 10nm 级赛区；对视觉硬件的直接含义是**安防相机/NVR/边缘盒子的 DRAM 成本继续成为设计约束**——内存贵过算力硅，2027 才见顶

---

## 📰 产业动态

- **出口管制**: [字节通过挪威 Nscale 数据中心拿到 2,000+ 颗 NVIDIA B200](https://www.tomshardware.com/tech-industry/data-centers/filing-reveals-how-bytedance-gained-access-to-over-2-000-nvidia-b200-chips-through-nscales-norway-data-center-singaporean-subsidiary-spring-contributed-73-percent-of-uk-neoclouds-2025-revenue)——新加坡子公司贡献该 neocloud 2025 年 **73%** 营收；算力租用成为绕开实体清单的通道
- **IP 与互连**: [GUC 发布 2nm 16 Gbps HBM4E PHY IP](https://www.eetimes.com/guc-announces-2nm-16-gbps-hbm4e-ip/)——HBM 提速直接决定视觉大模型推理的 batch 吞吐上限
- **封测地理**: [SEMICON INDIA 2026：印度开始封装芯片](https://www.eetimes.com/semicon-india-2026-india-starts-packaging-chips-as-ecosystem-takes-shape/)——供应链多元化从「设计」走向「后端」

---

*渠道: CNX Software / Tom's Hardware / EETimes / SemiEngineering / NVIDIA Blog / Sony Semicon / OmniVision / SemiAnalysis / GitHub · 备查: Sony 最新 9/7 后无新品；OmniVision 站点 404；Reddit 403；GitHub Search 限流；SemiAnalysis feed 停更*
