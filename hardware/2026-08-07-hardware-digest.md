# ⚙️ 2026-08-07 视觉硬件日报

> 今日扫描了 SemiAnalysis · EETimes · NVIDIA Blog · Tom's Hardware · SemiEngineering · Sony Semiconductor · OmniVision · GitHub · HuggingFace · Reddit 等 10 个渠道，精选 9 条
> 注: 8/6 日报已覆盖 Ikerlan BEGI 神经形态 3D 视觉传感器、SpaceX×xAI 独家 N 卡、Frore 液冷、Samsung 内存路线图、CXMT、昇腾 HBM 瓶颈等，本期聚焦 8/6–8/7 新动态，不重复。

---

## 🎥 传感器与采集

### [Depth Anything V3 (DA3) 1.1 系列 + MoGe-2-LiteRT：深度感知「软件化」趋势在 HF 霸榜](https://huggingface.co/depth-anything/DA3-GIANT-1.1)
- **什么**: HuggingFace depth-estimation trending 榜本周被 Depth Anything 3 的 1.1 版本刷屏 —— [DA3METRIC-LARGE](https://huggingface.co/depth-anything/DA3METRIC-LARGE)（69.5 万下载）、[DA3MONO-LARGE](https://huggingface.co/depth-anything/DA3MONO-LARGE)（10.2 万）、DA3-GIANT-1.1 / DA3-LARGE-1.1 均在榜；同期还有 [MoGe-2-LiteRT](https://huggingface.co/litert-community/MoGe-2-LiteRT)（Google LiteRT/on-device 运行时版单目几何估计）与 GeoStereo、PVDepth 等新深度模型
- **亮点**: DA3 系列区分 Metric（带尺度）与 Mono 两个支线，GIANT 档面向高精度离线，Small/B 档可跑端侧；MoGe-2 主打「单目 → 稠密 3D 几何」且已出 LiteRT 移动端导出格式
- **视觉关联**: 深度传感正在「去硬件化」—— 单目深度模型的精度爬升直接挤压低端 ToF / 双目 / 结构光模组（手机、扫地机、AMR、AR 头显）的生存空间；Metric 深度对机器人的避障/抓取是刚需
- **判断**: 这不是单纯模型新闻 —— 当 metric depth 能在 <5W 的 edge NPU 上实时跑，厂商会砍掉 BOM 里的专用深度传感器；对 Sony/OmniVision 的 ToF 产品线是结构性压力，与本期「传感器新品静默」互相印证（Sony/OV 新闻页本周无新品发布，页面多为 JS 渲染导航）

## 🖥️ GPU 与算力

### [AMD 收购 Taalas：把「整个 LLM 烧进硅片」的推理芯片初创，对标 NVIDIA×Groq 的 disaggregated inference](https://www.eetimes.com/ai-chip-startup-taalas-acquired-by-amd/)
- **什么**: AMD 官宣收购多伦多 AI 推理芯片初创 Taalas（2023 年创立，联合创始人为前 Tenstorrent CEO、前 AMD 高管 Ljubisa Bajic）；团队并入 Vamsi Boppana 领导的 AI 部门，金额未披露
- **性能**: Taalas 原型芯片在 **Llama3.1-8B 上实现 >16,000 tokens/s/用户**（比当前竞品高数倍）；方案完全 **SRAM-based、无指令集**，即「模型即芯片」—— 代价是单芯片只跑一个模型（约 8B 参数上限，视量化而定），换模型要重新 tape-out（约 2 张掩膜 = 权重 + dataflow，工具流号称 2 个月出片）；DeepSeek-671B 级模型需要约 30 次流片
- **视觉关联**: AMD 计划把 Taalas 技术集成进 **Instinct GPU 的系统级方案** —— 复制 NVIDIA「GPU 做 prefill + 专用芯片做 decode」的 disaggregated 推理路线（对标 NVIDIA 几乎全资收购 Groq 的 $20B 交易、以及 AMD×Cerebras 合作）；另一条路是用 Taalas 跑**小模型的完整推理**，EETimes 点名 **physical AI / 边缘机器人**（当前 AMD 用 FPGA 加速器和 SoC 覆盖的领域）—— 结构化 ASIC 形态对标 Intel 收购 eASIC 的路线
- **判断**: 这是「推理去通用化」的最强信号：巨头纷纷用专用片处理 decode 阶段来榨 tokens/s。对视觉/多模态推理，意味着边缘小模型（<8B）可能迎来「模型专用硅片」这一新硬件品类，但模型迭代速度和流片成本是硬伤，先看 AMD 把它放在云端 decode 还是边缘整推

### [Wistron 德州 Fort Worth 工厂投产：GB300 下线、Vera Rubin 备产，「美国制造」AI 超芯片落地](https://blogs.nvidia.com/blog/nvidia-and-partners-build-in-america-for-america/)
- **什么**: NVIDIA Blog 8/5 更新「Build in America」专题 —— Wistron 在 Fort Worth 的 32.4 万平方英尺首座美国工厂正式投产
- **性能**: 已开始生产 **GB300 Grace Blackwell Ultra Superchip**，正在为 **Vera Rubin Superchip** 做准备；对应 NVIDIA $7 亿美元美国先进制造承诺，创造 500+ 岗位（年底扩至 1,000）
- **视觉关联**: GB300/Rubin 是视觉大模型与多模态训练的主力算力；「整机在美国组装」意味着美国本土视觉/AI 研究机构（大学、NSF AI Hubs、国防）采购 NVL72 级系统的供应链风险下降、交付提速
- **对比**: 与台积电亚利桑那、Intel Ohio 同一波「先进制造回流」；对国内算力生态无直接影响，但反映美国政策面把 AI 算力视为战略基础设施

### [二手市场：22GB 魔改 RTX 2080 Ti 在 eBay 卖 $500 —— 本地 AI 推理的「穷人乐」](https://www.tomshardware.com/pc-components/gpus/pre-modded-rtx-2080-ti-cards-with-22gb-of-vram-surface-on-ebay-for-usd500-hong-kong-based-seller-offers-ai-friendly-memory-mod-for-a-reasonable-price)
- **什么**: Tom's Hardware 8/6 报道香港卖家在 eBay 出售预改 22GB 显存的 RTX 2080 Ti（原装 11GB）
- **亮点**: $500 拿下 22GB VRAM + CUDA 生态，是本地跑 7B–13B 量化视觉/多模态模型（LLaVA、Qwen-VL 类）的最低成本路径之一；魔改显存（2GB 颗粒替换）是 2080 Ti 的经典操作，如今有人预装好直接卖
- **视觉关联**: 个人研究者/小团队的 edge 实验平台 —— 批量做图像推理、embedding、微调实验的「穷人工作站」
- **判断**: 侧面反映 GDDR 短缺与旗舰卡涨价（同周 RTX 5090 实际成交价已近 2.5 倍 MSRP）把需求挤向二手魔改市场；对严肃训练无意义，但对「人手一张本地推理卡」的社区生态是真需求

## 🔩 芯片与半导体

### [Samsung 连发 zHBM / zNAND-O / BV-NAND 三件套：HBM 直接叠在 AI 加速器上，宣称 8× HBM5](https://www.tomshardware.com/pc-components/dram/samsung-debuts-three-next-generation-memory-technologies-for-ai-data-centers-zhbm-znand-o-and-bv-nand-all-rely-on-advanced-wafer-bonding-technologies)
- **动态**: 继 8/5 EETimes 的内存路线图报道后，Tom's Hardware 8/6 补全细节 —— Samsung 三项技术全部依赖**先进晶圆键合（wafer bonding）**
- **亮点**: ① **zHBM**：把 HBM 堆栈直接放在 AI 加速器**正上方**（而非周边 interposer），缩短数据路径，宣称「约 8 倍于 HBM5 的性能」、键合实现 >10× 内存密度，且支持客户定制 IP 集成进互连层（意味着 zHBM 可能是非标准方案）；② **zNAND-O**：4–8 层 NAND 堆在逻辑 die 之上，主打 edge AI 实时推理的低延迟高 I/O；③ **BV-NAND**：新品牌名 —— NAND array 键合在 I/O/logic wafer 之上，对应 400 层级第 10 代 V-NAND（28 Gb/mm²、5600 MT/s）
- **影响**: 对视觉硬件，zHBM 若兑现 = 视觉大模型推理的内存带宽墙直接后移（视频理解、多模态上下文最吃带宽）；zNAND-O 明确点名 edge AI —— 与机器人/端侧视觉的近存计算诉求同频
- **判断**: 数字（8× HBM5）营销味浓且未定义口径（带宽 or 应用性能？），时间表模糊（对标 HBM5 = 2020 年代末）；但「把内存叠上计算 die」的物理方向与 SK hynix HBM4 垂直集成传闻一致，是 2027+ 存储-计算融合的主路线

### [GlobalFoundries 硅光起飞：Q2 数据中心营收 +62%，SiGe 产能 2027 年前已订满，$3 亿美国商务部意向落地](https://www.eetimes.com/globalfoundries-growth-makes-the-case-for-a-u-s-photonics-buildout/)
- **动态**: EETimes 8/6 分析 GF Q2 财报 —— 总营收 $17.86 亿（+6% YoY），non-IFRS 毛利率 29.9%（同比 +5pp）；**通信基础设施与数据中心营收 +62% YoY / +20% QoQ**，全年该板块增速指引从「high 30s%」上调至 50–60%
- **亮点**: 硅光收入 2026 年预计**翻倍以上**；已与全球前五大光收发器供应商中的四家合作；SCALE 平台 7 个活跃客户项目、Q2 完成 1 个 tape-out、Q3 再 1 个；**SiGe 产能已超订到 2027**，Vermont/Malta 扩产、新加坡新增 300mm SiGe；与商务部 $3 亿意向协议（LOI）加速美国硅光产能
- **影响**: AI 数据中心互连（光模块、CPO、硅光引擎）是视觉训练集群的「隐形血管」—— GPU 规模上去了，光互连带宽就是下一个瓶颈；GF 的 SCALE 平台（硅光 + 封装）是美国本土 CPO 供应链的关键拼图
- **判断**: 与 NVIDIA Spectrum-6 千兆级 AI 工厂、xAI 1GW Colossus 2 形成互证：光互连产能是本轮算力扩张最紧俏的中间环节之一

### [DRAM 短缺开始卡苹果：约 $10 亿的 iPhone 18 Pro 芯片「躺在货架上等封装」](https://www.tomshardware.com/pc-components/dram/usd1-billion-of-iphone-18-pro-chips-on-the-shelves-awaiting-packaging-due-to-dram-shortages-memory-shortages-reportedly-put-a-wrinkle-in-apples-launch-plans)
- **动态**: Tom's Hardware 8/6 报道 —— 因 DRAM 短缺，价值约 **$10 亿的 iPhone 18 Pro 芯片已产出但无法进入封装**，苹果发布计划生变
- **影响**: 手机影像是视觉硬件最大出货池（ISP、AISP、相机模组全要配 DRAM/LPDDR）；DRAM 缺货→整机节奏乱→上游传感器/模组订单同步波动。同周连锁反应：Microsoft 悄悄删除 32GB RAM 推荐配置、RTX 5090 成交价飙至 2.5 倍 MSRP、8/5 已有 GPU 涨价风暴报道 —— 2026 下半年「内存超级周期」是视觉硬件 BOM 成本的最大变量
- **判断**: 与 8/6 的 Samsung 路线图、CXMT 扩产呼应 —— 短期供给紧、中期国产与 3D DRAM 技术路线都在抢时间；对终端视觉设备厂商的建议是提前锁 LPDDR/DRAM 长约

## 📦 开源硬件与工具

### [22GB RTX 2080 Ti 魔改卡量产化：HK 卖家预装出货，$500 级本地推理「即插即用」](https://www.tomshardware.com/pc-components/gpus/pre-modded-rtx-2080-ti-cards-with-22gb-of-vram-surface-on-ebay-for-usd500-hong-kong-based-seller-offers-ai-friendly-memory-mod-for-a-reasonable-price)
- 功能描述: 社区 2080 Ti 显存魔改（11GB→22GB，2GB GDDR6 颗粒替换）从「自己动手」变成商品化服务 —— eBay 上 $500 即可买到预改卡
- 上手方式: 即插即用；配 PyTorch/CUDA 生态直接跑 7B 级量化视觉模型；注意魔改卡无保修、显存散热与稳定性靠卖家手艺
- 视觉关联: 本地图像推理/embedding/数据清洗的最低成本工作站，适合个人研究者与边缘原型验证（同 GitHub 扫描结果：本周 embedded vision 新仓库以低 star 习作为主，无明星开源硬件项目，故本期开源板块以该社区硬件话题为代表）

## 📰 产业动态

### [NVIDIA Cosmos 3：开放世界模型家族，physical AI 的「合成数据发动机」](https://blogs.nvidia.com/blog/open-world-models-physical-ai/)
- 核心内容: NVIDIA Blog 8/6 推出「Open World Models / Into the Omniverse」专题 —— **Cosmos 3** 开放模型家族用于生成训练数据、测试策略、微调 specialized physical AI 系统；采用 Linux Foundation **OpenMDW 1.1** 许可（允许基于自有数据/硬件后训练），覆盖机器人、自动驾驶、视觉 AI
- 影响: 对硬件的意义在于「合成数据 → 缩小对真实传感器数据采集的依赖」—— 长尾场景（罕见事故、极端光照）可以在仿真里无限生成，间接降低自动驾驶/机器人公司采购传感器与路测车队的需求强度；与 7 月 200+ 家公司签署的《Open Weights and American AI Leadership》公开信同频
- 判断: 内容偏软件，但它是「物理 AI 数据工厂」叙事的一部分；对视觉硬件从业者，值得关注的是它是否会挤压真实 sensor 数据采集预算

### [弗吉尼亚州对 AI 数据中心开刀：76% 电价上涨后，要求企业自付全部专用上游电力设施](https://www.tomshardware.com/tech-industry/data-centers/after-severe-76-percent-electricity-price-hikes-due-to-ai-data-centers-virginia-requires-firms-to-pay-for-all-dedicated-upstream-electrical-infrastructure-state-regulators-crack-down-governor-says-move-will-save-civilians-hundreds-of-millions-of-dollars)
- 核心内容: Tom's Hardware 8/6 —— AI 数据中心导致居民电价暴涨 76% 后，弗吉尼亚州监管机构要求数据中心企业**全额承担专用上游电网设施成本**；州长称此举将为居民节省数亿美元
- 影响: 电力是算力的物理上限 —— 该政策会抬高美国东岸新建训练集群的资本开支与选址门槛，加速算力向「电力便宜 + 政策友好」地区（德州、西部）迁移；对视觉/多模态训练集群的 TCO 模型是直接输入变量，也呼应本期 xAI Colossus 2（1GW）与 GW 时代叙事
- 判断: 数据中心「电税」化是 2026 下半年全球性趋势（Virginia 之后料有更多州跟进），视觉训练预算的 30%+ 可能从 GPU 转向电力与基础设施

---

*数据窗口 2026-08-06 ~ 2026-08-07 · 来源: SemiAnalysis / EETimes / NVIDIA Blog / Tom's Hardware / SemiEngineering / Sony Semiconductor / OmniVision / GitHub / HuggingFace · Reddit API 本次仍被限流；Sony/OmniVision 新闻页为 JS 渲染，本周无可见新品发布；GitHub 搜索结果以低 star 新仓库为主，无入选项*
