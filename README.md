A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

I think I've got things running smoothly and fixed some major bugs, but feel free to file issues or make pull requests if you want to improve the generic template / theme.

### Note: if you are using this repo and now get a notification about a security vulnerability, delete the Gemfile.lock file. 

# Instructions

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

## To run locally (not on GitHub Pages, to serve on your own computer)

For windows:

 1. Install Ruby from here: https://rubyinstaller.org/

 2. Once this is done, open the command prompt and go to the directory where your project is.

 3. Now, go to Gemfile and add `gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw]` before plugins (around line 20).

 4. change the GemFile as follow:

   ```BASH
   # comment the line:
   #gem "github-pages", group: :jekyll_plugins
   # uncomment following lines:
   gem "jekyll"
   gem "jekyll-paginate"
   gem "jekyll-gist"
   gem "jekyll-redirect-from"
   gem "kramdown-parser-gfm"
   gem "webrick"
   ```

 5. (Skip this step during the first iteration.) Delete Gemfile.lock

 6. `bundle install`

 7. `gem uninstall eventmachine --force`

 8. `gem install eventmachine --platform ruby`

 9. `bundle exec jekyll liveserve --port 4001` **<u>（Local run）</u>**

 10. If this doesn't work, try step 4) and repeat.
   It should work like a charm. Drop a question in case this doesn't work.

For Linux:

1. Clone the repository and made updates as detailed above

2. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
3. Run `bundle clean` to clean up the directory (no need to run `--force`)
4. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
5. Run `bundle exec jekyll liveserve` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.

# Upload to GitHub

```bash
git pushgit add.
git commit -m 'msgs'
git push
```



# Notes

navigation list in `_data/navigation.yml`

Update the edited time in `\_includes/footer.html`
