# ⚙️ 2026-08-14 视觉硬件日报

> 今日扫描了 SemiAnalysis · EETimes · NVIDIA Blog · Tom's Hardware · SemiEngineering · EEJournal · Sony Semiconductor · OmniVision · AMD Newsroom · GitHub API · HuggingFace API · Reddit · Google News(国产芯片) 等 13 个渠道，精选 10 条
> ⚠️ Reddit API 仍 403；SemiAnalysis RSS 疑似停更（仍停在 2025-09 旧条目）；Sony/AMD 官网 JS 渲染抓不到列表；OmniVision 新闻页 404（唯一新条目是 1 月 CES 旧闻，不选）；GitHub trending 反爬（0 条），改用 API 搜索
> 注: 8/13 已覆盖 Sony×TSMC CIS 合资、RTX PRO 6000 涨价、GMSL、YMTC 前三等，本期不重复；头条是 **CXMT 市值超腾讯登顶中国第一** 与 **地平线征程7「星空」芯片获定点进入量产**

---

## 🎥 传感器与采集

### 1. [智能手机被芯片涨价「压垮」：iPhone 变贵、廉价机变少](https://www.eetimes.com/smartphone-makers-squeezed-by-soaring-chip-costs/)
- **什么**: EETimes 8/13 报道——芯片成本正在吞噬手机厂商毛利，行业进入「要么涨价、要么砍配置」的窗口
- **亮点**: 直接后果是 **iPhone 等旗舰涨价**、**廉价机型数量收缩**；驱动因素是 SoC/AP、内存与 CIS 全链条涨价（呼应 8/10 内存超级周期）
- **视觉关联**: 手机影像硬件是 CIS（索尼/三星/OV）最大的出货基本盘——成本压力下，厂商的第一刀通常砍在**中低端摄像头数量与规格**（双摄→单摄、去长焦），高端影像堆料（大底、潜望）会进一步向万元旗舰集中
- **判断**: 与 8/13 RTX PRO 6000 涨价是同一枚硬币的两面——**视觉硬件进入全面通胀周期**；对开发者：端侧视觉方案的 BOM 成本模型今年必须重算

## 🖥️ GPU 与算力

### 2. [EIZO Condor T5-IOX：搭载 NVIDIA IGX Thor 的军规级 3U VPX 单板机](https://www.eejournal.com/industry_news/eizo-rugged-solutions-launches-sosa-aligned-3u-vpx-single-board-computer-powered-by-nvidia-igx-thor-for-tactical-ai-edge-processing/)
- **什么**: EIZO Rugged Solutions 8/10（奥兰多发布）推出 **Condor T5-IOX**——SOSA™ 对齐的 3U VPX 单板计算机，核心是 **NVIDIA IGX T5000 模组（IGX Thor 平台）**
- **亮点**: 面向战术边缘的实时推理与**多传感器融合**；视频/数据接口含 **4× 12G-SDI 输入**、USB 3.2、RS-232、DisplayPort，可同时接入多路高清摄像头；军规加固
- **视觉关联**: IGX Thor = Blackwell 架构的机器人/边缘工业平台（Jetson 的「严肃工业版」）；12G-SDI 多路视频接入意味着无人机/无人车/安防的**多摄像头实时感知**在战术级硬件上落地
- **对比**: 与消费级 Jetson 不同，IGX Thor 主打功能安全与车规/军规认证——这是「机器人/自动驾驶视觉算力」向加固嵌入式市场渗透的信号；同天 EEJournal 还有 Peraso PRM2145 抗干扰通信模组，军规边缘生态在集体升温

