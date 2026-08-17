# ⚙️ 2026-08-17 视觉硬件日报

> 今日扫描了 SemiAnalysis（feed 停更）· EETimes · NVIDIA Blog · SemiEngineering · Tom's Hardware · Sony Semiconductor · OmniVision · Prophesee · GitHub API · HuggingFace API · Reddit · Google News(国产芯片) 等 12 个渠道，精选 11 条
> ⚠️ Reddit API 连续第三日 403 限流（已换 old.reddit 与 api.reddit 均被拒）；SemiAnalysis RSS 停在 2025-09（弃用）；**传感器新品进入第三周静默期**（Sony/OmniVision/ST/Prophesee 均无新品），传感器板块以产业观察为主
> 注: 不重复 8/12（800VDC/Intel $19.7B/NVIDIA $500B 基金）、8/13（Sony×TSMC CIS 合资/LYTIA 610/Expedera NPU）、8/14（智能手机芯片涨价/征程7 星空/CXMT）、8/16（AMD Helios/1MW 机架/Jetson 内存 Agent/SPIL 扩产/无人机关税）已覆盖内容；本期头条是 **Google 联手 AMD 造 TPU v10** 与 **TIER IV 开源 L4 AI 加速器**

---

## 🎥 传感器与采集

### 1. [传感器板块观察：CIS/事件相机新品静默期进入第三周，「新品节奏」让位于「制程军备竞赛」](https://www.sony-semicon.com/en/news/index.html) · [Prophesee 新闻页](https://www.prophesee.ai/company/news/)
- **什么**: 本周 Sony Semiconductor、OmniVision、ST、Prophesee 均无新传感器产品发布——自 8/8 起连续第三周无重量级新品；Prophesee 最新动态仍停在 3 月（与 IDS 深化工业事件相机合作）
- **亮点**: 供应链侧却动作频频：Sony×TSMC 的 CIS 合资终局条款已于 8/11 官方确认（Sony 绝对控股、出资 ¥465B、TSMC ¥282B、熊本新厂 2029 量产——8/13 已详报，不重复）；OmniVision 侧 TheiaCel 技术在 NVIDIA 平台上的上车适配是既有动向
- **视觉关联**: 手机影像、智驾、安防三大 CIS 主战场均处于「产品换代前夜」——旗舰传感器（1/1.3 型以上、多摄、TheiaCel 类 HDR）的下一波发布预计随 2027 旗舰机型节奏
- **判断**: 这是行业周期的正常消化期，但注意结构性信号——**CIS 竞争已从「像素/帧率参数战」转向「谁能拿到先进制程与封装产能」**（Sony 拉 TSMC 合资正是为此）；对视觉硬件从业者：传感器选型窗口期内，现有型号（IMX 系、OV50 系）的供货与价格反而更可预期

## 🖥️ GPU 与算力

### 2. [Google 联手 AMD 造第十代 TPU：v10 首次引入 on-package CPU 核，为 RL/agentic 推理重构架构](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reportedly-taps-amd-to-design-next-generation-tpu-hybrid-ai-asic-could-integrate-on-package-cpu-cores-for-reinforcement-learning)
- **什么**: Tom's Hardware（8/16）援引 SemiAnalysis 客户纪要——**Google 正与 AMD 合作开发 TPU v10 系列**，这是 AMD 首次真正参与定制 AI ASIC 项目；SemiAnalysis 判断 Google 拉 AMD 不是为了再造一颗常规 TPU（那是 Broadcom 的活），而是为了 **AMD 在先进封装（SoIC）与 CPU IP 上的积累**
- **亮点**: 核心变化是架构——Google 与客户正在推动 **TPU 集成 on-package CPU 核**，面向强化学习（RL）与 agentic 推理等 CPU-heavy 负载；对比数据：TPU 8i（推理/RL 定位）已做到 **1 颗 Axion CPU : 2 颗 TPU**，而 7 代 TPU 是 **1 颗 Xeon : 4 颗 TPU**——CPU 密度翻倍的曲线正是 v10 的铺垫
- **视觉关联**: 多模态 VLM 的 RL 微调、视觉语言动作模型（VLA）、robot policy learning 恰恰是「加速器 + CPU 密集」的典型负载——「推理 = 纯 GPU 活」的假设正在被 reasoning 模型打破；这与 8/16 的 AMD Helios（CPU 先行路线）是同一趋势的两面
- **判断**: 真假待官方确认，但即便只是方向性信号也足够重要——**AI 加速器架构正从「纯矩阵引擎」转向「加速器 + 大核 CPU 混合」**；对视觉推理集群选型，未来两年「CPU:加速器 配比」会成为新的采购参数

