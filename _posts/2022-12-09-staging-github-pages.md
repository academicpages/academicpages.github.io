---
layout: single
title:  "Staging site for GitHub Pages using GitHub Actions"
date: 2022-12-09
permalink: /posts/2022/12/staging-github-pages/
tags:
  - GitHub Actions
  - GitHub Pages
  - undergrad
  - technical
  - recommended read
---

I spent the last weekend writing a GitHub Action to deploy a PR to a development preview site. While there are awesome existing solutions such as Vercel and Netlify, I wanted to reinvent the wheel using only GitHub tooling.

I looked into ways to do this, and it seemed like no one has made a way to do this properly only using Github. I found two methods to do this. One blog post did this by using a Personal Action Token to automatically create a branch, clone the repo, and deploy to GitHub Pages so that you could see the previewed build and changes by invoking the command on a PR or on a commit. The other way just added the commit hash and deployed it to GitHub Pages at that subfolder. I did not like that the first approach sort of abuses GitHub APIs and is quite a hacky solution. The second violates the idea that staging should be completely independent from prod, which I did not like.

The main issue I ran into is that GitHub does not (currently) allow for multiple Pages environments of same repo. The solution I decided to go with was to let the GitHub build the code and then deploy it to a subfolder or subdomain. I really like this since you can easily modify the action to rsync the files over to your own server. This lets you take both use the convenience of Actions and own the hosting server. And since you own the server, you can keep these sites private and keep them for as long as you like. Naturally, this only works for static sites such as the project I was working on. For versioned backends you would definitely want a hosting service such as Netlify to manage all the networking and artifacts.

My approach is a little bit different than this since I can't directly control GitHub, so I use a second skeleton repo and a github submodule to link to original code without duplicating files and wasting GitHub resources.

