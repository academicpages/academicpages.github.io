---
title: Blogging with jupyter notebooks and jekyll
permalink: /posts/2018/03/ipython-notebooks-jekyll
date: 2018-03-07
tags:
    - coding
    - jekyll
---

One of the last parts before my full-fledged transition to github pages from wordpress was figuring out how to post nicely formatted jupyter notebooks.
This was actually the reason I wanted to switch in the first place, but it turns out it wasn't as straightforward as I'd hoped!
I think I've found an acceptable, though imperfect, way to do this: here's the general process I've settled on.

1. Write the jupyter notebook in the `_jupyter` folder   
1. When it's finished, `jupyter nbconvert <nb> --to markdown`   
1. Move it to the `_posts` folder   
1. Move the images to the `images` folder    
1. Add `/images/` to all image paths in the markdown file   

Some things I learned along the way:

## Keep notebooks in a separate folder

The majority of my blog posts are me just writing things and thus just normal markdown files.
At first, I was trying to troubleshoot my coding posts by putting the jupyter notebook in the `_posts` folder.
This ended up rendering the json under the notebook as the blog post, even if I converted the notebook to a markdown file.
As long as the `.ipynb` file was in there, that's what was being processed and displayed by jekyll.
One way to get around this is to include an exclusion for `*.ipynb` files in the `config.yml` file, as described in this helpful [blog post](https://adamj.eu/tech/2014/09/21/using-ipython-notebook-to-write-jekyll-blog-posts/).
However, I confess that I don't know all that's going on my `config.yml` file, and I didn't really want to troubleshoot to figure out where that should go.
Also, I think it will be nice to separate my coding posts from other, more text-based posts.

## Convert to markdown

Thankfully, this is very easy with jupyter's `nbconvert` tool.
A note that the markdown file name should have the same format as other blog posts, starting with `YYYY-MM-DD`.
Also, it seems that jekyll doesn't need the header with the post metadata in order for the post to show up, but you may want to add that to your post.

## Move the images

Here again, it's probably possible to configure jekyll to look for images in the `_jupyter` folder, where the `nbconvert` command will have created a folder with all associated images.
However, partially to avoid troubleshooting this and also partially to stay consistent with other images, I'm planning just to move the whole folder over to my `images` folder.

## Fix image paths

This was the part that took me a bit to figure out, which is probably just because I really don't know what's going on under the hood.
For the images to show up, you need to provide the full path to the image from the root directory of the repo.
In my case, that means adding `/images/` to each image path, since that's the folder that they're all in.

## Things I still need to fix

I don't love how the code blocks are showing up - the text is too small and I don't think the color highlighting is standard Python coloring.
Also, my cell blocks are missing the **In [5]** and **Out [5]** execution counters, which I'd like to have show up.
But for now, I think this is good enough.
Maybe one day I'll figure out where I can edit how these styles, perhaps starting from [this blog post...](https://linode.com/docs/applications/project-management/jupyter-notebook-on-jekyll/)
