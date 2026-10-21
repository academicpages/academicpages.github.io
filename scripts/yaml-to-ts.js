import fs from "fs";
import path from "path";
import yaml from "js-yaml";

import { ensureDirExists, addBasePathIfAbsolute } from "./utils.js";

const TYPE_MAP = {
  publications: "PublicationsType",
  giscus: "GiscusProps",
};

const sitePath = path.join(
  process.cwd(),
  "src",
  "data",
  "generated",
  "site.json",
);
const site = JSON.parse(fs.readFileSync(sitePath, "utf8"));

// function that convert a JavaScript object to a TypeScript-like string representation
export function toTS(obj, indent = 0) {
  const pad = (level) => " ".repeat(level);

  if (Array.isArray(obj)) {
    if (obj.length === 0) return "[]";
    const items = obj.map((i) => pad(indent + 2) + toTS(i, indent + 2));
    return `[\n${items.join(",\n")}\n${pad(indent)}]`;
  }

  if (obj && typeof obj === "object") {
    const entries = Object.entries(obj).map(([key, value]) => {
      const formattedKey = /^[a-zA-Z_$][a-zA-Z0-9_$]*$/.test(key)
        ? key
        : `"${key}"`;

      if (typeof value === "object" && value !== null) {
        return pad(indent + 2) + `${formattedKey}: ${toTS(value, indent + 2)}`;
      }

      if (key === "icon") {
        return pad(indent + 2) + `${formattedKey}: ${value}`; // write icon value as raw variable (no quotes)
      }

      if (typeof value === "string") {
        const finalValue = addBasePathIfAbsolute(value.trim(), site.base);
        return pad(indent + 2) + `${formattedKey}: \`${finalValue}\``;
      }

      return pad(indent + 2) + `${formattedKey}: ${value}`;
    });

    return `{\n${entries.join(",\n")}\n${pad(indent)}}`;
  }

  if (typeof obj === "string") return `\`${obj}\``;
  return String(obj);
}

// 1. Get YAML file from argument
const inputFile = process.argv[2]; // e.g., "config/profile.yaml"
if (!inputFile) {
  console.error("❌ Please provide the path to the YAML file.");
  console.error("Usage: node generate-data.js config/profile.yaml");
  process.exit(1);
}

const yamlPath = path.join(process.cwd(), inputFile);
if (!fs.existsSync(yamlPath)) {
  console.error(`❌ ${inputFile} not found!`);
  process.exit(1);
}

// 2. Load YAML
const yamlContent = fs.readFileSync(yamlPath, "utf8");
const data = yaml.load(yamlContent);
console.log(`✅ Loaded YAML: ${inputFile}`);

// 3. Prepare output directory
const outDir = path.join(process.cwd(), "src", "data");
ensureDirExists(outDir);

// 4. Helper: write TS file with imports
function writeTS(filename, variable, content) {
  const packageIconsMap = new Map(); // package -> Set of icon names

  // recursively collect assets (icons and images)
  function collectAssets(obj) {
    if (Array.isArray(obj)) {
      obj.forEach(collectAssets);
    } else if (obj && typeof obj === "object") {
      Object.entries(obj).forEach(([key, value]) => {
        if (key === "icon" && value?.name && value?.package) {
          if (!packageIconsMap.has(value.package)) {
            packageIconsMap.set(value.package, new Set());
          }
          packageIconsMap.get(value.package).add(value.name);
          obj[key] = value.name; // use raw variable
        } else if (typeof value === "object" && value !== null) {
          collectAssets(value);
        }
      });
    }
  }

  collectAssets(content);

  let importStatements = "";
  packageIconsMap.forEach((icons, pkg) => {
    importStatements += `import { ${Array.from(icons).join(", ")} } from "${pkg}";\n`;
  });

  // determine types based on filename/variable name
  const typeName = TYPE_MAP[variable];
  let typeImport = "";
  let typeAnnotation = "";

  if (typeName) {
    typeImport = `import type { ${typeName} } from "@/types/${variable}";\n`;
    typeAnnotation = `: ${typeName}`;
  }

  if (importStatements || typeImport) typeImport += "\n";

  // combine imports and TS content
  const tsContent = `${importStatements}${typeImport}export const ${variable}${typeAnnotation} = ${toTS(
    content,
  )};`;
  fs.writeFileSync(path.join(outDir, filename), tsContent);
}

// 5. Write TS files
Object.entries(data).forEach(([key, value]) => {
  // check for items array with featured property
  if (
    Array.isArray(value.items) &&
    value.items.some((item) => "featured" in item)
  ) {
    const featuredValue = {
      ...value,
      items: value.items
        .filter((item) => item.featured)
        .map(({ featured, ...rest }) => rest),
    };
    writeTS(`${key}.featured.ts`, `${key}Featured`, featuredValue);
  }

  writeTS(`${key}.ts`, key, value);
});

console.log("✅ Generated TS files successfully!");
