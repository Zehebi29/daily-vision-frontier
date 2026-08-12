# ⚙️ 2026-08-12 视觉硬件日报

> 今日扫描了 SemiAnalysis · EETimes · NVIDIA Blog · SemiEngineering · Tom's Hardware · AMD Newsroom · Sony Semiconductor · GitHub · HuggingFace · Hacker News 等 10 个渠道，精选 11 条
> ⚠️ Reddit API 仍被限流（403）；SemiAnalysis RSS 疑似停更（最新条目停在 2025-09）；AMD 官网新闻页为 JS 渲染抓不到条目，改走 EETimes 深度报道补位
> 注: 8/9 已覆盖 Firebird 亚美尼亚 AI 工厂、8/11 已覆盖 Rubin Ultra 降配内存版（192GB/HBM4），本期不重复；头条是 **AMD 机器人芯片路线图** 与 **FCC 光模块禁令**

---

## 🎥 传感器与采集

### 1. [Dirac：NV 色心金刚石量子传感器，用「地球磁场地图」做 GPS 拒止导航](https://www.eetimes.com/u-s-startup-fields-quantum-sensors-to-reduce-reliance-on-gps/)
- **什么**: 美国威斯康星初创 Dirac（2023 年成立，CEO Sanket Deshpande）量产的 NV-center（氮-空位色心）金刚石量子磁力计——把 70 年公开航测磁场数据融合成地球磁场地图，传感器本地匹配定位，彻底脱离卫星
- **硬件构成**: 5×5cm 封装立方体 = 金刚石衬底 + 光子提取层（塑料注塑光学件）+ 激光激发/荧光 + 光电二极管读出；边缘算力用 **NVIDIA Jetson Orin Nano**（后续计划换成 FPGA），模型量化后跑在「很小的芯片」上、不上云
- **供应链**: 金刚石来自芝加哥 Great Lakes Crystal Technologies 与 UChicago 衍生公司 staC12；目标进 **SkyWater 标准 CMOS 代工**量产（当前在大学 fab 小批量），约 1–2 年达到规模量产
- **视觉关联**: 与视觉 SLAM 是互补关系——地下/水下/隧道等视觉退化场景 + GPS 拒止环境（俄乌战场上 GPS 干扰已是常态）；应用包括海底电缆定位、海床测绘（全球 90% 海床未测绘）、无人机与飞行器导航；竞争对手 Q-CTRL、Google 系 SandboxAQ，中国量子传感进展被点名「紧追」
- **判断**: 值得关注的是「传感器走半导体化路线降本」而不是量子本身——把 NV-center 读出链路做成 CMOS 工艺，才是从实验室到量产的关键，这和 CIS 的早期路径一模一样

## 🖥️ GPU 与算力

### 2. [AMD 反「GPU 中心论」：Ryzen AI X100 + Kria AI SoM 押注人形机器人，126 TOPS 全整合 SoC](https://www.eetimes.com/amd-challenges-gpu-centric-architectures-as-it-takes-aim-at-nvidia-in-robotics/)
- **什么**: AMD Adaptive & Embedded 部门高调宣战 NVIDIA 机器人市场——核心论点「机器人脑子不只是一块大 GPU」：独立 CPU+GPU 有跨芯片延迟，物理 AI 要的是**确定性延迟**（camera input → ISP → 模型分类 → 动作闭环，全部限定延迟内完成）
- **规格**: Ryzen AI X100 = **Zen 5 CPU + 准独显级 RDNA 3.5 GPU + XDNA2 NPU** 单芯片 + 统一内存（软件动态分配内存给各计算引擎）；总 **126 TOPS INT8**，其中 NPU 约占 50 TOPS，负责常开的低功耗/低延迟 AI 负载
- **开放策略**: 新 Kria AI SoM 走 **COM-HPC 标准板型**（非私有格式）；载板上的 Spartan UltraScale+ FPGA 的 **原理图、BOM、RTL 全部开源**——直接对标 Jetson 生态的封闭性
- **视觉关联**: 机器人视觉感知是核心负载；AMD 强调「自主机器人 benchmark 里 CPU 需求 > GPU」，配合 FPGA/自适应 SoC 做全身分布式确定性计算（关节、传感器就近推理）
- **对比**: 这波是 AMD 对 Jetson Thor/Orin 在机器人侧的正面夹击——一边用 x86 生态 + 统一内存打「平台兼容」，一边用开源 RTL 打「开发者信任」；对视觉从业者意味着机器人端侧又多一个不绑 CUDA 的选择

