# Shawal Khalid Portfolio — publish to shawalkhalid.github.io

Target repository: https://github.com/ShawalKhalid/ShawalKhalid.github.io
Recommended publishing source: **Deploy from a branch** -> **master** -> **/(root)**.

## What this package includes
- index.html, research.html, publications.html, teaching.html
- css/style.css (original styling), assets/profile.jpg (original headshot)
- assets/Shawal-Khalid-CV-2026.pdf (REVIEW DRAFT before public release)
- other original support PDFs and `.nojekyll`

## Safe publishing workflow
1. GitHub Desktop: sign in to the **ShawalKhalid** account and clone the target repository.
2. Create a new branch named `portfolio-update-2026` from `master`.
3. In Finder, open the cloned repository folder. Remove the old Jekyll website files, **but preserve the hidden `.git` directory**. The old site remains safe in the remote `master` branch until merge.
4. Unzip this package, and copy its **contents** into the cloned repository root, with index.html at the top level.
5. Review file changes in GitHub Desktop, commit to `portfolio-update-2026`, and Publish branch.
6. Create a pull request with base `master` and compare `portfolio-update-2026`. Review the changed files, then merge.
7. In GitHub repository Settings > Pages, choose **Deploy from a branch**, branch `master`, folder `/(root)`, and Save.
8. Open https://shawalkhalid.github.io and test navigation, images, and PDF links.

This package deliberately omits the optional `.github/workflows/deploy.yml` from the earlier version, since that workflow targeted `main` while the destination repository currently uses `master`.
The original `shawalkhalid667` repository is not affected by these instructions.
No repository changes have been published by ChatGPT.