### 3. [Microsoft Maia 300 将于 9 月发布：第二代自研推理加速器，TSMC 产能成变量](https://semiengineering.com/chip-industry-week-in-review-151/)
- **什么**: SemiEngineering 周报（8/14）援引 The Information/Reuters——**微软预计 9 月发布新一代 Maia 300 加速器**，但 TSMC 产能可能是放量瓶颈
- **性能**: 规格未披露；第一代 Maia 100（2023 年，台积电 5nm，Azure 推理用）已部署于 OpenAI 工作负载，Maia 300 是 3 年一迭代的继任者，重点仍是推理与成本优化
- **视觉关联**: Azure 上所有视觉/多模态 API 的推理成本与供给，直接受 Maia 系列放量节奏影响；与 8/16 报道的 Google 自研 + AMD 合作、Anthropic 自研 ASIC（8/8）呼应——**超大规模厂商的「去 NVIDIA 化」在 2026H2 全面进入产品落地期**
- **获取方式**: 仅 Azure 云实例，不零售

### 4. [NVIDIA Jetson 全家桶官方推广：Orin Nano Super 67 TOPS + Device Skills 让 Agent 帮你写边缘视觉代码](https://blogs.nvidia.com/blog/build-ai-with-nvidia-jetson/)
- **什么**: NVIDIA Blog（8/12-13）为 Jetson 平台站台——从 **Jetson Orin Nano Super（67 TOPS，~$249 开发套件）** 到 AGX Thor 的完整产品线，主打「agentic-ready AI 平台」；新推 **Jetson Device Skills 与 Jetson BSP Skills**，用 coding agent 帮助开发者创建、优化、部署边缘 AI
- **亮点**: Device Skills 把 8/13 EETimes 报道的「用 Agent 管理 Jetson」从方法论变成官方产品能力——Agent 直接调用板卡 BSP/算子库，降低入门门槛
- **视觉关联**: 机器人/安防/零售边缘视觉的标准入口；67 TOPS 的 Nano Super 已能跑 YOLO 系检测 + 跟踪 + 轻量 VLM 的组合负载
- **对比**: 与 8/16 的 Hailo 生态（26-40 TOPS）同台竞技——NVIDIA 的护城河正在从「TOPS 数字」转向「Agent + 软件栈」的开发者体验

## 🔩 芯片与半导体

### 5. [TIER IV 将开发开源 L4 自动驾驶 AI 加速器：日本 JST 项目押注「开放芯片」路线](https://semiengineering.com/chip-industry-week-in-review-151/)
- **什么**: SemiEngineering 周报（8/14）——日本自动驾驶软件公司 **TIER IV** 将在日本 JST（科学技术振兴机构）项目下，**开发开源 AI 加速器用于 L4 自动驾驶**，范围包括芯片架构、编译器与工具链，目标「更安全、更低功耗的边缘 AI」
- **亮点**: 这是「开源硬件」路线在自动驾驶计算芯片上的罕见国家级背书——对标 RISC-V 在 CPU 领域的路径，把 L4 感知推理链路的芯片层也开放出来；TIER IV 是 Autoware 开源自动驾驶软件栈的旗手，软硬件同源开放是其基因
- **视觉关联**: L4 感知（多目相机 + LiDAR + 毫米波融合）的推理芯片是当前 NVIDIA Drive Thor / 地平线征程 / Mobileye EyeQ 的封闭战场；TIER IV 若成功，将给「不想被单一芯片生态锁死」的自动驾驶团队提供第四选项
- **判断**: 早期项目，架构与算力均未公开——**看点不是立刻可用，而是「自动驾驶芯片的开放性」第一次有了国家项目级试验**；建议跟踪其 2027 年的架构发布

