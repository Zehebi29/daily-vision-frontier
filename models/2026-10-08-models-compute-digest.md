# 🤖 2026-10-08 模型与算力日报（边缘 / VLA / 小模型）

> 今日扫描 HuggingFace（模型 API 检索×9 + 模型卡精读×6）· arXiv（VLA/量化/边缘/工业/小VLM 5 组 query）· GitHub（搜索×6）· HF Daily Papers

---

## 🦾 VLA 行动模型（机器人/操作）

### 1. [VLA-0-Smol：5 亿参数亚十亿 VLA 配方](https://huggingface.co/Robot-Learning-Collective/VLA-0-Smol)
- **什么**: 507M（0.5B）完整可复现 VLA，LeRobot 原生，LIBERO 高分；给出关键设计消融 · Apache-2.0
- **算力**: FP16≈**1.2GB** / INT4≈**0.3GB** —— 单张消费卡甚至 Orin Nano 可权重常驻
- **产线**: 目前最"轻"的开源操作策略模板，适合工位机做抓取/上料的低成本起点

### 2. [SpikingVLA：异步脉冲 VLA（10-07）](https://arxiv.org/abs/2610.09710)
- **什么**: ANN→SNN 转换框架，DIF（树突式积分-发放）神经元压通道 outlier，实现**低时延**脉冲推理
- **算力**: 主打超低功耗事件式计算；针对传统 SNN 需多 timestep、实时性不足的痛点
- **产线**: 若少步脉冲能保精度，是机器人端"毫瓦级"感知-决策的长期路线

### 3. [FastOPD：大 VLA 蒸馏到轻量部署（On-Policy Distillation）](https://arxiv.org/abs/2610.02832)
- **什么**: foundation-to-lightweight VLA 框架，flow-map 单步 teacher 监督 + 自一致损失，把多步 flow 策略压成少步
- **算力**: 目标把大 VLA 算力降到边缘可跑，同时保操作成功率
- **产线**: 与 π0 系"实时化"同源，部署前值得与步数裁剪方案对比

### 4. [OneVL-Q / sub4-vla：VLA 量化部署栈（GitHub）](https://github.com/Wanglaoban3/OneVL-Q)
- **什么**: OneVL-Q 给小米 OneVL 规划模型做 **INT8 W8A8 + TensorRT 就绪 QDQ ONNX**；sub4-vla 探索 **<4bit PTQ for VLA**
- **算力**: W8A8 权重/激活各 1B → 显存减半，TensorRT 直吃 INT8 张量核
- **产线**: VLA 端侧落地"最后一公里"工程件，比论文更贴近产线

## 🪶 边缘小模型（<7B）

### 5. [LiquidAI d1-3B / d1-omni-600M：边缘"决策模型"（10-05 新发）](https://huggingface.co/LiquidAI/d1-3B)
- **任务**: 给定状态（文本/JSON/图像/语音）直接输出**校准后类型化答案，零输出 token**（一次前向）
- **算力**: d1-3B 3.1B，**RTX 4090 单次决策 8ms** / M5 Pro 30ms；d1-omni-600M 仅 587M（381M 主干+94M 视觉+112M 音频）
- **亮点**: <10B 决策模型榜第一（48.57）；600M 版 ≈ FP16 1.4GB / INT4 **0.35GB**，[d1-omni-600M](https://huggingface.co/LiquidAI/d1-omni-600M) 嵌入式无压力

### 6. [VisionHOPE：自修改视觉主干（HF 分类榜首）](https://huggingface.co/PSRben/VisionHOPE)
- **任务**: 通用视觉 backbone，T/S/B 三档，覆盖 ImageNet 分类 / COCO 检测分割 / ADE20K；MIT
- **算力**: Tiny/Small 级可作边缘 backbone；论文 [arXiv 2609.33325](https://arxiv.org/abs/2609.33325)
- **亮点**: 今日 image-classification trending 第一（446 赞），可替代 ResNet/ViT 做产线特征提取

### 7. [YOLO26（Ultralytics）](https://huggingface.co/Ultralytics/YOLO26)
- **任务**: 检测/实例分割/分类/姿态/OBB 统一家族
- **算力**: nano 级可 **Jetson Nano + TensorRT FP16 实时**（社区已有 [jetson-edge-vision](https://github.com/triton0305/jetson-edge-vision) 复现）
- **产线**: 产线检测默认基线；AGPL-3.0，商用注意授权

## ⚡ 部署与算力速查

### 8. [Rethinking Small VLM Quantization（Jetson Orin 实机）](https://arxiv.org/abs/2607.08029)
- **方法**: 把 <3B VLM 拆成 视觉编码器 / projector / LLM 三段分别量化，在 **Orin NX + AGX** 上测 6 配置、验 5 假设
- **结论**: 量化敏感度由**结构范式（MoE vs dense）决定，而非纯规模**；MoE 主干能扛 INT4 噪声
- **产线**: 小 VLM 上边缘前必读——别对全模型一刀切量化

### 9. 量化方法速览
- **[P4Q](https://arxiv.org/abs/2609.34867)**: 视觉 token 剪枝 + PTQ **联合共设计**，序列长度与数值精度同步压
- **[SubRot](https://arxiv.org/abs/2609.34884)**: 符号梯度子空间校准，解决旋转量化跨样本统计不稳
- **[RGSQ](https://arxiv.org/abs/2609.25492)**: 流形几何敏感 VLM PTQ，纠正欧氏各向同性假设

| 精度 | 字节/参数 | 0.5B | 3B | 7B |
|------|-----------|------|----|----|
| FP16 | 2 | 1.2GB | 7.2GB | 16.8GB |
| INT8 | 1 | 0.6GB | 3.6GB | 8.4GB |
| INT4 | 0.5 | 0.3GB | 1.8GB | 4.2GB |

## 🏭 产线落地启示

- **[3D 异常检测·关系不一致建模](https://arxiv.org/abs/2609.35059)**（09-28）：点云质检不再只学"正常分布"，显式把缺陷建为邻域几何一致性违背，改善统一/跨域场景误报
- **[移动机器人在线故障检测](https://arxiv.org/abs/2609.29194)**（09-24）：TSPulse 教师生成伪标签 → **MiniRocket 轻量学生** + RLS 在线适配，端侧实时无监督异常
- **[LocateAnything-3B GGUF](https://huggingface.co/mudler/locate-anything.cpp-gguf)**：NVIDIA 开放词表检测/视觉定位 3B 的 **GGUF 量化版**，locate-anything.cpp 可纯 CPU / 端侧跑 grounding

## 📰 部署生态动态

- **[Rephrase Before You Act](https://arxiv.org/abs/2610.10526)**（10-07）：VLA 对指令措辞极敏感——"开火炉"100% vs"开热板"2%；π0.5 隐性风险，建议重述增强
- **[VLA-JEPA-LIBERO](https://huggingface.co/lerobot/VLA-JEPA-LIBERO)**：Qwen3-VL + V-JEPA2 世界模型 + flow-matching DiT 动作头，3.08B BF16≈**7.4GB** / INT4≈1.85GB
- **[YOLO26](https://huggingface.co/Ultralytics/YOLO26)** 与 **[VisionHOPE](https://huggingface.co/PSRben/VisionHOPE)** 今日 HF 趋势位领跑，边缘检测/主干选型可关注
