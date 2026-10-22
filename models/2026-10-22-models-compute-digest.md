# 🤖 2026-10-22 模型与算力日报（边缘 / VLA / 小模型）

> 今日扫描 HuggingFace（API 全量 547 个近 3 周新模型 + 模型卡精读）· arXiv（cs.RO/cs.CV 当日列表 + 7 组关键词）· GitHub（4 组新仓库搜索）· HF Daily Papers · 量化/部署生态 —— 共 5 个渠道

---

## 🦾 VLA 行动模型（机器人/操作）

### 1. [REKI-2B（Kyutai）](https://huggingface.co/kyutai/reki-2b)
- **什么**: Qwen3.5-2B VLM + 10 层 DiT 动作专家（768 隐层），flow-matching 出 1s/50 步动作块；32 个 register token 做「近期记忆」，缓存复用，读记忆耗时 **<1%**
- **参数量**: **2.4B** → FP16≈5.8GB / INT8≈2.9GB / INT4≈1.45GB
- **算力**: 单张 H100 编译后 **21.8ms/块**（双 256×256 视角）；Jetson Orin 32GB 估算 0.15–0.25s/块 → 4–6Hz，够非高速抓放
- **产线判断**: 纯公开数据预训练，OOD 最强（LIBERO-Plus 90.4 / RoboTwin Rand 65.8）；但权重 **CC-BY-NC-SA 4.0 不可商用**，上产线须先谈授权

### 2. [FlowVLA：把「倒多少」从动作里拆出来](https://arxiv.org/abs/2610.29692)
- **什么**: 共享 π0.5 action expert 负责接近/倾倒/回位，另一路 target-independent 估计器融合视觉 + 关节 + **腕部力矩** + 力信念递推，估已转移质量来决定何时收手
- **参数量**: π0.5 量级 **~3.3B** → FP16≈**7.9GB** / INT8≈4.0GB / INT4≈2.0GB
- **算力**: 倒液稳态时画面几乎不动，纯视觉 VLA 判不准——多一路低维力信号，比堆视觉 token 便宜得多
- **产线判断**: 定量灌装/涂胶/配料这类「过程量」工位，13.1g MacroMAE、53.7% 落在 ±10% 内；需机械臂带 F/T 传感器，是低成本硬件增项换精度

### 3. [VLA-Rolling：少步去噪 + 动作尾复用](https://arxiv.org/abs/2610.25043)
- **什么**: 推理框架而非新模型——把上一块未执行的动作尾当作下一块的初始化，按逐动作置信度分配去噪预算，**底座模型冻结**
- **算力**: 16 组 模型×benchmark 全部降本，最高 **1.48×** 加速；14 组成功率同时提升（最高 +15.08 点）
- **产线**: π0.5 / SmolVLA / X-VLA / MolmoAct2 全员适配 → 现有部署直接提速，无需重训，是「零成本上线」型收益

## 🪶 边缘小模型（<7B）

### 4. [NEU 钢板缺陷双小模型：TinyViT 113k vs CNN 106k](https://huggingface.co/Zainulabedin1/vit-casting-defect) · [3D 打印 stringing CNN](https://huggingface.co/Zainulabedin1/print-defect-cnn)
- **任务**: 六类热轧钢板表面缺陷分类；FDM 打印 stringing 二分类
- **参数量**: **113k / 106k** → FP32 仅 **0.45MB / 0.42MB**，CPU 训练 14 分钟
- **算力**: MCU/树莓派即可实时；无需 GPU
- **亮点**: 罕见的「负面结论也照实写」——from-scratch ViT 76.1% 输给同尺寸 CNN 85.0%，小数据上卷积归纳偏置仍胜；stringing 模型对缺陷类 100% 召回，符合质检筛查取舍

### 5. [MS2CAST：不用光流的视频异常检测](https://arxiv.org/abs/2610.29649)
- **任务**: 半监督预测式 VAD，MViTv2-S + ConvNeXt-T 多尺度交叉注意力融合，SwinLSTM / VMRNN 两档时序模块可换
- **参数量**: 双骨干合计 ~62M → FP16≈**0.15GB**，INT8≈0.08GB
- **算力**: 砍掉光流网络是最大收益——光流通常占 VAD 推理 60%+ 算力；现在单卡可跑多路摄像头
- **产线**: 装配线/仓储的在线异常监控，比追 SOTA 更值钱的是「去掉光流」这个工程决策

## ⚡ 部署与算力速查

### 6. [QSelect：给星载机器人拼一个「混血」低比特权重](https://arxiv.org/abs/2610.29302)
- **方法**: 逐线性层在 AWQ / GPTQ / AutoRound 三族里选一个量化器，按最终 next-token 分布打分，仅当对 BF16 的 forward KL 下降才接受替换
- **判断**: 无需标签、无需调阈值，产出**单个静态低比特工件**——正是产线/航天「配置受控、结果可复现」的要求，比裸 PTQ 可信
- **迁移**: 同一套流程可直接用于 VLA 的 VLM 主干压缩

### 7. [Specter：量化草稿 + 专家卸载（ASPLOS'27）](https://arxiv.org/abs/2511.14102)
- **问题**: MoE 显存超单卡 → 专家放主机内存，PCIe 成为关键路径瓶颈
- **方法**: 轻量**量化草稿模型**在设备上多步预判未来专家激活，提前搬运再验证
- **数字**: 单请求 TPOT 平均 **1.50×**、最高 **1.88×** 加速 → 单张消费级卡跑 MoE 变得实用

## 🏭 产线落地启示

### 8. [π0 / π0.5 微调洪流：HF 一周新增 100+ 检查点](https://huggingface.co/models?search=pi05&sort=createdAt&direction=-1)
- **场景**: 抓放、分拣、装盒、理线——大量 `pi05-so101-*`、`smolvla_so101_tray` 型个人/小团队权重
- **判断**: π0 系已成**事实上的微调底座**，SO-101 机械臂 + LeRobot 让单工位换型从「项目」变成「一周」；[官方 SO-101 仿真场景](https://huggingface.co/lerobot/so101-tabletop-isaac) 也已放出，可在仿真里先筛配方
- **算力账单**: π0.5 级 3.3B 微调需 1×A100/H100 数天；推理侧 SmolVLA 0.25B ≈ 0.6GB 显存，一台工控机带得动

## 📰 部署生态动态

- **[NVIDIA Nemotron-3.5-Super-VL-120B-A12B-NVFP4](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Super-VL-120B-A12B-NVFP4)**：120B 总参 / 12B 激活直接发 NVFP4 官方量化版 —— 只作对比：即便 4bit，权重仍 ~60GB，与边缘无关，但「官方首发即量化」已成大厂标配
- **[lerobot/so101-tabletop-isaac · mujoco](https://huggingface.co/lerobot/so101-tabletop-isaac)**：官方 SO-101 桌面任务仿真场景上架，sim2real 前先做配方筛选
- **REKI 工具链**：`pip install reki-vla` 已在 PyPI，且已去掉 flash-attn / causal-conv1d 编译依赖 —— 边缘镜像构建难度显著下降

| 精度 | 字节/参 | 0.5B | 2.4B | 7B |
|------|---------|------|------|----|
| FP16 | 2 | 1.2GB | 5.8GB | 16.8GB |
| INT8 | 1 | 0.6GB | 2.9GB | 8.4GB |
| INT4 | 0.5 | 0.3GB | 1.45GB | 4.2GB |
