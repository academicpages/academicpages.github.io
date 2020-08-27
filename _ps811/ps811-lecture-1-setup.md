---
title: "Setting Up"
collection: ps811
permalink: /ps811/ps811-lecture-1-setup
---

In this lecture, you will learn to:

1. [Install R.](ps811-lecture-1-setup#install-R)
2. [Install R Studio.]
3. [Install LaTeX.]
4. [Knit a document in R Markdown in PDF and HTML.]
5. Set up Git.
6. Connect R Studio to your Github account.
7. Set up a repository on Github.
8. Commit and push your R Markdown file to the Github repository.

# Installing R {#install-R}

R is a statistical programming language that is widely used in the discipline. Go to the [R official website](https://www.r-project.org/) to learn more about the software.

These instructions will help you download R on to your operating system.

1. Go to list of [CRAN mirrors](https://cran.r-project.org/mirrors.html). A "mirror" is essentially a distribution site for the software.

2. Select your preferred CRAN mirror. I recommend that you select the mirror closest to your current location. For example, if you are in Madison, WI, you should consider picking the mirror located at University of Michigan, though any of the midwestern universities will do.

3. Select the download for your operating system.

# Installing RStudio {#install-Rstudio}

RStudio is an integrated environment for R. If R is the engine, RStudio is the car. You can use the engine without the car, but you cannot drive the the car without the engine. In other words, you will not be able to use RStudio if you have not yet downloaded R. Always download R first. Go to the [RStudio official website](https://rstudio.com/) to learn more about the software.

These instructions will help you download RStudio on to your operating system.

1. Go to the [Download RStudio](https://rstudio.com/products/rstudio/download/) page. 

2. Click on the "Download" button" for RStudio Desktop Open Source Licnse Free.

3. Click on the "Download RStudio for [your OS]" button. The website should be detect which version of RStudio that you need to download.

# Installing LaTeX {#install-latex}

LaTeX is a software system for document prepartion. While we will not focus on LaTeX functionalities in this class, you will need to download it to compile R Markdown documents. Go to the [LaTeX official website](https://www.latex-project.org/) to learn more about the software.

If, for any reason, you would like to learn LaTeX, I would recommend opening an [Overleaf](https://www.overleaf.com) account and leveraging their [step-by-step tutorial](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes). While this course will primarily focus on teaching you how to write and generate your documents in R Markdown, you may encounter collaborators who use LaTeX. The good news is that R Markdown is pretty similar to LaTeX, so the skills are definitely transferrable.

These instructions will help you download LaTeX on to your operating system.

1. Scroll to the third section of the [Get](https://www.latex-project.org/get/) page where you see download options for Linux, MacOS, Windows, and Online.

2. Select your operating system.

- For MacOS users, you should download [MacTeX](http://www.tug.org/mactex/). You may access [step-by-step instructions here](http://www.tug.org/mactex/mactex-download.html).

- For Windows users, the website suggests that you download MikTeX, proTeXt, or TeX Live. There is a [StackExchange post](https://tex.stackexchange.com/questions/239199/latex-distributions-what-are-their-main-differences) discussing these options and then some. It appears like most people recommend [TeX Live](http://tug.org/texlive/).

# Knitting R Markdown Files {#knit-RMarkdown}

1. Open RStudio.

2. Click on File > New File.

3. Select R Markdown.

4. Make sure the sidebar is set to "Document."

5. Enter in the title of the document in the "Title" field and your name in the "Author" field.

6. Select HTML as the "Default Output Format" option for now. We will discuss how to output your file in PDF as well later in the lesson.

7. An R Markdown document (with the extension .Rmd) will appear. It will be called Untitled1.Rmd. R Markdown has a default template in place every time you create a new R Markdown document.

8. As you have selected HTML as the *default* output format, when you click the **Knit** button (it is the icon with a little ball of yarn and needle), it will automatically output the document as a HTML. Prior to outputing the HTML file, however, it will ask you to rename the file to something other than Untitled1.Rmd, which you should certainly do.

9. The HTML file will appear on the "Viewer" tab. To open the actual document, click on the button with the arrow pointing to the top right corner.

10. To output the same document as a PDF, click on the small down arrow next to the **Knit** button. Select "Knit to PDF."

As you can see, you have the option to "Knit to Word" but the political science community has recently turned on Word. As such, you are discouraged from knitting to Word, unless otherwise noted.

# Setting Up Git {#setup-git}

Git is a version-control system for tracking changes. Initially, software developers were the main users of Git. But lately, people of all stripes have adopted Git into their workflow. Git is especially useful for collaborative work because you will be able to identify information about edits to a file, including what changed, who made the change, and when the perrson made the change. Git is useful for solo work as well because it beats saving your document as a new document whenever you make a change. Visit [the official Git website](https://git-scm.com/) to learn more about Git.

The goal is to make sure you have Git all set up and things work as expected.