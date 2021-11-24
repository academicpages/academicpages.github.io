---
title: Obsidian integration
season: summer
tags: CMS
---

The main purpose of this fork, other than cosmetic changes, is to create a web representation of an [[Obsidian::https://obsidian.md]] vault, using the [[Simply-Jekyll::https://github.com/raghuveerdotnet/simply-jekyll]] template.

## Usage

Things to know :

- Markdown is fully-compatible (including Latex delimiters !)

- There are now only notes (no blog posts). If you really want blog posts along notes, a hack is to set the YAML season of blog posts to `summer` and notes to `automn` - they won't appear in feed but will be searchable and appear in tags page.

- Code is now correctly indented

- You can change the code template by replacing the css in `/assets/css/highlight.css` by any template from [[pygment.css::https://github.com/richleland/pygments-css]]

- Wikilinks are usable : **[​[**​...**]]**,

- Also alt-text wikilinks (with transclusion !) : **[​[**​original link\\|alternative text**]]**

Please note : You need to escape the pipe character in Obsidian (\\| instead of \|). This won't break Obsidian's functionality.

- **Fresh new feature** : you can also link headers ! Use # when typing the wikilink : **[​[**Obsidian integration#Obsidian setup\|Alt-text**]]** will create the following link : [[Obsidian integration#Obsidian setup\|Alt-text]] (click on it to see the effect)

Please note : This feature will work only if you write alternative text in the link : [[Obsidian integration#Obsidian setup]] won't work[^1]. 

[^1]: I don't use it, so I didn't change it but if it's important for you open an issue and I may fix it.

- You can use [[Simply-Jekyll custom features::https://simply-jekyll.netlify.app/posts/exploring-the-features-of-simply-jekyll]], such as flashcards : [[flashcards !::srs]] - but don't click on it in Obsidian, else it will create a new page.

## Obsidian setup

### Installation
After having forked [[notenote.link::https://github.com/Maxence-L/notenote.link]] on your computer, open Obsidian and create a vault in the root folder (`/notenote.link`).

This will allow you to modify all your markdown files inside the directory. 

`about.md` is in the root folder.

Your notes should go to the `_notes` folder, images in `assets/img`. You need to tell Obsidian where to put the new notes. In Preferences/File, enter the following settings :

![](/assets/img/new%20notes%20pref.png#center)

- Default location for new notes : In the folder specified below`
- Folder to create new notes in : `_notes`
- New link format : `Relative Path to file`
- Attachment folder path : `assets/img

### Frontmatter

Front matter is needed at the beginning of your note. Here is the template :

```YAML
---
title: My Note
tags: tag1
toc: true
season: winter
---
```

You can hide it in Obsidian by toggling the option "Show Frontmatter" in the Preferences/Editor menu.

### Images

Images are the tricky part : 

- You can use vanilla markdown links: `![](/asset/img/img.png)`
- You can drag/drop/paste images in Obsidian, which will create a link such as : `[​[​../assets/img/Pasted image.png]]`

A quick hack in the last case is just to change the brackets : `![](../assets/img/Pasted image.png)`


