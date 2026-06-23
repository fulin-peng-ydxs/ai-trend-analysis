# AI趋势投资知识源仓库

本项目定位为 AI 趋势投资研究的知识数据源仓库。

它不负责展示界面、实时行情分析、交易决策或投资建议，而是负责沉淀结构化、可追溯、可被外部系统读取的 Markdown 知识文档。

## 项目边界

本项目负责：

- 存储投资判断总纲；
- 存储方向研究、历史案例、观察清单和复盘记录；
- 保留判断依据、信息来源、更新时间和判断状态；
- 为外部系统提供稳定的数据源目录和元数据索引。

本项目不负责：

- 实时行情抓取；
- 自动买卖建议；
- 复杂可视化 UI；
- 投资组合管理；
- 替代最终投资决策。

## 目录结构

```text
data-source/
  00_投资总纲/     # 方法论和判断框架
  01_方向研究/     # AI 产业方向研究
  02_历史案例/     # 已验证或曾经验证过的案例
  03_观察清单/     # 季度或阶段性观察事项
  04_复盘记录/     # 判断复盘和年度总结
  05_信息候选池/   # 待判断、待确认或暂不进入正式知识库的信息
  99_模板/         # 后续新增文档模板

metadata/
  sources.json     # 文档索引，供外部系统读取
  taxonomy.json    # 分类、状态、置信度、标签规范
  direction-registry.json # 方向总表和方向状态
  source-registry.json # 固定信息源注册表
  automation-plan.json # 自动化维护计划和校验基准
  update-state.json # 自动化任务上次处理状态

CHANGELOG.md       # 全局更新记录
README.md          # 项目说明
```

## 文档规范

所有可被外部系统读取的 Markdown 文档，都应包含 YAML frontmatter：

```yaml
---
schema_version: 1
title: 文档标题
category: 方向研究
status: tracking
updated_at: 2026-06-21
confidence: medium
tags:
  - AI
  - 资本开支
sources:
  - name: 来源名称
    url: https://example.com
---
```

## 状态规范

枚举值的机器可读源头是 `metadata/taxonomy.json`；本节只做人工阅读说明。更新枚举时必须先改 `metadata/taxonomy.json`，再同步模板和说明文档，并运行本地校验。

文档状态用于描述单篇 Markdown 的研究成熟度：

- `watching`：观察中，尚未形成稳定判断；
- `tracking`：持续跟踪，已有明确判断链条；
- `validated`：核心判断已被关键证据验证；
- `weakened`：原判断被削弱，需要降级观察；
- `rejected`：原判断被证伪；
- `archived`：归档，仅保留历史记录。

方向状态用于描述一个产业方向的自动化调度策略，维护在 `metadata/direction-registry.json`：

- `candidate`：新方向候选，只进入候选池；
- `watching`：观察中，周频检查；
- `tracking`：持续跟踪，周频复核并可更新正式文档；
- `priority`：重点跟踪，日频重点关注；
- `weakened`：逻辑削弱，降低频率并观察证伪或反转证据；
- `paused`：暂停跟踪，默认不主动更新；
- `archived`：归档，仅保留历史；
- `rejected`：已证伪，除非强反转证据否则不更新。

新增方向不直接写入正式方向研究。自动化应先写入信息候选池并标记 `new_direction_candidate`，再按证据强度升级为 `watching` 或 `tracking`。

## 更新闭环

后续更新建议按以下流程执行：

```text
1. 捕捉新信息
   ↓
2. 写入或追加到信息候选池
   ↓
3. 判断是否值得进入正式知识库
   ↓
4. 判断影响哪个方向、案例或观察清单
   ↓
5. 按模板更新对应 Markdown
   ↓
6. 记录来源、时间、判断变化
   ↓
7. 更新文档内“更新记录”
   ↓
8. 必要时同步更新 metadata/sources.json 和 CHANGELOG.md
```

进入知识库的信息，至少应满足以下条件之一：

- 影响趋势判断；
- 验证或证伪关键瓶颈；
- 改变资本开支传导方向；
- 出现真实订单、收入、利润、产能、交付周期变化；
- 改变某个方向的状态或置信度。

候选信息处理结果分为：

