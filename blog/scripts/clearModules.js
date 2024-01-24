const fs = require("fs");

const clearModules = (filePath) => {
  if (fs.existsSync(filePath)) {
    let fileContent = fs.readFileSync(filePath, "utf8");
    fileContent = fileContent.replace(/require\s*\([\s\S]*?\)/, "");
    fs.writeFileSync(filePath, fileContent, "utf8");
  } else {
    console.log("File does not exist.");
  }
};

clearModules("go.mod");
clearModules("exampleSite/go.mod");
