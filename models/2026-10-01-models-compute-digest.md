# 🤖 2026-10-01 模型与算力日报（边缘 / VLA / 小模型）

> 今日扫描 HuggingFace（模型 API 检索×12 + 模型卡精读×10）· arXiv（VLA/量化/工业 5 组 query）· GitHub（搜索×5 + 仓库深读×3）· HF Daily Papers

---

## 🦾 VLA 行动模型（机器人/操作）

### 1. [RoboECC：VLA 边缘-云协同部署（IJCNN 2026）](https://github.com/zhengzihaoPKU/RoboECC)
- **什么**: 把 VLA 的 V/L/A 组件拆成顺序层链，用 roofline `max(算力, 带宽)` 估时搜分割点；LSTM 预测带宽 + 双阈值在线挪边界，边界块权重常驻双端 · ★116 · MIT
- **算力**: **Orin+A100 3.16–3.28×**、**Thor+A100 2.10–2.23×** 加速（vs 纯端侧推理），在线调度开销仅 **2.55–2.62%**
- **产线**: 工位机 + 车间共享 A100 是目前 VLA 上产线最现实的形态；代码开源、可直接复现

### 2. [Toward Real-Time VLAs：π0.5 推理 10 步砍到 2 步（61.6→22ms）](https://arxiv.org/abs/2609.39822)
- **什么**: 剖析 flow-matching 速度场——前期方向稳、末端才需强修正，据此做**两阶段非均匀去噪**；再配"推理/动作发布/机器人控制"三频解耦的分布式框架 · 09-30
- **算力**: π0.5 模型推理 **61.56ms → 21.96ms**；长程叠衣任务上横评 6 种实时执行策略
- **产线**: 不换模型、不加算力，把 VLA 从"慢半拍"拉进机器人控制节拍，可直接叠加到现有 π0 系部署

### 3. [Rho：可高效适配的双臂 VLA 权重族](https://arxiv.org/abs/2609.38164)
- **什么**: 开源权重双臂 VLA，覆盖 YAM Box / UR AI Trainer / FR3 Duo 三形态；在其 flow-matching 动作专家之上挂一个**内部 latent policy**，仅需 **15 段纠错 episode** 即可在线适配分布边缘情形 · 09-29
- **算力**: 摘要未披露总参数量；动作专家与主干解耦，适配只训轻量模块
- **产线**: "少样本现场适配"正是柔性产线刚需；但暂未见量化版，边缘部署需自行蒸馏

## 🪶 边缘小模型 / 可部署 VLA（<7B）

### 4. [MiniVLA：0.5B LLM 的 TensorRT 端侧 VLA](https://github.com/Zhenxintao/MiniVLA)
- **任务**: OpenVLA-Mini 骨架 + **Qwen-0.5B**，视觉编码器与 LLM 全量导出 ONNX/TensorRT，FastAPI 封 `/act` · ★22 · MIT
- **算力**: 在 **8GB 显存**（RTX 4060 笔记本作 Orin Nano 代理）跑实时推理；0.5B INT4≈**0.3GB**
- **亮点**: 目前最"能落地"的轻量 VLA 工程参考——混合 PyTorch+TRT 有回退路径

### 5. [TeleOCR：1.4B 文档解析 VLM（数字件+拍照件）](https://huggingface.co/XingChen-AGI/TeleOCR)
- **任务**: Qwen2.5-VL 底座的文档解析/OCR，兼容相机拍摄的扭曲文档 · Apache-2.0 · 31k 下载 / 1129 赞
- **算力**: 1.4B BF16 → **≈3.4GB** / INT4≈**0.85GB**；工业 PC / Orin 均可承载
- **亮点**: 产线的工序卡、铭牌、检测报告 OCR 可完全本地化，免云端回传

