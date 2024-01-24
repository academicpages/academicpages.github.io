const { exec } = require("child_process");

const repositoryUrl = "https://github.com/zeon-studio/hugoplate";
const localDirectory = "./themes/hugoplate";
const foldersToFetch = ["assets", "layouts"];
const foldersToSkip = ["exampleSite"];

const fetchFolder = (folder) => {
  exec(
    `curl -L ${repositoryUrl}/tarball/main | tar -xz --strip-components=1 --directory=${localDirectory} --exclude=$(curl -sL ${repositoryUrl}/tarball/main | tar -tz | grep -E "/(${foldersToSkip.join(
      "|",
    )})/") */${folder}`,
  );
};

// Fetch each specified folder
foldersToFetch.forEach((folder) => {
  fetchFolder(folder);
});