- `ignore`：不进入知识库，仅保留候选记录；
- `watch`：已进入候选池，等待更多证据或周频复核；日频发现的已有方向信息默认使用该状态；
- `new_direction_candidate`：新方向候选，进入候选池并等待升级判断；
- `update`：已完成已有正式文档更新；不能用于只建议后续更新但尚未写入正式文档的候选记录；
- `create`：已完成新建正式文档；不能用于只建议后续新建但尚未创建文档的候选记录；
- `review`：自动化无法可靠处理，需人工复核后再处理。

## 当前闭环

当前项目已经配置知识库更新闭环。日频任务已完成首次运行；周频、月频和季度任务尚未完成首次运行，实际运行结果以 `metadata/update-state.json` 为准：

```text
固定来源注册表
  -> 日频自动收集候选信息
  -> 按活跃研究周期写入信息候选池留痕
  -> 周频自动复核候选信息
  -> 必要时更新正式知识文档
  -> 同步方向总表、文档索引和运行状态
  -> 月频按活跃研究周期更新观察清单
  -> 季度/年度更新判断复盘
  -> 本地校验脚本验证结构一致性
```

已配置的 Codex 自动化任务：

- `ai`：日频候选收集，每天 20:00；
- `ai-2`：周频候选复核，每周一 21:00；
- `ai-3`：月频观察清单更新，每月 1 日 22:00；
- `ai-4`：季度判断复盘，1/4/7/10 月 1 日 23:00；
- `ai-5`：夜间自动提交并推送仓库变更，每天 23:00。

以上时间按北京时间说明；真实 Codex 自动化配置以本机自动化目录和本地校验脚本为准。

## 外部系统接入建议

外部系统优先读取：

1. `metadata/sources.json` 获取文档列表和路径；
2. Markdown frontmatter 获取分类、状态、标签、更新时间；
3. Markdown 正文获取研究内容；
4. 文档内“更新记录”获取判断演化过程。

推荐将本仓库作为 RAG、报告生成、趋势看板、知识图谱或研究工作台的数据源。

## 自动化维护

自动化方案记录在 `metadata/automation-plan.json`。

自动化任务的真实运行配置保存在本机 Codex 自动化目录；`metadata/automation-plan.json` 用于仓库内留痕和校验。两者不一致时，本地校验脚本会报错。

当前建议采用自动判断、异常回退模式：

- 自动化先读取 `metadata/update-state.json` 的 `period_policy.active_research_period`，当前活跃研究周期为 `2026Q2`；
- 自动化优先读取 `metadata/direction-registry.json`，不要在 prompt 中写死方向范围；
- 自动化优先读取 `metadata/source-registry.json`，未登记来源只能作为补充；
- frontmatter、`metadata/sources.json`、方向状态、候选处理结果和来源层级使用 `metadata/taxonomy.json` 中的英文机器枚举；正文表格中仅用于展示强度、确定性、优先级或预期差的字段使用中文值，如“高/中高/中/低”；
- 日频任务只追加信息候选池，不直接修改正式文档；日频不得把候选记录标记为 `update` 或 `create`，除非同一次执行已经实际写入或新建正式文档；
- 周频任务整理候选池、回写候选处理结果，并自动判断是否更新正式文档；
- 月频任务更新观察清单；
- 季度任务更新复盘记录；
- 证据冲突、来源不足或重大方法论变化时标记为 `review`。

## 本地校验

更新文档、索引或模板后，建议执行：

```bash
node scripts/validate-knowledge-base.js
```

校验内容包括：

- `metadata/*.json` 是否可解析；
- `metadata/sources.json` 中的文档路径是否存在；
- 数据源 Markdown 是否包含必需 frontmatter 字段；
- 文档索引 ID 是否重复；
- 文档的 `category/status/confidence` 是否符合 `metadata/taxonomy.json`；
- 方向总表中的方向状态、文档路径和索引关系是否有效；
- 来源注册表中的来源层级是否有效；
- 非模板 Markdown 是否已进入索引；
- 索引和 frontmatter 的核心字段是否一致；
- 正式文档是否包含“更新记录”；
- 信息候选池处理结果是否符合 `metadata/taxonomy.json`；
- 信息候选池处理统计是否覆盖全部候选处理枚举；
- 本地 Codex 自动化任务存在时，校验其状态、工作目录和调度时间是否与 `metadata/automation-plan.json` 一致。
