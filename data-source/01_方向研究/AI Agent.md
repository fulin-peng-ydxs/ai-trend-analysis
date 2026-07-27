---
schema_version: 1
title: AI Agent
category: 方向研究
status: tracking
updated_at: 2026-07-27
confidence: medium
tags:
  - AI
  - Agent
  - 推理
  - 企业软件
sources:
  - name: NVIDIA FY2027 Q1 results
    url: https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx
  - name: Microsoft FY2026 Q3 results
    url: https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast
  - name: Microsoft FY2026 Q3 earnings call
    url: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3
  - name: Amazon AWS Summit New York 2026 AI agents
    url: https://www.aboutamazon.com/news/aws/aws-summit-nyc-2026-ai-agents
  - name: Amazon and Pinterest AI infrastructure agreement
    url: https://www.aboutamazon.com/news/aws/pinterest-aws-4-billion-ai-infrastructure-deal
  - name: OpenAI GPT-5.6 preview
    url: https://openai.com/index/previewing-gpt-5-6-sol/
  - name: NVIDIA Palantir secure AI
    url: https://blogs.nvidia.com/blog/palantir-secure-ai-us-agencies-nemotron-open-models/
  - name: Qualcomm to acquire Modular
    url: https://investor.qualcomm.com/news-events/press-releases/news-details/2026/Qualcomm-to-Acquire-Modular/default.aspx
  - name: NVIDIA Vera Rubin
    url: https://blogs.nvidia.com/blog/vera-rubin/
  - name: Microsoft and Mistral strategic partnership
    url: https://news.microsoft.com/source/2026/07/21/microsoft-and-mistral-expand-strategic-partnership-to-give-enterprises-and-regulated-industries-frontier-ai-they-can-control/
  - name: OpenAI Presence
    url: https://openai.com/index/introducing-openai-presence/
  - name: AWS monday.com production agents
    url: https://aws.amazon.com/blogs/machine-learning/ai-teammates-how-monday-com-runs-production-ai-agents-on-amazon-bedrock/
  - name: Microsoft Databricks enterprise AI partnership
    url: https://news.microsoft.com/source/2026/07/23/databricks-and-microsoft-expand-partnership-to-help-enterprises-bring-business-context-to-enterprise-ai/
  - name: Microsoft Open Weights
    url: https://www.microsoft.com/en-us/corporate-responsibility/topics/open-weight/
---

# AI Agent

> 记录日期：2026-06-20
> 定位：方向研究，不构成投资建议。

## 1. 当前趋势

AI Agent 的核心变化，是 AI 从“回答问题”走向“执行任务”。普通 Chatbot 通常是一问一答，Agent 则可能拆解任务、调用工具、读取文件、访问网页、写代码、调用接口并反复验证结果。它的产业意义不只是产品形态变化，而是推理调用次数可能大幅放大。

