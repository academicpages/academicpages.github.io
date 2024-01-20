# Frequently Asked Questions

Here are some frequently asked questions. If you have a different question, please check if it was not already answered in the Q&A section of the [GitHub Discussions](https://github.com/alshedivat/al-folio/discussions/categories/q-a). If not, feel free to ask a new question there.

- [After I create a new repository from this template and setup the repo, I get a deployment error. Isn't the website supposed to correctly deploy automatically?](#after-i-create-a-new-repository-from-this-template-and-setup-the-repo-i-get-a-deployment-error-isnt-the-website-supposed-to-correctly-deploy-automatically)
- [I am using a custom domain (e.g., `foo.com`). My custom domain becomes blank in the repository settings after each deployment. How do I fix that?](#i-am-using-a-custom-domain-eg-foocom-my-custom-domain-becomes-blank-in-the-repository-settings-after-each-deployment-how-do-i-fix-that)
- [My webpage works locally. But after deploying, it fails to build and throws `Unknown tag 'toc'`. How do I fix that?](#my-webpage-works-locally-but-after-deploying-it-fails-to-build-and-throws-unknown-tag-toc-how-do-i-fix-that)
- [My webpage works locally. But after deploying, it is not displayed correctly (CSS and JS is not loaded properly). How do I fix that?](#my-webpage-works-locally-but-after-deploying-it-is-not-displayed-correctly-css-and-js-is-not-loaded-properly-how-do-i-fix-that)
- [Atom feed doesn't work. Why?](#atom-feed-doesnt-work-why)
- [My site doesn't work when I enable `related_blog_posts`. Why?](#my-site-doesnt-work-when-i-enable-related_blog_posts-why)
- [When trying to deploy, it's asking for github login credentials, which github disabled password authentication and it exits with an error. How to fix?](#when-trying-to-deploy-its-asking-for-github-login-credentials-which-github-disabled-password-authentication-and-it-exits-with-an-error-how-to-fix)

---

#### After I create a new repository from this template and setup the repo, I get a deployment error. Isn't the website supposed to correctly deploy automatically?

Yes, if you are using release `v0.3.5` or later, the website will automatically and correctly re-deploy right after your first commit. Please make some changes (e.g., change your website info in `_config.yml`), commit, and push. Make sure to follow [deployment instructions](https://github.com/alshedivat/al-folio#deployment). (Relevant issue: [209](https://github.com/alshedivat/al-folio/issues/209#issuecomment-798849211).)

#### I am using a custom domain (e.g., `foo.com`). My custom domain becomes blank in the repository settings after each deployment. How do I fix that?

You need to add `CNAME` file to the `master` or `source` branch of your repository. The file should contain your custom domain name. (Relevant issue: [130](https://github.com/alshedivat/al-folio/issues/130).)

#### My webpage works locally. But after deploying, it fails to build and throws `Unknown tag 'toc'`. How do I fix that?

Make sure you followed through the [deployment instructions](#deployment) in the previous section. You should have set the deployment branch to `gh-pages`. (Related issue: [1438](https://github.com/alshedivat/al-folio/issues/1438).)

#### My webpage works locally. But after deploying, it is not displayed correctly (CSS and JS is not loaded properly). How do I fix that?

Make sure to correctly specify the `url` and `baseurl` paths in `_config.yml`. Set `url` to `https://<your-github-username>.github.io` or to `https://<your.custom.domain>` if you are using a custom domain. If you are deploying a personal or organization website, leave `baseurl` blank. If you are deploying a project page, set `baseurl: /<your-project-name>/`. If all previous steps were done correctly, all is missing is [for your browser to fetch again the site stylesheet](https://github.com/alshedivat/al-folio/issues/1398#issuecomment-1609518404).

#### Atom feed doesn't work. Why?

Make sure to correctly specify the `url` and `baseurl` paths in `_config.yml`. RSS Feed plugin works with these correctly set up fields: `title`, `url`, `description` and `author`. Make sure to fill them in an appropriate way and try again.

#### My site doesn't work when I enable `related_blog_posts`. Why?

This is probably due to the [classifier reborn](https://github.com/jekyll/classifier-reborn) plugin, which is used to calculate related posts. If the error states `Liquid Exception: Zero vectors can not be normalized...`, it means that it could not calculate related posts for a specific post. This is usually caused by [empty or minimal blog posts](https://github.com/jekyll/classifier-reborn/issues/64) without meaningful words (i.e. only [stop words](https://en.wikipedia.org/wiki/Stop_words)) or even [specific characters](https://github.com/jekyll/classifier-reborn/issues/194) you used in your posts. Also, the calculus for similar posts are made for every `post`, which means every page that uses `layout: post`, including the announcements. To change this behavior, simply add `related_posts: false` to the front matter of the page you don't want to display related posts on.

#### When trying to deploy, it's asking for github login credentials, which github disabled password authentication and it exits with an error. How to fix?

Open .git/config file using your preferred editor. Change the `https` portion of the `url` variable to `ssh`. Try deploying again.