### 3. [高通 Snapdragon C 首次公开规格：$300 笔记本的 8 核 ARM SoC](https://www.tomshardware.com/pc-components/cpus/qualcomm-details-snapdragon-c-specs-for-usd300-laptops-for-the-first-time-claims-67-percent-faster-performance-on-battery-than-intel-n250-ac-performance-remains-a-mystery)
- **什么**: 高通 6 月预告的廉价笔记本平台 **Snapdragon C** 首次公布详细规格（8/12 发布、8/13 更新）
- **性能**: 8 核 Kryo CPU——1 核 3.0GHz / 3 核 2.6GHz / 4 核 2.0GHz（全核持续 2.0GHz）；Adreno GPU 最高 900MHz；**Hexagon NPU**（未公布 TOPS）；最高 16GB LPDDR5/5x/LPDDR4x；PCIe 3.0 NVMe；宣称电池下性能比 Intel N250 快 **67%**（AC 性能存疑）
- **视觉关联**: NPU 存在但算力未公开——「$300 笔记本」定位决定了它是**低成本端侧 AI 硬件**（会议摄像头、实时字幕、轻量 CV）的载体；Acer/Asus/HP/Lenovo 将出货
- **判断**: 这是高通用 Arm 低价位围剿 Intel 的排头兵，NPU TOPS 不公开说明这代定位「能跑但别指望大模型」；对视觉硬件：值得观察它能否像骁龙 X 一样把**端侧 NPU 生态**（QNN）带到百元级设备

## 🔩 芯片与半导体

### 4. [CXMT 市值 $524B 超腾讯，登顶中国第一：DRAM 国产巨头的 IPO 神话](https://www.tomshardware.com/tech-industry/cxmt-overtakes-tencent-to-become-chinas-most-valuable-company-17-days-after-its-ipo)
- **动态**: 8/13（周四）收盘，长鑫存储（CXMT）市值 **$524B**，正式超过腾讯（$511B），成为**中国市值最高公司**——距其 7/27 科创板 IPO 仅 17 天；IPO 首日暴涨 466%，募资 $8.6B，散户超额认购 212 倍
- **关键数据**: 2025 年全球 DRAM 份额 **7.67%**（第 4）；Q1 经营利润 ¥35.43B（$5.2B），去年同期亏损 ¥2.83B；服务器 DRAM 占营收从 2024 年 8.4% → 2025 年 26.5%；手握腾讯 $3B、字节 $7B/5 年的服务器 DRAM 大单；规划第 6 座 mega-fab、2030 年目标 **30% 全球份额**——但仍无 EUV 光刻机
- **影响**: 腾讯自己就是 CXMT 客户（6 月签 $3B 服务器 DRAM 协议）——「买算力的在跌、卖存储的在涨」；$524B 市值已是美光（~$1T）的一半、SK 海力士（~$880B）的六成
- **判断**: 这是**存储超级周期 × 国产替代**的双重定价：CXMT 从「价格屠夫」变成「定价方」（8/10 已报它拒绝苹果压价），如今资本把它按「中国台积电」叙事重估；对视觉硬件：服务器 DRAM/内存价格继续看涨，**端侧与推理集群的 memory 预算 2027 年前别指望回落**

### 5. [Expedera Origin：packet-based NPU 进入 LLM 时代——边缘芯片架构的转向信号](https://semiengineering.com/packet-based-npus-in-the-llm-era-from-compute-bound-cnns-to-memory-bound/)
- **动态**: SemiEngineering 8/13（赞助博客，作者 Sharad Chole）系统阐述 Expedera Origin NPU IP 的架构演进：从「逐层调度 CNN」转向 **packet 调度**，让 CNN 与 LLM/VLM 成为一等公民
- **技术要点**: 显式区分 **prefill（算力密集，接近 CNN 行为）与 decode（KV cache 内存流密集）**两阶段分别建模调度；通过减少外部内存搬移提升同功耗下 tokens/s；面向**汽车/边缘 SoC 的感知+舱内+生成式负载共存**（perception、DMS、infotainment、VLM 同片运行）；Origin Evolution 获 2026 Edge AI and Vision Product of the Year Awards「Best Edge AI Processor IP」
- **视觉关联**: 这是边缘 NPU 从「CNN 加速器」向「多模态/生成式加速器」迁移的架构样板——车载摄像头感知 + 座舱 VLM 用同一 NPU 跑，正是下一代舱驾一体 SoC 的算力需求（对照 #8 地平线征程7）
- **判断**: 厂商软文，判断要打折——但「prefill/decode 分阶段建模」确实是 2026 年 NPU IP 设计的主流方向，值得做边缘视觉的人跟进

