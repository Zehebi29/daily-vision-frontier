# 🤖 2026-09-03 模型与算力日报（边缘 / VLA / 小模型）

> 今日扫描 HuggingFace（API×12 + Daily Papers）· GitHub 新仓库×4 · arXiv×6 · Reddit（403 限流）共 4 渠道

---

## 🦾 VLA 行动模型（机器人/操作/驾驶）

### 1. [Qwen-Drive-1.0-4B：开源驾驶 VLA 底座](https://huggingface.co/Qwen/Qwen-Drive-1.0-4B)
- **什么**: [GitHub ★115](https://github.com/QwenLM/Qwen-Drive-1.0)，Qwen3.5-4B 共享 VLM + BEV/占用感知头 + flow matching Planning Expert，感知规控一体
- **参数量**: 全仓 VLM 9.1GB + planner-sft/rl 各 2.1GB + perception 0.5GB = **13.8GB BF16** · Apache-2.0
- **算力**: 全栈 BF16≈16.6GB→1×24GB；纯 VQA 4B FP16≈9.6GB / INT4≈2.4GB
- **产线**: NAVSIM PDMS/闭环对齐 AutoVLA 级；厂内 AGV/园区物流车的视觉导航底座，工控机单卡可跑

### 2. [VLAct：Qwen3-VL-4B 跨本体 VLA 预训练权重](https://huggingface.co/StarVLA/VLAct_Qwen3_Pretrain)
- **什么**: [GitHub ★94](https://github.com/starVLA/VLAct)，"Beyond Data Scaling"论文配套 100K 步 ckpt：冻结 vision encoder + LM 低 18 层，OFT+GR00T+PI 三动作头协同预训练（20D padded/50 步）
- **参数量**: 底座 Qwen3-VL-4B，ckpt 11.7GB · Apache-2.0 · 16 GPU 训练
- **产线**: 非直接部署权重，是机械臂新工位（AgileX/ALOHA/Franka）微调起点，自带 RoboTwin2.0/LIBERO-Plus/DOMINO 启动器；FP16≈9.6GB，量化后可下 Orin

### 3. [Muse-Robotics-1：122M 从零训练流匹配 VLA](https://huggingface.co/Muse-Ltd/Muse-Robotics-1)
- **什么**: NovaVLA：随机初始化在 DROID/BridgeV2 从头训练，8 个 latent plan token + rectified flow 输出 16 步动作块，双相机+proprio，FastAPI 服务
- **参数量**: **121.7M**（F32 0.49GB → BF16≈0.24GB）· MIT
- **产线**: 无预训练先验、上限有限，宜做低成本自训/基线；MIT 无底座授权风险，嵌入式随便跑

### 4. [GigaBrain-0.7-3.5B RoboTwin2.0 流策略 VLA](https://huggingface.co/open-gigaai/GigaBrain-0.7-3.5B-RoboTwin2.0-Clean)
- **什么**: RoboTwin2.0 数据训练的扩散 VLA：gemma/qwen3-VL 双流 LLM expert + robomanip cross-attn 流动作头（50 步 horizon、8 embodiment）
- **参数量**: ~3.5B（单文件 FP32 14.1GB → BF16≈7GB / INT4≈1.8GB）· Apache-2.0 · 09-01
- **产线**: INT4 可进 Orin NX 16GB；但扩散策略每步 50 次去噪，先测吞吐再上真机

## 🪶 边缘小模型 / 质检 VLM

### 5. [AnomalyThink：可解释质检 VLM 家族（含 GGUF）](https://huggingface.co/aacudad/AnomalyThink-LLaVA-OneVision-7B-SFT)
- **什么**: LLaVA-OneVision-7B / [Qwen2.5-VL-7B 版 GGUF](https://huggingface.co/mradermacher/AnomalyThink-Qwen2.5-VL-7B-KCR-GRPO-GGUF) 微调：输出缺陷**位置+类型+有无**（SFT→GRPO→KCR 三级）· Apache-2.0 · 09-02/03
- **参数量**: ~8.0B（含 vision）· BF16 全量≈19GB（1×24GB）；GGUF Q4≈5GB + mmproj≈1GB → Orin NX 16GB
- **亮点**: MMAD DS-MVTec 平衡准确率 **88.45** / VisA **74.25**（KCR，base 75.66/53.80）——质检从"出框"升级为"出人话报告"

### 6. [BAAI Recon2Reason-Reasoning-4B：空间推理小 VLM](https://huggingface.co/BAAI/Recon2Reason-Reasoning-4B)
- **什么**: Qwen3-VL-4B 微调：室内/具身场景的度量距离、相对位姿、物体空间关系推理，标准 Qwen3VL 接口 · Apache-2.0 · 09-03
- **参数量**: 4.44B BF16（≈10.6GB 含余量 → 1×24GB / INT4≈2.7GB）
- **亮点**: 视觉 agent 的"空间认知层"，可给抓取/VLA 做 metric 预判；发布当天 0 下载，先标记观察

## ⚡ 部署与算力速查

### [DeepSeek-V4-Flash-Vision-Exp（MoE 多模态，仅对照）](https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-Vision-Exp)
- 256 路由专家（6 激活）多模态 MoE · MIT · 08-31，3 天 5.4 万下载；官方 vLLM 方案 4×GB300 节点，unsloth UD-GGUF Q4_K_XL≈205GB——**非边缘**，仅作"大杯认知"参照
- 视觉塔 mmproj 独立 0.93GB，vision encoder 可单独迁移到小模型

| 精度 | 每参数字节 | 显存公式（×1.2） | 例：4B |
|------|-----------|------------------|--------|
| FP32 | 4 B | 参数×4×1.2 | 19.2GB |
| FP16/BF16 | 2 B | 参数×2×1.2 | 9.6GB |
| INT8 | 1 B | 参数×1×1.2 | 4.8GB |
| INT4/GGUF Q4 | 0.5 B | 参数×0.5×1.2 | 2.4GB |

## 🏭 产线落地启示

### [Qwen-Drive-1.0-4B](https://huggingface.co/Qwen/Qwen-Drive-1.0-4B)：AGV/厂内物流
- 全栈 13.8GB BF16，一台 RTX 4000 Ada/工控 16GB 闭环；planner-rl 可先在 NAVSIM 离线仿真验收再上车

### [AnomalyThink](https://huggingface.co/aacudad/AnomalyThink-LLaVA-OneVision-7B-SFT)：复检解释层
- 7B 不适合实时初检；建议 RTMDet/YOLO26（<100MB）粗检 + AnomalyThink 只对 ROI 复检并输出报告，GGUF 已可直接 llama.cpp 试点

### [VLAct](https://github.com/starVLA/VLAct)：机械臂新工位起点
- 4B 底座 + RoboTwin2.0 launcher，1×24GB 卡可微调；比从裸 Qwen3-VL 权重起步省数据，先 LIBERO 仿真验收

## 📰 部署生态动态

- **[unsloth/DeepSeek-V4-Flash-Vision-Exp-GGUF](https://huggingface.co/unsloth/DeepSeek-V4-Flash-Vision-Exp-GGUF)**：发布 48h 内 UD 动态量化全系 + mmproj 视觉支持跑通，多模态 MoE 的 GGUF 工具链已就绪
- **[nota-ai 的 Qwen3.8-Flash-Next NVFP4](https://huggingface.co/nota-ai/Qwen3.8-Flash-Next-Nota-NVFP4)**：边缘 AI 厂商 08-31 跟进专家 fp4 量化（底座 125B，仍属多卡级）
- **[Alibaba IndustryLLM 预告](https://huggingface.co/alibaba-multimodal-industrial-ai/IndustryLLM)**（09-03，Qwen3.5-35B-A3B 工业域续训）：权重未发布，暂不收主条目——防"只有 demo"
- **[IndustrialIntel-1.7B GGUF](https://huggingface.co/Similoluwa/IndustrialIntel-1.7B-GGUF)**：Qwen3-1.7B 读 PLC/DCS 报警+遥测，Q4≈1.2GB 离线跑——纯文本但产线价值明确
- **[FACET/Facet-0](https://github.com/PINE-Lab-NTU/FACET)**（09-02 ★11，arXiv 2609.01596）：contact-rich 精密操作 foundation model，code 已出、权重待确认
- Reddit 4 子版仍 403 限流，社区热度信号缺位
