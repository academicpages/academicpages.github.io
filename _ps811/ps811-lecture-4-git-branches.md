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

# Creating a branch

1. Open your ps811-project in RStudio.

2. Click on the "branch" icon in the Git pane.

    ![git new branch](https://marcyshieh.github.io/ps811/lecture4-img/new-branch.png)

    *New branch: test.*

3. In the "New Branch" pop-up, name your new branch "test."

    ![git branch pop-up](https://marcyshieh.github.io/ps811/lecture4-img/git-branch.png)

    *Git Branch pop-up.*

4. The Git Branch window will pop-up, creating your new branch.

    ![2 branches](https://marcyshieh.github.io/ps811/lecture4-img/git-pane.png)

    *RStudio Git pane takes you to the "test" branch.*

5. RStudio should have automatically transported you to the new branch on your Git pane.

    ![git branches](https://marcyshieh.github.io/ps811/lecture4-img/git-branches.png)

    *Git branches on GitHub.*
    
6. Go to the GitHub of your ps811-project repository. You should be able to see a branch called `test` in the branch dropdown menu. Next to it, GitHub should tell you that there are 2 branches within your project.

# Working in the branch

1. You are now in the "test" branch.

2. Go to the Files pane and select the `document.Rmd` file.

3. Make some edits to the `document.Rmd` file. Whatever you want!

4. Commit, write a commit message, and push. Do what you always do to push something to your repository.

    ![recent push](https://marcyshieh.github.io/ps811/lecture4-img/recent-push.png)

    *Recent push to repositorry.*

5. Go to your GitHub repository. You should see a banner that there has been a push to your test branch.

6. Click on the "Compare & pull request" button.

    ![git open pull request](https://marcyshieh.github.io/ps811/lecture4-img/open-pull.png)

    *Open pull request.*

7. On the "Open a pull request" page, make sure you are pulling the "test" branch to the "master" branch. Check if they are able to merge.

    - There could some changes that are too different to merge, but it should not be the case for you right now.
    
8. If you scroll down the "Open a pull request" page, you can see what changes were made. This tells you exactly what files were changed and where the changes occurred.

9. Scroll back up to the form.

    ![create merge](https://marcyshieh.github.io/ps811/lecture4-img/create-pull.png)

    *Create pull request.*

10. Click on the down arrow next to the green "Create pull request" button. You will see two options: "create pull request" and "create draft pull request."

    - Create pull request: this is the default option. This simply tells whoever is "in charge" of the repository that it is ready to be reviewed and merged. This hierarchy lends itself well to a team where there's some sort of supervisor.
    
    - Create draft pull request: this is the second option. This allows your team to review and comment on it before your supervisor sees it. I wouldn't worry too much about this option right now.

11. Click on "Create pull request." (You can leave a comment if you want.)

    ![create merge](https://marcyshieh.github.io/ps811/lecture4-img/create-merge.png)

    *Merge pull request > Create a merge commit*
    

12. This should take you to the "Pull Requests" page. You will see one pull request open. You will see three options: "create a merge commit," "squash and merge," and "rebase and merge."

    - Create a merge commit: this is the default option. This merges your changes on the test branch to the master branch.
    
    - Squash and merge: this combines your changes in the test branch into one commit and pushes it out to the master branch.
    
    - Rebase and merge: this adds the entire history of the test branch onto the master branch *and* commits your changes. Don't worry about this one, but if you would like to read more about it, [Atlassin Bitbucket](https://www.atlassian.com/git/tutorials/merging-vs-rebasing) has a helpful summary of differences between "merging" and "rebasing."

13. Click on the default, "Merge pull request."

14. Click "Confirm merge."

    ![create pull request success](https://marcyshieh.github.io/ps811/lecture4-img/pull-request-success.png)

    *Pull request success message.*

15. You will receive a message that "Pull request successfully merged and closed."

15. You should be able to see your recent commits from the test branch transferred to the master branch.

## Deleting the branch

There may come a time where you might want to delete your branch. How would you go about it?

1. Click on the "# branches" link. 

    ![your branches](https://marcyshieh.github.io/ps811/lecture4-img/your-branches.png)

    *Your branches.*

2. Click on the red trash on the far right to "test" under "your branches."

## Restoring the branch

The great thing about Git is that, even if you accidentally delete a branch, you can always restore it.

![create merge](https://marcyshieh.github.io/ps811/lecture4-img/pull-requests.png)

*Pull requests link.*

1. Click on "Pull Requests."

    ![2 closed](https://marcyshieh.github.io/ps811/lecture4-img/2-closed.png)

    *There are 2 closed branches within your repository.*

2. Click on "# closed."

3. Select the "Test" repository.

4. Click on the "Test" repository.

    ![restore branch](https://marcyshieh.github.io/ps811/lecture4-img/restore-branch.png)

    *Restore branch.*

5. Scroll near the bottom of the page and click on the "Restore branch" button.

6. Go back to the ps811-project main page. You should see "test" restored as a branch.