---
title: "Tutorial: MIT Thesis LaTeX Template with VS Code"
date: 2025-08-04
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

![Example view of the unzipped `mitthesis`](/images/2025-08-04-Tutorial-MIT-Thesis-LaTeX/mitthesis-unzipped.png)

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

![MIT-thesis-template folder opened in VS Code](/images/2025-08-04-Tutorial-MIT-Thesis-LaTeX/MIT-thesis-template-VSCode.png)

## 3. Trigger the build

At this time, you should see a "TEX" badge representing the LaTeX Workshop extension showing up on the left-most pannel of your window.

Now trigger a file save via the usual key combinations on your system:
* macOS: `command` + `S`
* Windows: `Ctrl` + `S`

As mentioned in the [previous tutorial]({% post_url 2025-06-29-Tutorial-LaTeX-VSCode %}), the save should have triggered the LaTeX Workshop extension to start building your LaTeX project. At the bottom left corner of the VS Code window, you should see a spinning "🔄 Build" indicating that the build is still in progress. This could take a minute to complete.

This is also a step that we likely could run into various issues, usually due to different local setups, somewhere / somehow. Please contact me with the error you run into and I could consolidate into quick fixes updated here. I also encourage you to try troubleshooting with your choice of GenAI tool. GitHub Copilot, if you have access to, is my go to choice.
{: .notice}

![Default MIT-Thesis compiled with resulting PDF displayed](/images/2025-08-04-Tutorial-MIT-Thesis-LaTeX/MIT-thesis-first-compiled-VSCode.png)

