# 🤖 2026-10-15 模型与算力日报（边缘 / VLA / 小模型）

> 今日扫描 HuggingFace（API 检索×26 + 模型卡精读×15）· arXiv（cs.RO + 4 组关键词）· GitHub（4 组仓库搜索）· HF Daily Papers · Reddit 等 6 个渠道

---

## 🦾 VLA 行动模型（机器人/操作）

### 1. [FoveaVLA：用"注视动作"取代腕部相机](https://arxiv.org/abs/2610.20064)
- **什么**: 在 π0.5 上构建，策略每次查询时同时预测下一帧要看的高清 crop 区域——省掉腕视相机又保住细节
- **算力**: π0.5 量级（~3B）+ 少量 crop 推理开销；Single/Dual 两档
- **产线**: 少一路相机 → 机械臂走线更简单，是"感知-行动"闭环轻量化新范式

### 2. [LingBot-VLA 2.0 · LeRobot 原生移植](https://huggingface.co/lerobot/lingbot_vla_v2_base)
- **什么**: Qwen3-VL-4B 主干 + sparse-MoE Qwen2 动作专家，flow-matching；上游 6.376B，fp32 逐张量对齐
- **算力**: FP16≈**15.3GB** / INT8≈7.7GB / INT4≈**3.8GB**（原权重 fp32 近 30GB，用前需转换）
- **产线**: 带 `lerobot-train` 直训配方，新工位微调即用

### 3. [Microsoft VITRA-VLA-3B：人手视频预训练 VLA](https://huggingface.co/microsoft/VITRA-VLA-3B)
- **什么**: 把第一视角人手视频（100 万+ episode）转成 VLA 训练数据，因果动作 Transformer；MIT
- **算力**: 3B → FP16≈**7.2GB** / INT4≈**1.8GB**，单张消费卡可推理
- **产线**: 少样本微调到真机操作，开源 3B VLA 里数据规模最有说服力的一档

## 🪶 边缘小模型（<7B）

### 4. [MiniCPM-V 4.7 1B：端侧 VLM 新 Pareto 前沿](https://huggingface.co/openbmb/MiniCPM-V-4.7-1B)
- **任务**: 单图/多图/视频理解小 VLM，ViT 内 early token 压缩 + 4x/16x 混合压缩
- **算力**: **1.554B**；FP16≈3.7GB / INT8≈1.9GB / INT4≈**0.93GB**（嵌入式可权重常驻）
- **亮点**: iOS/Android/HarmonyOS + **瑞芯微/后摩/Intel/AMD/Arm NPU 首发支持**，GGUF/AWQ/GPTQ/FP8 全齐

### 5. [Cosmos-Embed1-448p-anomaly-detection：视频异常检测 embedder](https://huggingface.co/nvidia/Cosmos-Embed1-448p-anomaly-detection)
- **任务**: 视频系异常检测（NVIDIA Cosmos-Embed1 蒸馏到异常任务）
- **算力**: **1.198B** → FP16≈2.9GB / INT4≈0.72GB，可做产线在线监控的 embedding 后端
- **亮点**: 工业视频质检少见的现成开源权重，社区使用量已达百万下载级

### 6. [UME-Recipes：2B 通用多模态检索 embedding（阿里工业 AI）](https://huggingface.co/alibaba-multimodal-industrial-ai/UME-Recipes)
- **任务**: Qwen2-VL-2B/7B + DoRA(r=16) 图文检索 embedding，MMEB 36 任务 P@1
- **算力**: 2B 版 FP16≈4.8GB / INT4≈1.2GB；LoRA 适配器增量极小
- **亮点**: 受控实验证明"硬负样本+去伪负+硬 batch"组合 +6.0%，工业图库检索可直接用

## ⚡ 部署与算力速查

### 7. [LFM2.5-24B-A2B-GGUF：MoE 24B 总参 / ~2B 激活](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-GGUF)
- **显存**: Q4_0 GGUF 权重≈**12GB**，但每 token 只激活约 2B → 算力按 2B 计，边缘 CPU/低端 NPU 可跑
- **量化**: 官方 **QAD（量化感知蒸馏）Q4_0** checkpoint，专门补回 Q4 掉的精度，而非裸 PTQ
- **适配**: llama.cpp 一行 `-hf` 直拉；MoE 边缘化路线值得与 MiniCPM-V 对比

### 8. [Beyond Independent Optimization：压缩×量化×MoE 路由耦合](https://arxiv.org/abs/2607.20981)
- **方法**: 综述视觉 token 压缩、KV-cache、MoE 路由、low-bit 量化在**边缘多模态**下的相互干扰
- **结论**: token 压缩会改变下游分布、影响 MoE 路由与量化误差——不能各自为政地优化
- **产线**: 端侧多模态部署做系统级调参的必读"避坑指南"

## 🏭 产线落地启示

### 9. [Industrial-YOLO：YOLOv8 边缘缺陷检测系统基准](https://arxiv.org/abs/2606.07659)
- **场景**: 钢板(NEU) + MVTec AD + 汽车/电池制造扩展，实时表面缺陷检测
- **判断**: 面向资源受限硬件做时延-精度权衡，附系统化 benchmark，可作产线选型基线
- **算力账单**: nano/s 档 → Jetson Orin + TensorRT INT8 可达实时帧率

### 10. [答案条件 CoT 蒸馏：3B 小 VLM 快速适配工业质检](https://arxiv.org/abs/2607.10666)
- **场景**: 缺陷类型频繁新增、标注稀缺的工厂视觉检测
- **判断**: 前沿 VLM 按"正确答案+理由"生成解释 → 3B 模型 LoRA 蒸馏，少样本快速换线
- **算力账单**: 3B FP16≈7.2GB / INT4≈1.8GB，一台边缘设备即可部署

## 📰 部署生态动态

- **[dreamforge](https://github.com/rzc156/dreamforge)**（★130，10 天新）：把世界模型"想象"转成机器人策略的纠错训练数据，世界模型 × 策略闭环工具链
- **[MiniCPM-V 4.7-35B-A3B-gguf](https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B-gguf)**：35B MoE(A3B) 版 VLM 已出 GGUF，量化后服务器-边缘两档可切

| 精度 | 字节/参数 | 1B | 3B | 7B |
|------|-----------|----|----|----|
| FP16 | 2 | 2.4GB | 7.2GB | 16.8GB |
| INT8 | 1 | 1.2GB | 3.6GB | 8.4GB |
| INT4 | 0.5 | 0.6GB | 1.8GB | 4.2GB |
