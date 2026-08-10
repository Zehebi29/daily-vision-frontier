# ⚙️ 2026-08-10 视觉硬件日报

> 今日扫描了 SemiAnalysis · EETimes · NVIDIA Blog · Tom's Hardware · SemiEngineering · Sony Semiconductor · Image Sensors World · GitHub · HuggingFace · Reddit · ITHome · Google/DDG 补充搜索 等 13 个渠道，精选 10 条
> 注: 8/9 日报已覆盖 Sony 熊本地震余波、CXMT DDR5-8800、Firebird 亚美尼亚 AI 工厂、Intel 轨道数据中心；本期数据窗口 8/9–8/10，头条是 **Sony×TSMC 熊本 1 万亿日元图像传感器合资厂**（日经 8/10），并补录此前遗漏的 Prophesee / eyeo 融资与 CXMT×苹果谈判。
> ⚠️ Reddit API 仍被限流（403），改走 RSS 仅 computervision 成功；SemiAnalysis RSS 疑似停更（最新条目停在 2025-09）；GitHub trending 反爬，沿用 API 搜索。

---

## 🎥 传感器与采集

### [索尼与台积电拟在熊本投资 1 万亿日元：2029 量产下一代图像传感器，合资公司供货 iPhone、瞄准 Physical AI](https://www.ithome.com/0/987/730.htm)
- **什么**: 日经新闻 8/10 —— Sony Group 与 TSMC 计划最早 **2029 年**在熊本量产下一代图像传感器；由合资公司运营，**索尼持股约 60% / 台积电约 40%**，总投资约 **1 万亿日元**（约 ¥427 亿人民币 / $6.7B）
- **节奏**: 2026 年 5 月已达成研发+量产合作基本协议；预计近期敲定量产投资方案，**2026 财年（截至 2027/3）结束前成立合资公司**；正在与日本经产省谈政府补贴
- **地点**: 熊本县菊阳町（Koshi）——Sony Semiconductor Solutions 现有图像传感器工厂内新建大规模研发设施与产线；距 2024 熊本地震震中约 30km，未受重大损害（与 8/9 日报地震余波报道互文）
- **视觉关联**: ① 明确为苹果 iPhone 供高性能摄像头传感器；② 长期目标是把传感器性能推到让 AI「更精准识别物体」，进军 **Physical AI**（机器人/车辆感知）——这是传感器大厂第一次把「传感器→物理 AI」写进投资公告的级别
- **判断**: ① 投资额 ≈ 索尼半导体业务 4 年资本支出、接近 JASM 第一座熊本厂总投资（$8.6B）——这是索尼 CIS 史上罕见的联合重注，说明下一代 sensor 对先进逻辑/堆叠工艺的依赖已无法靠索尼自有产线满足；② 索尼不会向台积电开放核心专有制造技术（防技术外溢），合作边界值得观察；③ 索尼全球 CIS 份额 >50% 仍要拉 TSMC 建「传感器+逻辑」一体化产能，OmniVision（豪威）与三星的追赶压力是真实存在的

### [Prophesee 融资 €20M 并发布 Mantara：首个全集成事件相机无人机探测系统（补录）](https://www.prophesee.ai/2026/06/15/prophesee-launches-mantara-event-based-drone-detection/)
- **什么**: 事件相机（event camera）龙头 Prophesee 于 6/15（Eurosatory/Vivatech 巴黎展会期间）宣布 **€20M 融资**（法国基金 Critical Path Ventures 领投，现有股东跟投），并发布 **Mantara®**——首个原生事件视觉（native event-based）的集成无人机探测/跟踪系统；公司目前由法国股东绝对多数控股
- **技术要点**: 每个像素独立、微秒级响应「运动事件」而非逐帧图像——常规相机在低光、逆光、杂乱背景下会模糊/丢失的快而飘忽的目标（小型无人机），Mantara 可完整检测与表征；延迟优势是核心：**常规系统拍一帧的时间里，Mantara 已完成检测**
- **软件层**: 搭载新平台 **Hearth®**（内置 AI 处理），是 OpenEB / Metavision SDK 的继任者——对做事件相机研究的人，SDK 迁移路线值得提前跟进
- **判断**: 事件相机商业化正在从「卖传感器/SDK」转向「卖整机系统」（反无人机、安防），且 Prophesee 明显在走欧洲/法国国防供应链路线；对研究者：事件视觉的落地主场景已从学术 demo 明确转向低延迟目标探测

