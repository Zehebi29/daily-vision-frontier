# ⚙️ 2026-09-30 视觉硬件日报

> 扫描 9 渠道（CNX Software · Tom's Hardware · SemiEngineering · EETimes · NVIDIA · Sony Semicon · GitHub · Reddit · SemiAnalysis），精选 6 条 + 快讯
> 窗口 09-24 ~ 09-30 | 主线：**AMD 把世界模型团队买进芯片公司**、**边缘端 GPU/AI-ISP 追着视觉负载走**、**热成像下放到 MCU**
> 注：Reddit 403/429、SemiAnalysis feed 403、GitHub trending 空、EETimes 正文多次超时（Calterah 条目仅据标题）；Sony Semicon 最新仍为 9/7 Aramco MoU，本周无新品

---

## 🎥 传感器与采集

### 1. [8devices 8Sight T100：Lynred LWIR 热成像 + STM32N6 NPU，38 克整机离线跑检测](https://www.cnx-software.com/2026/09/25/compact-long-wave-infrared-camera-pairs-stm32n6-mcu-with-lynred-ati320-thermal-sensor/)
- **什么**: 无人机/机器人用长波红外相机——Lynred **ATI320** 非制冷热传感器 + ST **STM32N657X0**（Cortex-M55 @800MHz）
- **规格**: **320×240 @60fps**，8–14µm，NETD **50mK**；NPU **600 GOPS** + 硬件 ISP；处理 <50ms、推理 <100ms；32MB RAM，**28.5×30.5×29.5mm / 38g**，NDAA+TAA 合规
- **视觉关联**: 夜航、工业异常检测、温度触发事件；USB2.0 出 **RAW8/RAW16**，可做原始热数据算法研究
- **判断**: 信号是**热成像不再等于「热像仪」**——MCU 级 NPU 就能在 1W 级功耗上跑热域目标检测；扣分项是官方未公开 SDK/模型部署流程

## 🖥️ GPU 与算力

### 2. [AMD 82 亿美元收购 World Labs，Fei-Fei Li 出任首席科学家](https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-acquires-ai-legend-fei-fei-lis-world-labs-for-usd8-2-billion-imagenet-pioneer-will-become-amd-chief-scientist-as-the-chipmaker-brings-her-lab-in-house)
- **什么**: 全股票交易，World Labs（空间智能/3D 世界模型，产品 Marble）并入 AMD；Li 任 EVP & Chief Scientist，直接汇报 Lisa Su
- **细节**: World Labs 曾用 **Instinct + ROCm** 做训练/推理调优（CES 上由 Li 确认），AMD 2 月已投其 $1B 轮，NVIDIA 同在该轮
- **判断**: AMD 史上第二大收购（仅次于 $50B 的 Xilinx）——**买的是"模型往哪走"的先验，不是产品线**。Li 明说"World Labs 需要离硬件更近"，等价于把**世界模型算力需求写进 Instinct 路线图**

### 3. [Imagination E-Series GPU IP：单核 32 TOPS INT8，图形与 AI 并发](https://semiengineering.com/e-series-gpu-ip-the-first-step-towards-converged-acceleration/)
- **什么**: 面向边缘 SoC 的 GPU IP——图形/计算/AI 融合架构 + 单一可编程软件栈，2025 发布，**首批硅片预计 2026 年底**
- **性能**: 单核 **32 TOPS INT8 @1GHz**，为 D-Series 的 **4×**；图形与 AI **同时运行**，可作 NPU 峰值时的协处理器
- **视觉关联**: 边缘 neural rendering、AR 眼镜、车机、机器人等 UI+感知共存设备
- **判断**: **"GPU 兼做 NPU"从省成本方案变成正式产品叙事**，对固定 NPU 路线的压力在于模型算子演进速度；32 TOPS 是否兑现要等 2026 年底硅片，别被 IP 白皮书数字带走