### 6. [地平线余凯放话：J7 会是「全球最强悍」自动驾驶芯片——国产智驾芯片进入正面叫板阶段](https://news.google.com/rss/articles/CBMipwFBVV95cUxPWEItS0twQTRFa0ZQekpsbGJOUWI3ejVzZUJSRHVPWU5oNU5yb1JfMmVhbUwyWnRRWGt1WXBYcUdtM25BMk5rZTJpaWRRTXIwLTdZQ2IzM01JbGtQbUs3VzJLc1VVekc0bGV4TmdaeFRaeE1mMUV)
- **什么**: 新浪财经（8/16）——地平线 CEO 余凯称 **征程 7（J7）将是全球最强悍的自动驾驶芯片**，对标英伟达与特斯拉的智驾芯片（报道亦提及「AI5 芯片」与大众合作背景）
- **亮点**: 延续 8/14 报道的征程7「星空」目标算力 + 首个纯国产舱驾一体定点——J7 已进入量产筹备期，这次 CEO 级公开对标是把「技术路线」升级为「市场竞争宣言」
- **对比**: 参考系是 NVIDIA Drive Thor（~2000 TOPS 级）与 Tesla HW5/AI5——J7 的实际算力与量产表现待数据验证
- **判断**: 一半营销话术、一半真实信号——**国产智驾芯片（地平线/黑芝麻/华为昇腾）已经从「追赶者叙事」切换到「正面叫板」**；判断真伪看两点：量产定点数量与实测 TOPS/W，2026H2 的车型 SOP 是检验窗口

### 7. [KAIST 可编程动态 memtransistor：硬件级动态行为控制，预测误差降低 40 倍](https://semiengineering.com/chip-industry-week-in-review-151/)
- **什么**: 周报（8/14）——KAIST 研发出「**可编程动态 memtransistor**」，双功能栅堆叠实现无需恒定偏置/输入预处理的硬件级动态行为控制，研究团队称预测误差较常规器件降低最多 40 倍
- **亮点**: 动态可编程 + 存算一体特性，是神经形态/类脑硬件（SNN、事件驱动计算）的器件级候选——与本周「事件相机生态缺的是工具链」（8/16）形成对照：器件层在进步，系统层在补课
- **视觉关联**: 事件相机信号处理、低功耗 always-on 视觉的目标硬件形态；实验室阶段，距离工程化（工艺整合、良率）尚远
- **判断**: 值得记入「边缘低功耗视觉的器件候补名单」，但 3-5 年内不会影响任何产品选型

### 8. [铜互连在 AI Scaling 中的地位开始松动：SE 特稿 + OCP 19 公司硅光子联盟](https://semiengineering.com/coppers-grip-on-ai-scaling-is-starting-to-slip/)
- **什么**: SemiEngineering 特稿（8/13）——**铜互连对 AI 扩展的主导地位开始松动**：数据中心网络架构再度转向，光互连在 AI 集群连接中占比上升；同期 OCP 框架下 **19 家公司联盟**公布「硅光子就绪数据中心基础设施」标准化计划，CPO（共封装光学）正从实验室走向产线 ATE（Sivers/SemiNex 启动 $3.4M InP 光源项目）
- **亮点**: 光互连的核心瓶颈从「能不能做」转向「成本与标准化」——与 8/12 FCC 拟禁中国光模块（占全球 56% 份额）叠加，2026H2 的光模块供应链处于「技术升级 + 地缘重排」双变量状态
- **视觉关联**: 多模态/视频训练集群的 scale-up/scale-out 互连决定集群成本与交付周期；对视觉算力采购者，**光模块交期与价格的不确定性是 2026H2 的预算变量**

## 📦 开源硬件与工具