### [eyeo 完成 €40M A 轮：纳米光子分色（NCOS）宣称「3 倍感光度、打破分辨率极限」（补录）](https://eyeo-imaging.com/knowledge/news/eyeo-raises-e40-million-to-fix-the-flaw-that-has-kept-every-camera-70-blind/)
- **什么**: 荷兰 Eindhoven 的 eyeo 5/11 宣布 **€40M Series A**（累计 €55M），领投方 Innovation Industries，imec.xpand、Invest-NL Deep Tech Fund、HTGF 等跟投；主打 **Nanophotonic Color Splitting (NCOS®)** 技术平台
- **技术逻辑**: 传统 Bayer CFA 滤色片是「拒绝式」——每像素只让 R/G/B 之一通过，**丢弃约 70% 的光**；eyeo 用纳米光子结构把光按波长「分色」导向对应像素，声称感光度提升 3 倍、并可突破分辨率/像素尺寸极限，面向手机、工业、XR、智能城市
- **判断**: 这是「传感器前道光学」层面的真创新方向（同赛道还有分光棱镜/多层 sensor 方案），但**量产成熟度是最大未知数**——融资额（€40M）对晶圆级光学工艺开发并不算充裕，建议当长期技术观察项而非短期产品信号；若 NCOS 真能在手机端量产，低光成像与 HDR 的格局会被改写

