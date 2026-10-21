import fs from "fs";
import path from "path";
import yaml from "js-yaml";
import { ensureDirExists } from "./utils.js";

// ======================================
// 1. Input YAML file (required)
// ======================================
const inputFile = process.argv[2]; // e.g. config/site.yaml
if (!inputFile) {
  console.error("❌ Please provide the path to the YAML file.");
  console.error("Usage: node generate-site-json.js config/site.yaml");
  process.exit(1);
}

const yamlPath = path.join(process.cwd(), inputFile);
if (!fs.existsSync(yamlPath)) {
  console.error(`❌ ${inputFile} not found!`);
  process.exit(1);
}

// ======================================
// 2. Load YAML
// ======================================
const yamlContent = fs.readFileSync(yamlPath, "utf8");
let data = yaml.load(yamlContent);

if (!data?.site) {
  console.error("❌ YAML must contain a top-level `site:` object.");
  process.exit(1);
}

console.log(`✅ Loaded YAML: ${inputFile}`);

let site = { ...data.site };

// ======================================
// 3. Auto-generate repoName & base
// ======================================

if (process.env.GITHUB_REPOSITORY) {
  site.repoUrl = `https://github.com/${process.env.GITHUB_REPOSITORY}`;
}

if (site.repoUrl) {
  const repoName =
    site.repoUrl
      .replace(/\.git$/, "")
      .split("/")
      .pop() || "";

  site.repoName = repoName;
  site.base = repoName.endsWith(".github.io") ? "/" : `/${repoName}/`;
} else {
  console.warn(
    "⚠️ No repoUrl found in site.yaml. Skipping repoName/base generation.",
  );
}

// ======================================
// 4. Output directory
// ======================================
const outDir = path.join(process.cwd(), "src", "data", "generated");
ensureDirExists(outDir);

// ======================================
// 5. Write JSON
// ======================================
const outputPath = path.join(outDir, "site.json");
fs.writeFileSync(outputPath, JSON.stringify(site, null, 2), "utf8");

console.log(`📄 Generated: src/data/generated/site.json`);
console.log(site);
console.log("✅ Site JSON generation complete!");
