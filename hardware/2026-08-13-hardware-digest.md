# ⚙️ 2026-08-13 视觉硬件日报

> 今日扫描了 SemiAnalysis · EETimes · NVIDIA Blog · SemiEngineering · Tom's Hardware · Sony Semiconductor · GitHub · HuggingFace · Bing(国产芯片) 等 9 个渠道，精选 10 条
> ⚠️ Reddit API 仍 403 限流；SemiAnalysis 依旧停在旧条目；OmniVision 官网为 JS 渲染抓不到列表；国产芯片只捞到 YMTC（见 #5），寒武纪/昇腾本轮无可靠新动态，不硬凑
> 注: 8/12 已覆盖 AMD 机器人芯片、FCC 光模块禁令、800VDC、Intel 融资，本期不重复；头条是 **索尼×台积电 $4.7B 图像传感器合资** 与 **RTX PRO 6000 翻倍涨价**

---

## 🎥 传感器与采集

### 1. [索尼 × 台积电 $4.7B 合资「Advanced Vision Semiconductor Manufacturing」：CIS 供应链的历史性合体](https://www.eetimes.com/sony-tsmc-4-7b-deal-helps-thwart-samsung-analysts-say/) · [索尼官方公告](https://www.sony-semicon.com/en/news/)
- **什么**: 索尼（Sony Semiconductor Solutions）与台积电成立图像传感器合资公司，8/11 官宣——索尼出资 **4650 亿日元（约 $2.9B）控股**，台积电出资 **2820 亿日元（约 $1.77B）**，合计约 **$4.7B**
- **亮点**: 选址日本 **熊本县**（紧邻台积电 JASM 晶圆厂）；**2029 年投产**；索尼主导核心传感器技术、产品规划与设计，台积电负责制造；此前 5/8 双方已签初步协议，8/11 正式落地
- **视觉关联**: 手机影像（分析称直接针对三星在 **Apple iPhone 图像传感器** 的渗透）、车规/工业 CIS 共用产线；「索尼像素技术 + 台积电先进制程/产能」= 全球 CIS 最高规格组合
- **判断**: 这是把 CIS 从「IDM 内制」推向「design + foundry 专业分工」的标志性事件——索尼此前图像传感器基本自产（长崎/熊本自家 fab），拉上台积电意味着先进制程（22nm 以下像素电路）与产能弹性都要外部化；对视觉硬件生态的信号：**传感器也会像 GPU 一样走向专业代工化**

### 2. [ADI 技术深潜：GMSL 的 Pixel Mode vs Tunnel Mode——车规相机 SerDes 怎么选](https://www.eetimes.com/navigating-gmsl-how-pixel-and-tunnel-modes-enhance-system-performance/)
- **什么**: EETimes 与 ADI 合作的技术文章，讲解 GMSL™（Gigabit Multimedia Serial Link）传输 CSI-2 视频数据时两种模式的选择
- **亮点**: **Pixel mode** 逐像素搬运 MIPI CSI-2 数据、保真度最高；**Tunnel mode** 把整条 CSI-2 流打包传输，适合**多路摄像头聚合 + MIPI PHY 转换 + 流聚合**场景；文章比较了数据完整性、带宽利用率与系统灵活性
- **视觉关联**: 自动驾驶环视/舱内摄像头、嵌入式视觉长距离传输（GMSL 铜缆可到 15m+）——任何「多摄像头 + 单 SoC」架构（Jetson、高通 Ride、地平线征程）都绕不开这条链路
- **对比**: 主流车规 SerDes 三强 ADI GMSL / TI FPD-Link / 索尼+瑞萨 GVIF，选型本质是「pixel 保真 vs tunnel 灵活」的工程权衡；8/12 EETimes 同期还有 GMSL 生态文章，说明车规相机互连正从「够用」走向「系统化设计」

## 🖥️ GPU 与算力

