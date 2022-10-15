---
layout: post
title:  "Edge Cases"
date:   2020-04-13 17:04:01
categories: post
---
Some edge cases and cautionary examples on using Markdown for writing content using this theme. In particular, list syntax can really knot things up.
<!--more-->

### Mathjax improperly parsing greater and less than and ampersands inside blocks

The mathjax HTML ```<head>``` scripts have been modified to properly render block style mathjax expressions inside a ```$$ ... $$``` set of character pairs,
using the standard Kramdown parser. Some examples sent to me by Quxiaofeng are now parsing correctly, I believe.

This code:

```latex
$$
  D = \left(\begin{matrix}
  1 & -1 & & & & \\
  &    & \cdots &   & \\
  &    &        & 1 & -1
 \end{matrix}
 \right)
$$
```
yields this:

$$
D = \left(\begin{matrix}
  1 & -1 & & & & \\
  &    & \cdots &   & \\
  &    &        & 1 & -1
\end{matrix}
\right)
$$

Other examples from the [wikia Tex reference](http://latex.wikia.com/wiki/Matrix_environments):

$$
\begin{matrix}
\alpha& \beta^{*}\\
\gamma^{*}& \delta
\end{matrix}
$$


$$
\begin{bmatrix}
\alpha& \beta^{*}\\
\gamma^{*}& \delta
\end{bmatrix}
$$

$$
\begin{Bmatrix}
\alpha& \beta^{*}\\
\gamma^{*}& \delta
\end{Bmatrix}
$$

$$
\begin{vmatrix}
\alpha& \beta^{*}\\
\gamma^{*}& \delta
\end{vmatrix}
$$

$$
\begin{Vmatrix}
\alpha& \beta^{*}\\
\gamma^{*}& \delta
\end{Vmatrix}
$$

$$
\begin{Vmatrix}
\alpha& \beta^{*}\\
\gamma^{*}& \delta
\end{Vmatrix}
$$

However, a problem still exists for inline matrix notation, from an example [here](https://en.wikibooks.org/wiki/LaTeX/Mathematics#Matrices_in_running_text):

A matrix in text must be set smaller: $$ \bigl(\begin{smallmatrix}a & b \\ c & d\end{smallmatrix} \bigr) $$ to not increase leading in a portion of text. The way this inline matrix is written is: ```$$ \bigl(\begin{smallmatrix}a & b \\ c & d\end{smallmatrix} \bigr) $$```

## Edge Case 1 from Quxiaofeng:

### No blank lines between Markdown list items

The issue arises when sidenotes and marginnotes are put into list items.  As mentioned in the main documentation page, lists can be problematic not only for semantic clarity, but also because they can creating formatting issues. For example:

### Related algorithms

+ Split Bregman iteration {% sidenote 1 'Goldstein, T. and Osher, S. (2009). The split Bregman method for l1-regularized problems. SIAM J. Img. Sci., 2:323-343.' %}
+ Dykstra's alternating projection algorithm {% sidenote 2 'Dykstra, R. L. (1983). An algorithm for restricted least squares regression. J. Amer. Statist. Assoc., 78(384):837-842.' %}
+ Proximal point algorithm applied to the dual
+ Numerous applications in statistics and machine learning: lasso, gen. lasso, graphical lasso, (overlapping) group lasso, ...
+ Embraces distributed computing for big data {% sidenote 3 'Boyd, S., Parikh, N., Chu, E., Peleato, B., and Eckstein, J. (2011). Distributed optimization and statistical learning via the alternating direction method of multipliers. Found. Trends Mach. learn., 3(1):1-122.' %}

### Why this matters

Notice how the sidenotes display properly, but the fact that sidenotes have more display 'volume' than the list items themselves causes a horizontal mismatch between the sidenote item's number and its corresponding list item.

Please note that there must be *no blank lines between your list items*. This is due to a really strange thing about the Jekyll Markdown engine I have never noticed before. If you have a list, and you put a blank line between the items like this:

```
  + list item 1

  + list item 2
```

It will create an html tag structure like this:

```
<ul>
   <li>
      <p>list item 1</p>
  </li>
  <li>
      <p>list item 2</p>
   </li>
</ul>
```
Which *totally* goofs up the layout CSS.

However, if your Markdown is this:

```
    + list item 1
    + list item 2
```

It will create a tag structure like this:

```
<ul>
   <li>list item 1</li>
   <li>list item 2</li>
</ul>
```

Here is the same content as above, with a blank line separating the list items. Notice how the sidenotes get squashed into the main content area:


### Remarks on ADMM version 2 - **one blank line** between Markdown list items

Related algorithms

+ Split Bregman iteration {% sidenote 1 'Goldstein, T. and Osher, S. (2009). The split Bregman method for l1-regularized problems. SIAM J. Img. Sci., 2:323-343.' %}

+ Dykstra's alternating projection algorithm {% sidenote 2 'Dykstra, R. L. (1983). An algorithm for restricted least squares regression. J. Amer. Statist. Assoc., 78(384):837-842.' %}

+ Proximal point algorithm applied to the dual

+ Numerous applications in statistics and machine learning: lasso, gen. lasso, graphical lasso, (overlapping) group lasso, ...
<br>
<br>
<br>
<br>

### Liquid tag parsing strangeness

Example of the proper way to write an url inside a *Liquid* full-width image tag.

This code: ```{{ '{% fullwidth "assets/img/rhino.png" "Tuftes pet rhino (via <a href=\"//www.edwardtufte.com/tufte/\">Edward Tufte</a>)" ' }} %}```

produces the following image with a title. Notice that I have had to escape the double quotes in the HTML with a backslash. Also, the example above leaves out the single quote in 'Tufte's" because of the topsy-turvy way that you have to escape the escapes in code sections that are used for illustrative purposes in this text. Bottom line is that there are occasionally some odd interactions between the Markdown parser, custom *Liquid* tags and HTML.
{% fullwidth "assets/img/rhino.png" "Tufte's pet rhino (via <a href=\"//www.edwardtufte.com/tufte/\">Edward Tufte</a>)" %}
