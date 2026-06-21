---
schema_version: 1
title: AI推理基础设施
category: 方向研究
status: tracking
updated_at: 2026-06-21
confidence: high
tags:
  - AI
  - 推理
  - 数据中心
  - 资本开支
sources:
  - name: NVIDIA FY2026 Q4 results
    url: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
  - name: Microsoft FY2026 Q3 results
    url: https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast
  - name: Amazon Q1 2026 results
    url: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-First-Quarter-Results/default.aspx
---

# AI推理基础设施

> 记录日期：2026-06-20
> 定位：方向研究，不构成投资建议。

## 1. 当前趋势

2026 年 AI 的核心变化，是从“训练大模型”继续转向“大规模使用模型”。

训练决定模型能力上限，推理决定 AI 能不能进入真实业务流量。用户每天使用搜索、办公、客服、代码、图片、视频、Agent 时，都会持续消耗推理算力。

公开信号：

- NVIDIA 2026 财年第四季度数据中心收入达到 623 亿美元，同比增长 75%，并强调 agentic AI 与 inference 需求。
- Microsoft 2026 财年第三季度披露 AI 业务年化收入运行率超过 370 亿美元，同比增长 123%。
- Amazon 2026 年一季度披露 AWS 增长 28%，并强调 Trainium、NVIDIA GPU 与 AI 基础设施投入。

## 2. 核心瓶颈

推理扩张后的瓶颈，不只是 GPU 数量，而是单位 token 成本、延迟、吞吐、调度效率和能耗。

需要重点观察：

- 推理请求量是否持续增长；
- 多模态和 Agent 是否显著增加 token 消耗；
- 云厂商是否继续扩大 GPU、自研芯片和推理集群；
- 推理成本下降是否带来更大使用量，而不是压缩收入。

## 3. 是否会形成资本开支

目前判断：会，而且已经形成。

推理如果变成搜索、办公、客服、编程、广告、推荐和企业流程的底层能力，就会从一次性训练投入变成持续性基础设施投入。

资本开支的传导链条：

用户使用增长
-> 推理 token 增长
-> 云厂商扩容
-> GPU、自研芯片、服务器、网络、存储、电力、散热投入增长
-> 上游硬件和数据中心基础设施受益

## 4. 钱最终流向谁

优先观察直接承接资本开支的环节：

- AI 加速芯片：GPU、自研 ASIC、推理芯片；
- 服务器整机与代工；
- 高速网络：交换芯片、网卡、光模块；
- 数据中心基础设施：电力、液冷、机柜、UPS、变压器；
- 云平台和推理服务平台。

## 5. 稀缺性判断

稀缺性主要来自三类：

- 算力稀缺：先进制程、HBM、先进封装、产能排期；
- 系统稀缺：能把芯片、网络、散热、电力整合成可交付集群；
- 生态稀缺：CUDA、云平台、开发者工具、企业客户关系。

## 6. 市场是否已经定价

2026 年推理基础设施已经是明牌方向，不能只看“相关性”。

更重要的是判断：

- 哪些环节仍在业绩加速；
- 哪些环节只是估值扩张；
- 哪些公司能把需求变成利润，而不是被成本吞掉；
- 哪些二级瓶颈还没有被充分交易。

## 7. 需要持续验证的信号

- 云厂商季度资本开支是否继续上修；
- AI 收入增速是否能覆盖折旧和电力成本；
- 推理芯片和 GPU 出货是否继续供不应求；
- 单 token 成本下降后，使用量是否弹性更大；
- 企业 Agent、AI 搜索、AI 编程助手的付费渗透率。

## 8. 当前判断

> 判断摘要：推理基础设施是 2026 年 AI 投资链条里确定性较高的主线，但容易出现“方向对、价格贵”的问题。研究重点应从“推理是不是机会”转向“推理扩张后最先卡住的基础设施环节是什么”。

| 项目 | 状态标记 | 文字说明 |
| --- | --- | --- |
| 方向状态 | priority | 推理基础设施是当前 AI 投资链条中确定性较高的主线，直接连接云厂商资本开支。 |
| 文档状态 | tracking | 已形成趋势、瓶颈、资本开支、受益方和验证信号的完整链条，需要持续跟踪。 |
| 置信度 | high | NVIDIA、Microsoft、Amazon 的公开信息共同验证推理和 AI 基础设施需求仍在扩张。 |
| 核心结论 | - | 推理增长会持续放大芯片、网络、电力、散热和调度系统的约束，真正价值在最先被卡住且必须扩容的环节。 |
| 关键追问 | - | 推理增长 10 倍后，最先不够用的是芯片、网络、电力、散热，还是软件调度？ |
| 下一步 | update | 重点跟踪云厂商资本开支、推理收入、GPU/自研芯片出货和单位 token 成本变化。 |

## 9. 参考来源

- NVIDIA FY2026 Q4 results: https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026
- Microsoft FY2026 Q3 results: https://www.microsoft.com/en-us/investor/earnings/fy-2026-q3/press-release-webcast
- Amazon Q1 2026 results: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-First-Quarter-Results/default.aspx

## 更新记录

| 日期 | 类型 | 变化 | 来源 |
| --- | --- | --- | --- |
| 2026-06-20 | 初始化 | 建立 AI 推理基础设施方向研究，并补充知识源仓库元信息 | NVIDIA / Microsoft / Amazon |
| 2026-06-21 | 规范化 | 同步 schema_version、方向注册表和自动化闭环规范 | 项目规范建设 |
| 2026-06-21 | 结构化 | 按新版模板补充当前判断状态表 | 模板规范同步 |
