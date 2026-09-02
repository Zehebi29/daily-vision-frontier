# ⚙️ 2026-09-02 视觉硬件日报

> 今日扫描 12 渠道（NVIDIA · EETimes·Asia · SemiEngineering · Tom's Hardware · Sony · GitHub · Google News 中/英 等），精选 7 条
> 主线：**CIS 供应链锁定先进制程**（Sony×TSMC JV）、**NVIDIA Vera CPU 出货**、**昇腾 950 十亿级订单**、**比亚迪自研 4D 雷达芯片量产**、端侧 AI「Microduck 现象」
> 注: 不重复 8/26（910C 缺货、征程6B 德系定点、瑞芯微 H1）；Reddit 连续第六日 403；Sony/OmniVision 本周无新品但有大动作

---

## 🎥 传感器与采集

### 1. [Sony×TSMC 就图像传感器合资公司签署最终协议（熊本·2029 量产）](https://www.sony-semicon.com/en/news/2026/2026081101.html)
- **什么**: 「Advanced Vision Semiconductor Manufacturing」JV 落地熊本县合志市——面向**智能手机图像传感器**的先进制程制造基地（[EETimes Asia 9/1 解读：AI/机器人需求拉动供应链强化](https://www.eetasia.com/sony-tsmc-venture-strengthens-image-sensor-supply-chain-amid-rising-ai-robotics-demand/)）
- **亮点**: Sony 注资约 4650 亿日元（含既有 fab 作价）+ TSMC 约 2820 亿日元；Sony 控股并表，2029 量产，寻求日政府补贴
- **视觉关联**: 手机 CIS 首次系统性地锁定先进制程逻辑产能——堆栈式/背照传感器走向更复杂晶圆级工艺
- **判断**: TSMC 从逻辑代工切入 CIS 代工——「索尼设计+台积电制造」对抗三星与国产 CIS 产能竞赛

### 2. [比亚迪自研 4D 毫米波雷达芯片量产：覆盖 L2-L4、泊车精度 0.05m](https://news.google.com/rss/articles/CBMiTEFVX3lxTE1EZmc4QzdEbmExOEYzTzFXNkRCbFk3Nkh6T1FSWkU0bDA2dW9NeW1MOHpwZlBaREgxUzBlcF8wdE9LekQ3eGpIUVhtNlo?oc=5)
- **什么**: 4D 成像雷达 SoC 上车（璇玑 A3 平台），垂直整合「雷达芯片→域控」全链路
- **亮点**: 俯仰/水平分辨率提升，泊车精度 0.05m；同期王传福预告自研 4nm 智驾 SoC「难度相当于 2nm 消费级芯片」
- **视觉关联**: 4D 雷达是 BEV+Transformer 融合感知中摄像头的关键互补传感器——自研芯片卡位融合入口
- **判断**: 「摄像头+4D 雷达」无激光雷达路线成本再降，2027 主流智驾传感器组合风向标；看点：车规量产良率

## 🖥️ GPU 与算力

### 3. [NVIDIA Vera CPU 开始规模出货：AWS 收到首台「Vera CPU + Vera Rubin GPU」服务器](https://blogs.nvidia.com/blog/vera-cpu-delivery/)
- **什么**: NVIDIA 首款自研 CPU（8/27 更新）进入交付期——AWS/OCI/Anthropic/OpenAI/SpaceXAI 均已收货；AWS 同步宣布追加 200 万颗 GPU
- **性能**: 88 核自研 Olympus、1.2TB/s 带宽、agent 负载每核 +1.8x；CPU 扛编排/工具调用/长上下文检索
- **视觉关联**: 多模态 Agent（视频/具身）推理不止 GPU——Vera 解 agent 化的 CPU 瓶颈，推理成本续降
- **对比**: 延续 8/26 Rubin NVL72 叙事；这次是 CPU 交付里程碑，2026H2 云实例逐步上线

### 4. [华为昇腾 950 获超 10 亿元订单：范式智能采购，国产算力进入头部 AI 企业生产环境](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBDcmtWNTJrU1g2Q3UtaEg5VEl6M1Ntd2lpc2R5SDc5Tk5lOThtYlBSTmphNE9qQ3FfMXJBTFVmZEVGd0RMemJSRzVUeG5vYTRkWERSTFFScmJ?oc=5)
- **什么**: AI 公司范式智能与华为签下超 10 亿元昇腾 950 采购大单——昇腾新一代旗舰从「评测」走向「生产」
- **亮点**: 多家头部模型公司被传跟进；国产算力叙事从「910C 供不应求」切换到「950 放量预期」
- **视觉关联**: 视频/多模态大模型训练推理迁往国产集群，直接检验 CUDA 替代生态（MindSpore/CANN）成熟度
- **判断**: 瓶颈仍在 HBM 与产能而非订单——昇腾能否兑现交付是 2026H2 国产算力最关键变量

## 📦 开源硬件与工具

### 5. [Microchip PolarFire Ethernet Sensor Bridge 2.0：边缘视觉「传感器桥」缩小 60%、支持 4 路相机](https://www.eetasia.com/microchip-shrinks-polarfire-ethernet-sensor-bridge-for-edge-ai-systems/)
- **功能**: NVIDIA Holoscan Sensor Bridge 兼容开发板——用 10GbE 统一「传感器→AI 主机」连接，替代私有接口拼装
- **规格**: 支持 SLVS-EC 2.0/12G-SDI/HDMI/DisplayPort 输入，MIPI CSI-2 + FMC 扩展；板载光延迟测量电路（配 NVIDIA Latency Display Analysis Tool）；USB-C 供电
- **视觉关联**: 面向 Jetson/Holoscan 生态，场景含医疗 AI、工业自动化、人形机器人感知
- **判断**: 边缘视觉卡在传感器接线长尾——标准化 bridge 直击痛点，是 Jetson 开发者的低成本相机前端

## 📰 产业动态

### 6. [Hugging Face「Microduck」$399 AI 鸭机器人爆卖万台，搭载瑞芯微芯片](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQNFlNYzhkNWgxVkZkVGYzMzVsdVVOU1NVZmZ1VWY3QUhGLTNPaGVXMFd4U1pFU2tEQ012UFN4Tk9CNnMzMkxCdTBzdThVYm5FZ?oc=5)
- **什么**: HF 桌面机器人（会滑冰/捡袜子）数日售出 10,000+ 台（峰值约 4 秒/台），主控为**瑞芯微 ARM SoC**（[华尔街见闻](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1qcWRvU1JYTDIyYXZKRk0wcFJxTlo2OHlVZEFMVl9GQW5IcGNxeHY1Nkc3ZExjbkJhQ2tHTVdLZTJyYURNMGVfOUxrZWFPRks2M3JZ?oc=5)）
- **影响**: 瑞芯微涨停、市值破 860 亿——端侧 AI 行情从「机器狗/开发板」转向**消费级小机器人**（视觉+语音+运动控制）
- **判断**: 「开源生态 × 国产 SoC」组合验证端侧视觉硬件进入消费放量期——与 8/26 瑞芯微 H1 财报（+40.6%）互相印证

### 7. [地平线 2026 H1：营收 20.55 亿（+33%），征程 6M 大规模量产上车、城区 NOA 下探 10 万元级](https://news.google.com/rss/articles/CBMif0FVX3lxTE9nUVpLaEE1S1VETFBNTUZIbHBDNk1aaVM1Z2Q1NVFsYlBMUmJoQ3NVYlVyeW9rbTZoZFVsWWZFTEZQdjBDenN5S1BKQVlLRzhvTWxINHpnU09?oc=5)
- **什么**: 征程系列出货 222 万套；6M（中端走量款）随长安启源 Q05 大规模量产，城区 NOA 首次进入 10 万元级市场（另有领克 20 用征程 6+LiDAR 128 TOPS 方案）
- **亮点**: 官方口径智驾芯片「全阶第一、高阶第二」；与 6B 的德系定点（8/26）形成「出海+下沉」双线
- **判断**: 中端档放量决定国产智驾芯片规模经济——6M 是 2026H2 观察哨，看点在交付与毛利而非订单数

---

*数据窗口 2026-08-27 ~ 09-02 · 渠道: NVIDIA / EETimes（America·Asia）/ SemiEngineering / Tom's Hardware / Sony / SemiAnalysis（停更）/ Hackaday / GitHub / Reddit（403 第 6 日）/ HuggingFace · 备查: SemiEngineering 关注边缘感知 fault-injection 功能安全与 imec CFET 路线图；EETimes 特写印度 HrdWyr physical-world AI SoC（规格未披露，仅记录）*
