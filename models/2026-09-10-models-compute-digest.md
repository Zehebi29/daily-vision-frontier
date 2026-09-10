# 🤖 2026-09-10 模型与算力日报（边缘 / VLA / 小模型）

> 今日扫描 HuggingFace（API×6 + Daily Papers）· GitHub 新仓库×8 · arXiv（cs.RO + 4 篇全文）· Reddit（403 限流）共 5 渠道

---

## 🦾 VLA 行动模型（机器人/操作）

### 1. [双机械臂 SmolVLA 叠毛巾（真机）](https://github.com/dk2472780158-ctrl/piper-dual-arm-smolvla-towel-folding)
- **什么**: [GitHub ★68](https://github.com/dk2472780158-ctrl/piper-dual-arm-smolvla-towel-folding)，SmolVLA（**SmolVLM2-500M** 视觉语言骨干 + 动作专家头）读三路相机+关节态直接出关节动作；叠加 ACT 安全底座做连续混合（authority∈[0,0.9]，无切换跳变）· Apache-2.0
- **参数量 / 算力**: **0.5B** → FP16≈1.2GB / INT4≈0.3GB，30Hz 实时闭环
- **产线**: **边缘 VLA 的标杆量级** — Orin Nano/工业 PC 无压力，双 AgileX Piper 真机已验证 grasp→fold→release，可直接抄作分拣/折叠工位基线

### 2. [VLA-Precision：高效真机在线 RL](https://github.com/scy-v/VLA-Precision)
- **什么**: [GitHub ★62](https://github.com/scy-v/VLA-Precision) · [arXiv 2609.04355](https://arxiv.org/abs/2609.04355)，非对称协同自举：用轻量可信 critic 修大 VLA 的值信号，解决"值不可靠→策略漂移 + 大 VLA 吞吐低"两大瓶颈，追求精度/可重复性 · Apache-2.0
- **算力**: **算法层方案、模型无关**（repo 走 LeRobot 生态，UR5e/UR7e/Franka 遥操作起点）；落地成本取决于所选底座
- **产线**: 高精度插装/装配工位的"后训练加速器"，先仿真验收再上真机做 trial-and-error 提升

### 3. [MotionVLA：把"运动"注入 π0 系 VLA](https://huggingface.co/hustvl/MotionVLA)
- **什么**: [GitHub ★15](https://github.com/hustvl/MotionVLA) · [arXiv 2606.08288](https://arxiv.org/abs/2606.08288) · **CoRL 2026**（华科+D-Robotics）。不再堆历史帧，而是用冻结 TraceAnything 编码器提供**仅过去**的 RGB 运动历史 token，Decouple 检索 + 末端重建接地，Recouple 可选回注 VLA 流 · Apache-2.0
- **参数量 / 算力**: π0 系底座 **~3.3B** → FP16≈8GB（1×24GB）；仓库为 openpi（JAX/OCDBT）权重格式，训练 ~16 GPU
- **产线**: 解决长程操作"几何漂移"的即插模块，适合已有 π0 部署的工位做时序增强

### 4. [Facet-0：接触密集精密操作基础模型（权重已放）](https://huggingface.co/Pinelab/Facet-0)
- **什么**: [arXiv 2609.01596](https://arxiv.org/abs/2609.01596)（NTU PINE Lab），**联合动作-力旋量提议**：因果 wrench 历史对齐视觉语言语义，flow matching 同时生成动作块与预期腕部力旋量；力是观测也是目标，配 wrench-conditioned RL 后训练 + 值估计集成 · Apache-2.0 · openpi
- **参数量 / 算力**: π0 系底座 **~3.3B** → FP16≈8GB；观测含 3 路图像 + 13 维状态（末端位姿 7 + 六轴力 6），动作 horizon 50 步
- **产线**: 亚毫米装配/插装专用，**力觉闭环**是它与通用 VLA 的关键差异；需腕部六轴力传感器

## 🪶 边缘小模型（<7B）

### 5. [MiniCPM5-2B（含官方 GGUF）](https://huggingface.co/openbmb/MiniCPM5-2B-GGUF)
- **任务**: 稠密 2B on-device 小模型（长上下文 / tool-calling），官方直接放 GGUF · Apache-2.0 · 09-05
- **算力**: 2B → FP16≈4.8GB / **GGUF Q4≈1.2GB**，嵌入式/工业 PC 轻松跑
- **亮点**: 2B 级开源 SOTA，主打 resource-constrained 本地部署；发布 5 天 4.2 万下载

### 6. [Ultralytics YOLO26（5 档边缘检测器）](https://huggingface.co/Ultralytics/YOLO26)
- **任务**: 检测/分割/分类/姿态/OBB 全系，**原生 NMS-free 端到端头**
- **参数量 / 算力**: n **2.4M**（INT8≈3MB）、s 9.5M、m 20.4M、l 24.8M、x 55.7M；COCO mAP 40.9–57.5，T4 TensorRT 1.7–11.8ms，**CPU ONNX 比 YOLO11n 快 43%**
- **亮点**: 产线初检默认解 — n/s 档在 CPU/边缘 NPU 上可跑高帧率

## ⚡ 部署与算力速查

### 7. [AxisQuant：从 kernel 侧重做 ViT 的 INT8 引擎](https://github.com/kohillyang/AxisQuant)
- **什么**: SAM 2.1 / SAM 3 / DINOv3 / ViT / DeiT 图像编码器跑 **INT8 tensor core**，W8A8 **无可见精度损失**：ImageNet top-1 与 fp32 差 <0.05，SAM 3 COCO segm AP 差 <0.0003，DINOv3 零样本头不变
- **算力**: 速度达 **TensorRT FP16 的 1.2–2×**，权重显存减半（ViT-L 300M → INT8≈0.36GB）
- **边缘适配**: 直接利好 SAM/DINO 系分割与特征骨干的定点部署

| 精度 | 每参数字节 | 显存公式（×1.2） | 例：0.5B | 例：3.3B |
|------|-----------|------------------|-----------|-----------|
| FP32 | 4 B | 参数×4×1.2 | 2.4GB | 15.8GB |
| FP16/BF16 | 2 B | 参数×2×1.2 | 1.2GB | 7.9GB |
| INT8 | 1 B | 参数×1×1.2 | 0.6GB | 4.0GB |
| INT4/GGUF Q4 | 0.5 B | 参数×0.5×1.2 | 0.3GB | 2.0GB |

## 🏭 产线落地启示

### [SmolVLA 真机方案](https://github.com/dk2472780158-ctrl/piper-dual-arm-smolvla-towel-folding)：双臂工位首选量级
- 0.5B / 1.2GB FP16 / 30Hz：**一台 Orin 就能跑双机械臂策略**，且用 ACT 做安全底座、SmolVLA 只做有界修正（≤0.15rad）——"不会失控"的工程设计比模型本身更值得抄

### [Facet-0](https://huggingface.co/Pinelab/Facet-0)：力控精密装配
- 3.3B / ~8GB 单卡，需六轴力传感器；适合插装、拧紧等接触任务，通用 VLA 缺力觉反馈的地方它是补充

### [YOLO26n](https://huggingface.co/Ultralytics/YOLO26) + [AxisQuant](https://github.com/kohillyang/AxisQuant)：视觉 Agent 的感知底座
- 检测用 YOLO26n（3MB INT8）出框，分割/特征用 AxisQuant 加速的 SAM/DINO——把感知端压到边缘算力预算内，把大模型留给需要"出报告"的复检环节

## 📰 部署生态动态

- **[Show-Harness](https://arxiv.org/abs/2609.10522)**（09-08）：给 VLM 一套离散语义动作单元 + 本体解释器，让通用 VLM "玩"机器人——VLA 之外的另一条 VLM-as-policy 路线
- **[StrandSeg-Lite](https://huggingface.co/EvanZhongg/StrandSeg-Lite)**（09-06）轻量分割，0 下载，标记观察
- **[AxisQuant](https://github.com/kohillyang/AxisQuant)** 的 W8A8 无损结论若可复现，会直接改写 ViT 系边缘部署的显存账本
- Reddit 3 子版仍 403 限流，社区热度信号缺位
