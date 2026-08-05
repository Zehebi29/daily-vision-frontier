# ⚙️ 2026-08-05 视觉硬件日报

> 今日扫描了 SemiAnalysis · EETimes · NVIDIA · SemiEngineering · Tom's Hardware · Sony Semiconductor · AMD · GitHub · HuggingFace · Reddit 等 10 个渠道，精选 11 条
> 注: 8/3 日报已覆盖 Sony × 三菱电机 JV、LYTIA 610、IMX711、AMD MI400/Kria、Vera Rubin、Jetson，本期聚焦 8/1–8/5 的新动态，不重复。

---

## 🎥 传感器与采集

> 本期窗口（8/1–8/5）Sony / OmniVision 均无重磅新品发布；Sony 近三个月动作集中在 [SPAD LiDAR 深度传感器](https://www.sony-semicon.com/en/products/smart_sensing/spad_tof/index.html) 与 [Event-based Vision Sensor (EVS)](https://www.sony-semicon.com/en/technology/sensor/evs.html) 两条前瞻产品线 —— 前者面向车载/机器人 LiDAR 量产上车，后者是低延迟事件视觉的商用化标杆，值得持续跟踪。

## 🖥️ GPU 与算力

### [NVIDIA Alpamayo 2 Super：面向 Robotaxi 的开源推理模型开放商用](https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available/)
- **什么**: Alpamayo 家族（HF 上最被广泛采用的自动驾驶开源推理模型）新一代旗舰，8/4 开放商用许可
- **亮点**: 基于 NVIDIA Cosmos 3 Super Reasoner，经 RL 后训练；统一支持检测/预测/规划/长尾场景推理，决策可 inspect；采用 Linux Foundation OpenMDW-1.1 许可，允许微调、衍生与商用再分发
- **视觉关联**: Robotaxi / L4 感知-决策全栈的「大脑」开源化；部署端跑在 Drive AGX / Thor 级车载算力上，推理时延直接决定安全冗余设计
- **对比**: 与闭源方案（如各厂自研端到端模型）相比，OpenMDW-1.1 让 OEM/Tier1 保留数据与模型主权；这是「模型开源 + 车载芯片锁定」双轮驱动的又一信号

### [AMD Q2 2026 财报：数据中心营收同比翻倍，游戏 GPU 大跌 31%](https://www.amd.com/news/amd-2q-2026-earnings/)
- **什么**: AMD 8/4 发布 2026 Q2 财报，AI 算力业务成为绝对主引擎
- **亮点**: 数据中心营收同比 +100%；游戏业务 -31%（Lisa Su 归因于价格与需求结构）；此前官宣与 Anthropic 合作部署至多 2 GW Instinct MI450 系列 GPU
- **视觉关联**: Instinct 系列是视觉大模型训练/推理的第二大算力来源，MI450 + HBM4 的放量节奏直接影响多模态模型训练成本
- **获取方式**: 云实例（Azure/AWS 等）与超大规模定制采购为主

### [GPU 价格风暴：RTX 50 韩国涨 30%、GDDR7 模组 $20/颗、TSMC 晶圆涨价传导](https://www.tomshardware.com/pc-components/gpus/in-a-troubling-sign-nvidia-rtx-50-series-prices-jump-up-to-30-percent-in-south-korea-tsmc-wafer-hikes-and-usd20-gddr7-modules-push-rtx-5090-past-usd5-100)
- **什么**: 8/3–8/4 多家渠道信号显示消费级 GPU 价格持续飙升，日本分销商警告 Gigabyte 订单再涨 20–40%
- **亮点**: RTX 5090 韩国市场已破 $5,100；TSMC 晶圆涨价 + GDDR7 颗粒 $20/颗是主因；内存短缺外溢到 PC（HP/Asus/Acer 开始小批量用 CXMT 国产内存）
- **视觉关联**: 边缘视觉/桌面 CV 工作站的 BOM 成本被推高；VRAM 涨价直接打击本地微调与大图推理的用户预算
- **对比**: 「AI 算力涨价 + 游戏 GPU 跌量」的结构性分化说明产能被 AI 虹吸，短期内 DIY/CV 玩家采购策略需提前

## 🔩 芯片与半导体

### [HBF 规范发布：Sandisk × SK hynix 把 NAND 做成「类 HBM」，GPU 可挂 TB 级内存](https://www.tomshardware.com/pc-components/ssds/sandisk-and-sk-hynix-unveil-hbf-spec-up-to-16-hi-nand-stacks-3-tb-s-bandwidth-ucie)
- **动态**: 8/4 双方经 Open Compute Project (OCP) 发布 High Bandwidth Flash (HBF) 开放规范，融合 3D NAND 非易失性与 HBM 高带宽
- **亮点**: 首批定义 8-Hi/16-Hi NAND 堆叠、单包最高 512GB；带宽分三档 0.4–3.0 TB/s —— 最高档超过单条 HBM4 (2 TB/s)；采用 UCIe 接口便于异构 chiplet 集成
- **影响**: 对 AI 推理与边缘视觉意味着「大容量权重 + 近存计算」的新内存层级；若落地，可缓解 GPU HBM 容量焦虑（TB 级权重常驻），对端侧大模型部署是长期利好
- **判断**: 真突破还是画饼？—— 规范先行、量产未定，且 NAND 延迟远高于 DRAM，适合权重流式加载而非随机访问；属「值得盯的路线图」而非今年可用的产品

### [Kioxia × Sandisk 展示全球最高密度 3D NAND：BiCS10 QLC，332 层 / 37 Gb/mm²](https://www.tomshardware.com/pc-components/ssds/kioxia-and-sandisk-demonstrate-the-worlds-highest-density-3d-nand-flash-332-active-layers-and-up-to-4-800-mt-s-interface)
- **动态**: FMS 2026 大会正式介绍 BiCS10 3D QLC NAND，面向数据中心级高容量 SSD
- **亮点**: 332 有源层、37 Gb/mm² 面密度（全球最密，较上代 TLC 的 29 Gb/mm² 提升约 28%）；接口最高 4,800 MT/s 并带 SCA 独立命令/地址能力；估计容量约 1.33 Tb；PI-LTT 技术降低高速输出驱动功耗
- **影响**: 视觉数据（监控录像、自动驾驶训练集、工业质检图库）是存储大头，更高面密度直接拉低 TB 成本；对边缘记录设备与数据中心冷存储都有意义

### [中国 DUV 光刻小批量下线：上海埃斯纳 5 台/年，ASML 市值蒸发 $440 亿](https://www.tomshardware.com/tech-industry/semiconductors/chinese-chipmaking-tool-roadmap-examined)
- **动态**: 7/27 报告称国产浸没式 DUV 光刻机开始小批量生产 —— 制造商为上海埃斯纳（2023/8 成立，注册资本 70 亿元，吸收华为系 Yuliangsheng 与 SMEE 团队）；2026 年约 5 台、2027 年约 20 台，首批交付 SMIC / 华虹 / CXMT 做产线验证
- **影响**: 5 台 vs ASML 年出货约 130 台，量产差距仍在一个数量级以上；但这是国产先进制程（7nm 级）自主化的关键一步，直接影响国产视觉 SoC（如昇腾、地平线、黑芝麻代工链）的供给安全叙事
- **判断**: 属「里程碑意义 > 产能意义」事件；对视觉硬件生态的短期影响在心理与政策层面，中期看代工产能释放

### [Intel Foundry 发布 240×240mm「超大规模」AI 芯片封装蓝图](https://semiengineering.com/from-blueprint-to-build-engineering-the-worlds-largest-ai-chips/)
- **动态**: 2026 ECTC 上 Intel Foundry 两支团队分别给出 HLFF (Hyper-Large Form Factor) 封装架构蓝图与配套封装材料工艺
- **亮点**: 单封装达 240×240 mm，集成计算 die 阵列 + HBM + I/O，基于 EMIB 互连；同步解决大尺寸封装的可靠封装（encapsulation）工艺
- **影响**: 视觉大模型训练靠「更大系统 + 更高算力密度」而非单纯制程微缩；这类封装能力决定下一代 AI 加速卡（含推理卡）的形态与成本，是先进封装军备竞赛的 Intel 回应

## 📦 开源硬件与工具

### [SpiNNaker2：TU Dresden × Manchester 发布「桥接深度网络与神经形态计算」的多核芯片](https://semiengineering.com/chip-bridges-neuromorphic-and-deep-network-computing-tu-dresden/)
- 功能描述: 论文 "The SpiNNaker2 Chip: A Many-Core Platform for Flexible and Scalable Brain-Inspired Computing"（IEEE OJCAS 2026）—— 面向 SNN/事件计算与常规深度网络双模式的 many-core 平台，基于 GlobalFoundries 22FDX、ARM M4F 核 + adaptive body biasing + DVFS
- 亮点: 高性能模式 INT8 最高 4.5 TOPS，高效率模式 2.7 TOPS/W；支持 event-based computing，Gbit 以太网互联、LPDDR4
- 上手方式: 学术路线为主（论文 + 开发板申请），适合事件相机（EVS）、脉冲神经网络、低功耗实时感知研究
- 视觉关联: 事件驱动视觉（event camera 后端处理）是天然适配场景；「深度网络 + SNN 混合」是边缘低功耗视觉的重要探索方向

### [Depth Anything 3 (DA3-BASE) 登顶 HuggingFace 深度估计趋势榜](https://huggingface.co/depth-anything/DA3-BASE)
- 功能描述: Depth Anything 系列第三代 Base 模型，趋势期下载量已超 10.6 万，稳居 depth-estimation 榜第一梯队；配合 `depth-anything.cpp-gguf` 等 GGUF 端口，可量化后在 CPU / Jetson / 树莓派类设备跑单目深度
- 上手方式: HF 直接下载权重；端侧用 GGUF + llama.cpp 系运行时
- 视觉关联: 单目深度是机器人、AR、自动驾驶 3D 感知的输入源，v3 系列在 edge 上的精度/功耗平衡值得实测

## 📰 产业动态

### [EETimes：NXP 看上 Ambarella —— 是汽车业务还是边缘 AI？](https://www.eetimes.com/nxp-eying-ambarella-is-it-about-automotive-or-edge-ai/)
- 核心内容: 8/3 分析报道，汽车 MCU 巨头 NXP 据传有意收购 Ambarella（边缘视觉 SoC 厂商：CV3-AD ADAS 系列、CV5/CV7x 安防与机器人视觉芯片）；市场关注点在其价值是车载摄像头 SoC 补强，还是更广的边缘 AI 卡位
- 影响: 若成真，这是继 Qualcomm×Modular 之后又一「边缘视觉算力整合」案例 —— Ambarella 的 ISP+NPU 架构与 NXP 的车规渠道互补性很强；对视觉硬件生态意味着边缘 SoC 竞争格局可能再次洗牌
- 判断: 目前是传闻/分析阶段，未官宣；但方向符合「汽车 + 边缘 AI 融合」的大逻辑

### [EETimes：太空新势力 —— 地球轨道之外的算力、功耗与散热挑战](https://www.eetimes.com/new-space-power-computing-and-thermal-challenges-beyond-earth/)
- 核心内容: 8/4 深度文章，讨论空间级（抗辐照）计算、成像载荷的功耗与散热约束 —— 视觉感知（星载相机、对地观测、在轨机器人视觉）在无对流散热、单粒子翻转环境下的硬件设计边界
- 影响: 太空视觉载荷从「定制辐照芯片」走向商用现货 (COTS) + 冗余架构，这对边缘视觉芯片厂商（Jetson 类、FPGA）是新兴市场信号

---

*数据窗口 2026-08-01 ~ 2026-08-05 · 来源: SemiAnalysis / EETimes / NVIDIA Blog / SemiEngineering / Tom's Hardware / Sony / AMD / GitHub / HuggingFace*