## 📦 开源硬件与工具

### 6. [GitHub 周扫描：事件相机生态仍偏学术，Zynq/K230 边缘视觉持续小步迭代](https://github.com/search?q=event+camera+created%3A%3E2026-08-07&s=stars&type=repositories)
- **功能**: 本周新建仓库整体低信号（星标普遍 0-2），值得看的三类：① **Neuromorphic-Webcam**——浏览器里跑的 DVS 像素模型（只报变化像素，纯学习向事件相机模拟器）；② ECCV 2026 官方代码 **"Static in Frames, Dynamic in Events"**（事件相机特征即运动线索）；③ 嵌入式视觉实践：**zynq-yolov3-tiny-accelerator**（FPGA 加速 YOLO）与 **k230-vision-tracking**（嘉楠 K230 RISC-V 端侧跟踪）
- **上手**: 前两个浏览器/GitHub 直接可看；后两个是 Xilinx/嘉楠开发板实战仓库
- **判断**: 事件相机工程化生态（对标 Prophesee/IMX636）在开源社区仍未成气候；端侧视觉则以「复现 + 板级 demo」为主，没有出现新的硬件级突破

### 7. [HuggingFace 端侧模型观察：抠图/深度/OCR 三线齐发，ONNX 化加速](https://huggingface.co/models?pipeline_tag=image-segmentation&sort=trending)
- **功能**: ① 分割/抠图：**briaai/RMBG-2.0**（63.7 万下载、1.4k likes）领跑，BiRefNet lite + ONNX 版齐上——这类「可导出 ONNX、跑在 CPU/NPU」的模型正是瑞芯微 RK 系、Jetson 的边缘部署主力；② 深度估计：**depth-anything/DA3-METRIC-LARGE**（52.4 万下载）与 DA3-SMALL（小模型端侧版）、apple/DepthPro-hf（109 likes）——Depth Anything v3 生态持续统治；③ 检测/OCR：**Ultralytics/YOLO26**（8.9k 下载）、**nvidia/nemotron-ocr-v2**（243 likes）
- **视觉关联**: 趋势明确——**模型体积与部署门槛同时下降**（RMBG-2.0、DA3-SMALL、mobilevit-small 都是百 MB 内可上边缘的量级），端侧硬件在等模型，而模型确实在变小
- **上手**: 全部可直接 `pip install` + transformers/onnxruntime 部署；测试端侧性能建议优先选 `-ONNX` / `-SMALL` / `-lite` 后缀

## 📰 产业动态

### 8. [地平线征程7「星空」敲定目标算力 + 首个纯国产舱驾一体定点：量产在即](https://news.google.com/rss/articles/CBMiW0FVX3lxTE5MeE40QmRtdnUwNVhJdDJpYWVXS3c5NXBUX1hNSU9OdVJYUDFRZ3dlQkd3cnNZUzJPUjYxQlpoenRXZS1KWXhaY0MwSThuU05iMDBrTEpFNmlxYkE?oc=5) · [中金在线 8/14：星空芯片获头部新能源车企定点，与博泰车联进入量产新阶段](https://news.google.com/rss/articles/CBMia0FVX3lxTE0zdnhZclM3RHZpY1M2YnZoeTZ0b0tKUnFnQXV2LU9va3Nzb0p0bGRNVFN5b01XQUZhSC12bnZMR2xheUhsVTM3b05PcUExdm1vWFUteGlyaldSSlpWS2swMjdNRXRubk10ajlv?oc=5)
- **核心内容**: ① **晚点独家（8/12）**：地平线已敲定 **征程7（Journey 7）目标算力**，舱驾一体（座舱+智驾融合）产品代号 **「星空」（Star Sky）**；② **博泰车联（HK:02889，8/11–8/12）**：获国内头部新能源车企项目定点，落定**行业首个纯国产舱驾一体芯片高端 AI 座舱项目**；③ **8/14**：星空芯片定点消息确认，地平线×博泰合作进入**量产新阶段**
- **视觉关联**: 征程7/星空是国产智驾芯片下一代旗舰——对标征程6（征程6M 已上车长安启源 Q05，8/9）；「舱驾一体」意味着**同一颗 SoC 同时跑 8+ 路摄像头感知与座舱多模态**，对 NPU 架构的要求正是 #5 说的「CNN + LLM 双一等公民」
- **判断**: 从「定点」到「量产」是国产智驾芯片最难的一关（此前多停留在发布/送样）；若星空如期量产，将与华为乾崑、英伟达 Thor 正面竞争——这是 2026 下半年最值得盯的国产视觉算力事件（注：Google News 转链，原文见晚点/车家号）