### 3. [RTX PRO 6000 Blackwell 标价翻倍至 $16,000：工作站显卡进入「爱买不买」模式](https://www.tomshardware.com/pc-components/gpus/nvidia-doubles-rtx-pro-6000-blackwells-msrp-to-a-staggering-usd16-000-96gb-card-started-pre-orders-below-usd8-000-last-year)
- **什么**: NVIDIA 再次「静默涨价」——RTX PRO 6000 Blackwell（96GB）在美国 Marketplace 标价涨到 **$16,000**
- **性能/价格轨迹**: 2025 年 3 月预购价低至 **$7,673**、4 月上市价 **$8,565** → 2026 年 6 月 **$13,250**（+57%）→ 8 月 **$16,000**（再 +20%）；**累计涨幅约 90%**，比首发价翻倍还多
- **视觉关联**: 这是本地/工作站侧跑大视觉模型（VLM、视频生成、3D 重建）的主力卡——涨价潮 8/11 已覆盖 RTX 50 系 +39%，本条是专业卡的具体落点：**本地视觉算力成本在加速恶化**
- **获取方式**: NVIDIA US Marketplace；云侧对应 RTX PRO 系列云实例同样水涨船高；预算敏感团队该认真考虑 Jetson/推理卡分流的性价比账

### 4. [CoreWeave 把 2020 年的 A100 签进 2029 年合同：老 GPU 的「九年后仍赚钱」经济学](https://www.tomshardware.com/tech-industry/coreweave-ceo-mike-intrator-says-it-has-signed-an-a100-contract-running-into-2029)
- **什么**: CoreWeave CEO Mike Intrator 确认已签 **A100 合约一直排到 2029 年**——发布近 9 年后，2020 年的老卡仍在产生利润
- **原因**: 电力约束与老旧基础设施决定了「算力分层」——推理、批处理、视觉数据管线这类**延迟不敏感负载**用老卡更划算，新卡留给训练与高价值推理
- **视觉关联**: 多模态/视频/机器人的「海量预处理 + 推理」负载正是 A100 长尾市场的基本盘；对从业者：**租算力别只看旗舰**，A100/A10G 等老卡在视觉批处理上性价比依然能打
- **判断**: 与 8/11「NVIDIA AI 工厂资产化」叙事闭环——GPU 寿命被拉到近 10 年，算力从「消耗品」变成「折旧资产」

## 🔩 芯片与半导体

### 5. [YMTC 首进全球 NAND 前三（14% 份额）：AI 服务器吃掉 48% 的闪存出货](https://www.tomshardware.com/tech-industry/ymtc-breaks-into-the-top-three-nand-makers-for-the-first-time)
- **动态**: Counterpoint 数据显示 2026 Q2 长江存储（YMTC）出货 **全球 14% 的 NAND**，首次进入前三、挤掉铠侠（Kioxia）；三星 25%、SK 海力士 22% 居前，美光居第五
- **关键数据**: 企业级 SSD 吸收了全球 **48% 的 NAND 比特**（一年前仅 26%）；行业收入同比增 **5 倍**；但按收入 YMTC 仍排第五——出货几乎全进消费产品，企业盘（KV cache、推理数据集）价格远高于消费盘
- **影响**: YMTC 自 2022 年 12 月被列入美国实体清单，无法进入西方服务器认证——**「产能前三、收入第五」的分裂**正是中国存储产业的现状写照；对视觉硬件：视频/图像数据集存储与模型 KV cache 的容量需求正是企业 SSD 暴涨的推手之一
- **判断**: 份额冲量靠消费盘，利润与生态卡在实体清单——观察点是 YMTC 能否拿到国产 AI 服务器（昇腾系）的 eSSD 订单来破局

### 6. [硅光成为 AI 下一个「热商品」：磷化铟短缺 + ST 在 300mm 晶圆上量硅光](https://www.tomshardware.com/tech-industry/photonics/how-optical-interconnects-and-silicon-photonics-emerged-as-ais-next-hot-commodity-looming-us-china-summit-puts-photonics-into-the-crosshairs) · [EETimes: AI 硬件下一站是「集成」](https://www.eetimes.com/ai-hardwares-next-frontier-is-integration/)
- **动态**: 光互连从「机架前端」走向「芯片级」——FCC 禁令（8/12 已报）后市场立刻反应：中国厂商中际旭创/新易盛/天孚通信股价大跌，**Coherent 涨 12.4%、Lumentum 涨 8.9%**；Marvell、NVIDIA 正在光模块公司上砸下数十亿美元收购；关键材料 **磷化铟（InP）被点名短缺**
- **技术纵深**: EETimes LID World Summit 2026 报道——**STMicroelectronics 正把硅光量产推上 300mm 晶圆**；CEA-Leti、Scintil Photonics、NcodiN 分别做 CPO 多波长激光源与面向 **photonic interposer** 的纳米激光器——光连接正从机架走向 advanced packaging 内部（chiplets 之间）
- **视觉关联**: AI 训练集群（视频/多模态）的 scale-out 带宽就是光模块需求基本盘；CPO 若成熟，边缘/车载芯片内部互连也会跟着变
- **判断**: 从「电互连」到「光互连进封装」是 3D-IC 之后的下一波架构红利；InP 短缺 + 中美政策风险 = 光互连供应链将重演 GPU 剧本

