---
title: "Lecture 3: Bibliography"
collection: ps811
type: "Graduate course"
venue: "Department of Political Science at the University of Wisconsin-Madison"
permalink: /ps811/ps811-lecture-3-bib
date: 2020-08-27
---

In this lecture, you will learn how to organize a bibliography within your workflow.

1. [Download Zotero.](ps811-lecture-3-bib#download-zotero)
2. [Download Better Bibtex for Zotero.](ps811-lecture-3-bib#download-bbt)
3. [Load the citr package](ps811-lecture-3-bib#load-citr)

# Downloading Zotero {#download-zotero}

You are going to read a lot of things and cite a lot of things in graduate school. And not only that, you will need to organize all your documents so your prelim studying won't be a mess. 

I recommend using [Zotero](https://zotero.org) to organize your bibliography and creating an account on Zotero so you can access your bibliographies anywhere. You are, of course, free to use other reference organizers, but I will use Zotero to go through these examples. Zotero is pretty user-friendly. Once you open it, most of the buttons are pretty self-explanatory. You can create new collections, new groups, etc. (i.e., a collection can be Fall 2020, and a group can the name of a class). You may tag an article with relevant categories, add a note, etc.

Once you have your folders all set up, you can just drag in a PDF into Zotero. Zotero will generate metainfo from most PDFs that you download from JSTOR or another catalog from the UW-Madison library, but in cases that the metainfo does not show up, Zotero makes it easy for you to enter in the fields yourself.

# Downloading Better Bibtex for Zotero {#download-bbt}

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

# Loading the citr package {#load-citr}

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