const fs = require("fs");
const path = require("path");

const root = process.cwd();
const requiredFields = [
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

function validateFrontmatter(file) {
  const frontmatter = extractFrontmatter(file);
  for (const field of requiredFields) {
    const pattern = new RegExp(`^${field}:`, "m");
    if (!pattern.test(frontmatter)) {
      throw new Error(`${file} missing frontmatter field: ${field}`);
    }
  }
}

function main() {
  const sources = readJson("metadata/sources.json");
  readJson("metadata/taxonomy.json");

  if (!Array.isArray(sources.documents)) {
    throw new Error("metadata/sources.json documents must be an array");
  }

  const ids = new Set();
  for (const doc of sources.documents) {
    if (!doc.id || ids.has(doc.id)) {
      throw new Error(`duplicate or empty document id: ${doc.id}`);
    }
    ids.add(doc.id);

    if (!doc.path || !fs.existsSync(path.join(root, doc.path))) {
      throw new Error(`indexed path does not exist: ${doc.path}`);
    }
    validateFrontmatter(doc.path);
  }

  const markdownFiles = walkMarkdown("data-source");
  for (const file of markdownFiles) {
    validateFrontmatter(file);
  }

  console.log(`Knowledge base validation passed. Indexed documents: ${sources.documents.length}. Markdown files: ${markdownFiles.length}.`);
}

main();