| 趋势信号 | 来源层级 | 关键证据 | 强度 | 对方向判断的影响 |
| --- | --- | --- | --- | --- |
| AI 从问答走向执行任务 | tier_1 | Microsoft 披露 AI 业务年化收入运行率增长，企业 AI 正在进入真实工作流 | 中 | 增强 |
| Agent 工作负载开始形成可量化推理消耗 | tier_1 | Microsoft FY2026 Q3 披露 agents 正在成为主导工作负载，Foundry 年内将有超过 300 家客户处理超 1 万亿 token | 中高 | 增强 |
| 企业 Agent 平台从功能发布走向生产化底座 | tier_1 | AWS 披露 Continuum、Context、Quick autonomous agents、Transform 和 Bedrock AgentCore 增强，并称 AgentCore 任务数过去 6 个月增长 15 倍 | 中高 | 增强 |
| 应用公司把 Agent 和推荐/搜索纳入多年云承诺 | tier_1 | Pinterest 与 AWS 的 40 亿美元云服务承诺覆盖视觉搜索、个性化推荐和 Pinterest Assistant | 中高 | 增强 |
| 长周期、多代理推理能力继续提高 | tier_1 | OpenAI 预览 GPT-5.6 Sol/Terra/Luna，强调长周期 agentic 能力、多子代理模式和更高 reasoning effort | 中 | 增强 |
| 高安全和隔离环境出现 Agent/模型部署路径 | tier_1 | NVIDIA 披露 Palantir 使用 Nemotron 和加速计算在 air-gapped 环境中部署定制模型，并由 AIP、Ontology、Foundry 和 Apollo 承接授权、隔离和审计 | 中 | 增强 |
| Agent 基础设施竞争转向每 token 成本和每兆瓦产出 | tier_1 | NVIDIA Vera Rubin、Microsoft/Mistral 和 Microsoft Open Weights 共同强调开放模型、受监管部署和较低每任务 AI 成本，agentic systems 会放大 token 成本差异 | 中高 | 增强 |
| 企业客服 Agent 出现生产指标 | tier_1 | OpenAI Presence 披露英文电话支持渠道已用 agents 解决 75% 入站问题，并用 Codex 改进循环在 10 天内减少 15 个百分点人工转接 | 中高 | 增强 |
| 软件工程 Agent 进入真实 SaaS 生产流程 | tier_1 | AWS/monday.com 案例显示 AI Teammates 通过 Slack、monday item 和 GitHub PR review request 进入工程工作流，90% builders 每月使用 AI coding tools，单工程师 PR throughput 提升超过 50% | 中高 | 增强 |
| 企业 Agent 需要业务上下文和治理底座 | tier_1 | Microsoft/Databricks 将 Genie、Genie Ontology、Unity AI Gateway 与 Microsoft 365、Teams、Copilot、Purview、Foundry 和 Power Platform 集成，强化数据、模型、agents、成本和治理闭环 | 中高 | 增强 |
| Agent 可能放大推理调用 | tier_1 | NVIDIA FY2027 Q1 继续验证数据中心和推理基础设施需求强劲 | 中 | 增强 |
| 应用层商业化仍需验证 | tier_3 | 企业试点、demo 和产品叙事多，但大规模付费与留存证据仍不足 | 中 | 待验证 |

## 2. 核心瓶颈

Agent 的瓶颈不只在模型能力，也在多步执行的成本、准确率、工具连接、权限安全和评估体系。它能否成为投资主线，取决于这些瓶颈是否形成真实采购和持续推理需求。

| 瓶颈 | 严重程度 | 触发条件 | 受影响环节 | 验证信号 |
| --- | --- | --- | --- | --- |
| 推理成本 | 高 | 单个任务触发多轮模型调用，token 和上下文长度增加 | 推理算力 / 云平台 | 云厂商披露 Agent 带来的算力需求 |
| 准确率 | 高 | 多步执行放大错误，任务需要反复验证 | Agent 应用 / 企业工作流 | 企业从试用转向生产部署 |
| 工具调用 | 中 | Agent 需要稳定连接浏览器、代码环境、数据库和企业系统 | 工作流编排 / 企业集成 | 工具调用平台和集成能力成为采购条件 |
| 权限与安全 | 高 | Agent 获得执行权限后风险高于聊天 | 安全 / 审计 / 权限管理 | 安全、权限、审计成为企业采购门槛 |
| 数据上下文和治理 | 高 | Agent 要进入生产工作流，需要跨系统取数、权限继承、上下文管理和审计 | 企业数据平台 / 云平台 / 安全 | Context、Ontology、Foundry、AgentCore 等平台层能力被客户采用 |
| 异构推理部署效率 | 中高 | Agent 负载可能跨云、边缘、设备和私有环境运行 | 推理软件栈 / 编译器 / 运行时 | Modular 类开放 AI-native 软件栈降低跨硬件部署难度 |
| 开放权重和自托管经济性 | 中高 | 企业希望降低每任务成本、控制数据和模型部署位置，且 Agent 多轮调用会放大模型成本差异 | 开放模型 / 私有云 / 云平台 / 企业软件 | 开放权重模型采用、私有/断连环境部署、每任务成本下降和自托管合规需求 |
| 人机升级、策略和评估闭环 | 高 | Agent 执行客户支持、销售、工程或内部流程时，需要规则、置信度、人工接管和持续评估 | 企业软件 / 安全治理 / Agent 平台 | 自动解决率、人工转接率、策略命中、误操作率和客户满意度 |
| 评估体系 | 中 | 企业需要证明 Agent 真实节省成本或提升收入 | 企业软件 / 咨询服务 | 出现可量化节省成本或提升收入的案例 |

