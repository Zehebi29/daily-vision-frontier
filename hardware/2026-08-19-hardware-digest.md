# ⚙️ 2026-08-19 视觉硬件日报

> 今日扫描了 SemiAnalysis · EETimes · SemiEngineering · Tom's Hardware · NVIDIA Blog · Sony Semiconductor · EET Asia · Hackaday · GitHub · HuggingFace · Reddit · Google News(国产芯片) 等 12 个渠道，精选 8 条
> ⚠️ Reddit 第四日 403 限流；Sony/OmniVision/Prophesee 无新品（静默期第四周）
> 注: 不重复 8/17（TPU v10、Maia 300、Jetson、TIER IV）已覆盖内容；主线是 **H200 对华首批到货**、**地平线征程6B 千万套定点**、**ABF 膜对华断供**

---

## 🎥 传感器与采集

### 1. [Comcast 把 Xfinity 路由器变成「无摄像头」运动探测器](https://www.tomshardware.com/networking/routers/comcast-turns-xfinity-routers-into-home-motion-detectors-free-wi-fi-sensing-feature-tracks-rf-interference-with-zero-extra-hardware-required)
- **什么**: 消费级 Wi-Fi sensing 首次大规模落地——用路由器 RF 信号做室内运动检测
- **亮点**: 追踪人体 RF 反射/干扰，无需摄像头与新增硬件，存量设备直接升级
- **视觉关联**: 与毫米波雷达、事件相机同属「非 RGB 感知」；安防/老人照护的 camera-free 选项
- **判断**: 对比 vs 摄像头方案在遮挡/多目标场景的准确率，决定它是补充还是替代

## 🖥️ GPU 与算力

### 2. [首批 NVIDIA H200 运抵中国：字节、腾讯收货，北京松绑进口限制](https://www.tomshardware.com/pc-components/gpus/first-nvidia-h200-shipments-reach-bytedance-and-tencent-as-beijing-loosens-its-import-block)
- **什么**: H200（141GB HBM3e / 4.8TB/s）首次对华出货，字节/腾讯已收货
- **亮点**: 限制仍在——许可芯片大多须留在香港，而香港缺乏供电与机房落地能力
- **视觉关联**: 国内多模态/视频训练集群「缺卡」局部缓解，算力落地仍受物理约束
- **判断**: 中美算力脱钩局部松动信号；真假待官方确认，但方向值得跟踪

### 3. [SemiEngineering 圆桌：AI 算力的未来不只靠一种芯片——异构集群成 2027 标配](https://semiengineering.com/the-future-of-ai-compute-wont-run-on-just-one-kind-of-chip/)
- **什么**: Arm/Cadence/Siemens/Synopsys/Expedera 专家圆桌——数据中心转向 CPU+GPU+NPU+光互连异构
- **亮点**: 内存（HBM 成本/带宽）成为关键瓶颈；软件编排决定异构利用率
- **视觉关联**: 与 8/17 TPU v10「on-package CPU」同频——视觉推理集群选型应从「只看 TOPS」转向「CPU:加速器 配比」
- **判断**: 趋势确认，纯 GPU 单一种类时代结束；对算力采购是中期架构变量

## 🔩 芯片与半导体

### 4. [味之素对华削减 30% ABF 载板膜供应，国产替代加速认证](https://www.tomshardware.com/tech-industry/semiconductors/ajinomoto-reportedly-cuts-abf-chip-packaging-film-supply-to-china-by-30-percent)
- **动态**: ABF（先进封装载板关键膜材，味之素全球垄断）对华减供 30%，紧随中国稀土出口管制
- **影响**: ABF 直接卡 AI 芯片/HBM/国产 GPU 的先进封装——「互相卡脖子」升级到材料层
- **判断**: 国产 ABF 替代（生益/华正等）进入认证窗口；国产智驾芯片封装成本与交期成新变量

### 5. [三星晶圆厂路线图剖析：Taylor/Pyeongtaek 良率困境与 $16.5B 特斯拉大单](https://www.tomshardware.com/tech-industry/samsungs-fab-roadmap-examined)
- **动态**: 2nm 良率承压背景下三星拿下特斯拉 $16.5B 订单；美国 Taylor 厂爬坡与 Pyeongtaek 是焦点
- **影响**: 代工格局（TSMC 独大 vs 三星/Intel 追赶）直接影响 AI 芯片与车规视觉 SoC 的流片选择
- **判断**: 若 Taylor 2nm 良率持续不振，特斯拉订单落地节奏受考验——车规视觉芯片流片需盯三星 2027 产能

## 🇨🇳 国产芯片

### 6. [博世基于地平线征程 6B 的 MPC4 获千万套量产定点，覆盖 25+ 车企](https://news.google.com/rss/articles/CBMiYkFVX3lxTE1sVklXX2x4dkZYa3FCd2FxMlZXbl9mdGM0Tm9sVllhYi1JZjRUVzdtb1NyMFJ0cGg5bXlZWV9jVXdpNWJnZzdKaXdUSXNoRUJYd2xiNVR5dV82NHNLZ2g2RTR3?oc=5)
- **什么**: 博世 MPC4（基于征程 6B 平台）获千万套级量产定点，覆盖超 25 家车企——Tier1 级别绑定量产
- **亮点**: 征程 6B 是 6 系中端（~10 TOPS 级）——「B 端放量」比 8/17 CEO 的 J7 放话更实
- **判断**: 地平线从「定点」走向「放量」，国产智驾芯片拐点确认；对智驾视觉供应链是产能/成本利好

### 7. [黑芝麻智能打入美的机器人供应链；宇树科技科创板上市首日高开 630%、市值超 4400 亿](https://news.google.com/rss/articles/CBMihAFBVV95cUxPdE5qSTJCV3ZRTTJHV3dUbWVEcVdtNDNzSmJzck91OVREN1BqVnp0SUtQc0dZZzdSRWl6MER3VGJyTzVEWjZJcmFUZjF2bU1xNEViSjRzLXhuMmZwcEtrTzdMaG5ULW9LOFprSkl3bGp1MGtqOGRjdkc5bnNPU1RGRlFsLXA?oc=5)
- **什么**: 黑芝麻与美的旗下美创希签芯片供应商框架协议；宇树 8/18-19 登陆科创板成「人形机器人第一股」
- **视觉关联**: 黑芝麻 SesameX（C1200 系）面向具身智能感知；宇树 IPO 标志机器人视觉硬件进入资本兑现期
- **判断**: 「智驾芯片转型具身」+「机器人公司上市」双信号——具身智能硬件热度 2026H2 持续升温

## 📦 开源硬件与工具

### 8. [zynq-yolov3-tiny-accelerator：Zynq-7000 上的 INT8 YOLOv3-Tiny 加速器（99★）](https://github.com/a2307588073-arch/zynq-yolov3-tiny-accelerator)
- **功能**: Verilog 实现 INT8 单类 YOLOv3-Tiny 加速器 + OV5640 相机→HDMI 裸机 demo，含 PyTorch 训练与参数导出工具
- **上手**: Zynq-7000 XC7Z100 板卡可复现，FPGA 视觉加速入门完整参考
- **视觉关联**: 「相机直连→FPGA 检测→显示」全链路开源，是边缘 FPGA 感知的低成本范本

---

*数据窗口 2026-08-18 ~ 08-19 · 来源: SemiAnalysis（停更）/ EETimes / SemiEngineering / Tom's Hardware / NVIDIA Blog / Sony（无新品）/ EET Asia / Hackaday / GitHub / HuggingFace / Reddit（403）/ Google News(国产芯片)*
