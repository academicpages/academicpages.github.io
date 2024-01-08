# How to publish from Release Pipeline in Azure DevOps

![Kunal Das, Author](https://miro.medium.com/v2/resize:fill:44:44/1*kfaefcgQPHrPsNobjuiiSg.jpeg)

Read on : 
 
<a href="https://kunaldaskd.medium.com/?source=post_page-----986bb257ea4--------------------------------">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0d/Medium_%28website%29_logo.svg/798px-Medium_%28website%29_logo.svg.png" alt="Medium Logo" width="200"/>
</a>

![](https://miro.medium.com/v2/resize:fit:700/1*A_IveIUhnhHOzi_a04hecA.png)

- [How to publish from Release Pipeline in Azure DevOps](#how-to-publish-from-release-pipeline-in-azure-devops)
  - [**Pushing the artifact in a git repo**](#pushing-the-artifact-in-a-git-repo)


In this section, I shall describe how you can get the artifact from the release pipeline,

Publishing any artifact from the build pipeline is pretty easy and there are plenty of tutorials available on the internet,

To publish an artifact from a build pipeline in Azure DevOps, you can use the `Publish Build Artifacts` task. Here's how you can do it:

1.  In your build pipeline, add the `Publish Build Artifacts` task to a phase that runs after the build is completed.
2.  In the `Path to publish` field, specify the path to the folder that contains the artifacts you want to publish. You can use a wildcard pattern to include multiple files and folders.
3.  In the `Artifact name` field, enter a name for the artifact.
4.  In the `Artifact publish location` field, choose whether you want to publish the artifact to the pipeline or to a file share.
5.  If you are publishing to a file share, enter the path to the share in the `Path to publish on the server` field.
6.  Save and run your pipeline.

That’s it! The `Publish Build Artifacts` task will publish the specified artifacts to the pipeline or file share you specified. You can then use the artifact in a release pipeline or download it from the Artifacts page in Azure DevOps.
```yaml
- task: PublishPipelineArtifact@1
  displayName: 'Publish Pipeline Artifact'
  inputs:
    targetPath: '$(Build.ArtifactStagingDirectory)'
    artifact: drop
```

Now for any reason, you may want to get the same result from the release pipeline as well, but unfortunately, the PublishPipelineArtifact@1 task does not support in release pipeline and even if you run it you will get some error, to solve this you can do one thing,

## **Pushing the artifact in a git repo**

in this way essentially you can save the copy of your updated artifacts in a separate folder inside your git repo.

let me show my scenario,

we are following the git flow branching strategy, so as you can see in each environment we need to save a copy of the updated ARM template .

![](https://miro.medium.com/v2/resize:fit:700/1*N02QCq_JlDm7I_FWyNanSg.png)

How did I achieve this?

Well, let me guide you step by step.

First, give all the permission required so that the pipeline can access the repo and push to it!

Go to project settings → Repository → select your repo →security → project collection Administrators → contribute → ALLOW

![](https://miro.medium.com/v2/resize:fit:700/1*AlJk6VeImXA3urf7XfHt_Q.png)

This setting essentially allows pushing from the build pipeline to the repo.

also, you have to check one more setting,

for the classic pipeline, select the below option.

![](https://miro.medium.com/v2/resize:fit:328/1*ImXJ-rMt4oEHY9BAHriYaw.png)

and for YAML, add the below code before the YAML code.

```yaml
variables:
  system_accesstoken: $(System.AccessToken)
```

now add this bash task in the pipeline.
```yaml
steps:
- bash: |
   git config --global user.email "azuredevops@microsoft.com"
   git config --global user.name "Azure DevOps"
   
   REPO="$(System.TeamFoundationCollectionUri)$(System.TeamProject)/_git/$(Build.Repository.Name)"
   EXTRAHEADER="Authorization: Bearer $(System.AccessToken)"
   git -c http.extraheader="$EXTRAHEADER" clone $REPO 
   cd $(Build.Repository.Name)
   
   mkdir 'QA-env'
   cd 'QA-env'
   
   cp '$(System.DefaultWorkingDirectory)/ARM/TemplateForWorkspace.json' .
   cp '$(System.DefaultWorkingDirectory)/ARM/TemplateParametersForWorkspace.json' .
   
   cd ..
   
   git add Template-QA/TemplateForWorkspace.json
   git add Template-QA/TemplateParametersForWorkspace.json
   
   
   MAINBRANCHNAME=main
   git config http.$REPO.extraHeader "$EXTRAHEADER"
   git commit -a -m "added QA json updated files"
   
   echo -- Merge $(Build.SourceBranchName) to $MAINBRANCHNAME --
   git fetch origin $(Build.SourceBranchName) --prune
   git merge origin/$(Build.SourceBranchName) -m "merge $(Build.SourceBranchName) to $MAINBRANCHNAME" --no-ff --allow-unrelated-histories
   
   
   
   git push origin $MAINBRANCHNAME
   git push origin --tags
   
  displayName: 'Bash Script'
```

If you are using a classic pipeline add a bash task

![](https://miro.medium.com/v2/resize:fit:700/1*dKCLnmrNT6qGFCkxWOYD6A.png)

And add the below script as inline,

```bash
git config --global user.email "azuredevops@microsoft.com"
git config --global user.name "Azure DevOps"

REPO="$(System.TeamFoundationCollectionUri)$(System.TeamProject)/_git/$(Build.Repository.Name)"
EXTRAHEADER="Authorization: Bearer $(System.AccessToken)"
git -c http.extraheader="$EXTRAHEADER" clone $REPO 
cd $(Build.Repository.Name)

mkdir 'qa1-ause-asy-01'
cd 'qa1-ause-asy-01'

cp '$(System.DefaultWorkingDirectory)/_Synapse-CI-pipeline/drop/ARM/TemplateForWorkspace.json' .
cp '$(System.DefaultWorkingDirectory)/_Synapse-CI-pipeline/drop/ARM/TemplateParametersForWorkspace.json' .

cd ..

git add Template-QA/TemplateForWorkspace.json
git add Template-QA/TemplateParametersForWorkspace.json


MAINBRANCHNAME=main
git config http.$REPO.extraHeader "$EXTRAHEADER"
git commit -a -m "added QA json updated files"

echo -- Merge $(Build.SourceBranchName) to $MAINBRANCHNAME --
git fetch origin $(Build.SourceBranchName) --prune
git merge origin/$(Build.SourceBranchName) -m "merge $(Build.SourceBranchName) to $MAINBRANCHNAME" --no-ff --allow-unrelated-histories



git push origin $MAINBRANCHNAME
git push origin --tags
```

you can update the commit message according to your need,

In this script, the following actions are being performed:

1.  The `mkdir` command is creating a new directory called `QA-env`.
2.  The `cd` command is changing the current working directory to `QA-env`.
3.  The `cp` command is copying the files `TemplateForWorkspace.json` and `TemplateParametersForWorkspace.json` from the `ARM` subdirectory of the default working directory to the current working directory (`QA-env`).
4.  The `cd ..` command is changing the current working directory back to the parent directory.
5.  The `git add` command is adding the files `TemplateForWorkspace.json` and `TemplateParametersForWorkspace.json` to the staging area in Git. This means that these files will be included in the next commit.

once done you will see the changes getting merged in the repo

![](https://miro.medium.com/v2/resize:fit:700/1*uFy8Cz23_1TFnnbKBoOCEQ.png)

That is it,

I guess you can try the steps and get back to me if any help is required!

Credit :

[https://learn.microsoft.com/en-us/azure/devops/pipelines/release/?view=azure-devops](https://learn.microsoft.com/en-us/azure/devops/pipelines/release/?view=azure-devops)

[https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/publish-build-artifacts-v1?view=azure-pipelines](https://learn.microsoft.com/en-us/azure/devops/pipelines/tasks/reference/publish-build-artifacts-v1?view=azure-pipelines)

[https://stackoverflow.com/questions/52837980/how-to-allow-scripts-to-access-oauth-token-from-yaml-builds](https://stackoverflow.com/questions/52837980/how-to-allow-scripts-to-access-oauth-token-from-yaml-builds)

[https://chuvash.eu/2021/04/09/git-merge-develop-to-main-in-an-azure-devops-release/](https://chuvash.eu/2021/04/09/git-merge-develop-to-main-in-an-azure-devops-release/)