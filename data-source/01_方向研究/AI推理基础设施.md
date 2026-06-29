---
schema_version: 1
title: AI推理基础设施
category: 方向研究
status: tracking
updated_at: 2026-06-29
confidence: high
tags:
  - AI
  - 推理
  - 数据中心
  - 资本开支
sources:
  - name: NVIDIA FY2027 Q1 results
    url: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx
  - name: Microsoft FY2026 Q3 results
    url: https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast
  - name: Amazon Q1 2026 results
    url: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-First-Quarter-Results/default.aspx
  - name: NVIDIA and IREN strategic partnership
    url: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-IREN-Announce-Strategic-Partnership-to-Accelerate-Deployment-of-up-to-5-Gigawatts-of-AI-Infrastructure/default.aspx
  - name: Alphabet 2026 Q1 earnings call
    url: https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx
  - name: Microsoft FY2026 Q3 earnings call
    url: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3
  - name: NVIDIA liquid cooling AI factories
    url: https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/
  - name: NVIDIA Vera Rubin for science
    url: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Delivers-World-Class-Supercomputers-for-Science/default.aspx
  - name: NVIDIA and AWS AI production scale
    url: https://blogs.nvidia.com/blog/nvidia-aws-ai-production-scale/
  - name: Amazon and Pinterest AI infrastructure agreement
    url: https://www.aboutamazon.com/news/aws/pinterest-aws-4-billion-ai-infrastructure-deal
  - name: OpenAI Broadcom Jalapeno inference chip
    url: https://openai.com/index/openai-broadcom-jalapeno-inference-chip/
  - name: Qualcomm data center roadmap
    url: https://www.qualcomm.com/news/releases/2026/06/qualcomm-unveils-comprehensive-data-center-roadmap-for-the-agent
  - name: Firmus NVIDIA DSX AI Factory campus
    url: https://firmus.co/newsroom/firmus-to-build-170-000-gpu-ai-factor-y-campus-with-nvidia-for-global-ai-natives
---

# AI推理基础设施

> 记录日期：2026-06-20
> 定位：方向研究，不构成投资建议。

## 1. 当前趋势

2026 年 AI 的核心变化，是从“训练大模型”继续转向“大规模使用模型”。训练决定模型能力上限，推理决定 AI 能不能进入真实业务流量。用户每天使用搜索、办公、客服、代码、图片、视频、Agent 时，都会持续消耗推理算力。

| 趋势信号 | 来源层级 | 关键证据 | 强度 | 对方向判断的影响 |
| --- | --- | --- | --- | --- |
| 数据中心收入继续高速增长 | tier_1 | NVIDIA FY2027 Q1 总收入 816 亿美元、数据中心收入 752 亿美元，数据中心网络收入 148 亿美元 | 高 | 增强 |
| AI 收入进入规模化阶段 | tier_1 | Microsoft FY2026 Q3 披露 AI 业务年化收入运行率超过 370 亿美元 | 高 | 增强 |
| 云厂商继续投入 AI 基础设施 | tier_1 | Amazon Q1 2026 披露 AWS 增长并强调 Trainium、NVIDIA GPU 与 AI 基础设施投入 | 高 | 增强 |
| AI 工厂扩容向园区和电力管线前置 | tier_1 | NVIDIA 与 IREN 计划在全球数据中心管线中部署最多 5GW、面向 DSX 架构的 AI 基础设施 | 高 | 增强 |
| 技术基础设施 CapEx 同时覆盖服务器、数据中心和网络 | tier_1 | Alphabet Q1 2026 CapEx 达 357 亿美元，技术基础设施投入约 60% 用于服务器、40% 用于数据中心和网络设备 | 高 | 增强 |
| Agent 和 Foundry token 使用量开始验证推理需求 | tier_1 | Microsoft 披露 AI ARR 超过 370 亿美元，Foundry 年内将有超过 300 家客户处理超 1 万亿 token | 中高 | 增强 |
| 高温液冷成为下一代 AI 工厂基础设计 | tier_1 | NVIDIA 披露 Rubin 代 AI 基础设施采用 100% 液冷架构，DSX 参考设计可减少机械制冷和设施冷却用水需求 | 中高 | 增强 |
| 整机架系统和科研/工业客户继续采用下一代平台 | tier_1 | NVIDIA Vera Rubin 平台披露单机架 AI for science 算力、FP64 能力、NVLink-C2C、ConnectX-9、BlueField-4 和直接液冷，LRZ、NERSC、LANL 等系统将采用 | 中高 | 增强 |
| 应用公司以多年云承诺锁定 AI 基础设施 | tier_1 | Pinterest 与 AWS 达成至 2031 年的 40 亿美元云服务承诺，用于 AI 训练、推理、视觉搜索、推荐和 Pinterest Assistant | 高 | 增强 |
| 模型厂商和芯片厂商推进定制推理平台 | tier_1 | OpenAI/Broadcom Jalapeno 推理芯片、Qualcomm Dragonfly 数据中心路线和 Modular 收购共同指向 ASIC、CPU、加速器、连接和软件栈一体化 | 中高 | 增强 |
| 区域 AI 工厂进入承购和园区建设阶段 | tier_1 | Firmus 与 NVIDIA 合作规划印尼 Batam 360MW DSX AI Factory，覆盖 17 万颗 AI 加速器和多年客户承购协议 | 中高 | 增强 |
| 推理从单次训练变成持续使用需求 | tier_1/tier_3 | 搜索、办公、客服、代码、多模态和 Agent 都会持续消耗推理算力 | 高 | 增强 |

