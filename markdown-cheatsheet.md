# Markdown cheatsheet

_(Also see [remarkable][], the markdown parser created by the author of this cheatsheet)_ 

## Table of contents

- [Standard features](#standard-features)
  * [Headings](#headings)
  * [Paragraphs](#paragraphs)
  * [Breaks](#breaks)
  * [Horizontal Rule](#horizontal-rule)
  * [Emphasis](#emphasis)
    + [Bold](#bold)
    + [Italics](#italics)
  * [Blockquotes](#blockquotes)
  * [Lists](#lists)
    + [Unordered](#unordered)
    + [Ordered](#ordered)
    + [Time-saving Tip](#time-saving-tip)
  * [Code](#code)
    + [Inline code](#inline-code)
    + ["Fenced" code block](#fenced-code-block)
    + [Indented code](#indented-code)
    + [Syntax highlighting](#syntax-highlighting)
  * [Links](#links)
    + [Autolinks](#autolinks)
    + [Inline links](#inline-links)
    + [Link titles](#link-titles)
    + [Named Anchors](#named-anchors)
  * [Images](#images)
  * [Raw HTML](#raw-html)
  * [Escaping with backslashes](#escaping-with-backslashes)
- [Non-standard features](#non-standard-features)
  * [Strikethrough](#strikethrough)
  * [Todo List](#todo-list)
  * [Tables](#tables)
    + [Aligning cells](#aligning-cells)
  * [Footnotes](#footnotes)
    + [Inline footnotes](#inline-footnotes)
  * [Additional Information](#additional-information)
    + [What is markdown?](#what-is-markdown)
    + [Other Resources](#other-resources)
    + [Contributing](#contributing)

<br>
<br>

# Standard features

The following markdown features are defined by the [CommonMark][] standard, and are generally supported by all markdown parsers and editors.

## Headings

Headings from `h1` through `h6` are constructed with a `#` for each level:

```
# h1 Heading
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading
```

Renders to:

# h1 Heading
## h2 Heading
### h3 Heading
#### h4 Heading
##### h5 Heading
###### h6 Heading

And this HTML:

```html
<h1>h1 Heading</h1>
<h2>h2 Heading</h2>
<h3>h3 Heading</h3>
<h4>h4 Heading</h4>
<h5>h5 Heading</h5>
<h6>h6 Heading</h6>
```

**A note about "Setext" Headings**

Note that this document only describes [ATX headings](https://spec.commonmark.org/0.28/#atx-headings), as it is the preferred syntax for writing headings. However, the CommonMark specification also describes [Setext headings](https://spec.commonmark.org/0.28/#setext-headings), a heading format that is denoted by a line of dashes or equal signes following the heading. It's recommended by the author of this guide that you use only ATX headings, as they are easier to write and read in text editors. 

<br>
<br>

## Paragraphs

Body copy written as normal plain-text will be wrapped with `<p></p>` tags in the rendered HTML.

So this:

```
Lorem ipsum dolor sit amet, graecis denique ei vel, at duo primis mandamus. Et legere ocurreret pri, animal tacimates complectitur ad cum. Cu eum inermis inimicus efficiendi. Labore officiis his ex, soluta officiis concludaturque ei qui, vide sensibus vim ad.
```

Renders to this HTML:

```html
<p>Lorem ipsum dolor sit amet, graecis denique ei vel, at duo primis mandamus. Et legere ocurreret pri, animal tacimates complectitur ad cum. Cu eum inermis inimicus efficiendi. Labore officiis his ex, soluta officiis concludaturque ei qui, vide sensibus vim ad.</p>
```

<br>
<br>

## Breaks

You can use multiple consecutive newline characters (`\n`) to create extra spacing between sections in a markdown document. However, if you need to ensure that extra newlines are not collapsed, you can use as many HTML `<br>` elements as you want.


## Horizontal Rule

The HTML `<hr>` element is for creating a "thematic break" between paragraph-level elements. In markdown, you can use of the following for this purpose:

* `___`: three consecutive underscores
* `---`: three consecutive dashes
* `***`: three consecutive asterisks

Renders to:

___

---

***

<br>
<br>

## Emphasis

### Bold

For emphasizing a snippet of text with a heavier font-weight.

The following snippet of text is **rendered as bold text**.

```
**rendered as bold text**
```
renders to:

**rendered as bold text**

and this HTML

```html
<strong>rendered as bold text</strong>
```

### Italics

For emphasizing a snippet of text with italics.

The following snippet of text is _rendered as italicized text_.

```
_rendered as italicized text_
```

renders to:

_rendered as italicized text_

and this HTML:

```html
<em>rendered as italicized text</em>
```

## Blockquotes

Used for defining a section of quoting text from another source, within your document.

To create a blockquote, use `>` before any text you want to quote.

```
> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante
```

Renders to:

> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.

And the generated HTML from a markdown parser might look something like this:

```html
<blockquote>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer posuere erat a ante.</p>
</blockquote>
```

Blockquotes can also be nested:

```
> Donec massa lacus, ultricies a ullamcorper in, fermentum sed augue.
Nunc augue augue, aliquam non hendrerit ac, commodo vel nisi.
>> Sed adipiscing elit vitae augue consectetur a gravida nunc vehicula. Donec auctor
odio non est accumsan facilisis. Aliquam id turpis in dolor tincidunt mollis ac eu diam.
>>> Donec massa lacus, ultricies a ullamcorper in, fermentum sed augue.
Nunc augue augue, aliquam non hendrerit ac, commodo vel nisi.
```

Renders to:

> Donec massa lacus, ultricies a ullamcorper in, fermentum sed augue.
Nunc augue augue, aliquam non hendrerit ac, commodo vel nisi.
>> Sed adipiscing elit vitae augue consectetur a gravida nunc vehicula. Donec auctor
odio non est accumsan facilisis. Aliquam id turpis in dolor tincidunt mollis ac eu diam.
>>> Donec massa lacus, ultricies a ullamcorper in, fermentum sed augue.
Nunc augue augue, aliquam non hendrerit ac, commodo vel nisi.

<br>
<br>

## Lists

### Unordered

A list of items in which the order of the items does not explicitly matter.

You may use any of the following symbols to denote bullets for each list item:

```
* valid bullet
- valid bullet
+ valid bullet
```

For example

```
+ Lorem ipsum dolor sit amet
+ Consectetur adipiscing elit
+ Integer molestie lorem at massa
+ Facilisis in pretium nisl aliquet
+ Nulla volutpat aliquam velit
  - Phasellus iaculis neque
  - Purus sodales ultricies
  - Vestibulum laoreet porttitor sem
  - Ac tristique libero volutpat at
+ Faucibus porta lacus fringilla vel
+ Aenean sit amet erat nunc
+ Eget porttitor lorem
```
Renders to:

+ Lorem ipsum dolor sit amet
+ Consectetur adipiscing elit
+ Integer molestie lorem at massa
+ Facilisis in pretium nisl aliquet
+ Nulla volutpat aliquam velit
  - Phasellus iaculis neque
  - Purus sodales ultricies
  - Vestibulum laoreet porttitor sem
  - Ac tristique libero volutpat at
+ Faucibus porta lacus fringilla vel
+ Aenean sit amet erat nunc
+ Eget porttitor lorem

And this HTML

```html
<ul>
  <li>Lorem ipsum dolor sit amet</li>
  <li>Consectetur adipiscing elit</li>
  <li>Integer molestie lorem at massa</li>
  <li>Facilisis in pretium nisl aliquet</li>
  <li>Nulla volutpat aliquam velit
    <ul>
      <li>Phasellus iaculis neque</li>
      <li>Purus sodales ultricies</li>
      <li>Vestibulum laoreet porttitor sem</li>
      <li>Ac tristique libero volutpat at</li>
    </ul>
  </li>
  <li>Faucibus porta lacus fringilla vel</li>
  <li>Aenean sit amet erat nunc</li>
  <li>Eget porttitor lorem</li>
</ul>
```

### Ordered

A list of items in which the order of items does explicitly matter.

```
1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. Facilisis in pretium nisl aliquet
5. Nulla volutpat aliquam velit
6. Faucibus porta lacus fringilla vel
7. Aenean sit amet erat nunc
8. Eget porttitor lorem
```
Renders to:

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. Facilisis in pretium nisl aliquet
5. Nulla volutpat aliquam velit
6. Faucibus porta lacus fringilla vel
7. Aenean sit amet erat nunc
8. Eget porttitor lorem

And this HTML:

```html
<ol>
  <li>Lorem ipsum dolor sit amet</li>
  <li>Consectetur adipiscing elit</li>
  <li>Integer molestie lorem at massa</li>
  <li>Facilisis in pretium nisl aliquet</li>
  <li>Nulla volutpat aliquam velit</li>
  <li>Faucibus porta lacus fringilla vel</li>
  <li>Aenean sit amet erat nunc</li>
  <li>Eget porttitor lorem</li>
</ol>
```

### Time-saving Tip

Sometimes lists change, and when they do it's a pain to re-order all of the numbers. Markdown solves this problem by allowing you to simply use `1.` before each item in the list.

For example:

```
1. Lorem ipsum dolor sit amet
1. Consectetur adipiscing elit
1. Integer molestie lorem at massa
1. Facilisis in pretium nisl aliquet
1. Nulla volutpat aliquam velit
1. Faucibus porta lacus fringilla vel
1. Aenean sit amet erat nunc
1. Eget porttitor lorem
```

Automatically re-numbers the items and renders to:

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. Facilisis in pretium nisl aliquet
5. Nulla volutpat aliquam velit
6. Faucibus porta lacus fringilla vel
7. Aenean sit amet erat nunc
8. Eget porttitor lorem

<br>
<br>

## Code

### Inline code

Wrap inline snippets of code with a single backtick: <code>`</code>.

For example, to show `<div></div>` inline with other text, just wrap it in backticks.

```html
For example, to show `<div></div>` inline with other text, just wrap it in backticks.
```

### "Fenced" code block

Three consecutive backticks, referred to as "code fences", are used to denote multiple lines of code: <code>```</code>.

For example, this:

<pre>
```html
Example text here...
```
</pre>

Appears like this when viewed in a browser:

```
Example text here...
```

And renders to something like this in HTML:

```html
<pre>
  <p>Example text here...</p>
</pre>
```

### Indented code

You may also indent several lines of code by at least four spaces, but this is not recommended as it is harder to read, harder to maintain, and doesn't support syntax highlighting.

Example:

```
    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code
```

    // Some comments
    line 1 of code
    line 2 of code
    line 3 of code


### Syntax highlighting

Various markdown parsers, such as [remarkable](https://github.com/jonschlinkert/remarkable), support syntax highlighting with fenced code blocks. To activate the correct styling for the language inside the code block, simply add the file extension of the language you want to use directly after the first code "fence": <code>```js</code>, and syntax highlighting will automatically be applied in the rendered HTML (if supported by the parser). For example, to apply syntax highlighting to JavaScript code:

<pre>
```js
grunt.initConfig({
  assemble: {
    options: {
      assets: 'docs/assets',
      data: 'src/data/*.{json,yml}',
      helpers: 'src/custom-helpers.js',
      partials: ['src/partials/**/*.{hbs,md}']
    },
    pages: {
      options: {
        layout: 'default.hbs'
      },
      files: {
        './': ['src/templates/pages/index.hbs']
      }
    }
  }
});
```
</pre>

Which renders to:

```js
grunt.initConfig({
  assemble: {
    options: {
      assets: 'docs/assets',
      data: 'src/data/*.{json,yml}',
      helpers: 'src/custom-helpers.js',
      partials: ['src/partials/**/*.{hbs,md}']
    },
    pages: {
      options: {
        layout: 'default.hbs'
      },
      files: {
        './': ['src/templates/pages/index.hbs']
      }
    }
  }
});
``

And this complicated HTML is an example of what might be generated by the markdown parser, when syntax highlighting is applied by a library like [highlight.js](https://highlightjs.org/):

```xml
<div class="highlight"><pre><span class="nx">grunt</span><span class="p">.</span><span class="nx">initConfig</span><span class="p">({</span>
  <span class="nx">assemble</span><span class="o">:</span> <span class="p">{</span>
    <span class="nx">options</span><span class="o">:</span> <span class="p">{</span>
      <span class="nx">assets</span><span class="o">:</span> <span class="s1">'docs/assets'</span><span class="p">,</span>
      <span class="nx">data</span><span class="o">:</span> <span class="s1">'src/data/*.{json,yml}'</span><span class="p">,</span>
      <span class="nx">helpers</span><span class="o">:</span> <span class="s1">'src/custom-helpers.js'</span><span class="p">,</span>
      <span class="nx">partials</span><span class="o">:</span> <span class="p">[</span><span class="s1">'src/partials/**/*.{hbs,md}'</span><span class="p">]</span>
    <span class="p">},</span>
    <span class="nx">pages</span><span class="o">:</span> <span class="p">{</span>
      <span class="nx">options</span><span class="o">:</span> <span class="p">{</span>
        <span class="nx">layout</span><span class="o">:</span> <span class="s1">'default.hbs'</span>
      <span class="p">},</span>
      <span class="nx">files</span><span class="o">:</span> <span class="p">{</span>
        <span class="s1">'./'</span><span class="o">:</span> <span class="p">[</span><span class="s1">'src/templates/pages/index.hbs'</span><span class="p">]</span>
      <span class="p">}</span>
    <span class="p">}</span>
  <span class="p">}</span>
<span class="p">});</span>
</pre></div>
```

<br>
<br>


## Links

### Autolinks

Autolinks are absolute URIs and email addresses inside `<` and `>`. They are parsed as links, where the URI or email address itself is used as the link's label.

```
<http://foo.bar.baz>
```

Renders to:

<http://foo.bar.baz>

URIs or email addresses that are not wrapped in angle brackets are not recognized as valid autolinks by markdown parsers.


### Inline links

```
[Assemble](http://assemble.io)
```

Renders to (hover over the link, there is no tooltip):

[Assemble](http://assemble.io)

HTML:

```html
<a href="http://assemble.io">Assemble</a>
```

### Link titles

```
[Upstage](https://github.com/upstage/ "Visit Upstage!")
```

Renders to (hover over the link, there should be a tooltip):

[Upstage](https://github.com/upstage/ "Visit Upstage!")

HTML:

```html
<a href="https://github.com/upstage/" title="Visit Upstage!">Upstage</a>
```

### Named Anchors

Named anchors enable you to jump to the specified anchor point on the same page. For example, each of these chapters:

```
# Table of Contents
  * [Chapter 1](#chapter-1)
  * [Chapter 2](#chapter-2)
  * [Chapter 3](#chapter-3)
```

will jump to these sections:

```
## Chapter 1 <a name="chapter-1"></a>
Content for chapter one.

## Chapter 2 <a name="chapter-2"></a>
Content for chapter one.

## Chapter 3 <a name="chapter-3"></a>
Content for chapter one.
```

**Anchor placement**

Note that placement of achors is arbitrary, you can put them anywhere you want, not just in headings. This makes adding cross-references easy when writing markdown.

<br>
<br>


## Images

Images have a similar syntax to links but include a preceding exclamation point.

```
![Minion](http://octodex.github.com/images/minion.png)
```

![Minion](http://octodex.github.com/images/minion.png)

or

```
![Alt text](http://octodex.github.com/images/stormtroopocat.jpg "The Stormtroopocat")
```
![Alt text](http://octodex.github.com/images/stormtroopocat.jpg "The Stormtroopocat")

Like links, Images also have a footnote style syntax

```
![Alt text][id]
```
![Alt text][id]

With a reference later in the document defining the URL location:

[id]: http://octodex.github.com/images/dojocat.jpg  "The Dojocat"

```
[id]: http://octodex.github.com/images/dojocat.jpg  "The Dojocat"
```

## Raw HTML

Any text between `<` and `>` that looks like an HTML tag will be parsed as a raw HTML tag and rendered to HTML without escaping. 

_(Note that no attempt is made by the markdown parser to validate your HTML)._

Example:

```
**Visit <a href="https://github.com">Jon Schlinkert's GitHub Profile</a>.**
```

Renders to:

**Visit <a href="https://github.com">Jon Schlinkert's GitHub Profile</a>.**

## Escaping with backslashes

Any ASCII punctuation character may be escaped using a single backslash.

Example:

```
\*this is not italic*
```

Renders to:

\*this is not italic*


# Non-standard features

The following markdown features are not defined by the [CommonMark][] specification, but they are commonly supported by markdown parsers and editors, as well as sites like GitHub and GitLab.

## Strikethrough

In GFM you can do strickthroughs.

```
~~Strike through this text.~~
```
Which renders to:

~~Strike through this text.~~

<br>
<br>

### Todo List

```
- [ ] Lorem ipsum dolor sit amet
- [ ] Consectetur adipiscing elit
- [ ] Integer molestie lorem at massa
```

Renders to:

- [ ] Lorem ipsum dolor sit amet
- [ ] Consectetur adipiscing elit
- [ ] Integer molestie lorem at massa

**Links in todo lists**

```
- [ ] [foo](#bar)
- [ ] [baz](#qux)
- [ ] [fez](#faz)
```

Renders to:

- [ ] [foo](#bar)
- [ ] [baz](#qux)
- [ ] [fez](#faz)

<br>
<br>

## Tables

Tables are created by adding pipes as dividers between each cell, and by adding a line of dashes (also separated by bars) beneath the header _(this line of dashes is required)_. 

- pipes do not need to be vertically aligned.
- pipes on the left and right sides of the table are sometimes optional
- three or more dashes must be used for each cell in the separator row

Example:

```
| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |
```

Renders to:

| Option | Description |
| ------ | ----------- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

And this HTML:

```html
<table>
  <tr>
    <th>Option</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>data</td>
    <td>path to data files to supply the data that will be passed into templates.</td>
  </tr>
  <tr>
    <td>engine</td>
    <td>engine to be used for processing templates. Handlebars is the default.</td>
  </tr>
  <tr>
    <td>ext</td>
    <td>extension to be used for dest files.</td>
  </tr>
</table>
```

### Aligning cells

**Center text in a column**

To center the text in a column, add a colon to the middle of the dashes in the row beneath the header.

```
| Option | Description |
| -:- | -:- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |
```

| Option | Description |
| -:- | -:- |
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |


**Right-align the text in a column**

To right-align the text in a column, add a colon to the middle of the dashes in the row beneath the header.

```
| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |
```

Renders to:

| Option | Description |
| ------:| -----------:|
| data   | path to data files to supply the data that will be passed into templates. |
| engine | engine to be used for processing templates. Handlebars is the default. |
| ext    | extension to be used for dest files. |

<br>
<br>

## Footnotes

> Markdown footnotes are not officially defined by the [CommonMark][] specification. However, the feature is supported by [remarkable][] and other markdown parsers, and it's very useful when available. 

Markdown footnotes are denoted by an opening square bracket, followed by a caret, followed by a number and a closing square bracket: `[^1]`. 

```
This is some text[^1] with a footnote reference link.
```

The accompanying text for the footnote can be added elsewhere in the document using the following syntax: 

```
[^1]: "This is a footnote"
```

When rendered to HTML, footnotes are "stacked" by the markdown parser at the bottom of the file, in the order in which the footnotes were defined.

### Inline footnotes

Some [markdown parsers][remarkable] also support inline footnotes. Inline footnotes are written using the following syntax: `[^2 "This is an inline footnote"]`.

<br>
<br>

## Additional Information

### What is markdown?

> Markdown is "a plain text format for writing structured documents, based on formatting conventions from email and usenet" -- [CommonMark][]

Sites like GitHub and Stackoverflow have popularized the use markdown as a plain-text alternative to traditional text editors, for writing things like documentation and comments. 

### Other Resources

- [We've been trained to make paper](https://ben.balter.com/2012/10/19/we-ve-been-trained-to-make-paper/) - A great blog post about why markdown frees us from the shackles of proprietary formats imposed by bloated word processors, such as Microsoft Word.
- [CommonMark](https://commonmark.org/) - "A strongly defined, highly compatible specification of Markdown"

### Contributing

All contributions are welcome!

Please let me know if you find typos, grammar or spelling mistakes, or have a suggestion for improving the cheatsheet (since GitHub does not send notifications for gists, it might be better to contact me on twitter, at [@jonschlinkert](https://twitter.com/jonschlinkert)).

Thanks for reading!


[remarkable]: https://github.com/jonschlinkert/remarkable
[commonmark]: https://commonmark.org/