> 📌 **传感器板块小结**: Sony/OmniVision 官方仍无新品发布（连续第四周「静默观察期」），但本周两条「结构级」消息分量更重——Sony×TSMC 合资建厂（产能/工艺结构）与 Prophesee/eyeo 融资（事件视觉与光学创新）；Image Sensors World 的 [Sony vs Samsung 200MP 对比视频](https://image-sensors-world.blogspot.com/2026/07/sony-and-samsung-200mp-sensors-compared.html)（HP3/HP5/HP9 vs LYTIA 901 vs 思特威 SCC80XS）也提示：高像素传感器已进入「ISP 调校比堆规格更重要」的阶段

## 🖥️ GPU 与算力

### [NVIDIA RTX Spark（N1X）现身 Geekbench：20 核 ARM 桌面芯片，全规格多核超越多数 x86 移动处理器](https://www.tomshardware.com/pc-components/cpus/two-variants-of-nvidias-rtx-spark-show-up-on-geekbench-revealing-a-cut-down-18-core-model-full-20-core-beats-most-x86-mobile-chips-across-multi-core-and-single-core-tests)
- **什么**: Tom's Hardware 8/9 —— RTX Spark（原 N1X，NVIDIA Windows-on-ARM 桌面平台）两个变体现身 Geekbench：**20 核全规格版 + 18 核阉割版**；工程样品 Cinebench 2026 多核 5,771 / 单核 540，功耗墙 **80W PL1 / 95W PL2**（[notebookcheck 汇总](https://www.notebookcheck.net/Nvidia-RTX-Spark-Arm-chip-surfaces-in-first-Cinebench-2026-leak.1346034.0.html)）
- **对比**: 与 AMD Ryzen AI Max+ 395、Intel Core Ultra X9 388H 互有胜负，多核/单核均快于多数 x86 移动芯片；弱于高通 Snapdragon X2 Elite 与 Apple M5 Max（videocardz 标题即「outpaces Ryzen AI Max+ 395 and Panther Lake」）
- **定位**: 官方已确认将用于笔记本、mini PC 与**紧凑型 AI 工作站**（Surface Laptop Ultra 等搭载）；NVIDIA 下场做「ARM CPU + 自家 GPU」整机平台，对标高通 X Elite 与 Apple Silicon
- **视觉关联**: 本地视觉/生成式 AI（ComfyUI、本地 VLM、边缘工作站）是这类紧凑 AI 平台的核心负载——若 RTX Spark 以「统一内存 + GeForce 图形」形态落地，是「能跑模型的小盒子」赛道的强变量
- **判断**: 工程样品数据（1.01GHz 频率读数是预发布固件错误），最终性能可能还有提升空间；重点不是跑分本身，而是 **NVIDIA 首次在消费级 CPU 市场与 x86/高通/苹果正面对撞**，视觉硬件生态（尤其是端侧 AI 盒子）多一个平台选项

## 🔩 芯片与半导体

### [CXMT 拒绝苹果压价：坚持 DRAM 报价不低于三星/SK 海力士，「第四大 DRAM 巨头」定价权逆转（补录）](https://www.ithome.com/0/986/176.htm)
- **什么**: ITHome 8/5（源：韩媒 Digital Daily）——苹果为降本考虑引入长鑫存储（CXMT）作为移动 DRAM（LPDDR5X）供应商，**降价谈判被 CXMT 拒绝**；CXMT 坚持价格 ≥ 三星/SK 海力士报价
- **底气来源**: 华为、小米等中国厂商通过长期合同锁定 CXMT DRAM 产能（国产自给优先）；字节跳动另有 5 年 $70 亿+ 采购协议；Counterpoint 数据显示 2026Q2 三星 DRAM 营收份额 39%、SK 海力士 26%、美光 25%，而 CXMT 与南亚科技营收同比分别 **+716% / +690%**
- **判断**: 与 8/9 日报「CXMT 在 AM5 达成 DDR5-8800」互证——国产 DRAM 已经走完「价格屠夫 → 生态接受 → 定价方」三部曲，连苹果都压不动价；对视觉硬件从业者：内存超级周期（8/8 日报：RAM 价格回到 2007 年水平）里，「国产产能」这个原本的降价变量正在失效，2027 年前采购策略应默认高成本

### [美光按原价赔偿退货的 Crucial 内存被曝「只有市价 37%」：存储超级周期把渠道关系也扭曲了](https://www.tomshardware.com/pc-components/ram/micron-reportedly-offers-pennies-on-the-dollar-for-crucial-ram-return-only-offers-to-reimburse-original-msrp-despite-it-being-only-37-percent-of-market-value-chipmaker-later-reverses-course-with-a-better-solution)
- **什么**: Tom's Hardware 8/9 —— 用户退回 Crucial 内存条后，美光仅按原 MSRP 赔偿（约等于当时市价的 37%），引发争议后改口提供「更好方案」
- **背景**: 与 8/9 日报「苹果 iPhone 17 将涨价」同一逻辑链——市场价远高于原厂标价的「价格倒挂」，是 2026 存储超级周期最直观的畸变；连退货估值体系都崩了
- **判断**: 这类「零售端小新闻」其实是供应链定价失灵的信号：原厂（三星/SK 海力士/美光）控产、渠道囤货、市价与 MSRP 脱钩；对视觉硬件 BOM（边缘设备 LPDDR、服务器 DDR5）意味着现货成本风险持续，锁长约仍是唯一对冲

## 📦 开源硬件与工具

### [GitHub 周扫描：事件相机/ISP 新增仓库仍是低 star 消化期；HF 侧出现无人机航拍 YOLO26 边缘分割模型](https://github.com/search?q=event+camera+created%3A%3E2026-07-21&s=stars&type=repositories)
- **GitHub**: 本周按「event camera / image signal processor / embedded vision / lidar perception」四组关键词新增的仓库仍以低 star 习作为主（多数 <5★），无重量级新项目——与 8/9 日报判断一致，开源视觉硬件处于消化期；上期已覆盖的 eraft_flow（事件相机稠密光流 + TensorRT 后端）仍是近期最有接线参考价值的项目
- **HuggingFace**: depth-estimation trending 继续被 [Depth Anything 系列](https://huggingface.co/depth-anything/DA3METRIC-LARGE) 包场（V2/V3 室内外档全在列）；image-segmentation 出现一个与边缘部署沾边的新面孔——[dronefreak/vdd-yolo26n-sem](https://huggingface.co/dronefreak/vdd-yolo26n-sem)：YOLO26 nano 语义分割，无人机航拍（VisDrone 类）数据集，nano 规格适合 Jetson/树莓派类边缘推理，可作无人机感知小模型基线
- **判断**: 「单目深度软件化继续挤压低端 ToF/双目硬件」的叙事进入第四周；本周开源侧没有硬件突破，但 YOLO26 系列在航拍/边缘场景的模型层持续下沉，值得无人机视觉开发者关注

## 📰 产业动态

### [FCC 拟「追溯性」禁售带 LiDAR/热成像的外国无人机：七类能力被划为 military-grade，DJI 号召用户反击](https://www.tomshardware.com/tech-industry/drones/fcc-moves-to-ban-lidar-equipped-foreign-drones-from-us-classifies-the-technology-as-military-grade-in-a-proposal-that-could-also-hit-thermal-models-and-the-swarms-used-drone-light-shows)
- **核心内容**: FCC 7/21 发布 Public Notice DA 26-758（PS Docket 26-189），拟禁止继续进口/销售 Covered List 上外国制造的无人机及关键部件，覆盖七类被定义为「military-grade」的能力：**起飞重量 ≥55 磅 / 农业喷洒平台 / 搭载热成像传感器 / 搭载 LiDAR / 停机坪（docking station）/ 专为整合国防物项设计 / 蜂群系统（定义宽到包含无人机灯光秀）**（[DroneXL 细节](https://dronexl.co/2026/08/08/dji-rallies-pilots-fcc-drone-ban/)）
- **关键升级**: 提案是**追溯性（retroactive）**的——已获 FCC 授权的产品也可能被禁售，且配件/替换部件同步断供；DJI 8/7 首次公开号召美国用户向 FCC 提交意见（受影响机型如 Matrice 400、Dock 2），意见窗口 **9/2 截止**
- **视觉关联**: 这是 2026 下半年无人机感知传感器（LiDAR 避障、热成像、视觉导航）最大的政策变量——「传感器能力」被直接当作出口管制/国家安全分级标准；对视觉硬件从业者：无人机视觉模组的中美供应链风险进一步上升，DJI 生态内的 LiDAR/热成像供应商需要提前做市场替代预案
- **判断**: 抛开立场，这是监管第一次把「机器感知能力」本身列为禁售依据（而非品牌/产地），对事件相机、LiDAR、热成像等感知硬件在消费/行业无人机的应用有长期示范效应

### [ams OSRAM 开发 micro-photodiode arrays：光互连接收端传感器化，光学半导体路线图延伸到 AI 数据中心](https://semiengineering.com/chip-industry-week-in-review-150/)
- **核心内容**: SemiEngineering 8/7 周报 —— ams OSRAM 已开始为 AI 数据中心**高带宽光互连的接收端**开发微光电二极管阵列（micro-photodiode arrays），在其 microLED 发射端路线图之外开辟接收端业务
- **影响**: 光互连（optical interconnect）在 AI 集群中的带宽瓶颈正把「光接收」变成传感器机会——与图像传感器同源的 PN 结/SPAD 工艺，从「拍图像」延伸到「收光信号」；对视觉半导体从业者：光电探测器阵列的工艺know-how（灵敏度、带宽、串扰）与事件相机/ToF 接收端高度可迁移，是传感器公司切入 AI 基础设施的隐秘入口

### [Terafab 占地投影更新：比 Pentagon + Apple Park + Mall of America + Giga Texas 总和还大（跟进）](https://www.tomshardware.com/tech-industry/semiconductors/musks-terafab-projected-to-be-larger-than-the-pentagon-apple-park-mall-of-america-and-giga-texas-combined-all-in-one-chip-manufacturing-facility-visualized-to-show-the-projects-massive-footprint)
- **核心内容**: Tom's Hardware 8/9 —— 根据可视化投影，Tesla/Musk 的 Terafab 一体化芯片制造设施占地将超过五角大楼、Apple Park、美国商城与 Giga Texas 的总和（跟进 8/9 日报的 Terafab 渲染视频，新增占地数据）
- **判断**: 占地投影仍是概念/营销层面，但「Terafab 尺寸 + Optimus 2027 夏量产 + 年产能 1,000 万台目标」组合起来，是机器人感知硬件（多目相机 + 车端推理 + 训练算力）长期需求的基本盘信号；对视觉从业者当长期需求曲线看，不必逐条跟进渲染视频

---

*数据窗口 2026-08-09 ~ 2026-08-10 · 来源: SemiAnalysis（feed 疑似停更）/ EETimes / NVIDIA Blog / Tom's Hardware / SemiEngineering / Sony Semiconductor / Image Sensors World / GitHub API / HuggingFace API / Reddit RSS（embedded/ML 被限流）/ ITHome / Google News 补充搜索 · Reddit API 持续 403；本期头条 Sony×TSMC 熊本 JV 为 8/10 日经首发；Prophesee/eyeo/CXMT×苹果为补录（6/15、5/11、8/5），此前日报未覆盖*
