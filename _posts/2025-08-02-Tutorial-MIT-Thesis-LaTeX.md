---
title: "Tutorial: MIT Thesis LaTeX Template with VS Code"
date: 2025-08-02
permalink: /posts/2025/08/MIT-Thesis-LaTeX/
tags:
  - tutorial
  - latex
  - vscode
---

MIT's libraries require theses to be deposited electronically using a strict format. To simplify formatting, the [**MIT thesis LaTeX template**](https://web.mit.edu/thesis/tex/) provides a class (`mitthesis.cls`) and a set of sample files that implement these requirements.

This tutorial blog builds on top of my previous ["Tutorial: Use LaTeX Locally with VS Code"]({% post_url 2025-06-29-Tutorial-LaTeX-VSCode %}). By following the previous tutorial, you are assumed to have the following in place:

* **Visual Studio Code with LaTeX Workshop installed.** The extension provides core LaTeX features such as auto‑building to PDF, an integrated PDF viewer, SyncTeX navigation, Intellisense and log parsing. It automatically runs the sequence of tools needed to build your document and highlights errors in the editor.
* **TeX Live 2022 or newer.** The MIT thesis class requires a recent LaTeX distribution; the README suggests November 2022 or later and is compatible back to 2020. A full TeX Live installation includes `pdflatex`, biber and other programs needed by the template.
* **Biber for bibliography management.** The template defaults to using biblatex with the biber backend. Biber is part of TeX Live and will run automatically if configured in LaTeX Workshop.

## 1. Acquire the template

Download it here: [https://mirrors.ctan.org/macros/latex/contrib/mitthesis.zip](https://mirrors.ctan.org/macros/latex/contrib/mitthesis.zip).

<details>
<summary>What's this website?</summary>

MIT distributes the thesis template through the Comprehensive TeX Archive Network (CTAN). This URL is referenced by the official <a href="https://web.mit.edu/thesis/tex/" target="_blank"> MIT Thesis template website</a>

</details>

Then unzip the archive to a convenient folder. I would unzip it to the actual folder where I am going to write my thesis.

![Example view of the unzipped `mitthesis`](/images/2025-08-02-Tutorial-MIT-Thesis-LaTeX/mitthesis-unzipped.png)

### Understand the contents

It is always a good idea to actually read the `README.md` file. The README lists the files contained in the distribution. It notes that the archive includes a class file and a `MIT-thesis-template` folder containing all the pieces needed to start writing your thesis:

| File/Folder	| Purpose |
|-------------|---------|
| `mitthesis.cls`	| Core LaTeX class implementing MIT formatting |
| `MIT-thesis-template/MIT-Thesis.tex` | Main LaTeX file for your thesis |
| `abstract.tex`, `acknowledgments.tex`, `biosketch.tex` | Files where you insert your abstract, acknowledgments and optional biosketch |
| `chapter1.tex`, `chapter...` | Sample chapters to use as templates |
| `committee_members.tex` | Optional page listing your thesis committee |
| `apendixa.tex`, `appendixb.tex` | Sample appendices showing code listing and long tables |
| `mitthesis-sample.bib` | Sample bibliography file with many entries |
| `mydesign.tex` | Optional file where you can load packages to customise colours, margins or caption styles |
| `fontsets/` | Subdirectory containing optional font definitions |

Somehow, the `README.md` mentions the existence of a `MIT-Thesis.pdf`, being _a sample thesis from the template, using default fonts_, but in the unzipped folder, I could not find it.
{: .notice}

Additionally, the `mitthesis-doc` directory contains detailed PDF documentation, while the examples directory provides sample theses in different fonts.

After extraction, keep the directory structure intact; LaTeX will look for chapter files relative to the main file. You can rename the outer folder to reflect your project's name.

## 2. Opening the project in VS Code

Launch **VS Code**, then choose **File → Open Folder…** and select the `MIT-thesis-template` folder (Not the outter `mitthesis` folder!).

VS Code will treat this directory as the workspace.

Open the `MIT-Thesis.tex` file as it is the root document.

![MIT-thesis-template folder opened in VS Code](/images/2025-08-02-Tutorial-MIT-Thesis-LaTeX/MIT-thesis-template-VSCode.png)

## 3. Trigger the build

At this time, you should see a "TEX" badge representing the LaTeX Workshop extension showing up on the left-most pannel of your window.

Now trigger a file save via the usual key combinations on your system:
* macOS: `command` + `S`
* Windows: `Ctrl` + `S`

As mentioned in the [previous tutorial]({% post_url 2025-06-29-Tutorial-LaTeX-VSCode %}), the save should have triggered the LaTeX Workshop extension to start building your LaTeX project. At the bottom left corner of the VS Code window, you should see a spinning "🔄 Build" indicating that the build is still in progress. This could take a minute to complete.

This is also a step that we likely could run into various issues, usually due to different local setups, somewhere / somehow. Please contact me with the error you run into and I could consolidate into quick fixes updated here. I also encourage you to try troubleshooting with your choice of GenAI tool. GitHub Copilot, if you have access to, is my go to choice.
{: .notice}

![Default MIT-Thesis compiled with resulting PDF displayed](/images/2025-08-02-Tutorial-MIT-Thesis-LaTeX/MIT-thesis-first-compiled-VSCode.png)

Scroll through the generated PDF file; it should closely match the [official example PDF](http://mirrors.ctan.org/macros/latex/contrib/mitthesis/examples/font_samples/Lmodern_sample.pdf) in formatting and structure.

Congratulations, by reaching here, you have your MIT Thesis LaTeX template ready.

## 4. Get familiarized with this template

We have to get comfortable with the structure of this template system -- there is no shortcut.

**Please read the [official documentation](http://mirrors.ctan.org/macros/latex/contrib/mitthesis/mitthesis-doc/mitthesis-doc.pdf) -- there is no shortcut**.

If I could offer only one pointer, that would be: skim through `MIT-Thesis.tex`, and you should see that it includes many `\input{}` statements that pull in separate files for each section of the thesis. Those referenced files are all in your workspace such as `abstract.tex`, `chapter1.tex`. Make some minor edits to these files. re-build your PDF, and observe the result. Action learning at its best!
