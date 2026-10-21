# ⚙️ 2026-10-21 视觉硬件日报

> 扫描 10 渠道（NVIDIA · EETimes · SemiEngineering · Tom's Hardware · SemiAnalysis · Sony · OmniVision · Mobileye · Samsung · GitHub），精选 7 条 + 快讯
> 窗口 10-15 ~ 10-21 | 主线：**边缘视觉「内存优先」重构**、**Vera Rubin 从产线走向机房**、**存储周期挤压 BOM**
> 注：Sony 最新 9/07、OmniVision 9/21、CIS 新品静默；Reddit 403、SemiAnalysis feed 停更于 2025-09；GitHub 事件相机均低星仓库

---

## 🎥 边缘视觉芯片

### 1. [Synaptics Astra SR200：把「HBM 式」内存搬进 MCU，单芯 400 GOPS 跑视觉 Transformer](https://www.eetimes.com/edge-ai-mcu-features-multimodal-compute-tiered-memory/)
- **什么**: 号称业界首个 **Cortex-M85 + Cortex-M52** 组合的 "xMCU"，集 **Torq NPU + Google Research Coral NPU**，同时吃 CNN 与 Transformer
- **规格**: **SR210 200 GOPS**（纯语音）/ **SR230 300 GOPS**（+视觉+显示）/ **SR250 400 GOPS**（双视觉通路）· **256MB in-package 定制 DRAM**（分层存储，HBM-like 思路）· 硬件信任根
- **视觉关联**: 常开穿戴、联网相机、工业视觉；官方称最大客户来自**人体佩戴设备**
- **判断**: 关键不是 TOPS 而是**先解决喂数据**——DRAM 做到几百 MB，等于承认端侧视觉瓶颈是内存带宽而非 MAC 数；三档 pin-compatible 让同一 PCB 从语音升到双路视觉

## 🖥️ GPU 与算力

### 2. [GTC Berlin：Vera Rubin 全面量产，DSX POD 把机房部署从 6 个月压到 14 天](https://blogs.nvidia.com/blog/gtc-berlin-2026-keynote/)
- **什么**: **Vera Rubin 进入 full production**；推出 **DSX POD**——合作伙伴在集装箱内完成整机集成与验证后再交付
- **参数**: 现场部署 **6 个月 → 14 天** · DSX 宣称**冷却用水最多降 100%、同算力省电 30%**
- **视觉关联**: 视频/VLM 训练与 RL 推理的底座；对视觉团队的意义是**算力采购单位从「卡」变成「箱」**
- **判断**: 竞争维度已从芯片移到**「供电+液冷+交付速度」**；把集成搬到工厂，是在复制台积电「turnkey」逻辑

### 3. [NVIDIA 车规与医疗视觉双线落地：Hyperion 拿下 Volvo/VW/JLR/奔驰，IGX Thor 进放疗闭环](https://blogs.nvidia.com/blog/gtc-berlin-2026-keynote/)
- **什么**: **Hyperion** 被 Volvo（配 Alpamayo 栈）、VW 商用车、JLR、奔驰下一代车型采用
- **医疗**: 与 Siemens Healthineers 做**自适应放疗**——**Holoscan + IGX Thor** 实时接影像与传感器，边照射边跟踪肿瘤位移
- **视觉关联**: 前者是车端多相机/激光雷达融合平台，后者是**实时分割 + 毫秒级闭环控制**的极端案例
- **判断**: 同一套 Blackwell 边缘栈同时吃车规与手术室，**「确定性延迟」正成为 NVIDIA 边缘叙事的核心指标**

### 4. [Google Cloud A5X 开放 GA：Vera Rubin NVL72 + ConnectX-9，规划最多 96 万颗 Rubin GPU](https://blogs.nvidia.com/blog/google-cloud-vera-rubin-infrastructure/)
- **什么**: A5X 下月 GA，整合 **Vera Rubin NVL72、ConnectX-9 SuperNIC、Virgo 网络、四代液冷**
- **参数**: 多站点合计规划至 **960,000 颗 Rubin GPU**；首批客户 Ineffable Intelligence（David Silver 创办，做持续学习 RL）
- **判断**: WPP 称过去需多节点集群的视频生成/超分工作流**单实例即可跑完**——对视觉生成类负载这是实用的容量信号

