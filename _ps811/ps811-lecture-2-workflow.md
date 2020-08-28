---
title: "Workflow"
collection: ps811
type: "Graduate course"
venue: "Department of Political Science at the University of Wisconsin-Madison"
permalink: /ps811/ps811-lecture-2-workflow
date: 2020-08-27
---

In this lecture, you will learn how to do everything you already do as a scholar but in a more organized and efficient manner. More specifically, you will learn how to do all these things in RStudio.

1. Create a project in RStudio.
2. Create a R Markdown document.
3. Write math in your R Markdown document.
4. Organize a bibliography.

# Why create a project?

You are probably used to storing all your project-related files in a project folder on your computer. And, you may tell yourself that if you wanted to send all the files to your collaborator, you can zip that folder up and upload everything on to your Box or Dropbox. Then your collaborator can unzip that folder, work on some files, and re-upload the files. But then you don't know which parts she edited unless you read her email, which *might* be detailed, but also might not be! You want to be prepared for the latter.

So this is why creating a project in RStudio and connecting it to GitHub is important. All project files will be in a central location and all collaborators will go to the same central location. There is no convoluted re-uploading and downloading of any sort where edits may get lost in the process.

And, if you have no collaborators, you will be able to track your own work carefully so if you were ever to invite someone to review your project or bring on a collaborator, it wouldn't be much of a hassle.

You also want to think ahead: many of the top journals in the discipline require you to provide replication files. Instead of having to go back and retrace your steps, you can just provide your R Project directory. In essence, whoever has access to your R Project directory will be able to replicate every step that generated the final paper and results.

So let's get started.

## Creating a project in RStudio

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

11. Click “Create Project.”

# Creating a R Markdown document

In the previous lesson, you took the README.md file from your Github repository, edited it, and pushed your changes back on to the repository. In this lesson, you will learn how to create a document on your computer in RStudio and push it to the repository.