## 3. 是否会形成资本开支

Agent 本身未必直接产生硬件订单，但它可能显著放大推理需求。判断链条是：Agent 渗透率提升 -> 单个任务模型调用次数增加 -> 推理 token 和上下文长度增加 -> 云厂商和模型厂商扩容 -> 算力、网络、存储、电力和散热需求增加。

| 付款方 | 支出类型 | 预算或订单信号 | 时间节奏 | 确定性 |
| --- | --- | --- | --- | --- |
| 云厂商 | 硬件/平台 | Agent 推动推理量增加后，需要扩容算力、网络、存储、电力和散热 | 中期 | 中 |
| 企业客户 | 软件/服务 | Agent 从试用进入企业采购，形成席位、订阅或集成项目 | 短期/中期 | 中 |
| 模型厂商 | 硬件/平台 | 多步任务和长上下文提高推理资源消耗 | 中期 | 中 |
| 数据和安全平台 | 软件/服务 | Agent 进入生产环境后需要上下文、权限、审计、隔离和持续治理能力 | 短期/中期 | 中 |

## 4. 钱最终流向谁

Agent 的投资价值不一定在“Agent 应用公司”，也可能在它引发的基础设施需求。需要分清直接应用收入、基础设施收入和安全集成收入。

| 环节 | 受益类型 | 收入承接方式 | 稀缺性来源 | 主要风险 |
| --- | --- | --- | --- | --- |
| 企业办公、编程、客服、销售和数据分析 Agent | 直接 | 订阅/席位/项目服务 | 入口、数据、工作流嵌入 | demo 热但付费和留存不足 |
| 推理算力和云平台 | 间接 | 云推理服务、GPU/ASIC、服务器和网络采购 | 算力、调度、平台生态 | 使用量增长但成本压力上升 |
| 长上下文存储、检索和工作流编排 | 间接 | 平台服务和企业集成 | 企业数据连接和系统集成能力 | 被大模型厂商或办公平台内置 |
| 权限、安全、审计 | 直接/间接 | 安全产品、审计服务、企业管理平台 | 合规、权限和审计能力 | 需求出现但预算释放慢 |

## 5. 稀缺性判断

Agent 应用层容易热闹，但护城河不一定强。更值得观察的稀缺性是高频入口、企业核心数据连接、真实工作流嵌入、安全权限审计和能量化 ROI 的能力。

| 稀缺性来源 | 当前状态 | 证据 | 持续性 | 对利润的影响 |
| --- | --- | --- | --- | --- |
| 高频入口 | 待验证 | 办公、编程、客服等入口存在，但竞争激烈 | 中 | 待验证 |
| 企业核心数据连接 | 待验证 | 企业 Agent 需要接入真实系统和数据 | 中 | 增强 |
| 工作流嵌入 | 待验证 | 只有嵌入真实流程才可能提高留存 | 高 | 增强 |
| 安全、权限、审计 | 观察中 | Agent 能执行任务后，风险显著高于聊天 | 高 | 增强 |
| 推理成本控制 | 观察中 | Agent 多步执行会放大推理调用 | 高 | 增强/削弱 |
| 业务上下文和治理网关 | 观察中 | Agent 进入生产环境需要把企业数据、权限、工具、模型选择和成本控制统一到治理层 | 高 | 增强 |
| 开放模型和可控部署 | 观察中 | 受监管行业需要在公共云、私有云、断连环境和本地数据边界之间保持同一套 Agent 操作路径 | 中高 | 增强/改变供给格局 |

## 6. 市场是否已经定价

