# 🤖 2026-09-17 模型与算力日报（边缘 / VLA / 小模型）

> 今日扫描 HuggingFace（API×20 + Daily Papers）· GitHub 搜索×16 · arXiv 关键词×10；Reddit 仍 403 限流

---

## 🦾 VLA 行动模型（机器人/操作）

### 1. [VLA-ULAP：边缘超轻量动作预测器，云 VLA 调用砍半](https://arxiv.org/abs/2609.18663)
- **什么**: **7.4M 参数**（含冻结视觉编码器）的本地预测器插值云端大 VLA 调用，输入当前视图+本体感知+动作历史，一次前向出 action chunk，不依赖隐状态、不联网校验 · 09-16
- **算力**: Jetson Orin Nano 单次 **19.9ms / 0.183J**；对照 GR00T 在 RTX A6000 上 **284.3ms / 50.55J**
- **产线**: SO-101 真机保 95.2–100% 成功率，省 47.9–58.0% 耗时、52.1–62.5% 能耗；延迟敏感任务反超 π0.5 11–15.5 点。**"边缘小脑 + 云端大脑"是现实路径**

### 2. [rMuscle：把"肌肉记忆"做成 VLA 推理缓存](https://arxiv.org/abs/2609.19104)
- **什么**: 发现跨次执行的任务相似性**延伸到模型内部状态**；Context Cache 复用视觉 token 输出，Action Cache 复用神经元激活模式，配在线重算+滑窗检索控制显存 · 09-16
- **算力**: RTX 4090 与 **Jetson Thor** 上 **1.29–1.42× 加速**，真机成功率不降；模型无关，可直接套 π0 / GR00T 类底座
- **产线**: 专为结构化工位+重复作业设计，纯部署层收益、零额外算力

### 3. [HuRo：人类视频"机器人化"做 VLA 预训练（CoRL 2026）](https://github.com/3587jjh/HuRo)
- **什么**: 人手动作重定向为关节轨迹 + 抹掉画面中手臂并渲染机器人替身，统一多种标注等级；产出 **63 万 robotized episode / 1.42 亿帧**，输出 LeRobot V2.0 · ★24
- **算力**: 管线开源；下游四个真机任务完成率 **51.5% → 80.3%**，空间/视觉 OOD **34.9% → 72.2%**
- **产线**: 数据侧的突破——**既有工艺录像可换预训练规模**，省真机示范采集

