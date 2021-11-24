---
title: How to use notenote.link features on your website
season: summer
tags: Theme
toc: true
comments: true
---

## The default features

All the default jekyll markdown features are made available such that they don't cause any conflict with the custom features that we have implemented. 

Internal links (simple and with alt-text) and LateX delimiters in markdown are compatible with [[Obsidian::https://obsidian.md]]. I'd recommend using it as a CMS for managing your notes. See the page about [[Obsidian integration]] for more details.

To see how to the raw markdown gets generated, go to the [[Test page to see how the raw markdown is rendered]]

## The Custom features

### 1. Creating a wiki-style link

**<u>General Syntax</u>**

- **Internal links:** **[​[**​Some Link**]]**

- **Internal links with alternative text:** **[​[**​Some Link\\|Alt text**]]**

- **External links:** **[​[​**Some Text::https://address-to-the-website**]]**

Anything text inside a double square bracket is considered as an internal link. The text has to be a valid title, if you provide a random text inside double square brackets, it will showup highlighted in yellow telling you that there is no essay/article/file with the mentioned title.

Similarly, for external links all you have to do is add a double colon after the "Alt text" and enter the link to the website after the double colon as seen below.

**Examples**

Example of an internal link that points to a valid post or page, that is, a page with the title (not url) mentioned in the double brackets.

> **Raw Syntax:** **[​[**​Obsidian integration**]]**
>
> **Rendered Text:** [[Obsidian integration]]


Example of an internal link that do not point to a valid post or page, that is, a page with the title (not url) mentioned in the double brackets.

> **Raw Syntax:** **[​[**Title of a non-existent page**]]**
> 
> **Rendered Text:** [[Title of a non-existent page]]

### 2. Creating a sidenote or a marginnote

**<u>General Syntax</u>**

- **Sidenote:** **[​[**Some Text**::keyword-of-the-type-of-the-sidenote]]**

- **Marginnote:** **[​[​**Some Text**::keyword-of-the-type-of-the-marginnote]]**

> |Type of the sidenote/marginnote|keyword|
  |:--|:--|
  |Left Sidenote| `lsn` |
  |Right Sidenote | `rsn` |
  |Left Marginnote| `lmn` |
  |Right Marginnote | `rmn` |


So, all you have to do is type in the keywords of the corresponding type of sidenote or marginnote after the double colon in the above syntax

**Examples**

Example of a sidenote to the right side of the page: 

> **Raw Syntax:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum tortor in pharetra vehicula. Fusce gravida lacus ac sem luctus congue at id justo. Ut sed tempus ante. **[​[**Phasellus mollis lectus id efficitur mollis.**::rsn]]** Suspendisse sit amet diam nec justo rhoncus tristique. Ut blandit faucibus nisi vitae rutrum. Vivamus fermentum efficitur justo non facilisis.
>
> **Rendered Text:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum tortor in pharetra vehicula. Fusce gravida lacus ac sem luctus congue at id justo. Ut sed tempus ante. [[Phasellus mollis lectus id efficitur mollis.::rsn]] Suspendisse sit amet diam nec justo rhoncus tristique. Ut blandit faucibus nisi vitae rutrum. Vivamus fermentum efficitur justo non facilisis.

Same goes with `lsn`, `rmn`, `lmn`

### 3. Highlighting a piece of text

**<u>General Syntax</u>**

- **[​[**​Some Link**::highlight]]**

There is only one color right now in which it highlights, a light bluish color, but you can easily extend it to support multiple colors by tinkering with it in `content.html` file in `_includes` directory.

**Examples**

> **Raw Syntax:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum tortor in pharetra vehicula. Fusce gravida lacus ac sem luctus congue at id justo. Ut sed tempus ante. **[​[**Phasellus mollis lectus id efficitur mollis.**::highlight]]** Suspendisse sit amet diam nec justo rhoncus tristique. Ut blandit faucibus nisi vitae rutrum. Vivamus fermentum efficitur justo non facilisis.
>
> **Rendered Text:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum tortor in pharetra vehicula. Fusce gravida lacus ac sem luctus congue at id justo. Ut sed tempus ante. [[Phasellus mollis lectus id efficitur mollis.::highlight]] Suspendisse sit amet diam nec justo rhoncus tristique. Ut blandit faucibus nisi vitae rutrum. Vivamus fermentum efficitur justo non facilisis.

### 4. Partial Transclusion

Transclusion is just a natural extension of sidenote and marginnote feature.

**<u>General Syntax</u>**

- **Sidenote-transclusion:** **[​[**Some Text**::keyword-of-the-type-of-the-sidenote-transclusion]]**

- **Marginnote-transclusion:** **[​[​**Some Text**::keyword-of-the-type-of-the-marginnote-transclusion]]**

> |Type of the sidenote/marginnote transclusion|keyword|
  |:--|:--|
  |Left Sidenote Transclusion | `lsn-transclude` |
  |Right Sidenote Transclusion | `rsn-transclude` |
  |Left Marginnote Transclusion | `lmn-transclude` |
  |Right Marginnote Transclusion | `rmn-transclude` |


So, all you have to do is type in the keywords of the corresponding type of sidenote or marginnote after the double colon in the above syntax

**Examples**

Example of a transclusion to the right side of the page: 

> **Raw Syntax:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum tortor in pharetra vehicula. Fusce gravida lacus ac sem luctus congue at id justo. Ut sed tempus ante. **[​[**Obsidian integration**::rmn-transclude]]** Suspendisse sit amet diam nec justo rhoncus tristique. Ut blandit faucibus nisi vitae rutrum. Vivamus fermentum efficitur justo non facilisis.
>
> **Rendered Text:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum tortor in pharetra vehicula. Fusce gravida lacus ac sem luctus congue at id justo. Ut sed tempus ante. [[Obsidian integration::rmn-transclude]] Suspendisse sit amet diam nec justo rhoncus tristique. Ut blandit faucibus nisi vitae rutrum. Vivamus fermentum efficitur justo non facilisis.

Same goes with `rsn`, `lsn`, `lmn`

### 5. Wrapping a text inside a box

**<u>General Syntax</u>**

- **[​[**Some Text**::wrap]]**

**Examples**

> **Raw Syntax:** **[​[**Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum tortor in pharetra vehicula. Fusce gravida lacus ac sem luctus congue at id justo. Ut sed tempus ante. Suspendisse sit amet diam nec justo rhoncus tristique. Ut blandit faucibus nisi vitae rutrum. Vivamus fermentum efficitur justo non facilisis**::wrap]]**.
>
> **Rendered Text:** [[Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec rutrum tortor in pharetra vehicula. Fusce gravida lacus ac sem luctus congue at id justo. Ut sed tempus ante. Suspendisse sit amet diam nec justo rhoncus tristique. Ut blandit faucibus nisi vitae rutrum. Vivamus fermentum efficitur justo non facilisis.::wrap]]

### 6. Flashcard

**<u>General Syntax</u>**

- **[​[**Some Text**::srs]]**

**Examples**

> **Raw Syntax:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. **[​[**Donec rutrum tortor in pharetra vehicula**::srs]]**. Fusce gravida lacus ac sem luctus congue at id justo. Ut sed tempus ante. Suspendisse sit amet diam nec justo rhoncus tristique. Ut blandit faucibus nisi vitae rutrum. Vivamus fermentum efficitur justo non facilisis.
>
> **Rendered Text:** Lorem ipsum dolor sit amet, consectetur adipiscing elit. [[Donec rutrum tortor in pharetra vehicula::srs]]. Fusce gravida lacus ac sem luctus congue at id justo. Ut sed tempus ante. Suspendisse sit amet diam nec justo rhoncus tristique. Ut blandit faucibus nisi vitae rutrum. Vivamus fermentum efficitur justo non facilisis.

### 7. Specific classes for changing font-type, font-size, and font-weight

There are classes like very-small, medium-small, small, small-medium, medium, medium-large, large, very-large; that can be used to change the size of your text directly from markdown like this:

> **Raw Syntax:**
> {:.regular-sans}
> ```
> {:.large}
> Some text here that needs to be enlarged
> ```
>
> **Rendered Text:**
> 
> {:.large}
> Some text here that needs to be enlarged


Similarly there are classes like regular-sans, serif, bold, italic, oblique, bolder, etc for formatting the text.

> **Raw Syntax:**
> 
> ```
> {:.medium .serif .oblique}
> Some text here that needs to be enlarged
> ```
>
> **Rendered Text:**
> 
> {:.medium .serif .oblique}
> Some text here that needs to be enlarged

Other common classes are .boxit that is used to wrap the text, .disable-user-select to disallow users from being able to select a particular piece of text by selecting it, etc. There are more classes like these which you can see in the file `style.css`. Once you figure out which class to use, all you have to do is just add the class before the text you want inside a curl brace like this ​{:\<classnames-with-dot-prepended-to-them>​}

### 8. Table of Content

notenote.link supports automatic table of content (toc) generation. Just add a `toc: true` line in the front matter at the beginning of your post.

You can modify the maximum header level included in the toc by changing number in the following option in `config.yml` :
```
toc:
  max_level: 3
```

### 9. Note maturity
Since this jekyll theme aims at mirroring your Obsidian notebook, the note content may note be mature or complete yet.

Therefore, we use front matter to classify the notes in the following categories (in order of appearance in the front page feed) : 

- `season: summer` : the note is near-complete (more than 80% done)
- `season: spring` : the note is in progress and has already good content
- `season: winter` : the note has just started, a summary is present however.
- `season: automn` : the note needs refactoring or some rewriting. It won't appear in the front-page feed.

Why use seasons ? Since this theme is a form of 'digital garden', I thought it would make sense to keep the analogy.

### 10. Other implicit features.

Features like backlinks, context menu, related posts, page preview are available by default as they are implemented using CSS and JS. So, you don't have to do anything other than write as you would normally to make use of those features.