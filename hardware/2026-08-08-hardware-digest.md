# ⚙️ 2026-08-08 视觉硬件日报

> 今日扫描了 SemiAnalysis · EETimes · NVIDIA Blog · Tom's Hardware · SemiEngineering · Sony Semiconductor · OmniVision · GitHub · HuggingFace · AMD Newsroom · Reddit 等 11 个渠道，精选 12 条
> 注: 8/6–8/7 日报已覆盖 Samsung zHBM/zNAND、GF 硅光、DRAM 短缺、AMD×Taalas、Wistron、Cosmos 3、弗吉尼亚电税等；本期聚焦 8/4–8/8 新动态（FMS 2026 存储军备竞赛、Terafab、Anthropic 自研芯片、NXP×Ambarella），不重复。

---

## 🎥 传感器与采集

### [Sony/OmniVision 本周无新品 + HF 深度模型持续霸榜：传感器板块进入「静默观察期」](https://www.sony-semicon.com/en/news/)
- **什么**: 本周扫描结论 —— Sony Semiconductor 与 OmniVision 新闻页均无可见新品发布（OV 新闻页本次直接 404，Sony 页面为 JS 渲染导航）；HuggingFace depth-estimation trending 榜依旧被 [Depth Anything 系列](https://huggingface.co/depth-anything/DA3METRIC-LARGE) 包场（V2/V3 Metric 室内外档全部在列），image-segmentation 榜则被 YOLO26 量化微调模型与 [RMBG-1.4](https://huggingface.co/briaai/RMBG-1.4)、[BiRefNet](https://huggingface.co/ZhengPeng7/BiRefNet) 等背景去除模型占据
- **亮点**: 连续第二周「传感器无新品」+「深度感知模型精度继续爬升」并存 —— 与 8/7 日报判断互证：单目深度模型的爬升正在结构性挤压低端 ToF / 双目 / 结构光模组的生存空间（手机、扫地机、AMR）
- **视觉关联**: 对传感器厂商而言这是「被软件侵蚀」的窗口期；对系统厂商则是 BOM 优化的机会窗口 —— 但高动态范围、低光、事件相机等硬件特性仍是模型替代不了的护城河
- **判断**: 本周传感器硬件侧确实无新闻，如实记录，不硬凑

## 🖥️ GPU 与算力

### [Anthropic 组建自研团队 co-design 推理 ASIC，三星被传为代工伙伴 —— 大模型公司「去 NVIDIA 化」再下一城](https://www.tomshardware.com/tech-industry/anthropic-to-build-its-own-co-designed-custom-ai-accelerator-for-inferencing-workloads-samsung-reported-to-be-partnering-with-the-claude-ai-maker-for-manufacturing)
- **什么**: Tom's Hardware 8/7 引 Business Insider —— Anthropic 官宣组建 in-house 芯片团队，与某合作伙伴 co-design 专用 ASIC 用于 AI 推理负载；招聘信息要求候选者「按进度把芯片设计落地」，节奏激进；三星被报道为潜在制造伙伴
- **性能**: 具体架构未披露；推理专用 ASIC 的逻辑是绕过 NVIDIA GPU 的推理定价与供给约束，配合模型侧优化（量化、投机解码）摊薄单位 token 成本
- **视觉关联**: Claude 系多模态（视觉理解、截图/文档解析）是 Anthropic API 的主力负载之一 —— 自研推理芯片若覆盖多模态 decode，会直接影响视觉推理的云成本曲线；与 AMD×Taalas（8/6）、Google TPU、AWS Trainium 同一趋势
- **对比**: 至此 OpenAI/Anthropic/Google/Meta/Amazon 五大模型厂全部押注自研或定制推理硅；三星若拿下代工 = 在 HBM4 之外再获 AI 推理芯片产能话语权（与本期 SK hynix $38B 扩产、CXMT 扩产形成存储+代工双线竞争格局）

### [NVIDIA Alpamayo 2 Super 开放商用：机器人出租车推理模型 + 车端硬件部署的「cloud-to-car」闭环](https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available/)
- **什么**: NVIDIA 8/4 宣布 Alpamayo 2 Super（基于 Cosmos 3 Super Reasoner + RL 后训练）开放商用，采用 Linux Foundation OpenMDW-1.1 许可（允许微调、衍生、商用分发）；整个 Alpamayo 家族（1/1.5/2 Super）全部转商用
- **性能**: LingoQA（自动驾驶推理基准）第一 —— Lingo-Judge 指标下领先 Qwen2.5-VL 72B 达 17.0 分、Gemini 2.5 Pro 15.1 分、GPT-4o 23.2 分；约为 10B 参数 Alpamayo 1.5 的 3 倍规模；支持 360° 环视相机融合推理，输出轨迹 + 因果链（chain-of-causation）多任务
- **视觉关联**: 官方定位「cloud-to-car」工作流 —— 云端跑前沿推理生成数据/蒸馏教师，车端跑蒸馏后的高效模型实时推理（即 NVIDIA Drive Thor/Orin 车端硬件）；对自动驾驶公司意味着：开放权重可自训自部署，减少对云端 API 的依赖，长尾场景合成数据 → 间接影响传感器采集预算（与 8/7 Cosmos 3 同主题，本期是车端落地版）
- **对比**: 7 月已有 200+ 家公司签署开放权重公开信，Alpamayo 商用化是 NVIDIA 在「车端 open model」上对 Tesla FSD 闭源路线的正面回应

## 🔩 芯片与半导体

### [Sandisk × SK hynix 发布 HBF 规范：单封装 512GB、最高 3TB/s 带宽的「NAND × HBM 混合体」，经 OCP 开放](https://www.tomshardware.com/pc-components/ssds/sandisk-and-sk-hynix-unveil-hbf-spec-up-to-16-hi-nand-stacks-3-tb-s-bandwidth-ucie)
- **什么**: 两家存储厂 8/4 通过 Open Compute Project（OCP）正式发布 High Bandwidth Flash（HBF）规范 —— 用 3D NAND 的非易失性 + HBM 式带宽，为 AI 推理提供新的内存层级
- **性能**: 单封装容量最高 512GB（8-Hi/16-Hi NAND 堆叠，非标准 3D NAND，而是带高速接口的 HBF core die）；带宽分 0.4 / 1.x / 3.0 TB/s 三档 —— 最高档超过单个 HBM4 堆栈的 2TB/s，但延迟仍高于 HBM；接口走 UCIe（SK hynix 口径）或 xPU-HBF（Sandisk 口径，即 UCIe 的实现变体）；单包 400GB/s 需 64 通道 × 64 GT/s UCIe，base die 复杂度不低
- **视觉关联**: 目标场景是「内存池需要比 HBM 大得多、但不需要 HBM 延迟」的推理负载 —— 多模态大模型（视频理解、长上下文）的 KV cache 与权重驻留正是这类负载；HBM4 单栈上限 64GB，HBF 单包 512GB，一个 8 包方案就是 4TB 级推理内存池
- **判断**: 数字（3TB/s vs HBM4 2TB/s）有营销成分（延迟差距未公布），且目前只有 Google、Tenstorrent 表态加入联盟，AMD/Broadcom 等态度不明 —— 2027 年前难落地，但「把闪存当内存」的层级化方向明确，是 zHBM（8/6 报道）之外的存储-计算融合第二条路线

### [SpaceX × Tesla Terafab 细节公布：100M sq ft 垂直整合晶圆厂，一期 $16.8B、用 Intel 14A，专产 Optimus/Cybercab 推理芯片](https://www.tomshardware.com/tech-industry/semiconductors/terafab-starts-to-take-shape-100-million-square-feet-of-manufacturing-space-and-usd16-8b-initial-capital-investment)
- **什么**: SpaceX 与 Tesla 8/6 正式公布德州 Grimes County Terafab 一期细节 —— 预计采用 **Intel 14A 工艺**，一期投资 $16.8B，规划总面积超 1 亿平方英尺（约 930 万 m²，是三星平泽园区 3 倍以上），至少 3,000 员工（60–80% 当地招聘）
- **亮点**: 定位**垂直整合**园区 —— 逻辑、存储、封装、测试同址（传统上分属不同 fab/工艺/设施），目标缩短生产周期与 time-to-yield；产品为 Tesla Optimus 人形机器人 + Cybercab 自动驾驶专用 AI 推理处理器，以及 SpaceX 太空数据中心用「高功率」处理器；公司称 SpaceX/Tesla/xAI 合计算力需求将超 **1TW/年**（远超当前全球供给）
- **视觉关联**: Optimus 与 Cybercab 是视觉感知最重的物理 AI 设备（多目相机 + 端到端模型 + 车端/机端推理）——「专用推理芯片 + 垂直整合制造」意味着马斯克系要把机器人/自动驾驶的视觉算力成本压到自给自足
- **判断**: $16.8B 只是一期、1 亿 sqft 是「制造空间」不是洁净室，实际洁净室规模与工艺能力未披露；Intel 14A 代工绑定是看点 —— 若成真，Intel 代工业务将拿到首个超大客户锚点；时间表未公布，先当长期叙事看待

### [FMS 2026 存储军备竞赛全景：BiCS10 332 层 QLC（37 Gb/mm²）、SK hynix 375 层 4D NAND + $38B 扩产、NEO 3D DRAM、Marvell PCIe 6.0](https://semiengineering.com/chip-industry-week-in-review-150/)
- **什么**: Future of Memory and Storage（FMS）大会本周召开，SemiEngineering 8/7 周报汇总多条存储路线图新闻
- **亮点**: ① **Kioxia/Sandisk BiCS10 3D QLC**：332 层、面积密度 **37 Gb/mm²**（全球最密 3D NAND），4800 MT/s 接口 + SCA 特性，目标数据中心 AI SSD（[Tom's 原文](https://www.tomshardware.com/pc-components/ssds/kioxia-and-sandisk-demonstrate-the-worlds-highest-density-3d-nand-flash-332-active-layers-and-up-to-4-800-mt-s-interface)）；② **SK hynix 375 层 4D NAND** 开发中，并批准约 **$38B** 新产能（Yongin Y2 + Cheongju M17，主攻 HBM/DRAM/NAND）；③ **NEO Semiconductor** 推出统一 AI 内存平台（SRAM 密度提升 + 用 3D NAND 工艺造 3D DRAM 以扩 HBM 容量）；④ **Marvell** 发布 PCIe 6.0 SSD 控制器 + 机架级内存池化方案；⑤ Silicon Box 先进封装产能今年扩 10 倍；CXMT 考虑北京第二厂
- **视觉关联**: 存储是视觉算力的「影子瓶颈」—— 视频训练集、多模态 KV cache、端侧模型驻留全吃 NAND/DRAM；密度与带宽曲线直接决定下一代视觉模型的成本结构
- **判断**: 与 8/7 的 Samsung zHBM 报道互证：2026 下半年存储供给紧 + 技术路线集体换代（300+ 层 NAND、3D DRAM、HBF），「内存超级周期」从价格信号升级为产能军备竞赛

### [RAM 价格回到 2007 年水平：AI 对 HBM 的需求把「20 年降价曲线」几个月内抹平](https://www.tomshardware.com/pc-components/ram/scientist-says-ram-pricing-has-reverted-to-normalized-2007-levels-memory-prices-have-been-falling-exponentially-for-decades-but-the-ai-shortage-undid-20-years-of-progress-in-a-matter-of-months)
- **什么**: Tom's Hardware 8/7 —— 性能专家 Daniel Lemire 对比历史内存价格：按单位容量计，当前 RAM 价格已回到 2007 年水平；Stanford DAM 项目数据：DDR5 约 $11.4–13.3/GB（2008 年 DDR2 为 $11–15/GB）
- **亮点**: Musk 在 SpaceX 财报电话会引用的供需缺口：存储产出年增约 20%，而 AI 需求年增 200%；SK 集团会长称 RAM 价格「abnormally high」；连国产 CXMT 内存价格也跟随三大厂上涨
- **视觉关联**: 内存涨价直接传导到视觉硬件 BOM —— 摄像头模组 ISP/AISP 的 LPDDR、边缘设备的 DRAM/NAND、GPU 服务器的 HBM，全链条成本上行（8/6 已见 iPhone 18 Pro 芯片等封装、RTX 5090 溢价 2.5 倍）
- **判断**: 「要么造出不那么吃内存的 AI 系统，要么造出更多更快的存储」（Lemire 原话）—— 这正是 HBF/zHBM/3D DRAM 等创新被加速的底层动力；对视觉设备厂商：锁长约、减内存依赖（量化、蒸馏、端侧模型小型化）是 2027 年前的生存策略

## 📦 开源硬件与工具

### [Hailo-10H Field Notes：Raspberry Pi AI HAT+2 实战笔记 —— 常开边缘 AI 盒子的 LLM/ASR 与「编译你自己的模型」踩坑实录](https://github.com/jaldertech/hailo10h-fieldnotes)
- 功能描述: 独立开发者记录在 **Hailo-10H（Raspberry Pi AI HAT+2 NPU）** 上搭建常开边缘 AI 盒子的全过程 —— 本地 Ollama 兼容 LLM API、本地 Whisper ASR API，以及社区最缺的「自编译模型上 Hailo」经验（HailoRT 5.3.0 + AI SW Suite 2026-04，2026 年 5–8 月实测）
- 上手方式: 仓库含配置脚本与踩坑记录；Hailo-10H 2025 年 7 月才商用、AI HAT+2 2026 年 1 月才开卖，公开实战材料稀缺，该仓库是目前最全的中小模型边缘部署参考
- 视觉关联: Hailo-10H 是 40 TOPS 级边缘 NPU（Hailo 主打的视觉/生成式混合负载），RPi + HAT+2 组合是 $100 级入门视觉 AI 原型平台 —— 比 Jetson 便宜、生态更草根；配套可见社区 NPU 池化探索（[hailort-k8s-npu-sharing](https://github.com/ssoonan/hailort-k8s-npu-sharing)，用 K8s 共享 NPU）

### [YOLO26 无人机航拍语义分割模型族登上 HF trending：Nano 档可上边缘 NPU 的 aerial 分割](https://huggingface.co/dronefreak/vdd-yolo26n-sem)
- 功能描述: HF image-segmentation trending 榜出现 dronefreak 的 VDD（无人机视频数据集）语义分割模型族 —— YOLO26 n/s/l/x 四档（vdd-yolo26n-sem 等），基于 Ultralytics/YOLO26 微调，另有 aeroscapes-yolo26s-sem 同族
- 上手方式: 标准 Ultralytics 流程加载，AGPL-3.0；nano 档（YOLO26n）可在 Jetson/Hailo 级边缘 NPU 上实时跑航拍分割
- 视觉关联: 无人机/低空经济的感知栈常被忽视 —— 航拍分割、车辆计数、灾后评估在边缘部署是典型刚需；同期 trending 上还有 [sam3.1-int8-int4-convrot](https://huggingface.co/Sparknight/sam3.1-int8-int4-convrot)（SAM 3.1 的 int8/int4 量化版），端侧分割生态持续活跃

## 📰 产业动态

### [NXP 洽购 Ambarella：$3B+ 的边缘视觉 SoC 公司，ADAS/机器人芯片整合信号](https://semiengineering.com/chip-industry-week-in-review-150/)
- 核心内容: SemiEngineering 8/7 周报引 Financial Times —— NXP 正在洽谈收购 **Ambarella**（估值超 $30 亿）。Ambarella 是边缘视觉 SoC 老兵：CV3-AD（5nm 车规 ADAS 中央域控）、CV5（8K 相机）、CV25，以及 GenAI 边缘芯片 N 系列，客户覆盖汽车前装、机器人、安防
- 影响: 车用半导体整合潮的直接例证 —— NXP 的 MCU/车载网络 + Ambarella 的视觉处理与 AI 栈合并，将形成「感知 SoC 全家桶」；与 SiEngine（芯擎）等国产座舱/ADAS SoC 厂商形成正面竞争；也是 8/7 EETimes「chiplet 路线解决汽车 SoC 成本爆炸」讨论的产业注脚
- 判断: FT 报道属传闻阶段，但方向明确 —— 2026 年汽车电子从「算力军备」转向「整合并购」，视觉 SoC 是核心标的

### [WSTS：2026 H1 全球半导体 $702B（+102% YoY），存储暴涨 305%；全年将达 $1.65T](https://semiengineering.com/chip-industry-week-in-review-150/)
- 核心内容: WSTS 数据 —— 2026 上半年全球半导体市场 $702B，同比 +102%；其中**存储 +305%**、逻辑 +45%；全年预测近 $1.65T
- 影响: 存储单价暴涨是主引擎（与本期 RAM 2007 价格、SK hynix $38B 扩产互证）—— 对视觉硬件从业者，这意味着模组/终端成本传导远未结束，而逻辑 +45% 部分反映 AI 加速器出货（NVIDIA/AMD/国产 NPU 都在此列）
- 判断: 数字口径为名义值、含涨价水分，但量级无可辩驳 —— 半导体在 2026 年重新成为全球制造业的「利润之王」，存储是绝对主角

### [AI 硬件初创融资潮：Lumilens $900M 出 stealth（CPO 光互连）、OLIX $312M（token 生产分阶段专用芯片）、SiEngine $200M（国产座舱/ADAS SoC）](https://semiengineering.com/chip-industry-week-in-review-150/)
- 核心内容: 本周三笔值得注意的融资 —— ① **Lumilens**：$900M 出 stealth，做 co-packaged / near-packaged / pluggable 光互连（CPO 路线，与 8/6 GF 硅光报道同赛道）；② **OLIX**：$312M，做「token 生产各阶段专用芯片」平台（disaggregated inference，与 AMD×Taalas 同思路）；③ **SiEngine（芯擎）**：$200M，做软件定义汽车的座舱 + ADAS SoC（国产车载芯片代表，对标 NXP×Ambarella 整合后的产品线）
- 影响: 三条线分别对应视觉/多模态算力链路的三个瓶颈 —— 集群互连（光）、推理成本（专用片）、车载感知（ADAS SoC）；资本在 2026 年明确押注「算力的精细化分工」
- 判断: 融资 ≠ 产品，但金额量级说明：AI 硬件从「通用 GPU 一家独大」走向「每个瓶颈环节都有专用玩家」的再分工时代

---

*数据窗口 2026-08-04 ~ 2026-08-08 · 来源: SemiAnalysis / EETimes / NVIDIA Blog / Tom's Hardware / SemiEngineering / Sony Semiconductor / OmniVision / GitHub / HuggingFace / AMD Newsroom · Reddit API 仍被限流；OmniVision 新闻页 404、Sony 为 JS 渲染，本周传感器无新品；EETimes 正文抓取超时，Imagination 战略稿（砍 CPU/NPU 押注 GPU IP + 中国）仅按摘要记录未入选；GitHub 新增仓库以低 star 习作为主，仅 Hailo 实战笔记入选*
