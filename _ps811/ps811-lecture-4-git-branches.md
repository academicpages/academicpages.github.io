---
title: "Lecture 4: Git Branch"
collection: ps811
type: "Graduate course"
venue: "Department of Political Science at the University of Wisconsin-Madison"
permalink: /ps811/ps811-lecture-4-git-branch
date: 2020-08-27
---

So far, you have been pushing all your files to the master branch. And that's fine when you are working on your own. But not so fine when you are working with other people!

The master branch is the front-facing view of your project. You can think of it as the latest "complete" version of the project, or the most up-to-date version of the project. You may not want all your works in progress to show up in the master branch, especially when decisions are still being made about certain aspects of the project. This becomes more crucial when you are part of a team.

One way to make sure that your collaborators do not overwrite the master branch with their changes without team approval is to have a branch that essentially clones the master branch but acts as a "workspace" for any revisions. This is especially helpful when each individual in a team is assigned a specific task to work on. They could do so in their own branch before merging all the results together.

This might be a relatable example: You have a personal statement for graduate school named `main_personal_statement.docx`. You send the document to your former advisors. Your advisors read the statement and send you a version of document with tracked changes called `main_personal_statement_their_initials.docx`. You want to be able to implement all their feedback into one document, so you open up each of document you get back and implement the feedback in the main version of the document.

With branches, each of your advisors could have worked in a branch, and you could have determined which parts of the duplicate version could be merged back into the main version.

In this lecture, I will go through how to work with branches in the RStudio environment.

1. Click on the "branch" icon in the Git pane.

2. In the "New Branch" pop-up, name your new branch "test."

3. 