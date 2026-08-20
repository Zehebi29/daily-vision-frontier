# 🤖 2026-08-20 模型与算力日报（边缘 / VLA / 小模型）

> 今日扫描 HuggingFace（trending×5 + Daily Papers）· GitHub 新仓库 · arXiv（cs.RO/cs.CV）· Reddit 等 4 个渠道；Reddit JSON 被 IP 限流，暂缺社区信号

---

## 🦾 VLA 行动模型（机器人/操作）

### [τ₀-VLA（sii-research）](https://huggingface.co/sii-research/tau-0-vla)
- **什么**: 分层机器人基础模型（[论文 2608.16885](https://arxiv.org/abs/2608.16885)，8/17 发布）；开源的 low-level policy = Qwen3.5-2B 底座 + MoT action expert，flow matching 10 步出 30×40 action chunk，4 万小时异构真机数据预训练
- **参数量/精度**: 3.0B · BF16 · Apache-2.0
- **算力需求**: BF16≈7.2GB / INT8≈3.6GB / INT4≈1.8GB；预训练为万卡时量级（未公开精确 GPU-hours）
- **产线适配**: 需 post-train 到具体工位；8GB 边缘卡量化后即可推理，world-model + test-time search 高阶层暂未开源，先按单策略落地

### [LingBot-VLA-V2（6B）](https://huggingface.co/robbyant/lingbot-vla-v2-6b)
- **什么**: 面向"预训练→应用"的 VLA-V2：MoE action expert + dual-query 蒸馏（DINO-Video/LingBot-Depth）；60k h 数据、20 种机器人构型，[代码开源](https://github.com/robbyant/lingbot-vla-v2)（Apache-2.0）
- **参数量/精度**: 6B · BF16
- **算力需求**: BF16≈14.4GB（1×24GB）/ INT4≈3.6GB（Orin 32GB 可试）
- **产线适配**: 双臂/灵巧手/移动底座统一 action space，多构型产线一条基座复用的现实选项

### [Tencent Hy-Embodied-0.5-VLA（RoboTwin）](https://huggingface.co/lerobot/hy_vla_robotwin)
- **什么**: 腾讯双臂 VLA 的 [LeRobot 官方转换版](https://huggingface.co/tencent/Hy-Embodied-0.5-VLA-RoboTwin)，16D 双臂 pose+gripper，10 步 Euler 采样；权重前向对齐验证误差 0.0；⚠️ 名字 "0.5" 是系列名，实际 **4.5B**
- **参数量/精度**: 4.5B · BF16 · Apache-2.0
- **算力需求**: BF16≈10.8GB（12-16GB 单卡）/ INT4≈2.7GB
- **产线适配**: RoboTwin 双臂工位开箱微调；量化后 Jetson Orin NX 16GB 可推理

### [NebulaVLA / LIBERO-VIFO（观察线）](https://arxiv.org/abs/2608.16503)
- **什么**: NebulaVLA = 异步双频架构（高频控制/低频语义解耦，LIBERO-Plus 85.5%）；LIBERO-VIFO = VLA 视觉 cue 跟随安全评测基准（[2608.17600](https://arxiv.org/abs/2608.17600)，8 类视觉 cue + 4 协议）
- **算力画像**: 均为论文无权重；异步解耦对边缘实时性友好，VIFO 可作产线 VLA 安全验收基准
- **产线判断**: 先标记等 release；安全评测协议值得先抄

## 🪶 边缘小模型（<7B）

### [LiquidAI LFM2.5-VL-3B](https://huggingface.co/LiquidAI/LFM2.5-VL-3B)
- **任务**: 小 VLM（自然语言 grounding / OCR+layout / 近实时检测）
- **参数量**: 2.6B LM + SigLIP2 NaFlex 400M 视觉塔 ≈3B；已出 [GGUF/ONNX/MLX](https://huggingface.co/LiquidAI/LFM2.5-VL-3B-GGUF) 全套量化导出
- **显存/门槛**: 官方实测 <3.3GB 内存跑通：228 tok/s（Apple M5 Max）、116 tok/s（AMD Ryzen AI Max+ 395）；Jetson Orin NX 16GB 级别可部署
- **亮点**: 文档 OCR 带 layout 标注、bbox 输出、WebGPU 浏览器演示；8/13 刚更新

### [TinyDETR-Pose](https://arxiv.org/abs/2608.15297)
- **任务**: 6DoF 位姿估计（端到端单阶段，免 PnP/NMS/迭代优化）
- **参数量**: LW-DETR 轻量底座（<50M 量级）
- **显存/门槛**: 论文称面向 edge；Jetson Orin 级别有望实时
- **亮点**: 抓取引导/视觉定位的 DETR 系轻量方案；8/15 发布，代码状态待确认

## ⚡ 部署与算力速查

### [FreeToken：边缘 MoE 推理系统](https://arxiv.org/abs/2608.16157)
- **做法**: 把个人机当弹性推理平台：expert 驻留调度、CPU-GPU 混合执行、带宽自适应
- **判断**: 边缘跑大 MoE（35B-A3B 系）的 serving 工程路线图，与 GGUF/INT4 互补

### [MoE-ViE：MoE 视觉编码器](https://arxiv.org/abs/2608.17402)
- **做法**: fine-grained MoE 拓扑扩展 CLIP 式视觉塔，dense 扩展的算力替代方案
- **判断**: 小 VLM 视觉塔瘦身方向，VLA/VLM 边缘化的潜在杠杆

### [YOLO26 / ObjectModel-v1（基线速查）](https://huggingface.co/Ultralytics/YOLO26)
- **YOLO26**: 检测/分割/pose/OBB 全家族（AGPL-3.0），ONNX/TFLite 导出成熟——产线检测基线首选
- **ObjectModel-v1**: NMS-free 紧凑检测器（[bench-labs](https://huggingface.co/bench-labs/objectmodel-v1)），单卡 RTX 5090 训 100 epochs 达 COCO AP 0.358——开源"低成本训练画像"参考

| 精度 | 每参数字节 | 显存公式（含 1.2 余量） | 例：3B | 例：7B |
|------|-----------|------------------------|-------|-------|
| FP32 | 4 B | 参数×4×1.2 | 14.4GB | 33.6GB |
| FP16/BF16 | 2 B | 参数×2×1.2 | 7.2GB | 16.8GB |
| INT8 | 1 B | 参数×1×1.2 | 3.6GB | 8.4GB |
| INT4/GGUF Q4 | 0.5 B | 参数×0.5×1.2 | 1.8GB | 4.2GB |

## 🏭 产线落地启示

### [VLM 工业仪表读数实证](https://arxiv.org/abs/2608.17723)
- **场景**: 指针仪表自动读数（合成集 + 真实压力表 + 私有产线数据）
- **判断**: Qwen2.5-VL-7B 零样本不稳，QLoRA 微调 20 epochs 后可靠，免指针分割几何管线——小 VLM 替换传统读表可行
- **算力账单**: 7B INT4≈4.2GB，8GB 工控机/Orin NX 可推理；微调 1×24GB 卡足够

### [τ₀-VLA / LFM2.5 的产线组合拳](https://huggingface.co/sii-research/tau-0-vla)
- **场景**: 机器人工位（感知+认知+动作）
- **判断**: 感知用 LFM2.5-VL-3B（<3.3GB），动作用 τ₀-VLA INT4（~1.8GB），两模型合计 ~5GB，一台 Orin 16GB 工控可同时驻留——2026 年下半年的典型轻量产线堆栈

## 📰 部署生态动态

### [Qwen3.8-27B 登顶 HF trending](https://huggingface.co/Qwen/Qwen3.8-27B)
- omni-modal 27B 一周 137 万下载；FP8 / INT4-AWQ / GGUF 生态 48h 内跟进——>30B 大模型不作主线，仅作量化生态风向标

### [社区讨论](https://huggingface.co/papers)
- HF Daily Papers 机器人侧今日偏 VLA 分层 / 测试时计算；Reddit（r/LocalLLaMA · r/robotics · r/computervision）本机 IP 被限流无法抓取，明日换通道补社区信号
