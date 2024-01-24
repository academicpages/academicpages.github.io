const fs = require("fs");
const path = require("path");

const toggleComment = ({ filepath, regex }) => {
  let updatedContent = fs.readFileSync(filepath, "utf8");
  const match = updatedContent.match(regex);

  if (match) {
    const matchedContent = match[0];
    const hasComment = matchedContent.startsWith("# ");
    if (hasComment) {
      updatedContent = updatedContent.replace(
        regex,
        matchedContent.replace("# ", ""),
      );
      fs.writeFileSync(filepath, updatedContent, "utf8");
    } else {
      const hasBreakline = matchedContent.includes("\n");
      if (hasBreakline) {
        const content = matchedContent
          .split("\n")
          .map((line) => "# " + line)
          .join("\n");
        updatedContent = updatedContent.replace(regex, content);
        fs.writeFileSync(filepath, updatedContent, "utf8");
      }
    }
  }
};

const getFolderName = (rootfolder) => {
  const configPath = path.join(rootfolder, "exampleSite/hugo.toml");
  const getConfig = fs.readFileSync(configPath, "utf8");
  const match = getConfig.match(/theme\s*=\s*\[?"([^"\]]+)"\]?/);
  let selectedTheme = null;
  if (match && match[1]) {
    selectedTheme = match[1];
  }
  return selectedTheme;
};

const deleteFolder = (folderPath) => {
  if (fs.existsSync(folderPath)) {
    fs.rmSync(folderPath, { recursive: true, force: true });
  }
};

const createNewfolder = (rootfolder, folderName) => {
  const newFolder = path.join(rootfolder, folderName);
  fs.mkdirSync(newFolder, { recursive: true });
  return newFolder;
};

const iterateFilesAndFolders = (rootFolder, { destinationRoot }) => {
  const directory = path.join(rootFolder);
  const items = fs.readdirSync(directory, { withFileTypes: true });
  items.forEach((item) => {
    if (item.isDirectory()) {
      createNewfolder(destinationRoot, item.name);
      iterateFilesAndFolders(path.join(directory, item.name), {
        currentFolder: item.name,
        destinationRoot: path.join(destinationRoot, item.name),
      });
    } else {
      const sourceFile = path.join(directory, item.name);
      const destinationFile = path.join(destinationRoot, item.name);
      fs.renameSync(sourceFile, destinationFile);
    }
  });
};

const setupProject = () => {
  const rootfolder = path.join(__dirname, "../");
  if (!fs.existsSync(path.join(rootfolder, "themes"))) {
    // remove this part if you don't using theme demo as a module
    [
      {
        filepath: path.join(rootfolder, "exampleSite/hugo.toml"),
        regex: /^.*theme\s*=\s*("[^"\]]+"|\S+)/m,
      },
      {
        filepath: path.join(
          rootfolder,
          "exampleSite/config/_default/module.toml",
        ),
        regex: /\[\[imports\]\]\s*\r?\npath = "([^"]+)"/,
      },
    ].forEach(toggleComment);

    const folderList = ["layouts", "assets", "static"];
    const folderName = getFolderName(rootfolder);
    const newfolderName = createNewfolder(
      path.join(rootfolder, "themes"),
      folderName,
    );

    folderList.forEach((folder) => {
      const source = path.join(rootfolder, folder);
      const destination = path.join(newfolderName, folder);
      if (fs.existsSync(source)) {
        fs.mkdirSync(destination, { recursive: true });
        iterateFilesAndFolders(source, {
          currentFolder: folder,
          destinationRoot: destination,
        });
        deleteFolder(source);
      }
    });

    const exampleSite = path.join(rootfolder, "exampleSite");
    iterateFilesAndFolders(exampleSite, { destinationRoot: rootfolder });
    deleteFolder(exampleSite);
  }
};

setupProject();
