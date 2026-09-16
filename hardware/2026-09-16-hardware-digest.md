# ⚙️ 2026-09-16 视觉硬件日报

> 扫描 12 渠道，精选 7 条 + 快讯 | 窗口 09-10 ~ 09-16
> 主线：**边缘视觉模组密集上新**（CVITEK / STM32N6 / Cortex-A320）、**84GB GDDR7 工作站卡补位**、**内存荒从涨价升级为「重新设计产品」**
> 注: Sony 本周无新品（9/7 Aramco MoU 已报）；OmniVision 被 Cloudflare 拦截；SemiAnalysis feed 停 2025-09；Reddit 403 第 8 日

---

## 🎥 传感器与采集

### 1. [AIMORELOGY Ovis：开源 AI 视觉相机模组，CVITEK CV1842H-P + AI-ISP 全彩夜视](https://www.cnx-software.com/2026/09/16/cvitek-cv1842h-p-based-edge-ai-camera-module-offers-night-vision-and-ai-isp-support/)
- **什么**: 众筹开源模组——20×20mm 堆叠 Core board（SoC+2Gbit NAND）+ SC235HAI 传感器板（带以太网/UART）
- **规格**: CV1842H-P = 1×A53@1.1GHz + 1×RISC-V C906@800MHz + **1.5 TOPS INT8（含 BF16）**；**AI-ISP 实时 1080p 全彩夜视**
- **判断**: 算力属轻量档，胜在 **AI-ISP 把 ISP 与 NPU 联合调优**（暗光降噪靠模型而非纯硬件 pipeline），是国产边缘视觉 SoC 的共同打法；开源+众筹可直接抄板

### 2. [CamThink NeoEyes NE302：STM32N6 驱动的拇指大 WiFi 6 边缘视觉相机](https://www.cnx-software.com/2026/09/12/neoeyes-ne302-a-tiny-usb-c-powered-wifi-6-edge-ai-vision-camera-based-on-stm32n6-mcu/)
- **什么**: NE301 减配版——去掉电池/4G/PIR/PoE/GPIO，USB-C 仅供电，32MB PSRAM + 64MB SPI flash
- **规格**: STM32N6（**Cortex-M55@800MHz + Helium + Neural-ART NPU**）+ 4MP OS04C10；WiFi 6
- **判断**: Neural-ART 是 MCU 视觉关键变量——**NPU 独立于 CPU 跑 CNN**，让 Cortex-M 从「传图」变「判图」，端侧隐私相机成本下探

## 🖥️ GPU 与算力

### 3. [NVIDIA RTX Pro 5500 Blackwell：84GB GDDR7 塞进 RTX 5090 同款 GB202](https://www.tomshardware.com/pc-components/gpus/gaming-takes-a-backseat-as-nvidia-overhauls-the-rtx-5090-for-maximum-ai-margins-rtx-pro-5500-delivers-2-6x-vram-at-matching-specs)
- **什么**: 工作站新 SKU，GB202 回收片——170/192 SMs、**21,760 CUDA cores**（≈RTX 5090）
- **规格**: **84GB GDDR7**（28 颗 clamshell，14+14），448-bit @25Gb/s → **1,400 GB/s**；夹在 Pro 5000 72GB（$9,209）与 Pro 6000 96GB（$15,599）之间
- **判断**: 典型的「**用容量而非带宽切市场**」——为把大 batch VLM/视频推理微调「装得下」而买；带宽仅比 Pro 5000 高 4%、比 5090 低 22%（被降频），别指望训练吞吐

### 4. [Amlogic A123X / C305X2：首批 Cortex-A320 SoC，8 TOPS 支持 ViT Transformer 硬件加速](https://www.cnx-software.com/2026/09/11/amlogic-a123x-and-c305x2-arm-cortex-a320-socs-target-industrial-and-low-power-aiot-applications/)
- **什么**: 四核 A123X / 双核 C305X2，**首个采用 Arm Cortex-A320（Armv9.2-A + SVE2）的硅**，面向 IP 相机/行车记录仪/机器人
- **规格**: A123X — 4K@60 编解码；**ADLA2 4 TOPS（检测/跟踪）或 ADLA3 8 TOPS（硬件加速 Transformer，跑 ViT/LLM）**
- **判断**: 安防 IP camera 将直接跑 ViT 级编码器而非小 CNN——**NPU 内置 Transformer 硬件路径 = 2026 边缘 SoC 分水岭**；Amlogic 抢下首发但规格披露极少，工具链成熟度待验证

## 🔩 芯片与半导体