Agent 是 2026 年最容易被叙事放大的方向之一。风险在于概念领先于收入，需要警惕只展示 demo、企业试点多但规模化部署少、使用量增长但毛利率恶化，以及被大模型厂商或办公平台快速内置。

| 定价状态 | 观察证据 | 过热风险 | 预期差 | 下一步观察 |
| --- | --- | --- | --- | --- |
| 交易中 | Agent 叙事强，企业 AI 和办公集成持续推进 | 高 | 应用层收入兑现仍不清晰 | 观察真实付费、留存、推理消耗和安全权限需求 |

## 7. 需要持续验证的信号

后续验证重点不是 Agent 概念是否成立，而是它是否带来真实企业采购、可量化 ROI 和推理调用增长。

| 验证信号 | 当前状态 | 触发阈值 | 观察频率 | 影响方向 |
| --- | --- | --- | --- | --- |
| Agent 产品从试用进入企业采购 | 观察中 | 出现明确企业付费、席位扩张或项目续约 | weekly | 增强 |
| 单客户付费金额提升 | 待验证 | ARPU、续费或合同金额提升 | monthly/event | 增强 |
| 出现明确节省成本的案例 | 待验证 | 客户披露可量化效率提升或成本下降 | event | 增强 |
| Agent 带来推理量显著增长 | 待验证 | 云厂商或模型厂商披露 Agent 对算力需求的拉动 | event | 增强 |
| Foundry 等平台级 Agent token 消耗 | 观察中 | 超过 300 家客户级别的万亿 token 处理信号持续扩大，并能和企业付费、留存或工作流部署对应 | event | 增强 |
| 安全、权限、审计成为采购门槛 | 观察中 | 企业采购要求明确包含权限、合规或审计能力 | weekly | 增强 |
| AgentCore、Context 等平台级任务量增长 | 已出现 | 云厂商披露任务数、客户案例或生产工作流承载量持续扩大 | event | 增强 |
| 长周期多代理能力进入产品化 | 观察中 | 模型厂商开放更高 reasoning effort、多子代理模式或长周期任务能力，并能转化为付费使用 | weekly/monthly | 增强 |
| 隔离环境和关键基础设施 Agent 部署 | 观察中 | 政府、能源、金融或关键基础设施客户要求 air-gapped、审计和权限治理 | monthly/event | 增强 |
| 客服、销售和工程 Agent 的生产指标 | 已出现 | 自动解决率、人工转接率、PR throughput、月活使用率、质量控制和客户满意度被客户或平台公开披露 | weekly/event | 增强 |
| Agent 数据治理和业务上下文平台 | 已出现 | Genie Ontology、Unity AI Gateway、Purview、Foundry、Copilot Studio、Agent Gateway 等能力被企业生产流程采用 | weekly/monthly | 增强 |
| 开放权重降低每任务成本 | 观察中 | 开放权重模型在企业、受监管行业和 Agent 平台中形成部署、成本或留存优势 | monthly/event | 增强/改变模型供给结构 |

## 8. 当前判断

> 判断摘要：Agent 更像“推理需求放大器”，而不是单独的一条硬件产业链。研究 Agent 时，不要只看产品演示，要追问它是否会迫使企业和云厂商增加真实支出。

| 项目 | 状态标记 | 文字说明 |
| --- | --- | --- |
| 方向状态 | tracking | Agent 可能放大推理调用和企业工作流集成需求，但商业化质量仍需验证。 |
| 文档状态 | tracking | 已形成基本判断链条，但收入、留存和企业采购仍需要后续证据。 |
| 置信度 | medium | 方向重要性较高，但应用层收入兑现和护城河仍不如基础设施确定。 |
| 核心结论 | - | Agent 的投资价值更可能通过推理调用、云基础设施和企业系统集成兑现，而不是单纯应用叙事。 |
| 关键追问 | - | 如果 Agent 真的普及，谁会被迫花更多钱，钱会流向应用软件，还是算力和云基础设施？ |
| 下一步 | watch | 继续观察企业付费、推理消耗、安全权限和工作流集成是否形成真实采购。 |

