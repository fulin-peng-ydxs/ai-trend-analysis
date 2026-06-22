const fs = require("fs");
const path = require("path");

const root = process.cwd();

// 知识库结构校验脚本。
//
// 设计边界：
// - 校验机器可读取的稳定契约，例如 metadata 索引、frontmatter、枚举值、自动化配置和注册表引用。
// - 校验知识库维护闭环所需的基础卫生，例如正式文档必须有更新记录，不能残留模板说明。
// - 不校验投资判断本身是否正确，也不把某个模板章节标题或表格结构写死为全局规则；
//   具体章节表达由模板、技能和人工判断共同约束，脚本只守住跨文档稳定不变量。
const requiredFields = [
  "schema_version",
  "title",
  "category",
  "status",
  "updated_at",
  "confidence",
  "tags",
  "sources",
];

function readJson(file) {
  const fullPath = path.join(root, file);
  return JSON.parse(fs.readFileSync(fullPath, "utf8"));
}

// 遍历 data-source 下的 Markdown，用于发现“存在但未被 metadata/sources.json 索引”的正式文档。
function walkMarkdown(dir) {
  const fullDir = path.join(root, dir);
  if (!fs.existsSync(fullDir)) return [];

  const files = [];
  for (const entry of fs.readdirSync(fullDir, { withFileTypes: true })) {
    const fullPath = path.join(fullDir, entry.name);
    const relPath = path.relative(root, fullPath);
    if (entry.isDirectory()) {
      files.push(...walkMarkdown(relPath));
    } else if (entry.isFile() && entry.name.endsWith(".md")) {
      files.push(relPath);
    }
  }
  return files.sort();
}

// 所有知识库 Markdown 都必须使用 YAML frontmatter。
// 这里不引入完整 YAML 解析器，是因为当前契约只依赖一层标量和一层列表。
function extractFrontmatter(file) {
  const content = fs.readFileSync(path.join(root, file), "utf8");
  if (!content.startsWith("---\n")) {
    throw new Error(`${file} missing frontmatter start`);
  }

  const end = content.indexOf("\n---\n", 4);
  if (end === -1) {
    throw new Error(`${file} missing frontmatter end`);
  }

  return content.slice(4, end);
}

function readMarkdown(file) {
  return fs.readFileSync(path.join(root, file), "utf8");
}