### 3. [NVIDIA 发布 800 VDC 供电架构：AI 工厂从「堆瓦数」转向「改输电路径」，MGX 800VDC 机柜 2026H2 落地](https://blogs.nvidia.com/blog/800-vdc-power-architecture-ai-factory/)
- **什么**: NVIDIA 官方长文解释下一代 AI 工厂供电范式——瓶颈不是瓦数而是「电从电网到 GPU 的路径」：传统 AC 多次变换每级都有损耗，**800V 直流直供**砍掉中间变换级，让更多功率真正到达加速器
- **关键数字**: 与 **Google、Microsoft 在 OCP 联合开发**；2026 年 3 月联合白皮书 + **2026 年 7 月 LVDC 固态变压器规范 v0.3**；已有 **80+ 设备/基础设施厂商**按此规范做产品；**MGX 兼容 800VDC 供电机柜 2026H2 出货**，可插进现有 AC 机房、无需改造楼宇配电
- **视觉关联**: AI 工厂里的多模态/视频/机器人训练负载就是这代供电的「客户」——Rubin 时代单机柜功率密度继续上冲，供电架构决定算力能不能真正跑起来
- **判断**: 从 HVDC 480V → 800VDC 是行业级标准动作（类似当年 PCIe 供电标准化），比任何单颗芯片发布对数据中心形态的影响都更底层

## 🔩 芯片与半导体

### 4. [FCC 拟禁止进口中国光模块：占全球 56% 份额，直击 AI 数据中心互连命门](https://www.tomshardware.com/tech-industry/fcc-proposes-import-ban-on-chinese-optical-transceivers-blockade-targets-key-ai-interconnects-as-china-holds-56-percent-global-market-share)
- **动态**: FCC 提案禁止进口中国产光收发模块（optical transceivers）——Tom's Hardware 独家报道，中国占全球市场 **56% 份额**，在 **CPO（共封装光学）制造产能**上优势更明显
- **影响**: AI 集群的 scale-out 互连（800G/1.6T 光模块、InfiniBand/Ethernet 光链路，如 NVIDIA Quantum-X800 Q3450 CPO 交换机）高度依赖中国供应；禁令若落地，北美 AI 数据中心互连成本/交期将重演 GPU 短缺剧本，同时利好美系光模块（Coherent、Marvell 光部门、Fabrinet 系）
- **视觉关联**: 多模态大模型训练与具身智能数据中心的带宽需求正是光模块需求基本盘——互连被卡 = 集群有效算力被卡
- **判断**: 这是继 FCC 无人机感知能力禁令（8/10 报道）后，监管第二次把「算力基础设施关键部件」当作安全审查抓手；政策风险将成为 2026H2 算力供应链的常态变量

### 5. [Intel 募资 $19.7B（认购 $100B）备战 14A 量产：代工翻身仗的钱到位了](https://www.tomshardware.com/tech-industry/semiconductors/intel-raises-usd19-7-billion-to-help-fund-future-projects-as-14a-production-looms-share-sale-attracted-usd100-billion-in-demand-report-claims)
- **动态**: Intel 新股发行募得 **$19.7B**（认购需求高达 **$100B**，超额 5 倍），为 14A 量产及后续项目输血；14A（RibbonFET + PowerVia 的 1.4nm 级节点）投产在即
- **影响**: 与 8/8 报道的 SpaceX×Tesla Terafab 一期绑定 **Intel 14A** 相互印证——14A 代工一旦跑通，Intel Foundry 将拿到首个超大客户锚点；对视觉硬件生态：14A 是下一代车规/机器人芯片与 AI 加速器的潜在代工选项，全球先进制程供给从「TSMC 单极」走向多元化
- **判断**: $100B 认购说明市场愿意为「美国先进制程本土化」故事买单，但钱 ≠ 良率，真正的验证在 14A 爬坡数据

### 6. [HBM 成为 3D 封装良率的「试验田」：TSV/微凸点缺陷检测进入体系化时代](https://semiengineering.com/hbm-becomes-testbed-for-3d-assembly-yield/)
- **动态**: SemiEngineering 深度文章——HBM 堆叠（TSV、微凸点、高带宽接口）成为 3D 组装测试、DFT、可靠性的试金石；**BiST、嵌入式监控、boundary scan、at-speed 测试 + 冗余修复 + 在系统监控**构成层级化缺陷捕获体系
- **关键矛盾**: HBM 是可靠性瓶颈——单点互连失效在 2.5D/3D AI 系统里放大成整卡故障；数据中心现场失效成本极高，倒逼 DFT 前移、对老化互连做「预告式」修复
- **视觉关联**: HBM 容量/带宽直接决定 GPU 能否装下更大的多模态与视频模型（Rubin Ultra 因 HBM 供应紧张被传降配，8/11 已报）；3D 堆叠良率就是下一代视觉算力的「卡脖子」环节
- **判断**: 「HBM 当试验田」意味着 3D IC 测试方法论会快速外溢到 CXL 内存、chiplet GPU、传感器堆叠（如索尼双层晶体管像素）等场景

## 📦 开源硬件与工具

