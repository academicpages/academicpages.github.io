import fs from "node:fs";
import path from "node:path";

// ensure the directory for a given file path exists.
export function ensureDirExists(filePath) {
  const dir = path.dirname(filePath);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

// determine whether a string represents a URL, absolute path, or relative path.
export function checkPathOrUrl(str) {
  if (typeof str !== "string" || str.trim() === "") return "invalid";
  try {
    const url = new URL(str);
    if (url.protocol === "http:" || url.protocol === "https:") return "url";
  } catch (err) {} // not a valid URL, continue
  if (path.isAbsolute(str)) return "absolute";
  if (/^(\.\/|\.\.\/)/.test(str)) return "relative";
  return "invalid";
}

// check if a string represents a local file path (absolute or relative), not a URL.
export function isLocalFile(str) {
  const result = checkPathOrUrl(str);
  return result === "absolute" || result === "relative";
}

// if the string is an absolute path, prepend a base path.
export function addBasePathIfAbsolute(str, basePath) {
  if (checkPathOrUrl(str) !== "absolute") return str;
  const cleanedBase = basePath.endsWith("/") ? basePath.slice(0, -1) : basePath;
  const normalized = str.startsWith("/") ? str : `/${str}`;
  return `${cleanedBase}${normalized}`;
}