// 读取 frontmatter 中的一层标量字段，例如 title/status/confidence。
function getScalar(frontmatter, field) {
  const match = frontmatter.match(new RegExp(`^${field}:\\s*(.*)$`, "m"));
  if (!match) return undefined;
  return match[1].trim().replace(/^["']|["']$/g, "");
}

// 读取 frontmatter 中的一层列表字段，例如 tags/sources。
// 同时兼容极少量 inline 值，避免因为空数组或单值写法导致脚本误判。
function getList(frontmatter, field) {
  const lines = frontmatter.split(/\r?\n/);
  const start = lines.findIndex((line) => line === `${field}:`);
  if (start === -1) {
    const inline = getScalar(frontmatter, field);
    if (!inline) return [];
    if (inline === "[]") return [];
    return [inline];
  }

  const values = [];
  for (let i = start + 1; i < lines.length; i += 1) {
    const line = lines[i];
    if (/^[a-zA-Z_][a-zA-Z0-9_]*:/.test(line)) break;
    const item = line.match(/^\s*-\s*(.*)$/);
    if (item) values.push(item[1].trim().replace(/^["']|["']$/g, ""));
  }
  return values;
}

// frontmatter 是文档和 metadata/sources.json、注册表之间的主同步点。
// 这里先校验基础字段存在，再校验格式和最小可用性。
function parseFrontmatter(file) {
  const frontmatter = extractFrontmatter(file);
  for (const field of requiredFields) {
    const pattern = new RegExp(`^${field}:`, "m");
    if (!pattern.test(frontmatter)) {
      throw new Error(`${file} missing frontmatter field: ${field}`);
    }
  }

  const parsed = {
    schema_version: getScalar(frontmatter, "schema_version"),
    title: getScalar(frontmatter, "title"),
    category: getScalar(frontmatter, "category"),
    status: getScalar(frontmatter, "status"),
    updated_at: getScalar(frontmatter, "updated_at"),
    confidence: getScalar(frontmatter, "confidence"),
    tags: getList(frontmatter, "tags"),
  };

  if (parsed.schema_version !== "1") {
    throw new Error(`${file} schema_version must be 1`);
  }
  if (!/^\d{4}-\d{2}-\d{2}$/.test(parsed.updated_at || "")) {
    throw new Error(`${file} updated_at must be YYYY-MM-DD`);
  }
  if (!parsed.tags.length) {
    throw new Error(`${file} tags must contain at least one item`);
  }

  return parsed;
}

function assertEqual(file, field, left, right) {
  if (left !== right) {
    throw new Error(`${file} ${field} mismatch: index="${left}" frontmatter="${right}"`);
  }
}

// 模板目录只用于生成正式文档，不纳入正式知识库索引和更新记录要求。
function isTemplate(file) {
  return file.startsWith("data-source/99_模板/");
}

// 正式文档必须保留“更新记录”，这样自动化更新、人工复盘和历史追踪能形成闭环。
function validateUpdateRecord(file) {
  if (isTemplate(file)) return;
  const content = readMarkdown(file);
  if (!content.includes("## 更新记录")) {
    throw new Error(`${file} missing 更新记录 section`);
  }
}

// 正式文档中不能残留模板填写提示，否则技能后续读取时容易把说明文本当成真实内容。
function validateNoTemplateInstructions(file) {
  if (isTemplate(file)) return;
  const content = readMarkdown(file);
  const blockedPatterns = [
    { name: "填写要求", pattern: /^填写要求：/m },
    { name: "待填写占位", pattern: /待填写/ },
    { name: "模板说明章节", pattern: /^##\s+.*模板\s*$/m },
    { name: "记录格式说明章节", pattern: /^##\s+.*记录格式\s*$/m },
    { name: "格式说明语句", pattern: /按下面格式记录/ },
  ];

  for (const item of blockedPatterns) {
    if (item.pattern.test(content)) {
      throw new Error(`${file} contains template instruction content: ${item.name}`);
    }
  }
}

// 候选池是自动化日频/周频任务最容易写入的文档。
// 这里校验候选记录表格形状、来源分层和“处理结果”枚举，确保任务输出能被后续流程稳定读取。
// 注意：candidate_decisions 表示候选信息的已处理状态，不表示“下一步建议动作”。
function validateCandidatePool(file, taxonomy) {
  const content = readMarkdown(file);
  const allowedDecisions = new Set(taxonomy.candidate_decisions || []);
  const allowedSourceTiers = new Set((taxonomy.source_tiers || []).map((item) => item.id));

  if (!allowedDecisions.size) {
    throw new Error("metadata/taxonomy.json candidate_decisions must contain at least one item");
  }

  for (const decision of allowedDecisions) {
    const rowPattern = new RegExp(`\\|\\s*${decision}\\s*\\|`);
    const descriptionPattern = new RegExp("`" + decision + "`");
    if (!rowPattern.test(content)) {
      throw new Error(`${file} processing stats missing decision row: ${decision}`);
    }
    if (!descriptionPattern.test(content)) {
      throw new Error(`${file} processing description missing decision: ${decision}`);
    }
  }

  const recordsStart = content.indexOf("## 候选记录");
  if (recordsStart === -1) {
    throw new Error(`${file} missing 候选记录 section`);
  }
  const recordsEnd = content.indexOf("\n## ", recordsStart + 1);
  const recordsSection = content.slice(recordsStart, recordsEnd === -1 ? content.length : recordsEnd);
  const rows = recordsSection.split(/\r?\n/).filter((line) => line.trim().startsWith("|"));
  for (const row of rows) {
    if (/^\|\s*-+\s*\|/.test(row) || row.includes("处理结果")) continue;
    const cells = row.split("|").slice(1, -1).map((cell) => cell.trim());
    if (cells.length !== 7) {
      throw new Error(`${file} candidate row must contain 7 columns: ${row}`);
    }
    const sourceTier = cells[1];
    const decision = cells[6];
    if (sourceTier !== "-" && !sourceTier.includes("/") && !allowedSourceTiers.has(sourceTier)) {
      throw new Error(`${file} candidate row has invalid source tier: ${sourceTier}`);
    }
    if (!allowedDecisions.has(decision)) {
      throw new Error(`${file} candidate row has invalid decision: ${decision}`);
    }
  }
}

// automation-plan.json 使用中文时间表达给技能和 README 阅读；
// 本函数把这些表达转换为本机 automation.toml 中应出现的 RRULE 片段。
// 当前本机自动化存在两类表现：
// - 日频/周频直接以北京时间小时写入 RRULE。
// - 月频/季频在 Codex 卡片中展示北京时间，但 RRULE 小时采用 UTC 等价值。
function scheduleRequirements(schedule) {
  if (schedule === "每天 22:00") return ["FREQ=DAILY", "BYHOUR=22"];
  if (schedule === "每周一 22:00") return ["FREQ=WEEKLY", "BYDAY=MO", "BYHOUR=22"];
  // Monthly/quarterly Codex automation cards display the local intended time when RRULE hours use UTC.
  if (schedule === "每月 1 日 22:00") return ["FREQ=MONTHLY", "BYMONTHDAY=1", "BYHOUR=14"];
  if (schedule === "1/4/7/10 月 1 日 23:00") {
    return ["FREQ=MONTHLY", "BYMONTH=1,4,7,10", "BYMONTHDAY=1", "BYHOUR=15"];
  }
  throw new Error(`unsupported automation schedule in metadata/automation-plan.json: ${schedule}`);
}

// automation.toml 里只需要读取 status/rrule 这类简单字符串字段。
function readTomlScalar(content, key) {
  const match = content.match(new RegExp(`^${key}\\s*=\\s*"([^"]*)"`, "m"));
  return match ? match[1] : undefined;
}

// 校验 automation-plan.json 和本机 Codex 自动化配置是否一致。
// 如果当前机器没有 ~/.codex/automations，则跳过本机配置校验，避免仓库在无自动化环境中无法检查。
function validateAutomations() {
  const plan = readJson("metadata/automation-plan.json");
  if (!Array.isArray(plan.configured_automations)) {
    throw new Error("metadata/automation-plan.json configured_automations must be an array");
  }

  const home = process.env.HOME;
  if (!home) return;
  const automationRoot = path.join(home, ".codex", "automations");
  if (!fs.existsSync(automationRoot)) return;

  for (const item of plan.configured_automations) {
    if (!item.automation_id || !item.job_id || !item.schedule) {
      throw new Error("configured automations must contain automation_id, job_id and schedule");
    }
    const file = path.join(automationRoot, item.automation_id, "automation.toml");
    if (!fs.existsSync(file)) {
      throw new Error(`configured automation does not exist locally: ${item.automation_id}`);
    }
    const content = fs.readFileSync(file, "utf8");
    if (readTomlScalar(content, "status") !== "ACTIVE") {
      throw new Error(`automation ${item.automation_id} must be ACTIVE`);
    }
    if (!content.includes(`"${root}"`)) {
      throw new Error(`automation ${item.automation_id} cwd must include ${root}`);
    }
    const rrule = readTomlScalar(content, "rrule") || "";
    for (const required of scheduleRequirements(item.schedule)) {
      if (!rrule.includes(required)) {
        throw new Error(`automation ${item.automation_id} rrule mismatch for schedule ${item.schedule}: missing ${required}`);
      }
    }
  }
}

// 方向注册表用于把“方向名称/状态/标签/正式文档”集中管理。
// 脚本只校验注册表引用和文档 frontmatter 的一致性，不再强制某个方向文档必须有固定章节名。
function validateDirectionRegistry(taxonomy, sources) {
  const registry = readJson("metadata/direction-registry.json");
  const allowedDirectionStatuses = new Set((taxonomy.direction_statuses || []).map((item) => item.id));
  if (!allowedDirectionStatuses.size) {
    throw new Error("metadata/taxonomy.json direction_statuses must contain at least one item");
  }
  if (!Array.isArray(registry.directions)) {
    throw new Error("metadata/direction-registry.json directions must be an array");
  }
  if (!Array.isArray(registry.candidate_directions)) {
    throw new Error("metadata/direction-registry.json candidate_directions must be an array");
  }

  const sourcePaths = new Set(sources.documents.map((doc) => doc.path));
  const ids = new Set();
  const names = new Set();
  for (const direction of registry.directions) {
    if (!direction.id || ids.has(direction.id)) {
      throw new Error(`duplicate or empty direction id: ${direction.id}`);
    }
    ids.add(direction.id);
    if (!direction.name || names.has(direction.name)) {
      throw new Error(`duplicate or empty direction name: ${direction.name}`);
    }
    names.add(direction.name);
    if (!allowedDirectionStatuses.has(direction.status)) {
      throw new Error(`direction ${direction.id} has invalid status: ${direction.status}`);
    }
    if (!Array.isArray(direction.tags) || !direction.tags.length) {
      throw new Error(`direction ${direction.id} tags must contain at least one item`);
    }
    if (direction.document) {
      if (!fs.existsSync(path.join(root, direction.document))) {
        throw new Error(`direction ${direction.id} document does not exist: ${direction.document}`);
      }
      if (!sourcePaths.has(direction.document)) {
        throw new Error(`direction ${direction.id} document is not indexed in metadata/sources.json: ${direction.document}`);
      }
      const frontmatter = parseFrontmatter(direction.document);
      if (frontmatter.category !== "方向研究") {
        throw new Error(`direction ${direction.id} document category must be 方向研究`);
      }
      if (frontmatter.title !== direction.name) {
        throw new Error(`direction ${direction.id} name must match document title`);
      }
    }
  }

  const candidateIds = new Set();
  // 候选方向可以先进入注册表，但不能和正式方向重名/重 ID；状态必须保持 candidate。
  for (const direction of registry.candidate_directions) {
    if (!direction.id || ids.has(direction.id) || candidateIds.has(direction.id)) {
      throw new Error(`duplicate or empty candidate direction id: ${direction.id}`);
    }
    candidateIds.add(direction.id);
    if (direction.status && direction.status !== "candidate") {
      throw new Error(`candidate direction ${direction.id} status must be candidate`);
    }
  }
}

// 来源注册表是“哪些来源值得自动化/人工定期看”的清单。
// 它不要求每个来源都已经产出文档，但要求来源 ID、分层、URL 和关注点可被技能稳定读取。
function validateSourceRegistry(taxonomy) {
  const registry = readJson("metadata/source-registry.json");
  const allowedTiers = new Set((taxonomy.source_tiers || []).map((item) => item.id));
  if (!allowedTiers.size) {
    throw new Error("metadata/taxonomy.json source_tiers must contain at least one item");
  }
  if (!Array.isArray(registry.sources)) {
    throw new Error("metadata/source-registry.json sources must be an array");
  }

  const ids = new Set();
  for (const source of registry.sources) {
    if (!source.id || ids.has(source.id)) {
      throw new Error(`duplicate or empty source id: ${source.id}`);
    }
    ids.add(source.id);
    if (!source.name) {
      throw new Error(`source ${source.id} missing name`);
    }
    if (!allowedTiers.has(source.tier)) {
      throw new Error(`source ${source.id} has invalid tier: ${source.tier}`);
    }
    if (!/^https?:\/\//.test(source.url || "")) {
      throw new Error(`source ${source.id} url must start with http:// or https://`);
    }
    if (!Array.isArray(source.focus) || !source.focus.length) {
      throw new Error(`source ${source.id} focus must contain at least one item`);
    }
  }
}

function main() {
  const sources = readJson("metadata/sources.json");
  const taxonomy = readJson("metadata/taxonomy.json");
  const allowedCategories = new Set(taxonomy.categories.map((item) => item.name));
  const allowedStatuses = new Set(taxonomy.statuses.map((item) => item.id));
  const allowedConfidence = new Set(taxonomy.confidence_levels);

  if (!Array.isArray(sources.documents)) {
    throw new Error("metadata/sources.json documents must be an array");
  }

  // 第一轮以 metadata/sources.json 为准，校验索引项和实际文档 frontmatter 是否同步。
  // sources.json 是外部检索、技能入口和索引类工具最稳定的读取入口，因此这里要求它不能漂移。
  const ids = new Set();
  const indexedPaths = new Set();
  for (const doc of sources.documents) {
    if (!doc.id || ids.has(doc.id)) {
      throw new Error(`duplicate or empty document id: ${doc.id}`);
    }
    ids.add(doc.id);

    if (!doc.path || !fs.existsSync(path.join(root, doc.path))) {
      throw new Error(`indexed path does not exist: ${doc.path}`);
    }
    indexedPaths.add(doc.path);

    const frontmatter = parseFrontmatter(doc.path);
    validateUpdateRecord(doc.path);
    validateNoTemplateInstructions(doc.path, frontmatter.category);

    assertEqual(doc.path, "title", doc.title, frontmatter.title);
    assertEqual(doc.path, "category", doc.category, frontmatter.category);
    assertEqual(doc.path, "status", doc.status, frontmatter.status);
    assertEqual(doc.path, "confidence", doc.confidence, frontmatter.confidence);

    if (!allowedCategories.has(doc.category)) {
      throw new Error(`${doc.path} category is not defined in metadata/taxonomy.json: ${doc.category}`);
    }
    if (!allowedStatuses.has(doc.status)) {
      throw new Error(`${doc.path} status is not defined in metadata/taxonomy.json: ${doc.status}`);
    }
    if (!allowedConfidence.has(doc.confidence)) {
      throw new Error(`${doc.path} confidence is not defined in metadata/taxonomy.json: ${doc.confidence}`);
    }
    if (!Array.isArray(doc.tags) || !doc.tags.length) {
      throw new Error(`${doc.path} indexed tags must contain at least one item`);
    }
  }

  // 第二轮以文件系统为准，发现遗漏索引的正式 Markdown，并对模板以外的文档执行通用卫生检查。
  // 这样可以同时覆盖“索引指向不存在文件”和“文件存在但未入索引”两类问题。
  const markdownFiles = walkMarkdown("data-source");
  for (const file of markdownFiles) {
    const frontmatter = parseFrontmatter(file);
    validateUpdateRecord(file);
    validateNoTemplateInstructions(file, frontmatter.category);
    if (frontmatter.category === "信息候选池") {
      validateCandidatePool(file, taxonomy);
    }

    if (!allowedCategories.has(frontmatter.category)) {
      throw new Error(`${file} category is not defined in metadata/taxonomy.json: ${frontmatter.category}`);
    }
    if (!allowedStatuses.has(frontmatter.status)) {
      throw new Error(`${file} status is not defined in metadata/taxonomy.json: ${frontmatter.status}`);
    }
    if (!allowedConfidence.has(frontmatter.confidence)) {
      throw new Error(`${file} confidence is not defined in metadata/taxonomy.json: ${frontmatter.confidence}`);
    }
    if (!isTemplate(file) && !indexedPaths.has(file)) {
      throw new Error(`${file} is not indexed in metadata/sources.json`);
    }
  }

  // 注册表和自动化配置是跨文档维护闭环的一部分，放在文档基础校验之后执行。
  validateDirectionRegistry(taxonomy, sources);
  validateSourceRegistry(taxonomy);
  validateAutomations();

  console.log(`Knowledge base validation passed. Indexed documents: ${sources.documents.length}. Markdown files: ${markdownFiles.length}.`);
}

main();