### 7. [Proton AI Core Vision+：带 IMU/安全芯片/麦克风/microSD 的 ESP32-S3 相机开发板（新开源硬件）](https://github.com/Protonverse-Labs/proton-ai-core-vision-plus)
- **功能**: ESP32-S3 相机开发板，板载 IMU、secure element、I/O 扩展、麦克风与 microSD——一颗板子覆盖「视觉 + 姿态 + 安全身份 + 存储」的最小边缘感知套件
- **上手**: 2026-08-10 新建仓库，C++ 固件 + Arduino/ESP-IDF 生态；适合做低成本安防相机、穿戴视觉、机器人感知原型
- **对比**: 对比市面 ESP32-CAM 的「裸摄像头」定位，Vision+ 把 IMU 与安全元件集成进来，更接近「端侧感知 + 安全启动」的完整形态；刚起步（★1），当 open-hardware 观察对象

### 8. [Dalaran：Rerun 硬分叉的机器人视觉数据基建——ROS 2 原生、直接读 .rrd 录包，5 天 686★](https://github.com/Flaminis/Dalaran)
- **功能**: Apache-2.0、Rust 写的 robotics-first 多模态时间序列可视化与数据基础设施；**ROS 2 原生**，兼容读取现有 Rerun 录包（.rrd），覆盖 lidar/pointcloud/视觉/IMU 时间序列
- **上手**: pip 安装 Python 绑定，与 ROS 2 bag 工作流无缝衔接；对做 SLAM/感知/实车调试的团队几乎是 Rerun 的直接替代品
- **判断**: 2026-08-07 创建即 686★——社区对「机器人专属可视化」需求明确；分叉 Rerun 意味着它继承了成熟的渲染栈，风险点在长期维护与生态迁移

### 9. [HuggingFace 趋势快照：Depth Anything V3 系列 + RMBG-2.0 ONNX 霸榜，边缘部署友好度上升](https://huggingface.co/models?pipeline_tag=depth-estimation&sort=trending)
- **深度估计**: depth-anything 官方 DA3 家族（DA3NESTED-GIANT-LARGE-1.1、DA3-SMALL）继续霸榜；**DA3-SMALL** 下载 4 万+，是可在 Jetson/手机 NPU 上跑的小模型——单目深度「软件化」趋势延续（8/7 已报）
- **分割/抠图**: briaai/RMBG-2.0（下载 61 万+）与 ZhengPeng7/BiRefNet 领跑，均提供 **ONNX 导出**——可直接部署到 RKNN/OpenVINO/TensorRT 边缘栈做实时抠图/文档分割
- **硬件关联**: 这些模型本身不是芯片，但「ONNX + 小尺寸」意味着边缘视觉硬件（瑞芯微/地平线/NVIDIA 边缘）的模型供给在变厚；建议关注带 onnx/tflite 标签的量化版

## 📰 产业动态

### 10. [AI 工厂成为「可投资资产类别」：NVIDIA 携六大金融机构撬动 $500B+ 第三方资本](https://blogs.nvidia.com/blog/nvidia-ai-factory-compute/) · [Tom's Hardware 报道](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-teams-up-with-financial-giants-to-create-usd500-billion-ai-infrastructure-funds-six-investment-firms-to-enable-access-to-long-term-funding-at-attractive-rates)
- **核心内容**: NVIDIA 8/12 官宣定位转变——AI 数据中心从「逐项目买芯片建机房」升级为 **DSX AI 工厂 = 可融资的生产性基础设施**；与六大投资机构合建平台，目标撬动 **$500B+ 第三方长期资本**；强调 CUDA 让工厂「越用越值钱」（A100 六年案例：每代软件迭代持续提升存量硬件 TCO）
- **影响**: 算力从「资本开支」变成「收租资产」，GPU 的金融化会进一步拉高对 NVIDIA 生态的锁定（与 8/9 亚美尼亚工厂、8/11 涨价潮是同一叙事）；对视觉硬件从业者：多模态/视频/具身负载是这些工厂的算力需求基本盘，融资到位 = 未来两年训练算力持续放量

### 11. [美国 AI 数据中心禁令突破 500 项：地方政治开始「否决」算力扩张](https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-bans-surge-past-500-nationwide-as-local-us-politicians-begin-blocking-new-developments-growing-public-outrage-and-bipartisan-pushback-threaten-big-tech-expansion-plans)
- **核心内容**: 全美地方层面 AI 数据中心禁令/限制累计 **突破 500 项**，两党议员与社区共同抵制新建设——电力、水资源、噪音与地价是主要争议点
- **影响**: 供给侧收紧与 8/11「RTX 50 系涨价 39%」互为镜像——需求暴涨但新机房落地受阻，算力价格与 GPU 稀缺可能长期化；对视觉硬件：边缘端（Jetson、端侧 NPU）作为「不进机房」的算力出口，性价比叙事反而加强
