#How to copy a GitHub repository

To ensure that your changes are kept private and not contributed back to the original repository, you should avoid creating pull requests from your fork to the original repository. Here are some steps to follow:

1. **Clone Your Fork:**
   - Clone your forked repository to your local machine using the following command:

```{bash}
     git clone https://github.com/your-username/your-forked-repo.git
```

2. **Make Changes Locally:**
   - Make any necessary changes or customizations to your local copy of the repository.
   
```{bash}
#copy publications biltex file to pub folder
cp ~/folder/pub.bib ./_publications
```

3. **Commit Changes:**
   - Commit your changes locally using Git. Use commands like:

```{bash}
     git add .
     git commit -m "Description of changes"
     ```

4. **Push Changes to Your Fork:**
   - Push your changes to your fork on GitHub:
     ```
     git push origin master
     ```

5. **Avoid Creating Pull Requests:**
   - Do not create pull requests from your fork to the original repository. Pull requests are the mechanism for proposing changes to be merged back into the original repository. If you don't create a pull request, your changes will not be merged into the original repository.

6. **Keep Changes Local:**
   - If you want to keep your changes only on your local machine and not push them to your fork on GitHub, simply don't execute the `git push` command.

By following these steps, you can keep your changes private and isolated to your forked repository. If you later decide to contribute back to the original repository or make your changes public, you can reconsider creating pull requests at that time.