## 2. 核心瓶颈

推理扩张后的瓶颈不只是 GPU 数量，而是单位 token 成本、延迟、吞吐、调度效率和能耗。推理如果成为 AI 应用底层流量，瓶颈会继续外溢到网络、存储、电力和散热。

| 瓶颈 | 严重程度 | 触发条件 | 受影响环节 | 验证信号 |
| --- | --- | --- | --- | --- |
| 推理算力 | 高 | 推理请求量、多模态和 Agent 调用持续增长 | GPU / ASIC / 服务器 | 数据中心收入、推理芯片出货和云厂商扩容 |
| 单 token 成本 | 高 | 推理使用量增长但成本下降不够快 | 云平台 / 模型服务 | AI 收入能否覆盖折旧、电力和芯片成本 |
| 网络和存储 | 中高 | 集群规模扩大，节点间通信和数据访问压力上升 | 交换机 / 网卡 / 光模块 / 存储 | 数据中心网络收入、光模块和交换芯片需求 |
| HBM 和数据中心存储 | 中高 | 推理和训练集群扩大，HBM、服务器 DRAM 和企业级 SSD 被高优先级 AI 需求吸收 | 内存 / SSD / AI 服务器 | HBM 出货、服务器 DRAM 价格、企业级 SSD 容量和交期 |
| 电力与散热 | 高 | 高密度推理集群提高机柜功率和散热压力 | 电力设备 / 液冷 / 数据中心 | 并网延迟、液冷渗透率、变压器和 UPS 订单 |
| 异构推理软件栈 | 中高 | CPU、GPU、NPU、ASIC 和云端/边缘部署并存，性能可移植性和调度效率成为瓶颈 | 编译器 / 运行时 / 云平台 | Modular 类软件栈、向量检索加速、跨硬件部署效率 |
| 调度系统 | 中 | 多模型、多租户和低延迟推理需求提升 | 云平台 / 推理服务 | 推理服务效率、延迟和利用率改善 |

## 3. 是否会形成资本开支

目前判断：会，而且已经形成。推理如果变成搜索、办公、客服、编程、广告、推荐和企业流程的底层能力，就会从一次性训练投入变成持续性基础设施投入。

