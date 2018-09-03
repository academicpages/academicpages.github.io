# Notes for me

**Info about which pages to edit** is in `_pages/markdown.md`

**Change content of main landing page** in `_pages/about.md`.

**Change sidebar content** in `_config.yml`

**Change how sidebar shows up** in `_includes/author-profile.html`

**To run the site locally**, run `bundle exec jekyll serve`

**To change formats of things**, try to find the respective `.scss` file in the `_sass` folder.

Looks like the `archive-single.html` file in `_includes` is used in a lot of the html files.
For example, in `year-archive.html`, the line `{% include archive-single.html %}` basically does all of the heavy lifting and defines how things will look.
I changed the `archive-single.html` file to change how my blog posts were being shown.

**To change main navigation content**, edit `navigation.yml` in `_data`.

## Notes on blog posts

Individual blog posts are in the `_posts` folder.
The files need to be formatted as `yyyy-mm-dd` for them to be parsed by the code in `_pages/year-archive.md` and added to the main blog page.

The header info for each blog post needs the following:

- `title`: title of the blog post. No need for single quotes unless there's a special character (especially a colon) in the title.   
- `permalink`: link to the post. Note that if you also have something called `link`, then the `title` will link to whatever you put in `link` and the `Read more` will link to the `permalink`. Best to only have one link though...   

The main blog page will show the first paragraph of text, and then include a `Read more...` link.
Most of the blog post behavior is defined in `{% include archive-single.html %}` (`archive-single.html` is in the `_includes` folder).

## Notes on notebooks

1. Write the jupyter notebook in the `_jupyter` folder   
1. When it's finished, `jupyter nbconvert <nb> --to markdown`   
1. Move it to the `_posts` folder   
1. Move the images to the `images` folder    
1. Add `/images/` to all image paths in the markdown file   

You can also run the `convert_and_move.sh` function in the `_jupyter` folder.
Note that you still have to go in and manually add the `/images/` path,
and if there are any non-extension dots in the file name these should be changed
to hyphens. You also need to go and add the header to the post.

Still to figure out: how to change font size/format of cells, how to have **[In 1]** show up, how to add image captions.

## TODO

- fix images in blog posts, so they don't point to wordpress    
- fix the ipython notebook blog post (Scatter plotting in...)    
- see if I can figure out how to manually place the `Read more...` location in each blog post (i.e. change how excerpts get defined)   
- see if I can do an automatic population of publications (like in the original) but with nicer formatting    
    - I think this can be done with writing a new `_includes` html file with the formatting for the publications, similary to the `archive-single.html`
- remove unused pages (e.g. look at how messy the sitemap is!)
- put CV back in

## Done
- change the format of the year-archive.html page so that titles are larger, published date is smaller   
- migrate my wordpress posts to `_posts` (write script to do this...)      


# Notes from the original repo

A Github Pages template for academic websites. This was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License. See LICENSE.md.

I think I've got things running smoothly and fixed some major bugs, but feel free to file issues or make pull requests if you want to improve the generic template / theme.

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
1. Clone the repository and made updates as detailed above
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle clean` to clean up the directory (no need to run `--force`)
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `bundle exec jekyll serve` to generate the HTML and serve it from localhost:4000

# Changelog -- bugfixes and enhancements

There is one logistical issue with a ready-to-fork template theme like academic pages that makes it a little tricky to get bug fixes and updates to the core theme. If you fork this repository, customize it, then pull again, you'll probably get merge conflicts. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch.

To support this, all changes to the underlying code appear as a closed issue with the tag 'code change' -- get the list [here](https://github.com/academicpages/academicpages.github.io/issues?q=is%3Aclosed%20is%3Aissue%20label%3A%22code%20change%22%20). Each issue thread includes a comment linking to the single commit or a diff across multiple commits, so those with forked repositories can easily identify what they need to patch.