### 7. [Meta 用 CXL 把退役 DDR4 接回新服务器：服务器数量砍 25%](https://www.eetimes.com/meta-cuts-server-count-25-by-reusing-old-memory-can-anyone-else-do-it/)
- **动态**: Meta 在**数百万台服务器**上部署 CXL 内存扩展，把退役机器拆下的 **DDR4 模块放在 CXL 控制器后面**继续服役（论文 Vistara 上月公开），宣称可**减少 25% 的服务器数量**并降低运营成本
- **底层逻辑**: 服务器 4–5 年一换代，而 DDR4 内存寿命 10–12 年——换代时内存还有约一半寿命，与其报废不如通过 CXL 续命；Marvell 存储/内存产品线 VP 确认「超大规模厂商普遍在做」
- **视觉关联**: 内存墙是视觉大模型（KV cache、多模态推理）的核心瓶颈；「内存复用 + CXL 池化」让数据中心内存总容量显著变多，等效于**同样的 GPU 能装更大的模型**
- **判断**: 这不是小聪明而是行业级省钱运动——CXL 从「纸上标准」变成「千万台级部署」，对内存控制器/Retimer 芯片厂商（Marvell、澜起等）是直接利好

## 📦 开源硬件与工具

### 8. [cactus-compute/needle：14MB 的端侧基础模型——给手机/可穿戴/机器人用的「迷你脑」](https://github.com/cactus-compute/needle)
- **功能**: 主打 **14MB** 的 on-device 基础模型（MIT 协议，Python），面向手机、可穿戴、智能家居与机器人；GitHub 今日 trending（★4.3k，2026-08-12 仍有更新）
- **上手**: `pip install` 即可在本地跑；作者称是「14MB foundation model for tiny devices」
- **视觉关联**: 虽不是视觉模型本身，但这类「MB 级模型 + MCU/低功耗 NPU 可部署」的趋势，正是边缘视觉硬件（瑞芯微 RK 系列、ESP32-S3、Jetson Nano 级设备）最缺的模型供给；与 8/12 的 DA3-SMALL/RMBG-ONNX 是同一叙事：**端侧算力在等模型变小**
- **判断**: 观察即可——14MB 能否保真存疑，但它代表了「模型体积内卷」的新水位线

### 9. [GitHub 周扫描：事件相机/嵌入式视觉新仓库整体低信号，亮点是 ECCV 2026 官方代码](https://github.com/search?q=event+camera+created%3A%3E2026-08-06&s=stars&type=repositories)
- **功能**: 本周新建仓库里几乎没有高星视觉硬件项目——event camera 搜索下值得看的是 ECCV 2026 官方代码 **"Static in Frames, Dynamic in Events: Rethinking Features in Event Cameras as Motion Cues"**（事件相机特征即运动线索，重构了事件特征表达）；另有浏览器版 DVS 像素模拟器 Neuromorphic-Webcam（纯学习向）
- **上手**: 前者是学术复现入口，后者直接在浏览器看 DVS 事件流效果
- **判断**: 趋势面：事件相机生态仍以学术为主，工程化产品化（对标 Prophesee/索尼 IMX636 商用生态）尚未在开源社区形成气候；持续观察即

## 📰 产业动态

### 10. [AI 数据中心开发商开始起诉地方政府：500+ 禁令后的法律反击战开打](https://www.tomshardware.com/tech-industry/data-centers/ai-data-center-developers-begin-suing-local-jurisdictions-behind-bans-and-moratoriums-claims-range-from-officials-exceeding-authority-to-violations-of-due-process-and-equal-protection-laws)
- **核心内容**: 8/12 报道的「全美 500+ 数据中心禁令」迎来反转——开发商开始起诉颁布禁令/暂停令的地方政府，理由从「官员越权」到「违反正当程序与平等保护」
- **影响**: 这是 8/12「禁令突破 500 项」的必然续集：算力需求侧资本不会默默退场，法律战会把「机房能不能建」的争议拖入数年诉讼周期；对视觉硬件：数据中心供给的不确定性继续强化**边缘端算力**（Jetson、端侧 NPU、机器人芯片）的替代叙事，也抬高了对「确定性交付」的定制硬件需求