| 付款方 | 支出类型 | 预算或订单信号 | 时间节奏 | 确定性 |
| --- | --- | --- | --- | --- |
| 云厂商 | 硬件/数据中心/网络/电力 | AI 基础设施投入、GPU/自研芯片部署、数据中心扩张 | 短期/中期 | 高 |
| AI 数据中心业主 | 园区/电力/数据中心运营 | IREN 这类算力基础设施运营商与芯片厂商绑定 DSX AI 工厂架构和电力管线 | 短期/中期 | 中高 |
| 应用公司 | 云服务/自研芯片/托管基础设施 | Pinterest 多年云承诺、模型公司自研推理芯片和 Agent 产品对低延迟推理的持续需求 | 短期/中期 | 中高 |
| 区域 AI 工厂运营商 | 园区/电力/液冷/GPU 云 | Firmus 类区域 AI 工厂以承购协议和收入分成模式绑定算力供给 | 中期 | 中 |
| 模型厂商 | 硬件/云服务 | 推理请求量增长、长上下文和多模态需求扩大 | 中期 | 中高 |
| 企业客户 | 云服务/推理平台 | 企业 Agent、AI 搜索、AI 编程助手和办公 AI 付费渗透 | 中期 | 中 |

## 4. 钱最终流向谁

优先观察直接承接资本开支的环节：AI 加速芯片、服务器整机、高速网络、数据中心基础设施、云平台和推理服务平台。真正价值在最先被卡住且必须扩容的环节。

| 环节 | 受益类型 | 收入承接方式 | 稀缺性来源 | 主要风险 |
| --- | --- | --- | --- | --- |
| AI 加速芯片 | 直接 | GPU、自研 ASIC、推理芯片 | 先进制程、HBM、先进封装、生态 | 估值已充分定价或自研芯片替代 |
| 服务器整机与代工 | 直接 | AI 服务器和集群交付 | 系统集成和供应链能力 | 毛利率被压缩 |
| 高速网络 | 直接 | 交换芯片、网卡、光模块 | 带宽密度、客户认证、良率 | 产品迭代和竞争加剧 |
| 数据中心基础设施 | 直接 | 电力、液冷、机柜、UPS、变压器 | 交付周期、并网、工程能力 | 一次性工程收入占比过高 |
| 云平台和推理服务 | 直接/间接 | 推理 API、企业 AI 平台 | 客户关系、调度系统、生态 | AI 收入无法覆盖成本 |

## 5. 稀缺性判断

稀缺性主要来自算力、系统和生态三类。算力稀缺来自先进制程、HBM 和先进封装；系统稀缺来自芯片、网络、散热和电力的整体交付；生态稀缺来自 CUDA、云平台、开发者工具和企业客户关系。

| 稀缺性来源 | 当前状态 | 证据 | 持续性 | 对利润的影响 |
| --- | --- | --- | --- | --- |
| 算力稀缺 | 紧张 | NVIDIA 数据中心收入和云厂商投入继续增长 | 高 | 增强 |
| 系统交付能力 | 紧张 | AI 集群需要芯片、网络、散热、电力一起交付 | 中/高 | 增强 |
| 网络能力 | 紧张 | 数据中心网络收入高增长，CPO/光互连成为二级瓶颈 | 中 | 增强 |
| 电力与散热 | 紧张 | 数据中心扩张导致电力接入、液冷和变压器约束 | 中/高 | 增强 |
| 平台生态 | 紧张 | CUDA、云平台和企业客户关系形成壁垒 | 高 | 增强 |

## 6. 市场是否已经定价

2026 年推理基础设施已经是明牌方向，不能只看“相关性”。更重要的是判断哪些环节仍在业绩加速，哪些只是估值扩张，哪些公司能把需求变成利润，哪些二级瓶颈还没有被充分交易。

| 定价状态 | 观察证据 | 过热风险 | 预期差 | 下一步观察 |
| --- | --- | --- | --- | --- |
| 交易中/部分充分定价 | 推理基础设施已经成为市场主线，NVIDIA 和云厂商披露持续验证需求 | 中高 | 网络、电力、散热、调度等二级瓶颈仍可能存在预期差 | 跟踪资本开支、AI 收入、折旧、电力成本和二级瓶颈订单 |

## 7. 需要持续验证的信号

后续需要验证推理需求是否持续增长，AI 收入是否能覆盖成本，以及推理扩张后最先卡住的是芯片、网络、电力、散热还是软件调度。