### 4. [Quectel SE200ZC-AP：40×40mm 模块，RV1126B + 3 TOPS，接 5 路 12MP 相机](https://www.cnx-software.com/2026/09/24/quectel-se200zc-ap-smart-module-supports-up-to-five-cameras-with-rockchip-rv1126b-bj-soc/)
- **什么**: 智能视觉模组——Rockchip **RV1126B/RV1126BJ** 四核 A53（1.6GHz/工业 1.3GHz）
- **规格**: **12MP ISP + 8MP AI-ISP + 3 TOPS NPU**（INT4/8/16/FP16）；**2×4-lane MIPI CSI + DVP = 最多 5 路 12MP@30fps**；LPDDR4x 1/2/4GB + 64GB eMMC；H.265 4K；2× CAN FD、GMAC、USB3.0；**-35~+80℃**
- **视觉关联**: 安防多目、机器人视觉、AGV（CAN FD 直连底盘）
- **判断**: **"AI-ISP 独立于 NPU"是最关键的一行**——去噪/HDR 交给专用硬件后，3 TOPS 才真正留给感知模型；国产 ISP+NPU 已进入可量产形态，代价是 3 TOPS 上限卡死大模型侧

## 🔩 芯片与半导体

### 5. [TSMC OIP：行业直冲 1.7 万亿美元，AI 独占 >1T；Jalapeño ASIC 九个月流片](https://semiengineering.com/tsmc-oip-chip-industry-growth-blows-past-forecast/)
- **动态**: TSMC 北美 CEO 称行业 2026 年底达 **~$1.7T**（AI 部分 >$1T）——2024 年"2030 年破 $1T"的预测被**低估约 $700B**；8 月营收同比 **+53.3%**
- **技术读数**: N5/N3/N2 新 tape-out 数增 **4×**；A14 Nanoflex 单元高度 1.5×（前代 2×），vs N2P **+14% 速度 / −23% 功耗**；五年内 **HBM 带宽 34×、3D DRAM 115×、SRAM 830×**；Broadcom 称 OpenAI **Jalapeño ASIC 从 kickoff 到 tape-out 仅 9 个月**
- **影响**: 视觉大模型推理的**真瓶颈是显存带宽（HBM 34×）而非 FLOPS**；9 个月流片意味着专用视觉 ASIC 的进入成本快速塌陷——既是机会也是同质化风险

## 📦 开源硬件与工具

### 6. [OpenArm 2.0：开源 7-DOF 机械臂，QDD 关节 + 手内相机 + 双侧力反馈](https://www.cnx-software.com/2026/09/30/openarm-2-0-an-open-source-7-dof-robot-arm-with-qdd-joints-bilateral-force-feedback-in-hand-camera/)
- **什么**: 东京 Enactic 发布的开源硬件机械臂，面向 physical AI 研究、遥操作与接触密集型数据采集
- **规格**: 7 轴 + 平行夹爪（8 执行器，达妙电机），额定 4.1kg / 峰值 6kg，臂展 606mm，**CAN-FD 1kHz 控制环**，爪行程 88mm，**爪内相机 + 可换指尖**
- **上手**: 开源 CAD/BOM/固件 + **ROS 2 / MuJoCo / Isaac Lab** + 数据集工具，主机 Linux SocketCAN
- **判断**: 价值在**力反馈可回驱（backdrivable）**——模仿学习最缺的是接触力真值，而多数低成本臂只有位置控制；`Isaac Lab + 真机`双栈可直连 sim-to-real，是视觉-触觉多模态数据集的现成基座

---

## 📰 产业动态

- **车舱感知**: [Calterah 把 UWB 数字钥匙改造成舱内传感器](https://www.eetimes.com/calterah-turns-uwb-digital-keys-into-in-cabin-sensors/)——UWB 从"开门"转向"看人/看座"，是活体检测与安全带检测的低成本路线（**正文多次超时，仅据标题**）
- **内存墙**: [Astera Labs 更新 Leo 控制器针对内存瓶颈](https://www.eetimes.com/astera-labs-leo-controller-update-targets-memory-constraints/)；[Xcena 以削减数据搬运应对内存墙](https://www.eetimes.com/xcena-cuts-data-movement-to-address-memory-bottlenecks/)——与 TSMC 的 HBM/3D DRAM 读数同向
- **大厂静默**: Sony Semiconductor 9 月起无新品，最新仍为 **9/7 Aramco MoU**；关键看 5/8 与 TSMC 的**下一代图像传感器合资**进展
- **算力资本**: NVIDIA 追加 **$1500 亿**回购授权（余 $2350 亿）；另据 Tom's Hardware，NVIDIA 本月初以 **$129.3 亿**收购 Hugging Face——开源模型分发口正被算力厂商收编

---

*渠道: CNX Software / Tom's Hardware / SemiEngineering / EETimes / NVIDIA Newsroom / Sony Semicon / GitHub / Reddit / SemiAnalysis · 失败源: Reddit 403·429、SemiAnalysis 403、GitHub trending 空、EETimes 正文超时*