### 4. [ActionPiece：重构自回归 VLA 的动作 tokenizer](https://github.com/DeepCybo-PhysAI/ActionPiece)
- **什么**: 提出 PRC（physical rank consistency）衡量 token 化后动作**邻域物理顺序**是否保留（MSE 看不见的指标），物理秩保持+量化正则联合监督编码器与码本 · [arXiv](https://arxiv.org/abs/2609.18487) · ★13
- **算力**: Qwen3-VL-4B 设定下 LIBERO **94.8%**、未见 LIBERO-Plus **68.8%**、SimplerEnv 71.9%；**只换 tokenizer 不改策略**
- **产线**: 插装/涂胶等需动作细腻度的工位可低成本替换；已接入 PhysBrain1.5

## 🪶 边缘小模型（<7B）

### 5. [Qwen3.5-0.8B-Detection：0.8B 提示式检测 VLM](https://huggingface.co/ReconAI/Qwen3.5-0.8B-Detection)
- **任务**: Qwen3.5-0.8B + COCO 检测 SFT + **GSPO RL**；prompt 列类别 → 直接回 JSON 框，训练时混入图内不存在的类别抗干扰 · Apache-2.0 · 09-13
- **算力**: 0.8B → FP16≈**1.9GB** / INT4≈**0.5GB**，Orin Nano / 工业 PC / 手机 NPU 均可
- **亮点**: <1B 做开放词表 grounding，把"指定类别检测"变成 VLM 一句话任务

### 6. [sam3-p150：SAM3 跑上 Tenstorrent NPU（非 NVIDIA 路线）](https://huggingface.co/changh95/sam3-p150)
- **任务**: Meta **SAM3（840.5M，ViT-H/14 + fusion encoder）**文本提示开放词表实例分割，整套迁到单张 **Tenstorrent Blackhole p150a**（tt-nn）：图像+名词短语进，掩码/框/分数出
- **算力**: 840M → FP16≈**2.0GB**，NPU 侧无需 CUDA 生态；模型卡含精度与速度对比 · [上游 SAM3](https://arxiv.org/abs/2511.16719)
- **亮点**: 边缘感知算力**去 NVIDIA 化**的实锤，自研/国产加速卡适配可参考其 port 流程

## ⚡ 部署与算力速查

### 7. [Is INT8 Portable? 七类硬件实测：量化一次、到处部署不成立](https://arxiv.org/abs/2609.16085)
- **实验**: 固定 ONNX 产物与 scale，只让整数 kernel/ISA 变；覆盖 ARM/x86 CPU、独显、**Jetson AGX Orin iGPU 与 NVDLA**、**Qualcomm Hexagon HTP**、**DEEPX DX-M1**
- **三条结论**: ① 加速方向由点积 ISA 决定——有 ARM dotprod/SDOT、x86 VNNI 快 **2.1×**，没有反慢 **1.7×**；② INT8 输出不可移植：同 kernel 1000/1000 一致，跨 kernel 仅 **958–965/1000**，top-1 看不出（对逐输入确定性场景是隐患）；③ 厂商 NPU 掌控量化：自带 QDQ 图可**静默失效**（0.75 → 0.005，编译/剖析/运行全无报错）
- **旁证**: 边缘 NPU 延迟瓶颈是输出/device-to-host 传输量而非算力；发布 32 份报告+脚本

### 8. [EdgeVL 系：量化感知蒸馏 + 跨模态对齐（含非 RGB）](https://arxiv.org/abs/2609.16689)
- **什么**: 把 CLIP 表征蒸馏进轻量编码器并做 QAT，用统一 teacher-anchored 框架联合优化蒸馏与量化，再以轻量 cross-attention adapter 用 RGB 语义补强非 RGB · 09-15
- **算力**: 面向边缘开放词表分类；**红外/热成像/多光谱**恰是工业质检常见输入。论文阶段、无公开权重——列观察

| 精度 | 字节/参数 | 显存（×1.2） | 0.8B | 5.4B | 7.4M |
|------|-----------|--------------|------|------|------|
| FP16/BF16 | 2 B | 参数×2×1.2 | 1.9GB | 13.1GB | 18MB |
| INT8 | 1 B | 参数×1×1.2 | 1.0GB | 6.5GB | 9MB |
| INT4/GGUF Q4 | 0.5 B | 参数×0.5×1.2 | 0.5GB | 3.3GB | 4MB |

## 🏭 产线落地启示

### [VLA-ULAP](https://arxiv.org/abs/2609.18663) + [rMuscle](https://arxiv.org/abs/2609.19104)：两种"不加算力提响应"的路子
- ULAP 走**架构混合**（7.4M 本地 + 云端），适合允许联网的柔性工位，单台 Orin Nano 承接；rMuscle 走**缓存复用**，适合离线、动作高度重复的固定工位。可叠加：缓存挡重复、小脑挡延迟

### [Qwen3.5-0.8B-Detection](https://huggingface.co/ReconAI/Qwen3.5-0.8B-Detection) + [sam3-p150](https://huggingface.co/changh95/sam3-p150)：感知端边缘账单
- 出框 0.8B（INT4 0.5GB）+ 分割 840M（2GB），一台工位级设备覆盖"定位+精细轮廓"；走非 NVIDIA NPU 前先按 INT8 报告逐机型复验量化产物

## 📰 部署生态动态

- **[LUMIN](https://arxiv.org/abs/2609.04775)**：轻量工业检测网络，PSP 采样**零 backbone 前向**建 memory bank（传统 FPS/K-Means 需数分钟至数小时），直击产线毫秒节拍
- **[ApexInspect-AI](https://github.com/imtarget05/ApexInspect-AI)**：工厂质检 Agent 脚手架，YOLOv8 ONNX 边缘推理 ~28 FPS + SOP RAG + 人工复核回路
- **[MolmoAct2-Think](https://huggingface.co/allenai/MolmoAct2-Think)**（5.45B，出动作前先预测 10×10 离散深度图）：09-17 出现镜像再传，FP16≈13.1GB
- **[ISTA-DASLab Qwen3.8-27B-GSQ-RCO-GGUF](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF)**：GSQ+RCO 量化管线 102 万下载，其低位方法可反哺边缘 VLM 量化（大模型仅作方法参考）
