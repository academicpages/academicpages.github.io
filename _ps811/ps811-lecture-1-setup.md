---
title: "Setting Up"
collection: ps811
type: "Graduate course"
venue: "Department of Political Science at the University of Wisconsin-Madison"
permalink: /ps811/ps811-lecture-1-setup
date: 2020-08-27
---

In this lecture, you will learn to:

1. [Install R.](ps811-lecture-1-setup#install-R)
2. [Install R Studio.]
3. [Install LaTeX.]
4. [Knit a document in R Markdown in PDF and HTML.]
5. Create a Github account.
6. Set up Git.
7. Connect RStudio to your Github account.
8. Set up a repository on Github.
9. Commit and push your R Markdown file to the Github repository.

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

# Creating a Github Account

Github is a website that hosts software development and version control via Git. While you are welcome to use Github alternatives to host your open-source projects in the future, this class will use Github.

1. Create an account on [Github](https://github.com/).

2. With the  [GitHub Student Developer Pack](https://education.github.com/pack), students get [Github Pro](https://education.github.com/discount_requests/student_application) and many other computing tools for free. You will need to use your university email address to apply, but the application process only took me a few minutes. Review the full list of [Github Pro features here](https://docs.github.com/en/github/getting-started-with-github/githubs-products#github-pro).

# Setting Up Git {#setup-git}

Git is a version-control system for tracking changes. Initially, software developers were the main users of Git. But lately, people of all stripes have adopted Git into their workflow. Git is especially useful for collaborative work because you will be able to identify information about edits to a file, including what changed, who made the change, and when the perrson made the change. Git is useful for solo work as well because it beats saving your document as a new document whenever you make a change. Visit [the official Git website](https://git-scm.com/) to learn more about Git.

The official Git website has a helpful guide on [installing Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for your operating system. I don't think I can improve on their existing guidance other than the fact that I do *not* recommend that you download from the source.

# Connecting RStudio to Git and Github

Much of this section is indebted to [Happy Git and GitHub for the useR](https://happygitwithr.com/rstudio-git-github.html) page on integrating RStudio with Git and Github.

Since I spend the better part of my life in RStudio, I want it to be able to connect to everything, including Git and Github. You are welcome to use [SourceTree](https://www.sourcetreeapp.com/) and other Git clients, but I prefer to consolidate all my work into my trusty RStudio environment due to convenience/laziness. As such, my lectures will simply assume that you use Github and RStudio and not their alternatives. Of course, you are welcome to expore the alternatives in your free time. In fact, I highly recommend that you do so  because I want you to end up with a workflow that works for you. The good news is, once you start familiarizing yourself with these basic building blocks, other tools will be easier to pick up.

## Say hello to git on RStudio

1. Click on the Terminal tab in RStudio.

2. Enter the following commands into the Terminal (i.e., also known as "the shell") and click "Enter." You may copy and paste all three lines at once then click "Enter," or type each line one by one, clicking "Enter" each time you need to start a new line.

```
git config --global user.name 'Your Name'
git config --global user.email 'yourgithub@email.com'
git config --global --list
```

You have "introduced" yourself to Git. Hopefully this is the beginning of a beautiful friendship.

## Create a repository

3. Go to the main [Github](https://github.com) site and make sure you are logged in. On the main page, click on the green "New" button on the right sidebar to create a new repository on Github.

4. On the "Create a new repository" page, enter the following:

* Repository name:` my_repository`, or whatever you want (this is basically like naming a folder)
* Description (optional): You can enter some description here about your folder, such as "test repository," though it is optional.
* Select "Public" for now, though you do have the option for "Private" for future repositories.
* Check "Add a README file."

5. Click on the "Create repository" button.

Your repository has been created.

## Connect Github to RStudio (the fun part)

The process technically *clones* the Github repository to your computer, but so much of the magic happens in RStudio that it *feels* that I am connecting Github to RStudio.

6. Go to RStudio. Go to File > New Project.

7. Select "Version Control."

8. Select "Git."

9. Go to Github. Find the Git repository that you created in Step 5.

10. Click on the "Code" button (in green). Copy and paste the URL under "Clone with HTTPS." The URL will end in .git, e.g., `https://github.com/marcyshieh/ps811.git`.

11. Go back to RStudio and fill out the following:
* Repository URL: The .git URL you copied in Step 10.
* Project directory name: This will default to whatever you named your Github repository. You can change it, or you can keep it the same for consistency (or, so you won't be confused).
* Create project as a subdirectory of: Find the directory on *your computer* that you want this copy of your Github repository to live in.

12. Check the "Open in New Session" box so you can have your projects (and misc non-project files) in different RStudio windows, but this is not necessary.

13. Click "Create Project."

14. You should see all the files from your Github repository in the RStudio file browser pane. This means that everything has been *cloned* from your Github repository to your computer or, in other words, downloaded.

## How does this all work?

15. In the file browser pane, open `README.md`.

16. Type in whatever you want in the file. A joke, the name of your celebrity crush, your favorite *Riverdale* character. Whatever you want, as long as it's not rude and/or incendiary.

17. Save the file.

18. Click on the Git tab on the upper right pane. 

The Git tab only shows up once you create an RStudio Project.

19. You will see that the `README.md` filepath you just edited show up under the Git tab. The Status will be a "M," which stands for "Modified."

20. Check the "Staged" box.

21. Click Commit.

22. The "RStudio: Review Changes" window will appear as a pop-up. Essentially, this allows you to validate whether or not you want to push the changes you made on your computer to your Github repository. There are 3 panes, which I will discuss in clockwork order.

**Pane 1** The files you changed.
**Pane 2** Commit messsage textbox. Here, you write some notes on what you changed. I am personally *horrible* at writing commit messages because I get impatient and lazy---I honestly just want to write, "I changed some stuff"---but that really negates the whole purpose, doesn't it? So let's make it our goal to get better at writing commit messages.
**Pane 3** The large pane on the bottom that show the changes you made. New additions are in gray, deletions are in red, and replacements are in green. You have the options of "stage chunk" or "discard chunk." If you select "stage chunk," you will be confirming the change