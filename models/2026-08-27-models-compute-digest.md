# 🤖 2026-08-27 模型与算力日报（边缘 / VLA / 小模型）

> 今日扫描 HuggingFace（API×6 + Daily Papers）· GitHub 新仓库×4 · arXiv（3 组）· Reddit（403 被限流）共 4 渠道

---

## 🦾 VLA 行动模型（机器人/操作）

### [W2-VLA（World-to-Wrist）](https://huggingface.co/yuuu94/W2-VLA)
- **什么**: [论文 2608.05369](https://arxiv.org/abs/2608.05369)，Qwen3-VL-4B 底座 + 任务条件化 wrist 未来建模，LIBERO 权重已开源（Apache-2.0，[GitHub ★24](https://github.com/yyyyu120/W2-VLA)）
- **参数量/精度**: 4B · BF16 · Apache-2.0
- **算力需求**: FP16≈9.6GB / INT8≈4.8GB / INT4≈2.4GB；LIBERO 级微调 1×24GB 卡够
- **产线适配**: 小 VLA 里少见的"开源即插"项；量化后 Jetson Orin NX 16GB 可推理，适合视觉引导精细插装工位

### [StreamPI：流式时序 VLA 推理](https://github.com/hku-sail/StreamPI)
- **什么**: [论文 2608.26067](https://arxiv.org/abs/2608.26067)，基于 openpi/π0.5：pair 内双向 + pair 间因果注意力 + KV cache，**零新增参数**给单帧 VLA 加时序记忆；8/26 开源代码
- **算力画像**: 无新权重，显存同底座（π0.5 约 3.3B，INT8≈4GB）；KV cache 免历史帧重算，长程延迟显著下降
- **产线判断**: 对实时控制环是"免费"时序升级，比多帧窗口省算力，可直接移植到开源 VLA 栈

### [Cosmos-Predict2.5-2B GR1 Action-Conditioned](https://huggingface.co/morinoppp/comos_predict_2B_GR1_action_cond)
- **什么**: NVIDIA Cosmos-Predict2.5-2B 微调的 action-conditioned 世界模型：首帧 + 29D 动作 → 13 帧未来视频
- **参数量/精度**: 2B · BF16（EMA 权重 ~4GB）· Apache-2.0
- **算力需求**: 权重小但推理链含 Wan2.1 VAE + Cosmos-Reason1-7B 文本编码器，实为**工作站级**（24GB 单卡）；微调 4×H200 × 4k iter 量级
- **产线适配**: 双臂工位的数字孪生/动作预演（先看后做），不适合真机实时闭环

## 🪶 边缘小模型（<7B）

### [SAM3-LiteRT：Meta SAM3 全端侧版](https://huggingface.co/mlboydaisuke/SAM3-LiteRT)
- **任务**: 开放词表检测+实例分割（ViT-L/14 @1008² + CLIP-L 文本 + DETR head，~830M）
- **参数量**: ~830M · FP16 四段图 ~1.7GB（vision 930MB / text 607MB / head 68MB）
- **门槛**: Pixel 8a 首次 9.2s / **换词重提示 1.9s**；iPhone 17 Pro 重提示 1.3s；⚠️ SAM3 底座为 Meta gated license
- **亮点**: 手机 GPU 上"type 即检测"，open-vocab 对产线换料不重训

### [LibrePicoSAM3：IMX500 传感器内分割](https://huggingface.co/LibreYOLO/LibrePicoSAM3)
- **任务**: promptable 分割（仅 box prompt），PicoSAM3 学生蒸馏自 SAM2.1/SAM3
- **参数量**: 1.37M CNN（比 MobileSAM 少 7 倍参数）
- **门槛**: 单线程 CPU **8.6ms/prompt**，可跑进 Sony IMX500 传感器内；FP32 权重 <3MB
- **亮点**: COCO box-prompt mIoU 0.697（MobileSAM 0.800，质量换 47 倍延迟）；Apache-2.0，工业相机端 ROI 分割的极致轻量选项

### [qualcomm/RTMDet：NPU 实时检测](https://huggingface.co/qualcomm/RTMDet)
- **任务**: 实时目标检测（MMDetection RTMDet-M 移植）
- **参数量**: 27.5M · ONNX float · Apache-2.0
- **门槛**: Snapdragon 8 Gen 3 12.4ms / **工业级 Dragonwing IQ-8275 26.8ms**，峰值内存 5-51MB，纯 NPU
- **亮点**: Qualcomm AI Hub 编译导出自定义权重；Dragonwing 系 SoC 是面向产线的工业计算平台

### [LitePT：轻量点云 Transformer](https://huggingface.co/prs-eth/LitePT)
- **任务**: 3D 点云语义/实例分割与检测（ETH，[论文 2512.13689](https://arxiv.org/abs/2512.13689)）
- **参数量**: S 12.7M / B 45.1M / L 85.9M · MIT · 权重已发布
- **门槛**: 全系 <100MB，Jetson/工控机任意可跑
- **亮点**: NuScenes 82.2 mIoU / ScanNet 76.5；"低层卷积+高层注意力"设计，3D 料箱抓取/堆垛的端侧语义候选

## ⚡ 部署与算力速查

### [Qwen3.8-Flash-Next：6B 激活的 Qwen4 架构预览](https://huggingface.co/Qwen/Qwen3.8-Flash-Next)
- **画像**: 125B 总参/6B 激活 + 51B n-gram embedding + 4B MTP ≈ 180B 权重，FP8 全驻留 ~180GB → 数据中心级；6B 激活算力单卡可推理，n-gram embedding 可 offload，但总量仍是内存瓶颈
- **生态**: 发布 48h 内 unsloth GGUF / FP8 / NVFP4 全线跟进，量化工具链风向标

### [GLM-5.3-Flash](https://huggingface.co/zai-org/GLM-5.3-Flash)（320B/18B 激活，MIT）
- GLM 系列首个原生多模态 MoE，unsloth [GGUF 已出](https://huggingface.co/unsloth/GLM-5.3-Flash-GGUF)；仅作 >30B 对照，不追

| 精度 | 每参数字节 | 显存公式（含 1.2 余量） | 例：4B |
|------|-----------|------------------------|-------|
| FP32 | 4 B | 参数×4×1.2 | 19.2GB |
| FP16/BF16 | 2 B | 参数×2×1.2 | 9.6GB |
| INT8 | 1 B | 参数×1×1.2 | 4.8GB |
| INT4/GGUF Q4 | 0.5 B | 参数×0.5×1.2 | 2.4GB |

## 🏭 产线落地启示

### [SAM3-LiteRT + RTMDet 组合拳](https://huggingface.co/mlboydaisuke/SAM3-LiteRT)
- **场景**: 视觉引导抓取 / 换料不停机（open-vocab 改 prompt）
- **判断**: SAM3 830M 开放词表定位分割（~2GB）+ RTMDet 27.5M NPU 粗定位（<100MB），同驻一台 Dragonwing/QCS 工业 SoC；风险是 SAM3 的 Meta gated license 需走商务

### [W2-VLA INT4 + SAM3-LiteRT 的 Orin 工位](https://huggingface.co/yuuu94/W2-VLA)
- **场景**: 精细插装/装配工位（感知+动作一体）
- **判断**: W2-VLA 4B INT4≈2.4GB + SAM3-LiteRT≈2GB，一台 Orin NX 16GB 可同时驻留；LIBERO 权重已开源，先仿真验收再上真机

## 📰 部署生态动态

### [ClustRS：训练-free 的 VLM token 剪枝](https://arxiv.org/abs/2608.19285)
- 注意力加权聚类选代表 token，576/729 视觉 token 可剪且无需重训——小 VLM 边缘提速杠杆

### [社区信号](https://huggingface.co/papers)
- HF Daily Papers 机器人侧偏 VLA 时序/检索增强（RA-VLA 2608.25585 测试时适配、MA-VLA 2608.25864 多臂协同）；Reddit 仍被 IP 限流，社区信号暂缺