### 6. [DCM-SAM：SAM ViT-B 上 Qualcomm Hexagon NPU 做缺陷分割](https://arxiv.org/abs/2609.38811)
- **任务**: 冻结 SAM 主干 + 每类缺陷独立 Conv-LoRA 专家，**只训 4.4% 参数**；金属增材 XCT 孔隙/夹杂分割，仅用合成切片 · 09-30
- **算力**: ViT-H/ViT-L 在 NPU **1024² 直接分配失败**（激活超上限，量化权重救不了）；ViT-B 经数值等价 attention 改写后 **FP16@1024² 全程不回落 CPU**，掩码与 FP32 差 <0.01%
- **产线**: **机上质检**的直接证据——NPU 瓶颈是激活内存而非权重；LoRA 专家库让"多缺陷类型"可增量扩

## ⚡ 部署与算力速查

### 7. [EdgeVLN](https://arxiv.org/abs/2609.35570) · [RAMP](https://arxiv.org/abs/2609.28262) · [SPHQuant](https://arxiv.org/abs/2609.24875)
- **EdgeVLN**（09-28）: 量化 StreamVLN + 轻量停走头 LATTE，经 **llama.cpp VLN driver** 在端侧重建流式上下文/剪 memory token；扫 8→2bit 权重 × 7 种 runtime，全 1839 条 R2R val-unseen 上报成功率+延迟+能耗+常驻内存（NVIDIA Jetson）
- **RAMP**（09-23）: 系统评测 **13 种 INT8 敏感度指标** × 4 网络 × 2 款 ARM64；梯度类方法在 8 组配置中 4 组失效，**Jensen-Shannon 散度零灾难失败**——混合精度选层别再迷信梯度
- **SPHQuant**（09-21）: 免旋转的**球坐标 weight-only 量化**（符号+半径+单位方向），把 outlier 幅度隔离进半径，主打 **2–3bit VLM** + 硬件友好 GEMV 核

| 精度 | 字节/参数 | 显存（×1.2） | 0.5B | 1.4B | 3B | 7B |
|------|-----------|--------------|------|------|----|----|
| FP16/BF16 | 2 | 参数×2×1.2 | 1.2GB | 3.4GB | 7.2GB | 16.8GB |
| INT8 | 1 | 参数×1×1.2 | 0.6GB | 1.7GB | 3.6GB | 8.4GB |
| INT4/Q4 | 0.5 | 参数×0.5×1.2 | 0.3GB | 0.85GB | 1.8GB | 4.2GB |

## 🏭 产线落地启示

- **[DCM-SAM](https://arxiv.org/abs/2609.38811)**：机上 XCT 质检，单张 Hexagon NPU 跑 FP16@1024²，适合增材制造/铸件孔隙检测；**部署前务必测激活内存，而非只看权重量化**
- **[PCB-MC](https://arxiv.org/abs/2609.39427)**：PCB 缺件检测数据集（RF100 上 197 种板型，防位泄露交叉验证）。结论泼冷水——监督模型对未见板型漏检率高、无监督因缺位对齐**完全失效**，缺件检测仍属开放难题
- **[FLASH](https://arxiv.org/abs/2609.37314)**：VLM 引导 + "生成一次、合成多次"范式，在 MVTec AD 2 上低成本扩缺陷样本，缓解产线缺陷样本荒

## 📰 部署生态动态

- **[FastCrest/tether](https://github.com/FastCrest/tether)**（★84）：VLA 部署 CLI，单块 ONNX 与参考 PyTorch **cos=+1.000000** 对齐，覆盖 SmolVLA/π0/π0.5/GR00T N1.6，产端 parity 证书
- **[Spike-driven VLA](https://arxiv.org/abs/2609.39514)**：首个脉冲神经网络（SNN）驱动的 VLA，稀疏事件式计算，LIBERO/Meta-World 验证——超低功耗路线
- **[FRESHLATENT](https://arxiv.org/abs/2609.30629)**：Jetson AGX Xavier **10W** 分裂式 VLM 感知，信道感知 latent adapter 比重型 codec 省 **37–40×** 编码器参数、**8.8–10×** 接口能耗
- **[lingbot-vla-v2-6b](https://huggingface.co/tsangb34/lingbot-vla-v2-6b-so101-cube-drawer-10ep)**：6B VLA 的 SO-101 任务微调权重今日密集上传，FP16≈**14.4GB** / INT4≈**3.6GB**
