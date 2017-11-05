---
permalink: /markdown/
title: "GitHub Pages And Markdown"
author_profile: true
redirect_from: 
  - /md/
  - /markdown.html
---

This website is hosted on **GitHub pages**. [GitHub pages](https://pages.github.com) is a free service in which websites are built and hosted from code and data stored in a GitHub repository, automatically updating when a new commit is made to the respository. Pages are created by [**Jekyll Now**](http://www.jekyllnow.com/), a more user-friendly version of [**Jekyll**](https://jekyllrb.com/) and perfect for building minimal and static, yet beautiful, secure, and stable websites. A really quick and easy-to-follow guide is provided [here](https://www.smashingmagazine.com/2014/08/build-blog-jekyll-github-pages/). For a quick start, you can also find the source code for setting up your own website at [barryclark/jekyll-now](https://github.com/barryclark/jekyll-now).  

I used the front page of a website that is powered by the [academicpages template](https://github.com/academicpages/academicpages.github.io). This template was forked from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/) created by Michael Rose, and then extended to support the kinds of content that academics have: publications, talks, teaching, a portfolio, blog posts, and a dynamically-generated CV. You can fork [this repository](https://github.com/academicpages/academicpages.github.io) right now, modify the configuration and markdown files, add your own PDFs and other content, and have your own site for free, with no ads! An older version of this template powers my own personal website at [stuartgeiger.com](http://stuartgeiger.com), which uses [this Github repository](https://github.com/staeiou/staeiou.github.io).


Make sure you check this [guide](http://jmcglone.com/guides/github-pages/) as well. Personally, I found it very useful and succinct. 


## Why Jekyll at all? 

You can do so much with Jekyll. Some of the best web developers use it for building their own websites. Here is a good examples:
[CSS Wizardy](https://csswizardry.com/about/).

But if you are, like me, an academic and want to publish your website with the help of Jekyll as fast as possible and not necessarily concerned about how fancy your website should look like, you may be interested in reading
[Github for academics](http://blogs.lse.ac.uk/impactofsocialsciences/2013/06/04/github-for-academics/).

Also, a really cool maths blog on discrete geometry, graph theory, and other stuff built by Jekyll: [11011110](https://11011110.github.io/blog/)

<!--- Write more here about the knowledge economy and more open ways of sharing knowledge
[Punctum](https://punctumbooks.com/blog/here-be-monsters-a-punctum-publishing-primer/) -->

### How to write maths with Jekyll? 

**MathJax** is an open source JavaScript display engine for mathematics that works in all browsers.

[Kramdown](https://kramdown.gettalong.org/) comes with optional support for LaTeX to PNG rendering via MathJax within math blocks. This [blogpost](http://gastonsanchez.com/visually-enforced/opinion/2014/02/16/Mathjax-with-jekyll/) has a good tutorial on how to use MathJax with Jekyll. Also, you will probably find the official [MathJax](http://docs.mathjax.org/en/latest/start.html) website useful.


### Tips and hints for using Markdown

* Name a file ".md" to have it render in markdown, name it ".html" to render in HTML.
* Go to the [commit list](https://github.com/academicpages/academicpages.github.io/commits/master) (on your repo) to find the last version Github built with Jekyll. 
  * Green check: successful build
  * Orange circle: building
  * Red X: error
  * No icon: not built

### Resources
 * [Liquid syntax guide](https://shopify.github.io/liquid/tags/control-flow/)

### Markdown guide

#### Header four

##### Header five

###### Header five



### Blockquotes

Single line blockquote:

> Quotes are cool.

### Tables

#### Table 1

| Entry            | Item   |                                                              |
| --------         | ------ | ------------------------------------------------------------ |
| [John Doe](#)    | 2016   | Description of the item in the list                          |
| [Jane Doe](#)    | 2019   | Description of the item in the list                          |
| [Doe Doe](#)     | 2022   | Description of the item in the list                          |

#### Table 2

| Header1 | Header2 | Header3 |
|:--------|:-------:|--------:|
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
|-----------------------------|
| cell1   | cell2   | cell3   |
| cell4   | cell5   | cell6   |
|=============================|
| Foot1   | Foot2   | Foot3   |

### Definition Lists

Definition List Title
:   Definition list division.

#dowork
:   Coined by Rob Dyrdek and his personal body guard Christopher "Big Black" Boykins, "Do Work" works as a self motivator, to motivating your friends.


### Unordered Lists (Nested)

  * List item one 
      * List item one 
          * List item one
          * List item two
          * List item three
          * List item four
      * List item two
      * List item three
      * List item four
  * List item two
  * List item three
  * List item four

### Ordered List (Nested)

  1. List item one 
      1. List item one 
          1. List item one
          2. List item two
          3. List item three
          4. List item four
      2. List item two
      3. List item three
      4. List item four
  2. List item two
  3. List item three
  4. List item four

### Buttons

Make any link standout more when applying the `.btn` class.

### Notices

**Watch out!** You can also add notices by appending `{: .notice}` to a paragraph.
{: .notice}

### HTML Tags

#### Address Tag

<address>
  1 Infinite Loop<br /> Cupertino, CA 95014<br /> United States
</address>

#### Anchor Tag (aka. Link)

This is an example of a [link](http://github.com "Github").

#### Abbreviation Tag

The abbreviation CSS stands for "Cascading Style Sheets".

*[CSS]: Cascading Style Sheets

#### Cite Tag

"Code is poetry." ---<cite>Automattic</cite>

#### Code Tag

You will learn later on in these tests that `word-wrap: break-word;` will be your best friend.

#### Strike Tag

This tag will let you <strike>strikeout text</strike>.

#### Emphasize Tag

The emphasize tag should _italicize_ text.

#### Insert Tag

This tag should denote <ins>inserted</ins> text.

#### Keyboard Tag

This scarcely known tag emulates <kbd>keyboard text</kbd>, which is usually styled like the `<code>` tag.

#### Preformatted Tag

This tag styles large blocks of code.

<pre>
.post-title {
  margin: 0 0 5px;
  font-weight: bold;
  font-size: 38px;
  line-height: 1.2;
  and here's a line of some really, really, really, really long text, just to see how the PRE tag handles it and to find out how it overflows;
}
</pre>

#### Quote Tag

<q>Developers, developers, developers&#8230;</q> &#8211;Steve Ballmer

#### Strong Tag

This tag shows **bold text**.

#### Subscript Tag

Getting our science styling on with H<sub>2</sub>O, which should push the "2" down.

#### Superscript Tag

Still sticking with science and Isaac Newton's E = MC<sup>2</sup>, which should lift the 2 up.

#### Variable Tag

This allows you to denote <var>variables</var>.
