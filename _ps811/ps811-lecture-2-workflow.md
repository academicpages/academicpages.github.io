---
title: "Lecture 2: Workflow"
collection: ps811
type: "Graduate course"
venue: "Department of Political Science at the University of Wisconsin-Madison"
permalink: /ps811/ps811-lecture-2-workflow
date: 2020-08-27
---

In this lecture, you will learn how to do everything you already do as a scholar but in a more organized and efficient manner. More specifically, you will learn how to do all these things in RStudio.

1. [Create a project in RStudio.](ps811-lecture-2-workflow#create-proj)
2. [Push a R Markdown document to your GitHub repository.](ps811-lecture-2-workflow#push-git)
3. [Write a paper in R Markdown.](ps811-lecture-2-workflow#write-paper)
4. [Organize a bibliography.](ps811-lecture-2-workflow#org-bib)

# Why create a project?

You are probably used to storing all your project-related files in a project folder on your computer. And, you may tell yourself that if you wanted to send all the files to your collaborator, you can zip that folder up and upload everything on to your Box or Dropbox. Then your collaborator can unzip that folder, work on some files, and re-upload the files. But then you don't know which parts she edited unless you read her email, which *might* be detailed, but also might not be! You want to be prepared for the latter.

So this is why creating a project in RStudio and connecting it to GitHub is important. All project files will be in a central location and all collaborators will go to the same central location. There is no convoluted re-uploading and downloading of any sort where edits may get lost in the process.

And, if you have no collaborators, you will be able to track your own work carefully so if you were ever to invite someone to review your project or bring on a collaborator, it wouldn't be much of a hassle.

You also want to think ahead: many of the top journals in the discipline require you to provide replication files. Instead of having to go back and retrace your steps, you can just provide your R Project directory. In essence, whoever has access to your R Project directory will be able to replicate every step that generated the final paper and results.

So let's get started.

# Creating a project in RStudio {#create-proj}

The goal of this section is for you to be able to create a project in RStudio that you can connect to Github. Some of these steps are a review of what we learned in the previous lesson.

1. Log in to GitHub, if you are not already logged in.

2. Click on the green "New" button to create a new repository.

3. On the "Create a new repository" page, enter the following into the form:

    - Repository name: ps811-project
    - Select "Public"
    - Check "Add a README file"

4. Open RStudio. Go to File > New Project.

5. Select “Version Control.”

6. Select “Git.”

7. Go to GitHub. Find the Git repository that you created in Step 3.

8. Click on the “Code” button (in green). Copy and paste the URL under “Clone with HTTPS.” The URL will end in .git, e.g., `https://github.com/marcyshieh/ps811.git`.

9. Go back to RStudio and fill out the following:

    - Repository URL: The .git URL you copied in Step 8.
    
    - Project directory name: This will default to whatever you named your Github repository. You can change it, or you can keep it the same for consistency (or, so you won’t be confused).
    
    - Create project as a subdirectory of: Find the directory on your computer that you want this copy of your Github repository to live in.
  
10. Check the “Open in New Session” box so you can have your projects (and misc non-project files) in different RStudio windows, but this is not necessary.

# Pushing a R Markdown document to your Github repository {#push-git}

In the previous lesson, you took the README.md file from your Github repository, edited it, and pushed your changes back on to the repository. In this lesson, you will learn how to create a document on your computer in RStudio and push it to the repository.

1. Go to File > New File > R Markdown.

2. Enter a sample title for "Title" and your name for "Author."

3. Select PDF as the default output format.

    This file should look familiar to you. It is the same default R Markdown template you knitted in the previous lesson.

4. Go to File > Save As and make sure you are in the `ps811-project` directory. Once you confirm that, you can save it as an .Rmd file, such as `example.Rmd`.

5. Knit the file as a PDF.

6. Push the directory onto your GitHub repository. Go to the "Git"" pane. Click "Commit." Check "Staged" for the `.gitignore`, `ps811-project.Rproj`, `sample.Rmd`, and `sample.pdf` files. Type a commit message on what changes you made so you (or your collaborators) can note what happened.

    The `.gitignore` file contains files that Git should ignore. In this case, RStudio produces some metadata (e.g., logs) when you create and revise files, but Git defaults to ignoring those files, i.e., not pushing changes to their on to your GitHub repository. If, in any case, you want to tell Git to not ignore certain R-generated files, you can always open up the `.gitignore` file and edit it to *not* ignore those files.

7. Click the green "Push" up arrow.

    ![repository](https://marcyshieh.github.io/ps811/lecture2-img/repository.png)

    *This is how your repository for ps811-project should look like.*

8. Go back to GitHub on your browser and click on your ps811-project repository. (Refresh if you never left the repository page.)

9. You should be able to see your `.gitignore`, `ps811-project.Rproj`, `sample.Rmd`, and `sample.pdf` files in your GitHub repository.

    ![files-pane](https://marcyshieh.github.io/ps811/lecture2-img/files-pane.png)

    *Delete files from your files pane.*

10. But you don't really need `sample.Rmd` and `sample.pdf` in your repository. So you want to delete it from the directory on your computer and the repository on GitHub. Go ahead and check the boxes next to `sample.Rmd` and `sample.pdf` in the "File" pane. Then, click "Delete."

    ![git-pane-delete](https://marcyshieh.github.io/ps811/lecture2-img/git-pane-delete.png)

    *Your Git pane should look like this once you delete your files from the directory in your computer.*

11. Your Git pane should show `sample.Rmd` and `sample.pdf` with little red "D" statuses next to them (D for Delete!). Go ahead and click commit, stage these changes, write a commit message, and push.

12. Go back to GitHub on your browser and click on your ps811-project repository. (Refresh if you never left the repository page.)

13. The two files you just deleted---`sample.Rmd` and `sample.pdf`---are now gone. Because you deleted them.

    ![commits](https://marcyshieh.github.io/ps811/lecture2-img/commits.png)

    *Click on the [#] commits link to see the history of your repository.*

14. Your files are gone but not forgotten. The great thing about Git is that you can go back and look at the files you deleted and retrieve them if necessary. Go to the counter-clockwise clock icon and click on the "[#] commits" link.

    ![commits-page](https://marcyshieh.github.io/ps811/lecture2-img/commits-page.png)

    *This is the commits page.*

15. There, you will see the record of your changes and can click on the icons (as discussed in the previous lesson) to review or retrieve anything you deleted.

# Writing a paper in R Markdown {#write-paper}

Now you are hopefully more comfortable doing simple things with RStudio, R Markdown documents, Git, and GitHub. So now let's move on to how to do stuff that you already do and figure out how the Git workflow (in conjunction with RStudio) can make it better.

When you write papers for your classes, you want to write it with the hope that it will turn into a publishable paper. That is the goal, anyway, so let's strive for it. Political science manuscripts use the [APA style](https://ccconline.libguides.com/c.php?g=242121&p=3409502) so you want to find a template that conforms to that style. 

There are many R Markdown templates out there, even specific templates for specific journals, and there are certainly ways you can customize templates to your heart's desire. When you create a new R Markdown document, you can select "From Template" from the sidebar and see what has already been pre-loaded. 

For the sake of catering to everyone's needs, we are going to work with the  [papaja](https://crsh.github.io/papaja_man/introduction.html) R package. papaja, as you may have easily guessed, stands for "preparing APA journal articles." It's a package that's currently in the process of being developed so there might be some kinks here and there (though I haven't encountered any in my own work). Ultimately, this lesson is to give you a sense of how R Markdown templates work so you go out and explore on your own.

## Prerequisites

Just so you know what is required to run the papaja R package, I'm going to do a breakdown for you. **You should have fulfilled all the prequisites if you completed the previous lesson.**

1. To install papaja, you need to install R, which you should have already done. If not, what have I been doing this whole time...?

2. You also need to install [pandoc](https://pandoc.org/index.html), which you *should* have if you already installed RStudio. Pandoc is a document converter that is pretty versatile and can convert a file from one format to the other pretty easily. It's worth checking out sometime. But for now, we just need it for papaja to work.

3. You need a TeX distribution, which you already do, from installing LaTeX in the first lesson.

## Installing papaja

1. papaja is not yet available on CRAN (the Comprehensive R Archive Network), so you need to install it from the creator's GitHub. To do so, you need to install the `devtools` package by entering the following into your console.

    ```
    install.packages("devtools")
    ```

    Once you install a package to your computer, you do not have to install it again, unless you update to a new version of R. You can check your installed packages with the `installed.packages()` command.
    
2. Access the package you just installed by entering the following into the console.

    ```
    library(devtools)
    ```

    Think of this as telling your computer to point and click on a program to "open" it. You need to do this every time you open a new R session and wish to use the package---in the same way that you need to click on the RStudio icon every time you want to use it.
    
3. Enter the following command into the console. This installs the *stable* development version of the package from Github.

    ```
    devtools::install_github("crsh/papaja")
    ```

    The `devtools::`` part of the command simply tells R where the `install_github` part of the command is coming from. There are cases where you may have loaded two packages and both packages have `install_github` as a command. Doing the double-colon simply ensures that you are specifying the package that the command is coming from. Since you have only loaded the devtools package so far, you don't need to specify that `install_github` is coming from the devtools package, but I just wanted to demonstrate this point in case you ever end up in such a conundrum.
    
## Opening the template

1. Go to File > New File > R Markdown.

    ![apa-article](https://marcyshieh.github.io/ps811/lecture2-img/addins.png)

    *Select APA article (6th edition) from the menu.*

2. Select "From Template" from the sidebar and select "APA article (6th edition)" on the list. As you can see, it tells you that this template is from papaja package.

3. Click OK.

    ![template](https://marcyshieh.github.io/ps811/lecture2-img/template.png)

    *This is how the template should look like.*

4. The template appears.

## Getting to know your APA R Markdown template

**Lines 1 to 64** is a form-like feature that you can fill out with your own information. This is called a [YAML front matter](https://en.wikipedia.org/wiki/YAML), which you can read more about on your own time. Basically, it's basically a form you can fill out to define what should be going on in the back end. Most of these fields should be pretty self-explanatory, but I'd like to point out a few things.

- **Line 49** To figure out word count, I recommend the [wordcountaddin](https://github.com/benmarwick/wordcountaddin) package. Not only does it tell you how many words and characters are in your document, but provides some information on the readability of your statistical tables (e.g., regression tables) as well. I suggest not being too worried about this right now, but it is worth thinking about now.

- **Line 51** papaja comes with a "r-reference.bib" file for all your R Markdown documents. You should see the file on your "Files" pane. Your bibliography will live in the .bib file. I'll talk more about .bib files later.

- **Lines 53-59** may sound ambiguous, but the official papaja page has definitions for each field on their [Rendering Options](https://crsh.github.io/papaja_man/r-markdown-components.html#rendering-options) section.

### Let's talk about code chunks

Put your R commands in a [code chunk](https://rmarkdown.rstudio.com/lesson-3.html). With code chunks, you are basically telling RStudio, "hey, i need you to run this." Code chunks look like the following.

<pre>
```{r}
[insert your R code here]
```
</pre>

Of course, you can customize what you do tell your code chunks to do. Here are some examples, but for the full list of options, check out the [R Markdown Cheat Sheet - Section 5: Embed Code](https://rstudio.com/wp-content/uploads/2015/02/rmarkdown-cheatsheet.pdf).

* `include = FALSE` tells R to run the code in the background but NOT show the results or the code on the R Markdown document. This is helpful if you want to show results in a chunk later in the file, but you want to run some commands in the current chunk.

<pre>
```{r include = FALSE}
[insert your R code here]
```
</pre>

* `echo = FALSE` tells R to run the code in the background and not show the code in the R Markdown document, but to show the results. This is helpful for tables and graphics.

<pre>
```{r echo = FALSE}
[insert your R code here]
```
</pre>

* `message = FALSE` tells R to not show messsages generated by the comamnds in the code chunk. For instance, some packages might provide some messages (e.g., citations) but you do not want it to show up in your R Markdown document.

<pre>
```{r message = FALSE}
[insert your R code here]
```
</pre>

* `fig.cap = "..."` tells R to add a caption to your figure. You simply replace `...` with the caption.

<pre>
```{r fig.cap = "This is a photo of all my favorite NYC brownstones."}
[insert your R code here]
```
</pre>

    * You may combine these options by separating them with a comma.

        <pre>
        ```{r echo = FALSE, fig.cap = "This is a photo of all my favorite NYC brownstones."}
        [insert your R code here]
        ```
        </pre>
        
    * You may even name your chunks. In this example, the code chunk is named "chart." Note that you do NOT separate the name and the options with a comma.
    
        <pre>
        ```{r chart echo = FALSE, fig.cap = "This is a photo of all my favorite NYC brownstones."}
        [insert your R code here]
        ```
        </pre>
        
Now that you have an understanding of code chunks, let's explore the code chunks on the R Markdown template we downloaded.

## Code chunks in the papaja template

**Lines 66-69** is where you put your packages. As you grow into a proficient R user, you are going to use many packages (not just devtools!) and you should load them all in a section that looks like this. In other words...

<pre>
```{r setup, include = FALSE}
[load your packages using the library() function]
[load your .bib file using the r_refs() function]
```
</pre>

**Lines 71-75** are where you can set your analysis preferences. The default appears to be code that sets a seed for a random number generator. You may need a seed when you run a say, k-means clustering algorithm, but I wouldn't worry too much about it right now.

## Body of the papaja template

**Lines 79-94** shows headings for the document. This is how the headings will look like based on the number of hashes (#) they put. A good way to think about it is `#` is a the largest heading, and every `#` you add on makes the heading smaller. For a comprehensive list of headings, check out check out the [R Markdown Cheat Sheet - Section 3: Markdown](https://rstudio.com/wp-content/uploads/2015/02/rmarkdown-cheatsheet.pdf).

# Methods (one hash - #)

## Participants (two hashes - ##)

## Material (two hashes - ##)

## Procedure (two hashes - ##)

## Data analysis (two hashes - ##)

# Results (one hash - #)

# Discussion (one hash - #)

Now, you can create headings and subheadings and subsubheadings, etc.

**Lines 97-106** is the last few pages of the document, which will be devoted to the bibliography. And much of the end of this template is some [TeX markup language](https://en.wikibooks.org/wiki/TeX), which dominates LaTeX but is only sometimes used in R Markdown documents. You don't have to change any of this, but here is some background on the building blocks.

- `\newpage` command just creates a new page and comes from the TeX language.
- `\begingroup` begins a group and `\endgroup` ends a group. In essence, you're putting stuff in a box.
- So you've built your box. Within that box, you want your bibliography to indent a certain way. With `\parindent`, you are indenting the first line of a paragraph (i.e., each new line) and with `\leftskip`, you can reduce the paragraph size from the left.
- The grouping and the formatting are for the bibliography, which the template inserts with the following HTML code. This template handles the bibliography style using HTML/CSS, but this might not be the case with all templates.

```
<div id="refs" custom-style="Bibliography"></div>
```

# Organizing a bibliography {#org-bib}

## Downloading Zotero

You are going to read a lot of things and cite a lot of things in graduate school. And not only that, you will need to organize all your documents so your prelim studying won't be a mess. 

I recommend using [Zotero](https://zotero.org) to organize your bibliography and creating an account on Zotero so you can access your bibliographies anywhere. You are, of course, free to use other reference organizers, but I will use Zotero to go through these examples. Zotero is pretty user-friendly. Once you open it, most of the buttons are pretty self-explanatory. You can create new collections, new groups, etc. (i.e., a collection can be Fall 2020, and a group can the name of a class). You may tag an article with relevant categories, add a note, etc.

Once you have your folders all set up, you can just drag in a PDF into Zotero. Zotero will generate metainfo from most PDFs that you download from JSTOR or another catalog from the UW-Madison library, but in cases that the metainfo does not show up, Zotero makes it easy for you to enter in the fields yourself.

## Downloading Better Bibtex for Zotero

To make sure that you can translate the information from Zotero into information for the reference page in your R Markdown file, you will need to download [Better BibTeX for Zotero (BBT)](https://retorque.re/zotero-better-bibtex/). 

1. Go to [BBT GitHub](https://github.com/retorquere/zotero-better-bibtex/releases/tag/v5.2.63) and download the `zotero-better-bibtex-5.2.63.xpi` file. 

    - If you use Firefox, you need to right click on the .xpi link and select Save As. 

2. Follow the instructions on the [BBT installation page](https://retorque.re/zotero-better-bibtex/installation/).

3. When you restart BBT, there will be a pop-up window tiutled "Welcome to Better BibTex for Zotero." Click "Continue."

4. Select "Use the BBT default citekey format" (by default). Click "Continue."

5. Check "Enable drag-and-drop-citations" (by default). Click "Continue."

6. Check "Unabbreviate journal names on import" and "expand @string journal names on import" (by default). Click "Continue."

7. There's some information about exporting using BBT. Read and make sure that in the future, instead of choosing "BibTeX" for your Zotero exports, you can pick "Better BibTeX," and click "Continue."

8. Click "Done." You'll be prompted to restart Zotero again.

9. Just upload a PDF copy of a journal article from one of your classes to Zotero.

## Loading the citr package

1. Install the `citr` package in the console.

    ```
    install.packages("citr")
    library(citr)
    ```

2. Restart RStudio. Reopen your project.

3. Place your cursor on line 80 (under the Methods section).

    ![addins](https://marcyshieh.github.io/ps811/lecture2-img/addins.png)

    *Addins button on the far right of the menu.*

4. Now click on the Addins button on the top of your RStudio. You should be able to see a section for CITR and selection an option to "Insert Citations."

5. Go to "Settings" (bottom of pop-up window).

    ![citr-settinngs](https://marcyshieh.github.io/ps811/lecture2-img/citr-settings.png)

    *Check the settings and make sure they match.*

6. Your parent document should be `document.Rmd` and you should add references to `r-references.bib`. This might be set automatically but if not, make sure these are the fields.

7. Return to "Insert Citations" (bottom of pop-up window).

8. Enter (or start entering) the title of the article you dragged into Zotero. It should show up in the search so you can just select it. You have the option to add the citation with parentheses (e.g., (Author, 1999)) or without parentheses (e.g., Author (1999)).

9. Click "Insert Citation."

10. Go to your "Files" pane on RStudio and click on the `r-references.bib` file. On line 16, you will see that they created the citation for you.

11. Now when you knit the file to a PDF, the citation appears under the Methods section of your PDF!

    - You may use the Zotero Chrome extension to add any article from your Chrome browser to your Zotero article. 
    
    - If you add a new article to your Zotero library, it may not show up on citr unless you restart R.
    
    - citr Addins is admittedly a bit janky and if you would prefer to enter the commands on the console manually, you are welcome to read the [citr R documentation](https://cran.r-project.org/web/packages/citr/citr.pdf). 
    
12. Finally, push all your files out to your repository. Do the steps from memory. If you don't remember them, go back and look at the steps. Once you have successfully pushed all the files to the repository, they should show up in your `ps811-project` GitHub repository.