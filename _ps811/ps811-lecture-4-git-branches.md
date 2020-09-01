---
title: "Lecture 4: Git Branch"
collection: ps811
type: "Graduate course"
venue: "Department of Political Science at the University of Wisconsin-Madison"
permalink: /ps811/ps811-lecture-4-git-branch
date: 2020-08-27
---

In this lecture, you will learn how to create and utilize git branches.

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

    ![create pull](https://marcyshieh.github.io/ps811/lecture4-img/create-pull.png)

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

# Using Git on the command line

There are a wealth of other things Git can do, and you will find a wealth of resources about Git online. Many of the resources you encounter will pertain to using Git with the command line, which is how software developers have traditionally used it. You may want to be a little bit familiarize with that, as many of the help resources tend to be specific to Git command line functions, not RStudio functions.

RStudio provides a good jumping off point, though. The Git pane in RStudio opens a shell that takes you to your exact project. In essence, the shell is a tool that allows you to type in commands that tell the computer what to do. In this case, you can type in all the Git commands you need to do without having to go back and forth in the RStudio and GitHub environments. The [Git Cheat Sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet) provides pretty good guidance on Git commands.

I will walk through a command line example with you that shows you how to commit and push a file into your repository using the command line. You should already be pretty familiar with the process at this point, so none of the inputs and outputs should not be a surprise to you.

1. Go to RStudio.

2. Open the `document.Rmd` file.

3. Make some edits to the file. Whatever you want!!

4. Knit the file to a PDF. See the edits you made in the .Rmd file show up in the PDF.

    ![git-shell](https://marcyshieh.github.io/ps811/lecture4-img/shell.png)

    *Open the Shell through the Git pane on RStudio.*

    ![git-shell-open](https://marcyshieh.github.io/ps811/lecture4-img/shell-open.png)

    *The shell opened. In MacOS, it's called a "Terminal" (featured here). In Windows, it's called a Command Prompt. They're equivalent.*

5. Now open up the Shell.

    ![git-status](https://marcyshieh.github.io/ps811/lecture4-img/git-status.png)

    *Check out the Git status on the shell.*

6. Type `git status` into the command line. You should see information in the shell that mirrors the information in the Git pane.

    ![git-add](https://marcyshieh.github.io/ps811/lecture4-img/git-add.png)

    *Add, i.e., stage all the files.*

7. Type `git add .` into the command line. This tells the computer that you want to stage all the changes (`git add`) in the ps811-project directory (`.` represents the directory you are currently in). The Git pane reflects this change without you having to check all the boxes.

    If you do not see the expected changes on your RStudio Git pane, just click on the RStudio window to make it active again and you will see the changes.
    
    ![git-reset](https://marcyshieh.github.io/ps811/lecture4-img/git-reset.png)

    *Reset, i.e., unstage all the files.*

8. Type `git reset .` into the command line. This tells the computer that you want to unstage all the changes in the ps811-project directory. The Git pane reflects this change without you having to uncheck all the boxes.

    ![git-add-doc](https://marcyshieh.github.io/ps811/lecture4-img/git-add-doc.png)

    *Stage the document.pdf file.*

9. Type `git add document.pdf` into the command line. This only stages the `document.pdf` file.

    ![git-commit](https://marcyshieh.github.io/ps811/lecture4-img/git-commit.png)

    *Commit document.pdf and see what happens to the Git pane on RStudio. This means that the test branch (the branch you are working in) has one more commit than the master branch. Which makes sense, because you just made a commit on the test branch.*

10. Type `git commit -m "<your message>"`. This allows you to commit the file and type a commit message. From my example, my commit message is, `pdf changes only`, but you are welcome to write what you want.

    ![git-push](https://marcyshieh.github.io/ps811/lecture4-img/git-push.png)

    *Push the document.pdf file.*

11. Type `git push`. This is akin to pushing the green push arrow icon in RStudio.

12. Go to the ps811-project repository on GitHub. Go to your test branch. You will see that your `document.pdf` has just been updated a few seconds ago.

    ![git-commit-others](https://marcyshieh.github.io/ps811/lecture4-img/git-commit-others.png)

    *Commit the document.Rmd and document.tex files.*

13. Go back to the Shell. You still have `document.Rmd` and `document.tex` in limbo. Commit both files and push.

    ```
    git add .
    git commit -m "i am committing both document.Rmd and document.tex right now"
    git push
    ```
    ![git-branch-repo](https://marcyshieh.github.io/ps811/lecture4-img/git-branch-2.png)

    *View all the branches in the repository.*

14. Go back to the Shell. Type in `git branch`. It will show all the branches in your ps811-project repository and the branch you are currently in---the test branch---will be denoted by an asterisk (*). In my operating system, it's showing up as neon green text.

    ![git-checkout-master](https://marcyshieh.github.io/ps811/lecture4-img/git-checkout-master.png)

    *Go to the master branch.*

15. Type in `git checkout master`.

    `git checkout master` is the equivalent of switching from the test branch to the master branch on the GitHub repository.

    ![git-merge-test](https://marcyshieh.github.io/ps811/lecture4-img/git-merge-test.png)

    *Merge the test branch with the master branch.*    

16. Type in `git merge test`. This merges everything from the test branch to the master branch.

    `git merge test` is *kinda* equivalent to opening a pull request and creating a merge on the GitHub repository.
  
    ![git-push-final](https://marcyshieh.github.io/ps811/lecture4-img/git-push-final.png)

    *The final push.*

17. Type in `git push`. This pushes the merge out into the master branch of your GitHub repository.

    `git push` at this point is *kinda* equivalent to confirming the merge on the GitHub repository. This is to make sure the two branches (test and master) are even, or the same.

Most of you might not be comfortable with the command line yet and would prefer the point-and-click ease of RStudio, and that's okay! This is *your* workflow and you should choose to work in a way that makes you the most comfortable. You may want to expedite your workflow someday, and this option is here for you if you want it!