| 验证信号 | 当前状态 | 触发阈值 | 观察频率 | 影响方向 |
| --- | --- | --- | --- | --- |
| 云厂商季度资本开支继续上修 | 已出现 | Microsoft、Amazon、Meta、Alphabet 等继续提高 AI 或数据中心投入 | event | 增强 |
| AI 工厂园区和电力管线被提前锁定 | 已出现 | 芯片厂商、云厂商或 AI 数据中心业主以战略合作方式锁定 GW 级电力和园区资源 | event | 增强 |
| 技术基础设施投入结构继续指向网络和数据中心 | 已出现 | 云厂商披露 CapEx 在服务器、网络设备、数据中心之间同步扩张 | event | 增强 |
| 高温液冷和节水架构进入参考设计 | 已出现 | 下一代 AI 工厂参考设计采用 100% 液冷、高温冷却液、干冷器或近零设施冷却用水方案 | event | 增强 |
| AI 收入覆盖折旧和电力成本 | 待验证 | AI 收入增速、毛利率和折旧压力匹配度改善 | event | 增强/削弱 |
| GPU 和推理芯片继续供不应求 | 已出现 | 出货、收入和交期继续指向供给紧张 | event | 增强 |
| 定制 ASIC 和异构推理平台进入部署 | 已出现 | OpenAI/Broadcom、Qualcomm 等路线显示模型厂商和芯片厂商继续为推理成本、能效和供给安全投入 | event | 增强/削弱 GPU 集中度 |
| 应用公司多年云基础设施承诺 | 已出现 | 应用公司围绕推荐、视觉搜索、Assistant 和个性化推理签署多年云承诺 | event | 增强 |
| HBM、服务器 DRAM 和企业级 SSD 紧张 | 观察中 | 存储厂商财报和行业研究显示 AI 数据中心需求吸收高端存储供给 | monthly/event | 增强/约束交付 |
| 隔离环境和主权 AI 推理部署 | 观察中 | 政府、关键基础设施或区域 AI 工厂要求私有、隔离或本地化推理部署 | monthly/event | 增强 |
| 单 token 成本下降带来更大使用量 | 待验证 | 成本下降后，使用量弹性超过价格下降影响 | monthly | 增强 |
| Agent、AI 搜索和 AI 编程助手付费渗透率提升 | 观察中 | 企业或消费者付费、使用时长和留存提升 | weekly/monthly | 增强 |

## 8. 当前判断

> 判断摘要：推理基础设施是 2026 年 AI 投资链条里确定性较高的主线，但容易出现“方向对、价格贵”的问题。研究重点应从“推理是不是机会”转向“推理扩张后最先卡住的基础设施环节是什么”。

| 项目 | 状态标记 | 文字说明 |
| --- | --- | --- |
| 方向状态 | priority | 推理基础设施是当前 AI 投资链条中确定性较高的主线，直接连接云厂商资本开支。 |
| 文档状态 | tracking | 已形成趋势、瓶颈、资本开支、受益方和验证信号的完整链条，需要持续跟踪。 |
| 置信度 | high | NVIDIA、Microsoft、Amazon 的公开信息共同验证推理、AI 基础设施和数据中心网络需求仍在扩张。 |
| 核心结论 | - | 推理增长会持续放大芯片、网络、电力、散热和调度系统的约束，真正价值在最先被卡住且必须扩容的环节。 |
| 关键追问 | - | 推理增长 10 倍后，最先不够用的是芯片、网络、电力、散热，还是软件调度？ |
| 下一步 | update | 重点跟踪云厂商资本开支、推理收入、GPU/自研芯片出货和单位 token 成本变化。 |

## 9. 参考来源

支撑当前判断的来源主要来自公司财报和投资者披露，优先用于验证推理需求、AI 收入、云厂商资本开支和数据中心网络需求。