### 5. [SK hynix 洽谈赴美造内存（租 Intel 俄亥俄厂/与超算厂合资）；内存荒改写设备设计](https://www.tomshardware.com/tech-industry/semiconductors/sk-hynix-reportedly-discussing-us-memory-chip-manufacturing-with-intel-options-include-leasing-ohio-plant-or-forming-joint-venture-with-other-ai-hyperscalers)
- **动态**: Reuters——选项含租用 Intel Ohio One 在建厂区，或与 Intel + AI hyperscaler 合资；Indiana HBM 封装厂已动工
- **影响（视觉硬件）**: [Fairphone CEO 称内存已占 **~$400 手机 BOM 的 60%**](https://www.tomshardware.com/pc-components/ram/ai-induced-memory-shortage-is-changing-how-devices-are-built-fairphone-says-memory-now-60-percent-of-materials-cost-smaller-laptop-and-phone-makers-are-redesigning-products-and-have-to-test-for-fake-chips)；Counterpoint 预计今年全球手机出货 **-13.9% 至 10.8 亿台（史上最大跌幅）**
- **连锁反应**: Jolla 设计**两套主板**在「合封 vs 分立」间切换、逐批抽检防翻新颗粒冒充新品；Framework 走模块化+用户自备旧内存
- **判断**: 内存从成本项变成**设计约束**——安防相机/NVR/边缘盒子同样吃 DRAM，2027 才是 SK hynix CEO 口中的「最坏一年」

### 6. [黄仁勋：中国 2030 年将拥有自己的先进光刻设备](https://www.tomshardware.com/tech-industry/semiconductors/jensen-huang-thinks-china-will-develop-its-own-advanced-lithography-systems-by-2030-nvidia-ceo-says-achievement-of-that-capability-is-just-a-matter-of-time)
- **动态**: All-In Podcast——「规模化生产是中国的强项，这只是时间问题……两三年在他们看来只是一瞬」
- **反方校验（Tom's）**: SMEE 目前仅能量产 193nm ArF **干式**（90nm 级）；28nm 浸没式无公开量产证据；DUV 被评「≈ASML 2004 年」；EUV 连原型机都无——LPP 光源 ≠ 可交付扫描机
- **影响**: 光刻决定**图像传感器逻辑层 / ISP / NPU** 的制程上限，也决定国产车载 CIS 与边缘 SoC 天花板
- **判断**: 2028–29 前国产浸没式难规模上产线，但「差距以年计而非代计」正是厂商愿意下注的前提——别把表态当路线图

## 📦 开源硬件与工具

### 7. [Arduino UNO Media Carrier：为 UNO Q / VENTUNO Q 补齐双 MIPI CSI + MIPI DSI](https://www.cnx-software.com/2026/09/10/arduino-uno-media-carrier-adds-mipi-csi-dsi-and-audio-connectors-to-uno-q-and-ventuno-q-boards/)
- **功能**: 官方载板（ASX00083）——2× 22-pin **MIPI-CSI（兼容 IMX219 / 树莓派 Camera Module 2）**、22-pin MIPI-DSI、3× 3.5mm 音频
- **上手**: 免去从 JMEDIA/JMISC 60-pin 裸排线接线；配套 5/8/10.1 吋 Waveshare 触摸屏
- **判断**: 把「Q 系列」从 GPIO 玩具推向**可装相机的视觉原型平台**；对教学与双目/多相机标定快速验证价值大于参数本身

---

## 📰 产业动态

### 8. 快讯
- **边缘算力**: [LattePanda Mu Ultra](https://www.cnx-software.com/2026/09/10/lattepanda-mu-ultra-compute-module-features-intel-core-ultra-5-226v-7-256v-lunar-lake-cpu-for-ai-workloads/)——Lunar Lake COM，**最高 115 TOPS 综合算力**、16GB DDR5、69.6×60mm，直指 vision AI / 机器人
- **MCU 视觉**: [Alif Balletto B1 / Ensemble E1C StartKits](https://www.cnx-software.com/2026/09/15/alif-semi-balletto-b1-and-ensemble-e1c-startkits-feature-cortex-m55-ethos-u55-mcu-for-iot-and-edge-ai/)——Cortex-M55@160MHz + **Ethos-U55 NPU** + **Arducam 相机排针** + 双 PDM 麦
- **异构互连**: [d-Matrix 采用 NVLink Fusion 接 Raptor XPU](https://blogs.nvidia.com/blog/d-matrix-nvlink-fusion/)——推理芯片商接入 NVLink scale-up + Spectrum-X scale-out + MGX 液冷机架，「自研 XPU 借 NVIDIA 底座上市」成标准路径（接续 8/26 Raptor 直叠 DRAM）
- **NVIDIA 生态**: [AI Infra Summit 8000 人参会](https://blogs.nvidia.com/blog/ai-infra-summit-vera-rubin-dsx-energy-efficiencies-tokens-per-watt-ai-factories/)（去年 3,500，翻倍），主题从 FLOPS 转向 **tokens/W**；[Skild AI S1](https://blogs.nvidia.com/blog/skild-ai-s1-physical-ai/) 靠单段视频学长程机器人任务

---

*渠道: CNX Software / Tom's Hardware / NVIDIA Blog / SemiEngineering / EETimes / Sony Semicon / GitHub / Reddit / HuggingFace / SemiAnalysis · 备查: Sony 9/7 后无新品；OmniVision Cloudflare 拦截；Reddit 403；SemiAnalysis feed 停 2025-09*