### 5. [中国大厂下单 3M 颗 RTX Pro 5500：$35B 订单，NVIDIA 只能交付 5–10%](https://www.tomshardware.com/pc-components/gpus/chinas-tech-giants-drop-usd35-billion-on-export-compliant-nvidia-rtx-pro-5500-workstation-gpu-orders-to-power-ai-ambitions-according-to-reports-bytedance-alibaba-and-tencent-order-3-million-cards-despite-warnings-that-only-10-percent-of-orders-are-fulfillable)
- **什么**: 字节、阿里、腾讯合计下单 **>300 万颗** RTX Pro 5500（合规型号），单价约 **$11,400**
- **参数**: **GB202 同款 CUDA 核数 + 84GB GDDR7**；NVIDIA 2027 年全球产能约 300 万颗，**订单已吃掉整年产能**
- **视觉关联**: 国内视觉大模型/标注/仿真训练最现实的算力来源；缺口意味着**GPU 租赁价格继续上行**

## 🔩 芯片与半导体

### 6. [存储超级周期压向边缘 BOM：Micron 桃园 10/22 罢工，三星/海力士在华厂升级 NAND](https://www.tomshardware.com/pc-components/dram/microns-taiwan-union-will-launch-a-one-day-strike-this-week-threatening-round-the-clock-fab-operations-workers-demand-concrete-terms-for-2026-bonus-and-clearer-profit-sharing-arrangements)
- **动态**: Micron 桃园厂（产 DDR5/LPDDR）10/22 一日停工，台中厂同日劳资调解；三星西安（占其 NAND 产量约 40%）年内切 **286 层 V9**，SK 海力士大连 **192 → 240 层**
- **背景**: CXMT 2026 H1 营收 **$22.41B**、净利 **$11.57B**；YMTC 称 2027 年底做到 NAND 全球第一
- **影响**: AI 数据中心挤占消费级产能 → **相机模组、边缘盒子、开发板的 LPDDR/eMMC 报价继续上探**；选型应优先看**单板内存天花板**

### 7. [Arteris：Physical AI 的真问题是「数据搬多少次」，一致性互连给 CPU、非一致性给加速器](https://semiengineering.com/scaling-data-movement-for-physical-ai/)
- **动态**: Arteris 拆解机器人/自驾 SoC 互连取舍：CPU 用 coherent、AI 加速器用 non-coherent，核心指标是**每帧数据被搬运的次数**
- **影响**: 与 SR200 的「堆内存」互为镜像——**端侧视觉 SoC 的架构分歧已经清晰：要么把内存搬到片上，要么把数据流焊死在互连上**

---

## 📰 快讯

- **DGX Spark 64GB 版 10/23 开售**，ConnectX-7 + Sync 支持 8 台组簇；DGX Station Windows 版 12 月到（[链接](https://blogs.nvidia.com/blog/local-ai-gtc-rtx-dgx-spark-station-sync/)）
- **TSMC 高雄 2nm 建厂工地坠落事故致 3 死 1 重伤**（疑似钢构连接板螺栓断裂），先进制程扩产的安全与工期风险抬头（[链接](https://www.tomshardware.com/tech-industry/semiconductors/three-workers-killed-one-in-intensive-care-after-fall-at-tsmcs-2nm-fab-construction-site-in-kaohsiung-broken-bolt-on-a-steel-connection-plate-suspected-as-cause-behind-tragic-accident)）
- **Qualcomm 对 Arm 关键诉求胜诉，但赔偿仅 $2**——架构授权之争未完，Arm 自研芯片路线仍受压（[链接](https://www.eetimes.com/qualcomm-wins-key-claims-against-arm-but-damages-total-just-2/)）
- **AMD/Intel 合并 CPU 推理栈**：ZenDNN 并入 oneDNN，统一 PyTorch CPU 后端——无 GPU 的视觉推理部署少一道适配（[链接](https://www.tomshardware.com/pc-components/cpus/amd-and-intel-will-work-together-to-create-a-single-pytorch-code-path-for-ai-inference-on-cpus-amd-zendnn-library-gets-folded-into-intel-onednn-to-make-cpu-ai-simpler)）

---

*📅 每日更新 · 硬件层追踪*