**Try it yourself:** [PR trigger](https://github.com/cse110-fa22-group23/cse110-fa22-group23/blob/main/.github/workflows/staging.yml) and [build and deploy action](https://github.com/cse110-fa22-group23/staging/blob/main/.github/workflows/static.yml)
![example action usage](/images/example-action-run.png)

**Overview:** You trigger the action by commenting `.deploy` on any PR, which kicks off the runner that will build and deploy to staging, commenting on its progress as it goes.

Let's go through and see how the code works

```ruby
name: Manual branch staging site deploy

on:
  issue_comment:
    types: [created]

# Permissions needed for reacting and adding comments for IssueOps commands
permissions:
  pull-requests: write
  deployments: write
  contents: write # you might only need 'read' here
```

First, I specify that this action should run when a comment is added and add the necessary permissions to the action runner. Next, I will need to filter the trigger to only process comments on a PR.

{% raw  %}

```ruby
jobs:
  deploy:
    name: deploy
    runs-on: ubuntu-latest
    if: ${{ github.event.issue.pull_request }} # only run on pull request comments

    steps:

        # The branch-deploy Action
      - name: branch-deploy
        id: branch-deploy
        uses: github/branch-deploy@v3.0.3
        with: # bypass branch approval protection in order to deploy
          admins: cse110-fa22-group23/staging-deploy-permission
```
The `job:` information defines the environment of the action and tells it when to run.

I used GitHub's branch-deploy action. This is a great action that takes care of a bunch of edge cases and also enforces repo protections. By default, you can only deploy after all automated checks and code review requirements pass, which prevents random people from opening PRs and triggering the action from trying to run malicious code. We bypass this for trusted contributors with the permission group.

```ruby
        # clone staging repository
      - name: checkout staging
        continue-on-error: true # git may return error code if nothing to push
                                # (prev deployment from this PR)
        # If the branch-deploy Action was triggered, run the deployment (i.e. '.deploy')
        if: ${{ steps.branch-deploy.outputs.continue == 'true' && steps.branch-deploy.outputs.noop != 'true' }}
        uses: actions/checkout@v2.5.0
        with:
          repository: cse110-fa22-group23/staging
          path: 'staging'
          token: ${{ secrets.ACTION_PAT }}
```

Checkout repo and set git auth.

```ruby
        # push change, triggering staging github pages action rerun
      - name: trigger staging redeploy
        if: ${{ steps.branch-deploy.outputs.continue == 'true' && steps.branch-deploy.outputs.noop != 'true' }}
        run: |
          git config --global user.name github-actions
          git config --global user.email github-actions@github.com
          cd staging
          echo ${CURR_BRANCH}
          git config -f .gitmodules submodule.cse110-fa22-group23.branch ${CURR_BRANCH}
          git submodule update --remote
          echo $GITHUB_SHA > force_pages_deploy.txt
          git diff
          git add .
          git commit -m $GITHUB_SHA
          git status
          git push
          echo "DEPLOY_MESSAGE=Deployed to staging!\nhttps://cse110-fa22-group23.github.io/staging/" >> $GITHUB_ENV
        env:
          CURR_BRANCH: ${{ steps.branch-deploy.outputs.ref }}
```

Trigger the update on the staging Pages environment. Fail if same code is already deployed.

## On the staging side

```ruby
# Simple workflow for deploying static content to GitHub Pages
name: Deploy static content to Pages

on:
  # Runs on pushes targeting the default branch
  push:
    branches: ["main"]

  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

# Sets permissions of the GITHUB_TOKEN to allow deployment to GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Allow one concurrent deployment
concurrency:
  group: "pages"
  cancel-in-progress: true
```

Setup for permissions and config.

```ruby
jobs:
  # Single deploy job since we're just deploying
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
        with:
          # submodules: 'true' # this does not work bc git does a shallow copy and you can't switch branches
          path: 'staging'
          token: ${{ secrets.ACTION_PAT }}
```

Get the code

```ruby
      - name: Update and commit new submodule reference
        continue-on-error: true
        run: |
          cd staging
          git config --global user.name github-actions
          git config --global user.email github-actions@github.com
          git submodule update --init --recursive
          git submodule status
          git submodule sync
          git submodule update --remote
          git submodule status
          git diff
          git add .
          git commit -m $GITHUB_SHA
          git status
          git push
```

Update the submodule and get the new code. You would have to add a step here to build the code if your files are not already static.

```ruby
      - name: Setup Pages
        uses: actions/configure-pages@v2
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v1
        with:
          # Upload site folder static files from submodule
          path: './staging/cse110-fa22-group23/source/'
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v1
```

{% endraw %}

Upload the static folder to Pages and publish it.

Funnily enough, the GitHub engineer who wrote the branch-deploy action actually made an [issue](https://github.com/cse110-fa22-group23/cse110-fa22-group23/issues/149) to reach out on our repo. That was quite exciting to see.

### Future work

One problem was I only made a commit to change the action and did not change the reference of the submodule. So when it gets copied by the default github pages deploy action, it is only a shallow copy of that one ref and you can't checkout another commit or branch. I made it clone the entire repo which is a suboptimal approach. In the future, I would instead just checkout the hash that I put in the file or in the future I would just deploy it my own static hosting server. Also the admin permissions to bypass commit checks did not work and I did not get around to debugging that.

## Closing thoughts

This was a fun, brief foray into CI. It proved quite helpful as we were having some problems checking PWA and service worker stuff without deploying first. I wouldn't really recommend anyone use this since commercial deployment tools work a lot better and GitHub is going to add this as a first party [feature](https://github.com/actions/deploy-pages/blob/368bf1aa22b9265440e251b9216520e3f91c2d5b/action.yml#L37) soon anyway. I can also recommend Cloudflare Pages, which works really well. I really liked working with GitHub Actions and in combination with the pre-commit hook I wrote, it made development a lot faster to run the same checks locally as the things being verified by our other action checks. The only problem I had was that it was a bit frustrating to work with the GitHub's runner since I had to keep committing directly to main and then making empty commits to retrigger PR checks. In the future, I would try to spend more time looking at action examples. Or maybe I would just have ChatGPT write it for me 🤖💭[^1],[^2]

It enjoyed trying out git submodules and seeing the shallow clone optimizations GitHub uses for their actions.

### Some meta-thoughts

Although I have been doing a lot of work and making a lot of very cool things in the past two years, I have been having a hard time pushing some projects and especially blog posts to completion. I am hoping releasing this will lead to a deluge of posts from me. I have many posts stuck in the editing stage that I have not gotten around to cleaning up and feeling good enough to release. This post is quite rough, but I think it has some value in releasing for me and others.

## References

Some interesting related links I found in the process of making this. Surprisingly, I couldn't find anything that accomplishes what this action does the way that I do it. Similar actions also made to use GitHub Pages don't work as cleanly as the way I have done it.

<https://www.netlify.com/github-pages-vs-netlify/>

<https://poetryincode.dev/multi-environment-flutter-deployments-using-github-pages>

<https://medium.com/geekculture/when-youre-working-on-a-static-site-and-github-pages-feels-like-the-perfect-hosting-solution-a41c37f4e326>

<https://github.com/octobay/app-dev>

<https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token>

[^1]: ChatGPT makes a good attempt to replicate my work. Thoughts on this for another time. At least I know I can't be replaced yet... ![ChatGPT tries to replicate my work](/images/chatgpt-github-action.jpg)

[^2]: Let's see what stable diffusion has to say about this. ![person sleeping while the computer codes itself](/images/stablediffusion-doing-all-the-work.png) <br> Indeed me irl