### 9. [GitHub 边缘视觉扫描：Radxa 两轮车感知、ESP32-CAM Linux 视觉终端、Rust 视觉管线三线活跃](https://github.com/DuyLeTran/EdgeMotoPerception) · [esp32-t153-vision-terminal](https://github.com/fish-eat-no/esp32-t153-vision-terminal) · [SightLoom](https://github.com/sergii-ziborov/SightLoom)
- **功能**: ① **EdgeMotoPerception**——在 **Radxa Q6A**（瑞芯微系 SoC）上用单目 RGB + 2D LiDAR 融合做两轮车边缘感知，含 metric 跟踪与不确定性建模；② **esp32-t153-vision-terminal**——ESP32-CAM + TLT153（Linux 微 SoC）组合的嵌入式视觉终端，HTTP/MJPEG 推流 + OpenCV + LVGL；③ **SightLoom**——Rust 原生的边缘/嵌入式视觉管线库
- **上手**: 前两者都是「低成本开发板 + 相机」组合，可直接复现；SightLoom 面向 Rust 生态的嵌入式视觉开发者
- **视觉关联**: 三个项目共同指向一个信号——**「小算力 SoC 跑完整感知栈」在海外开发者群体持续活跃**，Radxa/瑞芯微生态热度上升（对比 8/16 的 Jetson/Hailo 主线，这是「非 NVIDIA」路线的长尾供给）
- **判断**: 单看都是小项目，但「国产边缘 SoC + 开源感知栈」的组合正在形成惯性——对国产芯片出海是低成本但持续的生态积累

## 📰 产业动态

### 10. [垂直整合成为常态：软件迭代快于硬件，co-design 成了硬件的「追赶游戏」](https://semiengineering.com/vertical-integration-becoming-pervasive/)
- **核心内容**: SemiEngineering 特稿（8/13）——**垂直整合（设计 + 制造 + 系统一体化）在半导体业成为主流**；但软件迭代周期远快于硬件，硬件团队被迫用新工具追赶：Google 加入 OpenROAD 开源硅计划、Samsung 用 Claude Code 把定制 SoC 功能验证周期显著缩短、Movellus 遥测 IP 进入三星先进代工生态
- **影响**: 对视觉硬件意味着——**从 Sony CIS 到地平线 NPU，所有芯片公司都必须「软硬一体」交付**（传感器要配 ISP 算法栈，NPU 要配编译器+模型库）；纯卖硬件的商业模式窗口正在关闭；同时「AI 辅助 EDA/验证」让小型视觉芯片团队也有机会追赶

### 11. [产业快报：中国成熟制程产能 2030 年将占全球近半（Rhodium）+ Intel 完成 $20B 增发募资](https://semiengineering.com/chip-industry-week-in-review-151/)
- **核心内容**: ① Rhodium Group 预测——**中国成熟制程（legacy node）产能到 2030 年将接近全球产量一半**，且国产设备商同步扩张，尽管先进 AI 芯片获取仍受限；② **Intel 完成 $20B 增发**（8/14，跟进 8/12 报道的 $19.7B 认购潮），CEO Lip-Bu Tan 称资金将投向先进节点晶圆制造、先进封装与 CPU 产能
- **影响**: 成熟制程是中国 CIS（思特威/格科微/韦尔豪威）与边缘视觉 SoC（瑞芯微/全志）的产能底座——「2030 占全球一半」意味着**国产视觉芯片的成本与供货弹性将持续优于先进制程路线**；Intel 的钱则继续支撑其 18A/14A 代工叙事，对 GPU/加速卡代工格局（AMD/微软/Google 都在台积电排队）构成远期变量

---

*数据窗口 2026-08-16 ~ 2026-08-17 · 来源: SemiAnalysis（feed 停更，弃用）/ EETimes / NVIDIA Blog / SemiEngineering / Tom's Hardware / Sony Semiconductor（无新品）/ OmniVision（无新品）/ Prophesee（无新品）/ GitHub API（event camera/embedded vision/ISP/lidar 等查询）/ HuggingFace API（DA3NESTED-1.1 深度模型持续霸榜，无硬件级新动态）/ Reddit（403 限流）/ Google News（国产芯片：地平线 J7 等）*
