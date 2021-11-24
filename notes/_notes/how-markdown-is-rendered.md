---
title: Test page to see how the raw markdown is rendered
tags: markdown 
season: summer
---

This is intended as a quick reference and showcase. 

**Table of Contents**
- [[Headers::#heading]]
- [[Emphasis::#emphasis]]
- [[Lists::#lists]]
- [[Links::#links]]
- [[Images::#images]]
- [[Code and Syntax Highlighting::#syntax]]
- [[Math Expressions::#math]]
- [[Tables::#tables]]
- [[Blockquotes::#blockquotes]]
- [[Inline HTML::#inline]]
- [[Horizontal Rule::#hr]]
- [[Line Breaks::#br]]

{:#heading}
### Headings 
---

{:.regular-sans}
```
# H1 
## H2 
### H3 
#### H4 
##### H5 
###### H6
```

# H1
## H2
### H3
#### H4
##### H5
###### H6

{:#emphasis}
###  Emphasis 
---

{:.regular-sans}
```
Emphasis, aka italics, with *asterisks* or _underscores_. 

Strong emphasis, aka bold, with **asterisks** or __underscores__. 

Combined emphasis with **asterisks and _underscores_**.

Strikethrough uses two tildes. ~~Scratch this.~~ 
```

Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Combined emphasis with **asterisks and _underscores_**.

Strikethrough uses two tildes. ~~Scratch this.~~

{:#lists}
### Lists

{:.regular-sans}
```
1. First ordered list item 
...1. Ordered sublist 
2. Another item 
...* Unordered sublist 
3. Actual numbers don't matter, just that it's a number 
4. And another item. 

⋅⋅⋅You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown). 

⋅⋅⋅To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅ 
⋅⋅⋅Note that this line is separate, but within the same paragraph.⋅⋅ 
⋅⋅⋅(This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.) 

* Unordered list can use asterisks 
- Or minuses
+ Or pluses
```

1. First ordered list item 
   1. Ordered sublist 
2. Another item 
   - Unordered sublist
3. Actual numbers don't matter, just that it's a number 
4. And another item. 

    You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

    To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
    Note that this line is separate, but within the same paragraph.⋅⋅
    (This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

* Unordered list can use asterisks 
- Or minuses
+ Or pluses

{:#links}
### Links
---

{:.regular-sans}
```
[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com
```

[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links. 
http://www.example.com or <http://www.example.com> and sometimes 
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com

{:#images}
### Images
---

{:.regular-sans}
```
Here's our logo (hover to see the title text):

Inline-style: 
![alt text](/assets/img/profile.png "Logo Title Text 1")

Reference-style: 
![alt text][logo]

[logo]: /assets/img/profile.png "Logo Title Text 2"
```

Here's our logo (hover to see the title text):

Inline-style: 

```
![alt text](/assets/img/profile.png "Logo Title Text 1")
```

![alt text](/assets/img/profile.png "Logo Title Text 1")

Reference-style: 

```
![alt text][logo]
 
 [logo]: /assets/img/profile.png "Logo Title Text 2"
```

![alt text][logo]

[logo]: /assets/img/profile.png "Logo Title Text 2"

You can center the picture by adding `#center` at the end of the image path :

```
![alt text](/assets/img/profile.png#center "Logo Title Text 1")
```

![alt text](/assets/img/profile.png#center "Logo Title Text 1")

{:#syntax}
### Code and Syntax Highlighting
---

Code blocks are part of the Markdown spec, but syntax highlighting isn't. However, many renderers -- like Github's and Markdown Here -- support syntax highlighting. Which languages are supported and how those language names should be written will vary from renderer to renderer. Markdown Here supports highlighting for dozens of languages (and not-really-languages, like diffs and HTTP headers); 

{:.regular-sans}
```
Inline `code` has `back-ticks around` it.
```

Inline `code` has `back-ticks around` it.

Blocks of code are either fenced by lines with three back-ticks ```, or are indented with four spaces. I recommend only using the fenced code blocks -- they're easier and only they support syntax highlighting.

<pre class="regular-sans"> 
<code>
```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
 
```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```
</code>
</pre>

```javascript
var s = "JavaScript syntax highlighting";
alert(s);
```
 
```python
s = "Python syntax highlighting"
print s
```
 
```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```

{:#math}
### Math expressions
---

You can write math expressions using the Latex [markup language](https://en.wikipedia.org/wiki/LaTeX) between dollar signs. 

They can be written inline (single-dollar signs `$...$`) or as a whole block (double dollar signs with a line above and under `$$...$$`).

For example,
```
Bayes Theorem is $P(A \vert B) = \frac{P(B \vert A)\cdot P(A)}{P(B)}$
```
will render as :

Bayes Theorem is : $P(A \vert B) = \frac{P(B \vert A)\cdot P(A)}{P(B)}$

Whereas

```
Bayes Theorem is :

$$P(A \vert B) = \frac{P(B \vert A)\cdot P(A)}{P(B)}$$

````

will render as :

Bayes Theorem is :

$$P(A \vert B) = \frac{P(B \vert A)\cdot P(A)}{P(B)}$$


Please note that for a math block to be displayed correctly, it needs to be separated by an empty line, above and below. Besides, the pipe character \| may conflict with Markdown : it is recommended to use \vert instead.

{:#tables}
### Tables
---

Tables aren't part of the core Markdown spec, but they are part of GFM and Markdown Here supports them. They are an easy way of adding tables to your email -- a task that would otherwise require copy-pasting from another application.

{:.regular-sans}
```
Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3
```

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the 
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

{:#blockquotes}
### Blockquotes
---

{:.regular-sans}
```
> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote.
```

> Blockquotes are very handy in email to emulate reply text.
> This line is part of the same quote.

Quote break.

> This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote.

{:#inline}
Inline HTML
---

You can also use raw HTML in your Markdown, and it'll mostly work pretty well.

{:.regular-sans}
```
<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>
```

You can also use raw HTML in your Markdown, and it'll mostly work pretty well.

<dl>
  <dt>Definition list</dt>
  <dd>Is something people use sometimes.</dd>

  <dt>Markdown in HTML</dt>
  <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
</dl>

{:#hr}
### Horizontal Rule
---


{:.regular-sans}
```
Three or more...

---

Hyphens

***

Asterisks

___

Underscores
```

Three or more...

---

Hyphens

***

Asterisks

___

Underscores

{:#br}
### Line Breaks
---

My basic recommendation for learning how line breaks work is to experiment and discover -- hit <Enter> once (i.e., insert one newline), then hit it twice (i.e., insert two newlines), see what happens. You'll soon learn to get what you want. "Markdown Toggle" is your friend.

Here are some things to try out:

{:.regular-sans}
```
Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also a separate paragraph, but...
This line is only separated by a single newline, so it's a separate line in the *same paragraph*.
```

Here's a line for us to start with.

This line is separated from the one above by two newlines, so it will be a *separate paragraph*.

This line is also a separate paragraph, but...
This line is only separated by a single newline, so it's a separate line in the *same paragraph*.


License: CC-BY