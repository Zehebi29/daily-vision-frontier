# 🤖 2026-08-17 模型与算力日报（边缘 / VLA / 小模型）

> 今日扫描了 HuggingFace（搜索脚本 195 条 + 模型卡直读）· HF Daily Papers · GitHub（Search API）· arXiv · Reddit（hot.json，返回 403 未取到）共 5 个渠道；精选 12 条，全部附参数量与显存画像。

---

## 🦾 VLA 行动模型（机器人/操作）

### [LingBot-VLA-V2-6B（robbyant）](https://huggingface.co/robbyant/lingbot-vla-v2-6b)
- **什么**: 面向真实机器人应用的 VLA foundation model。60,000 小时预训练数据（50k 小时、20 种机器人构型的轨迹 + 10k 小时第一人称人类视频）；action expert 内用 sparse MoE 分层，统一动作空间覆盖机械臂/末端/夹爪/灵巧手/腰/头/移动底盘；用 LingBot-Depth + DINO-Video 做未来预测蒸馏（dual-query distillation）。V2 新增 RobotWin 格式 checkpoint（[lingbot-vla-v2-6b-robotwin](https://huggingface.co/robbyant/lingbot-vla-v2-6b-robotwin)），可直接进 LeRobot 生态。
- **参数量 / 精度**: 6.38B · 官方 BF16，可自行 INT8/INT4
- **算力需求**: BF16 权重 ≈ 6.4×2×1.2 ≈ **15.4GB** → 单张 24GB 卡（RTX 4090 / L4 / A5000）即可推理；INT8 ≈ 7.7GB；INT4 ≈ 3.8GB → Jetson Orin 16GB 可跑、32GB 舒适。训练为大规模预训练，量级在数千 GPU-hours（A100 级），但社区版面向 SFT/微调场景。
- **产线适配**: ✅ 已跨 20 种机器人构型，动作表示统一，多工位复用同一套权重；Apache-2.0 商用无碍。边缘侧建议 INT8 上 Orin 32GB 或工控机单卡 24GB。

### [Hy-Embodied-0.5-VLA（腾讯，UMI 版）](https://huggingface.co/tencent/Hy-Embodied-0.5-VLA-UMI)
- **什么**: 腾讯 Robotics X × Hy 团队的全栈轻量 VLA（数据采集→预训练→SFT→RL→部署）。基于 Hy-Embodied-0.5 MoT 骨干 + flow-matching action expert + 紧凑 memory encoder（多帧历史）+ delta-chunk 动作表示。10000+ 小时 UMI 演示数据，RoboTwin 2.0 基准 **90.9% / 90.1%**（Clean / Randomized），跨 4 种真实机器人迁移。同系列还有 [lerobot/hy_vla_robotwin](https://huggingface.co/lerobot/hy_vla_robotwin) 与 [lerobot/hy_vla_umi](https://huggingface.co/lerobot/hy_vla_umi) 两个 LeRobot 格式官方 checkpoint（7-28 发布）。
- **参数量 / 精度**: 实测权重 **4.53B**（命名 "0.5" 指系列/骨干规模，非总参数）· BF16 官方，Apache-2.0
- **算力需求**: BF16 ≈ 4.5×2×1.2 ≈ **10.9GB** → 16GB 卡即可；INT8 ≈ 5.4GB → **Orin 16GB 可跑**；INT4 ≈ 2.7GB → Orin 8GB 可试。注意 flow-matching 推理含 10 步 denoise（config `num_steps: 10`），实际是 10 次前向，RTX 4090 上约 5–15 Hz，边缘 INT8 约 1–3 Hz，适合 5–10 Hz 的低速操作。
- **产线适配**: ✅ 本批最接近"上产线"的 VLA：Apache-2.0 商用 + 轻量权重 + UMI/LeRobot 数据闭环齐全，分拣/简单装配工位可直接评估。

### [Xiaomi-Robotics-1-VLABench（小米）](https://huggingface.co/XiaomiRobotics/Xiaomi-Robotics-1-VLABench)
- **什么**: 小米机器人 1 号人形 VLA 的 VLABench 评测 checkpoint（`MiBoTForActionGeneration` 自定义架构），含权重、processor、tokenizer 与动作归一化统计，覆盖 VLABench 5 个 track（in-distribution / cross-category / common-sense / semantic instruction / unseen texture）。
- **参数量 / 精度**: **5.05B** · Apache-2.0（checkpoint 与配套代码）
- **算力需求**: 与 6B 同级：BF16 ≈ 12GB（16GB 卡）；INT8 ≈ 6GB；INT4 ≈ 3GB。评测配置 action chunk=10、replan=5，参考环境要求 PyTorch 2.8 + FlashAttention 2。
- **产线适配**: ⚠️ 当前定位是**评测用 checkpoint**（VLABench），非开箱部署包；可作为人形 VLA 与 VLABench 评测的对标基准，直接商用还需等待官方完整部署栈。

### [UnifoLM-VLA-0（宇树 Unitree）](https://huggingface.co/unitreerobotics/UnifoLM-VLA-Base)
- **什么**: 宇树 UnifoLM 系列的人形机器人操作 VLA，从 VLM 继续预训练到"具身大脑"，增强 2D/3D 空间语义与物理常识；官方称单策略完成 12 类复杂操作任务。含 Base 与 [Libero](https://huggingface.co/unitreerobotics/UnifoLM-VLA-Libero) 两个 checkpoint，GitHub ★560。
- **参数量 / 精度**: HF 未暴露 safetensors 参数索引，官方未明确公开（7B 级人形 VLA 惯例）；按 7B 估算
- **算力需求**: 7B BF16 ≈ 17GB（24GB 卡）；INT8 ≈ 8.4GB；INT4 ≈ 4.2GB → Orin 8GB 可试
- **产线适配**: ❌ **License 硬伤：CC BY-NC-SA 4.0（非商用）**，工业产线直接商用不合规；适合高校/研究所做人类形态操作研究。

### [W2-VLA（World-to-Wrist）](https://huggingface.co/yuuu94/W2-VLA)
- **什么**: 用 **Qwen3-VL-4B-Instruct + V-JEPA2** 做 task-conditioned future wrist modeling 的细粒度操作 VLA（arXiv 2608.05369），已放 LIBERO checkpoint 与训练数据。
- **参数量 / 精度**: 4B LLM 级 + V-JEPA2 视觉主干 ≈ 5B 上下 · Apache-2.0
- **算力需求**: ≈ 4B 级：BF16 ≈ 10GB；INT8 ≈ 5GB；INT4 ≈ 2.5GB → Orin 16GB（INT8）可评估
- **产线适配**: ⚠️ 学术新方法（8-8 发布，★21），腕部未来建模对精密装配有吸引力，但成熟度低，先以 LIBERO 基准验证。

## 🪶 边缘小模型（<7B）

### [Moondream 3.1（9B-A2B MoE VLM）](https://huggingface.co/moondream/moondream3.1-9B-A2B)
- **任务**: 小 VLM（视觉问答 + 开放词汇检测 + 指点 + 描述，全部原生结构化输出）
- **参数量**: **9.27B 总 / 2B 激活**（MoE，推理算力按 2B 计）· 官方 Photon 推理引擎支持 NVIDIA Ampere+ 与 Apple Silicon；另有社区 4-bit 版
- **显存 / 推理门槛**: 权重侧按 9B 计：INT8 ≈ 11GB、INT4 ≈ 5.6GB → **Orin 16/32GB**；计算侧每 token 仅 2B 激活，单帧问答延迟远低于同尺寸 dense 模型
- **亮点**: 一个模型同时给"看、说、指、框"，检测/指点技能对视觉 Agent 的 grounding 非常实用；license 为 moondream 自有模型协议（商用需核对其条款）

### [Ultralytics YOLO26](https://huggingface.co/Ultralytics/YOLO26)
- **任务**: 检测 / 实例分割 / 语义分割 / 深度 / 姿态 / OBB 六合一实时视觉
- **参数量**: n→x 五档（YOLO26n ≈ 2.6M 参数级），HF 模型卡 COCO mAP@0.5:0.95 **57.5**
- **显存 / 推理门槛**: n 级 FP16 权重仅 ~5MB 级，INT8 TensorRT 在 Jetson Orin Nano 上数百 FPS；x 级（~57M 参数）单卡 GPU 即可
- **亮点**: 一条链路覆盖产线视觉八成任务；⚠️ **AGPL-3.0，商用需购 Enterprise License**——选型时必须把许可费计入成本

### [Google TIPSv2（B/14）](https://huggingface.co/google/tipsv2-b14)
- **任务**: 零样本分类 / 特征提取 /（配 DPT head）零样本分割
- **参数量**: 86M 视觉 + 110M 文本 ≈ **0.2B** · Apache-2.0 · arXiv 2604.12012
- **显存 / 推理门槛**: FP16 ≈ 0.2×2×1.2 ≈ **0.5GB** → 瑞芯微/地平线 NPU、Orin Nano、工控机 CPU 无压力
- **亮点**: 带空间感知的对比学习表征，B/14 之外还有 L/14、SO400m/14、g/14（最大 1.5B）——零样本分割能力对"未见缺陷类型"的质检预筛有实际价值

### [bench-labs/objectmodel-v1](https://huggingface.co/bench-labs/objectmodel-v1)
- **任务**: NMS-free 端到端检测器（DETR 系，global semantic latent + query-conditioned 全分辨率金字塔采样）
- **参数量**: 20–40M 实时检测器档位（作者自述对标区间）· Apache-2.0
- **显存 / 推理门槛**: 单卡 RTX 5090 训练 100 epoch 完成；ONNX 导出已实现，边缘可部署
- **亮点**: 难得的"诚实科研"样例——COCO AP 35.8 且明确声明"不是 benchmark claim、未跑多 seed/消融"，v1 定位为研究 checkpoint。可作为检测架构研究动向观察，**不建议直接上产线**

## ⚡ 部署与算力速查

### [Ling-3.0-tiny-int4（inclusionAI）](https://huggingface.co/inclusionAI/Ling-3.0-tiny-int4)
- **显存估算**: 7.9B 总 / **1.3B 激活**（128 routed + 1 shared expert，每 token 8 expert），INT4 权重 ≈ 7.9×0.5×1.2 ≈ **4.7GB**
- **量化方案**: 官方同时给 BF16 / FP8 / INT4；**MIT license**；官方验证平台 DGX Spark、Apple Silicon MacBook/Mac mini
- **边缘适配**: 轻量 hybrid-linear（KDA+MLA 3:1）推理 MoE，配 INT4 可在 Mac mini / DGX Spark 这类统一内存设备本地跑 agentic 推理——作为"边缘大脑"给视觉 Agent 做规划层的低成本选项（纯语言模型，但部署价值明确，故收录）

### [Qwen3.8-27B GGUF / AWQ 生态（unsloth 等）](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF)
- **显存估算**: 27.8B 多模态（image-text-to-text，Apache-2.0，8-5 发布），INT4/GGUF Q4 ≈ 27.8×0.5×1.2 ≈ **17GB** → 单卡 24GB；FP8 ≈ 27GB；AWQ INT4 版（[cyankiwi](https://huggingface.co/cyankiwi/Qwen3.8-27B-AWQ-INT4)）同档
- **生态信号**: unsloth 版下载 194 万+、trending 1399，一周内涌现几十个 GGUF/AWQ/abliterated 变体——27B VLM 已成"本地多模态 + 机器人高维推理"的事实标准档位
- **边缘适配**: INT4 可上 Orin 64GB / 工作站单卡；对产线是"重武器"，一般留给上位机做视觉 Agent 的复杂推理，不直接进控制器

### [Red Hat 量化系列（w4a16 / w8a8）](https://huggingface.co/RedHatAI/Qwen3.5-9B-quantized.w4a16)
- **显存估算**: Qwen3.5-9B w4a16 ≈ 9×0.5×1.2 ≈ **5.4GB**（+KV cache）；[Qwen3.5-4B w8a8](https://huggingface.co/RedHatAI/Qwen3.5-4B-quantized.w8a8) ≈ 4×1×1.2 ≈ **4.8GB**
- **量化方案**: Red Hat 出品的生产级量化路线（企业部署导向），w4a16/w8a8 覆盖"精度保留 vs 显存下降"两档，比社区随意 GGUF 更可信
- **边缘适配**: 9B w4a16 → Orin 16GB 可跑；4B w8a8 → Orin 8GB。适合产线私有化小 VLM 服务

## 🏭 产线落地启示

### [Hy-Embodied-0.5-VLA 上分拣/装配工位](https://github.com/Tencent-Hunyuan/Hy-Embodied-0.5-VLA)
- **场景**: 机器人分拣、简单上下料、双机械臂协同（UMI 格式天然支持 bimanual）
- **判断**: ✅ 本批最该先做 POC 的 VLA——Apache-2.0 商用无碍、4.5B 权重 INT8 上 Orin 16GB、RoboTwin 2.0 双 90%+、UMI/LeRobot 采集-训练-部署闭环完整。短板是 flow-matching 10 步 denoise 的延迟，需测实际 Hz 是否满足节拍。
- **算力账单**: Jetson Orin 16GB 开发套件 ~¥1.2–1.8 万；如追求 10 Hz+ 用 4090 工控机 ~¥3–4 万。相对自研视觉+轨迹规划方案，VLA 主要省的是**部署代码量**而非硬件。

### [LingBot-VLA-V2 多工位复用](https://github.com/robbyant/lingbot-vla-v2)
- **场景**: 20 种机器人构型的跨本体迁移、多工位共权重
- **判断**: ✅ 60k 小时预训练 + 统一动作空间 + Apache-2.0，是"一套权重吃多个工位"的正面案例；6.4B 规模 INT4 ≈ 3.8GB，Orin 32GB 单机可同时跑 2 个工位推理。⚠️ 预训练数据与机器人类型偏科研/通用场景，专用工艺（如点胶、锁付）仍需自采数据 SFT。
- **算力账单**: Orin 32GB ~¥2.5–3 万/台，覆盖 2 工位；对比每工位一台 4090 工控机（~¥4 万）有明显成本优势。

### [YOLO26 + TIPSv2 做视觉质检预筛](https://huggingface.co/Ultralytics/YOLO26)
- **场景**: 产线实时缺陷/工件检测（YOLO26）+ 未见类型异常零样本预筛（TIPSv2）
- **判断**: ✅ 检测层 YOLO26 仍是性价比之王（n 级几 MB 权重、Orin 上数百 FPS）；TIPSv2 0.2B 可做"语义漂移"哨兵。⚠️ 两者都是 Apache/AGPL 混合，YOLO26 商用必须买 Ultralytics Enterprise License，报价要提前入账。
- **算力账单**: Orin Nano 8GB（~¥3500）+ 相机，单工位硬件 <¥1 万；质检准确率受数据标注质量主导，模型本身不是瓶颈。

## 📰 部署生态动态

### [LeRobot 官方发布 Hy-VLA checkpoints（robotwin/umi 双格式）](https://huggingface.co/lerobot/hy_vla_robotwin)
- 轻量 VLA 正在"LeRobot 化"：腾讯 Hy-VLA 权重已可直接 `from_pretrained` 进 [LeRobot](https://github.com/huggingface/lerobot)（★26.7k，8-16 仍在更新）生态，与 [SmolVLA](https://huggingface.co/lerobot/smolvla_base)（单卡可训、消费级硬件部署）并列。边缘 VLA 的"标准数据格式 + 标准推理接口"正在收敛，这比单点模型突破更值得跟。

### [DreamX-Phi 1.0：Action-Conditioned 操作视频世界模型](https://huggingface.co/papers)（arXiv 2608.13489）
- Phi 系轻量世界模型：输入当前帧 + 语言指令 + 动作序列（末端位姿/夹爪），预测未来观测；论文强调"真实感 ≠ 保真度"（会动错手臂/丢操作物）。对 VLA 的**想象式规划/仿真预演**有意义，轻量级可进边缘做 rollout 校验。

### [H2R-Bench：人→机器人操作视频生成基准](https://huggingface.co/papers)（arXiv 2608.13049）
- 把人手演示视频生成"可迁移到机器人"的操作视频作为评测对象，回应"人数据多、机器人数据贵"的行业痛点——直接影响 VLA 预训练数据的供给路线。

### [SKILLER：小语言模型的技能抽取 RL](https://huggingface.co/papers)（arXiv 2608.10538）
- 在 small language model 上用 language-level RL 抽可复用 skill，降低 agent 对闭源大模型的推理依赖——与"边缘做认知层"的方向一致，适合视觉 Agent 的 skill 库落地。

### [SPARGen：原生多模态生成统一空间感知与推理](https://huggingface.co/papers)（arXiv 2608.14138）
- 把几何结构恢复、对应关系、空间关系统一进生成式多模态框架，替代"任务专属架构 + 外部几何模块"的碎片化做法；对 VLA 的 3D grounding 与机械臂空间推理是值得关注的架构方向。

---

### 算力速查表（本批重点模型）

| 模型 | 参数量 | FP16 显存 | INT8 | INT4 | 最低门槛 |
|---|---|---|---|---|---|
| LingBot-VLA-V2 | 6.4B | 15.4GB | 7.7GB | 3.8GB | 24GB GPU / Orin 16GB(INT4) |
| Hy-Embodied-0.5-VLA | 4.5B | 10.9GB | 5.4GB | 2.7GB | 16GB GPU / Orin 8GB(INT4) |
| Xiaomi-Robotics-1 | 5.1B | 12.1GB | 6.1GB | 3.0GB | 16GB GPU / Orin 16GB(INT8) |
| Moondream 3.1 | 9.3B/2B active | 22GB(权重) | 11GB | 5.6GB | Orin 16GB(INT4) |
| TIPSv2 B/14 | 0.2B | 0.5GB | 0.2GB | — | NPU / 嵌入式无压力 |
| Ling-3.0-tiny | 7.9B/1.3B active | 19GB | — | 4.7GB | Mac mini / DGX Spark / Orin 32GB |

> 公式：参数量 × 每参数字节 × 1.2（FP16=2B、INT8=1B、INT4=0.5B）；MoE 按"权重全量"估算显存、按"激活参数量"估算算力。