| 来源 | 层级 | 链接 | 关键证据 |
| --- | --- | --- | --- |
| NVIDIA FY2027 Q1 results | tier_1 | https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx | 总收入、数据中心收入和数据中心网络收入验证 AI 基础设施需求。 |
| Microsoft FY2026 Q3 results | tier_1 | https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast | AI 业务年化收入运行率和 Azure 增长验证企业 AI 与云基础设施需求。 |
| Amazon Q1 2026 results | tier_1 | https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-First-Quarter-Results/default.aspx | AWS 增长和 AI 基础设施投入验证云厂商持续扩容。 |
| NVIDIA and IREN strategic partnership | tier_1 | https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-IREN-Announce-Strategic-Partnership-to-Accelerate-Deployment-of-up-to-5-Gigawatts-of-AI-Infrastructure/default.aspx | 5GW AI 基础设施管线和 DSX AI 工厂架构验证算力扩容向园区、电力和运营能力前置。 |
| Alphabet 2026 Q1 earnings call | tier_1 | https://abc.xyz/investor/events/event-details/2026/2026-Q1-Earnings-Call-2026-nW8kCrBAKS/default.aspx | CapEx 结构显示服务器、数据中心和网络设备同步承接 AI 技术基础设施投入。 |
| Microsoft FY2026 Q3 earnings call | tier_1 | https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3 | Foundry token 使用量和 Agent 负载验证推理需求外溢。 |
| NVIDIA liquid cooling AI factories | tier_1 | https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/ | Rubin 与 DSX 参考设计验证下一代 AI 工厂对高温液冷、节水和设施能耗优化的要求。 |
| NVIDIA Vera Rubin for science | tier_1 | https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Delivers-World-Class-Supercomputers-for-Science/default.aspx | 整机架系统、网络/DPU 和直接液冷验证基础设施从芯片扩展到系统级交付。 |
| NVIDIA and AWS AI production scale | tier_1 | https://blogs.nvidia.com/blog/nvidia-aws-ai-production-scale/ | 云平台向推理、图形、数据分析、向量数据库和托管训练工作负载扩展。 |
| Amazon and Pinterest AI infrastructure agreement | tier_1 | https://www.aboutamazon.com/news/aws/pinterest-aws-4-billion-ai-infrastructure-deal | 应用公司多年云承诺验证推荐、视觉搜索和 Assistant 对 AI 基础设施的真实需求。 |
| OpenAI Broadcom Jalapeno inference chip | tier_1 | https://openai.com/index/openai-broadcom-jalapeno-inference-chip/ | 模型厂商向定制推理芯片、多代平台和 GW 级数据中心延伸。 |
| Qualcomm data center roadmap | tier_1 | https://www.qualcomm.com/news/releases/2026/06/qualcomm-unveils-comprehensive-data-center-roadmap-for-the-agent | 异构推理平台、CPU/加速器/连接和低 TCO 路线补充 GPU 之外的供给路径。 |
| Firmus NVIDIA DSX AI Factory campus | tier_1 | https://firmus.co/newsroom/firmus-to-build-170-000-gpu-ai-factor-y-campus-with-nvidia-for-global-ai-natives | 区域 AI 工厂、液冷架构和客户承购协议验证算力供给区域化。 |

## 更新记录

| 日期 | 类型 | 变化 | 来源 |
| --- | --- | --- | --- |
| 2026-06-20 | 初始化 | 建立 AI 推理基础设施方向研究，并补充知识源仓库元信息 | NVIDIA / Microsoft / Amazon |
| 2026-06-21 | 规范化 | 同步 schema_version、方向注册表和自动化闭环规范 | 项目规范建设 |
| 2026-06-21 | 结构化 | 按新版模板补充当前判断状态表 | 模板规范同步 |
| 2026-06-21 | 来源更新 | 将 NVIDIA 来源更新至 FY2027 Q1，并补充数据中心网络收入信号 | NVIDIA |
| 2026-06-21 | 模板迁移 | 按新版方向研究模板补充趋势、瓶颈、资本开支、受益环节、稀缺性、定价和验证信号表格 | 模板规范同步 |
| 2026-06-22 | 周频更新 | 补充 IREN 5GW AI 工厂、Alphabet 技术基础设施 CapEx 结构、Microsoft Foundry token 信号和 NVIDIA 高温液冷参考设计，强化推理基础设施向园区、网络、Agent 使用量和散热架构外溢的判断 | 周频候选复核 |
| 2026-06-29 | 周频更新 | 补充 Vera Rubin 整机架系统、AWS/Pinterest 多年云承诺、OpenAI/Broadcom 推理 ASIC、Qualcomm 异构推理平台、Firmus 区域 AI 工厂和 HBM/存储供给线索，强化推理基础设施向定制芯片、软件栈、存储、电力园区和应用客户承诺外溢的判断 | 周频候选复核 |