Scroll through the generated PDF file; it should closely match the [official example PDF](http://mirrors.ctan.org/macros/latex/contrib/mitthesis/examples/font_samples/Lmodern_sample.pdf) in formatting and structure.

Congratulations, by reaching here, you have your MIT Thesis LaTeX template ready.

## 4. Get familiarized with this template

We have to get comfortable with the structure of this template system -- there is no shortcut.

**Please read the [official documentation](http://mirrors.ctan.org/macros/latex/contrib/mitthesis/mitthesis-doc/mitthesis-doc.pdf) -- there is no shortcut**.

If I could offer only one pointer, that would be: skim through `MIT-Thesis.tex`, and you should see that it includes many `\input{}` statements that pull in separate files for each section of the thesis. Those referenced files are all in your workspace such as `abstract.tex`, `chapter1.tex`. Make some minor edits to these files. re-build your PDF, and observe the result. Action learning at its best!

If you are a candidate in MIT's [Leaders for Global Operations (LGO)](https://lgo.mit.edu/), MS/MBA dual-degree program, please continue reading this post. Otherwise, you are all set.

## 5. Tweaks for an LGO thesis

The official template package comes with an example that is applicable to an LGO thesis: [`mitthesis/examples/cover_page_samples/latex_sources/One_author_two_degrees.tex`](https://mirrors.ctan.org/macros/latex/contrib/mitthesis/examples/cover_page_samples/latex_sources/One_author_two_degrees.tex). I've adapted it into a something that is hopefully easier to follow.

1. In your root document file (`MIT-Thesis.tex`), find the lines that goes
    ```tex
    \begin{document}
    %%% edit the following commands to match your thesis %%%%%%%%%%
    ```
    We need to edit the ensuing lines.
2. Replace everything between `\title{...}` and `\ThesisDate{...}` (including these two commands) with the following content
    ```tex
    \title{Simplify and Accelerate: An Awesome Dual-Degree Thesis Title}

    % \Author{Author full name}{Author department}[Author's first PREVIOUS degree][Author's second PREVIOUS degree][...
    % Note that third, fourth, fifth, and sixth arguments are optional [] and may be omitted

    \Author{LGO Student Name}{MIT Sloan School of Management and Department of Electrical Engineering and Computer Science}[B.S. Previous Degree, Previous College, 2018]

    % Use once for each degree fulfilled by thesis
    % For two degrees from one department, leave the department argument blank for the second degree {}.
    \Degree{Master of Business Administration}{MIT Sloan School of Management}
    \Degree{Master of Science in Electrical Engineering and Computer Science}{Department of Electrical Engineering and Computer Science}

    % If there is more than one supervisor, use the \Supervisor command for each.
    \Supervisor{Sloan Advisor Name}{Professor of Operation Management}
    \Supervisor{Engineering Advisor Name}{Professor of Electrical Engineering and Computer Science}

    % Professor who formally accepts theses for your department (e.g., the Graduate Officer, Professor Sméagol,...)
    % If you need to reduce vertical space, put the acceptor title in the second argument and leave the third blank {}.
    \Acceptor{Engineering Acceptor Name}{Professor of Electrical Engineering and Computer Science}{Graduate Officer, Department of Electrical Engineering and Computer Science}
    \Acceptor{Sloan Acceptor Name}{Assistant Dean}{MBA Program, Sloan School of Management}

    % If your title page is overflowing (from too many names, degrees, etc.), you can scale 
    %    down the Signature block at the bottom with this command, or use another creative solution...
    \SignatureBlockSize{\footnotesize}
    \AuthorNameSize{\normalsize}

    % Usage: \DegreeDate{Month}{year}
    % Valid degree months are September, February, or June.  
    \DegreeDate{May}{2026}

    % Date that final thesis is submitted to department
    \ThesisDate{May 8, 2026}
    ```

Not done yet -- the LGO program office also required:

> Please ensure that you include a statement recognizing that your thesis is submitted… “IN CONJUNCTION WITH THE LEADERS FOR GLOBAL OPERATIONS PROGRAM AT THE MASSACHUSETTS INSTITUTE OF TECHNOLOGY”.
>
> -- "Thesis Review and Submission Process", _LGO Handbook_ (accessed on August 3, 2025)

To achieve this, we have to have our own version of the `mitthesis.cls` (remember it from the "outter" directory?)

1. Copy the `mitthesis.cls` file to your project workspace (i.e. same folder as your `MIT-Thesis.tex`)
2. In your **copied** `mitthesis.cls` file, find the line that goes `at~the\par`. It should appear right after a line that goes `\__degree_block:`
3. Insert the following line in between `\__degree_block:` and `at~the\par`:
    ```
    in~conjunction~with~the~Leaders~for~Global~Operations~program\par
    ```
    Remember to maintain the same leading indentation as the two reference lines.
4. So we end up with something like:
    ```
    \__degree_block:
		in~conjunction~with~the~Leaders~for~Global~Operations~program\par
    at~the\par
    ```
    (Leading indentation omitted to save some spaces here.)

By doing so, our LaTeX project build should pick up our copied and edited `mitthesis.cls` file instead of the default `mitthesis.cls` provided by the template package.
<details>
<summary>This hot-fix comes with a tiny risk.</summary>

When the official template package is updated and we thought we've pulled the latest updates from CTAN, those new changes won't show up in our thesis workspace unless we merge the new version of `mitthesis.cls` into our local copy of `mitthesis.cls` while keeping the "in conjunction..." hot fix.

My gut feeling: risk is trivial. We only work on our thesis for less than a year and then will never touch it after thesis submission, so we could not care less about getting the latest template updates...

</details>

Re-build your LaTeX project and you should see something like this:

![An example of LGO thesis cover page rendered](/images/2025-08-04-Tutorial-MIT-Thesis-LaTeX/LGO-Thesis-Cover-Example.jpg)

### Known issues

* `\SignatureBlockSize{\footnotesize}` in my example is to avoid a long department name like "Electrical Engineering and Computer Science" causing overflow; particularly, under "Authored by:", the line that shows both Sloan and EECS is too long and only `\footnotesize` could tame this loong (dragon).
    * I am searching for a solution that could add a line break and avoid such a small font size...

Did I miss any other places in the templat that requires tweaking for an LGO thesis? Please let me know!
{: .notice}