### 9. [NPO（近封装光学）上位：业界用「折中方案」对冲 CPO 的成长阵痛](https://www.tomshardware.com/tech-industry/near-packaged-optics-gains-ground-aso-the-industry-hedges-against-co-packaged-optics-growing-pains)
- **核心内容**: SemiAnalysis 8/10 连发三条 X 线程力推 **NPO**——可插拔光模块到真正 CPO 之间的过渡架构；三个卖点：**模块可现场更换、故障爆炸半径限定在单插座单元、光引擎与交换 ASIC 分装（组装更简单）**；两个月前 SemiAnalysis 刚把 CPO 规模量产预期推迟到 2027（scale-out）/2028–2029，曾单日砸掉 Applied Optoelectronics 17%、Lumentum 8% 市值
- **生态佐证**: Broadcom 在 2026 年 3 月 OFC 展示了 **3.2T VCSEL 的 NPO 产品线**；6 家连接器/光学厂商同期成立标准组，为 NPO 定义统一 socket
- **影响**: 对视觉硬件——AI 集群的 scale-out 带宽（多模态/视频训练）是光互连需求基本盘；CPO 推迟 + NPO 顶上意味着 **2027 年前机架内互连仍以可维护性优先**，产业链（光引擎、socket、连接器）先吃 NPO 红利
- **判断**: 与 8/13「硅光成为热商品」同一叙事线的落地修正：**CPO 是好目标，NPO 是好生意**——短期看空 CPO 纯玩家、看多 NPO 组件厂

### 10. [Cerebras 财报不及预期股价暴跌近 20%：卖芯片转卖算力的转型阵痛](https://www.tomshardware.com/tech-industry/artificial-intelligence/cerebras-shares-plunge-nearly-20-percent-after-missing-earnings-expectations-hardware-sales-drop-but-ai-cloud-revenue-climbs-281-percent)
- **核心内容**: 8/13 Cerebras 财报后股价 **-20%**：硬件销售同比 **-23%**，而云/服务收入暴增 **+281%**——客户从「买 WSE 整机」转向「租 Cerebras 云算力」
- **原因**: 商业模式从「TSMC 造晶圆级引擎 → 卖 CS 系统」转向「自持硬件 + 自建数据中心 + 卖推理/训练算力」——**先砸巨额资本开支、后赚云收入**，现金流模型陡变，市场用脚投票
- **影响**: 这是「AI 硬件公司资产化」（8/13 CoreWeave A100 叙事）的镜像案例——**卖算力比卖芯片更性感，但更烧钱**；对视觉从业者：推理算力定价正在从「买卡折旧」转向「云上按需」，长期利好租算力的一方，短期波动是常态
- **判断**: 与 8/13「NVIDIA AI 工厂资产化」对照看：整个 AI 硬件行业都在从「设备商」变成「运营商」，Cerebras 是第一个被市场教育「转型要付代价」的

---

*数据窗口 2026-08-13 ~ 2026-08-14 · 来源: SemiAnalysis（feed 停更）/ EETimes / NVIDIA Blog / Tom's Hardware / SemiEngineering / EEJournal / Sony Semiconductor（JS 渲染无果）/ OmniVision（仅旧闻）/ AMD Newsroom（仅 8/6 旧闻 Taalas，已覆盖）/ GitHub API（event camera/ISP/embedded vision/lidar）/ HuggingFace API（5 条 pipeline）/ Reddit（403 限流）/ Google News（国产芯片：昇腾/寒武纪/地平线/瑞芯微/黑芝麻）*