## 9. 参考来源

支撑当前判断的来源主要用于验证推理基础设施需求和企业 AI 商业化进展。Agent 应用层收入兑现仍需更多直接来源。

| 来源 | 层级 | 链接 | 关键证据 |
| --- | --- | --- | --- |
| NVIDIA FY2027 Q1 results | tier_1 | https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Announces-Financial-Results-for-First-Quarter-Fiscal-2027/default.aspx | 数据中心和推理基础设施需求保持强劲。 |
| Microsoft FY2026 Q3 results | tier_1 | https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast | AI 业务年化收入运行率增长，企业 AI 需求继续扩张。 |
| Microsoft FY2026 Q3 earnings call | tier_1 | https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3 | Agent 工作负载和 Foundry token 使用量用于验证 Agent 对推理需求的放大作用。 |
| Amazon AWS Summit New York 2026 AI agents | tier_1 | https://www.aboutamazon.com/news/aws/aws-summit-nyc-2026-ai-agents | Agent 平台、企业客户案例和任务量增长用于验证生产化底座。 |
| Amazon and Pinterest AI infrastructure agreement | tier_1 | https://www.aboutamazon.com/news/aws/pinterest-aws-4-billion-ai-infrastructure-deal | Pinterest Assistant、视觉搜索和个性化推荐把 Agent/AI 功能与多年云承诺绑定。 |
| OpenAI GPT-5.6 preview | tier_1 | https://openai.com/index/previewing-gpt-5-6-sol/ | 长周期 agentic 能力、多子代理模式和更高 reasoning effort 用于观察 Agent 工作负载变化。 |
| NVIDIA Palantir secure AI | tier_1 | https://blogs.nvidia.com/blog/palantir-secure-ai-us-agencies-nemotron-open-models/ | 高安全、隔离环境和权限审计验证企业/政府 Agent 落地门槛。 |
| Qualcomm to acquire Modular | tier_1 | https://investor.qualcomm.com/news-events/press-releases/news-details/2026/Qualcomm-to-Acquire-Modular/default.aspx | 异构硬件软件栈补充 Agent 推理跨平台部署瓶颈。 |

## 更新记录

| 日期 | 类型 | 变化 | 来源 |
| --- | --- | --- | --- |
| 2026-06-20 | 初始化 | 建立 AI Agent 方向研究，并补充知识源仓库元信息 | NVIDIA / Microsoft |
| 2026-06-21 | 规范化 | 同步 schema_version、方向注册表和自动化闭环规范 | 项目规范建设 |
| 2026-06-21 | 结构化 | 按新版模板补充当前判断状态表 | 模板规范同步 |
| 2026-06-21 | 来源更新 | 将 NVIDIA 来源更新至 FY2027 Q1，保持 Agent 与推理需求证据同步 | NVIDIA |
| 2026-06-21 | 模板迁移 | 按新版方向研究模板补充趋势、瓶颈、资本开支、受益环节、稀缺性、定价和验证信号表格 | 模板规范同步 |
| 2026-06-22 | 周频更新 | 补充 Microsoft FY2026 Q3 Agent 工作负载和 Foundry token 使用量信号，强化 Agent 作为推理需求放大器的早期证据 | 周频候选复核 |
| 2026-06-29 | 周频更新 | 补充 AWS AgentCore 任务量、Pinterest Assistant 云承诺、OpenAI 长周期多代理能力、Palantir 隔离环境部署和 Modular 异构推理软件栈，强化 Agent 从演示走向生产工作流、数据治理和安全权限门槛的判断 | 周频候选复核 |
| 2026-07-27 | 周频更新 | 补充 Vera Rubin agentic workload 成本/能效、Microsoft/Mistral 主权和开放模型基础设施、OpenAI Presence 客服自动解决率、AWS/monday.com 生产工程 Agent、Microsoft/Databricks 企业数据治理，以及 Microsoft Open Weights 政策信号，强化 Agent 生产化正被推理成本、业务上下文、权限治理和开放部署方式共同约束的判断 | 周频候选复核 |
