---
title: 'Better Beamer Presentations the Easy Way'
date: 2019-10-01
permalink: /posts/2019/10/better-beamer
excerpt_separator: <!--more-->
tags:
  - references
  - bash
---

Everyone knows that Beamer makes frankly terrible presentations without a good deal of help. A well crafted Beamer presentation can be a thing of beauty, especially since you can use knitr or R Markdown to automatically generate tables and figures, but it takes *a lot* of work.
<!--more-->
We all have our own little tricks to do things like get more space between items in a list (ending every `\item` line with `\\~\\`) and the simple but repetitive tasks we have to do every single slide (opening a `\Large` environment to make text more readable).

I finally got tired of all this and decided to waste a lot of time now to save even more time later. To do that, I headed to Stack Exchange and started digging into the Beamer documentation.

## Give Me Some Space

We'll start with the base Beamer class. There are a number of Beamer [themes](https://hartwork.org/beamer-theme-matrix/) that are much better than the default theme, but I'm going to focus on things we can do to improve even the default theme. Here's our humble starting point.

```latex
\documentclass{beamer}

\begin{document}
	
\begin{frame}[fragile]{My default slide}
	\begin{itemize}
		\item Foo
		\item Bar
		\begin{itemize}
			\item Below is an equation
			\[ y = mx + b \]
			\item It is very hard to read
		\end{itemize}
		\item Baz
	\end{itemize}
\end{frame}

\end{document}
```

![](/images/posts/Slide_Default.png)

The first thing anyone who's ever taken a graphic design class will tell you is that we need to space out those lines. With them all crammed in the middle, they're harder to read and there's ton of empty space up top and down below. We can insert a `\vfill` at the top and bottom of the slide, and between each line, but this gets old quickly. After plenty of googling and a few less than perfect solutions, I came across this Stack Exchange [answer](https://tex.stackexchange.com/questions/369504#369597). By adding the following code to your preamble, any items in a `\itemize` environment will be evenly spaced vertically.

{% raw %}
```latex
\makeatletter
\renewcommand{\itemize}[1][]{%
	\beamer@ifempty{#1}{}{\def\beamer@defaultospec{#1}}%
	\ifnum \@itemdepth >2\relax\@toodeep\else
	\advance\@itemdepth\@ne
	\beamer@computepref\@itemdepth% sets \beameritemnestingprefix
	\usebeamerfont{itemize/enumerate \beameritemnestingprefix body}%
	\usebeamercolor[fg]{itemize/enumerate \beameritemnestingprefix body}%
	\usebeamertemplate{itemize/enumerate \beameritemnestingprefix body begin}%
	\list
	{\usebeamertemplate{itemize \beameritemnestingprefix item}}
	{\def\makelabel##1{%
			{%
				\hss\llap{{%
						\usebeamerfont*{itemize \beameritemnestingprefix item}%
						\usebeamercolor[fg]{itemize \beameritemnestingprefix item}##1}}%
			}%
		}%
	}
	\fi%
	\setlength\itemsep{\fill}
	\ifnum \@itemdepth >1
	\vfill
	\fi%  
	\beamer@cramped%
	\raggedright%
	\beamer@firstlineitemizeunskip%
}
\def\enditemize{\ifhmode\unskip\fi\endlist%
	\usebeamertemplate{itemize/enumerate \beameritemnestingprefix body end}
	\ifnum \@itemdepth >1
	\vfil
	\fi%  
}
\makeatother
```
{% endraw %}

![](/images/posts/Slide_Better.png)

Looking better already!

## Super Size It

Next we need to enlarge our text to make it easier to read. Again, we can do this manually on every slide, but that's a giant pain. I found this [old thread](https://latex.org/forum/viewtopic.php?t=8515) on latex.org which explains how to redefine the font size of `\itemize` and `\enumerate` items.

```latex
\setbeamerfont{itemize/enumerate body}{size=\Large}
\setbeamerfont{itemize/enumerate subbody}{size=\large}
\setbeamerfont{itemize/enumerate subsubbody}{size=\normalsize}
```

While this has fixed the font size of our lists, now our still too small equation will look even more out of place. I learned from this Stack Exchange [answer](https://tex.stackexchange.com/a/40531) that the `\[` and `\]` math mode separators actually call the `equation*` environment. With this knowledge, I used the [`etoolbox`](https://ctan.org/pkg/etoolbox?lang=en) package's `\BeforeBeginEnvironment` and `\AfterEndEnvironment` commands to change the font size to LARGE for any `equation*` environments.

```latex
\usepackage{etoolbox}
\BeforeBeginEnvironment{equation*}{\begingroup\LARGE}
\AfterEndEnvironment{equation*}{\endgroup}
```
![](/images/posts/Slide_Better_Equation.png)

Now we've got a much more readable slide that will be automatically replicated for every other slide in our presentation. If you have multi-line equations in your slides, you can similarly redefine the `align*` environment to enlarge these equations as well. 

## Don't Forget Numbers

As we can see above, our redefinition of the `\itemize` environment also evenly spaces sub-bullets. However, it doesn't do anything for numbered lists defined with `/enumerate` as the slide below shows.

![](/images/posts/Slide_Enumerate_Default.png)

To evenly space items in numbered lists, we just need to take the same changes to the `\itemize` environment we introduced above, and apply them to the `\enumerate` environment as well. Unfortunately, I'm not nearly fluent enough in TeX to understand what this code does. Luckily, I know how to run a [diff](https://en.wikipedia.org/wiki/Diff). Diffing two files will point out all differences between the two. By comparing the modified code from Stack Exchange with the original in [`beamerbaselocalstructure.sty`](http://mirrors.ctan.org/macros/latex/contrib/beamer/base/beamerbaselocalstructure.sty), we can figure out which lines have been added and copy them over to Beamer's definition of the `\enumerate` environment.

{% raw %}
```diff
\makeatletter
\renewcommand{\itemize}[1][]{%
	\beamer@ifempty{#1}{}{\def\beamer@defaultospec{#1}}%
	\ifnum \@itemdepth >2\relax\@toodeep\else
	\advance\@itemdepth\@ne
	\beamer@computepref\@itemdepth% sets \beameritemnestingprefix
	\usebeamerfont{itemize/enumerate \beameritemnestingprefix body}%
	\usebeamercolor[fg]{itemize/enumerate \beameritemnestingprefix body}%
	\usebeamertemplate{itemize/enumerate \beameritemnestingprefix body begin}%
	\list
	{\usebeamertemplate{itemize \beameritemnestingprefix item}}
	{\def\makelabel##1{%
			{%
				\hss\llap{{%
						\usebeamerfont*{itemize \beameritemnestingprefix item}%
						\usebeamercolor[fg]{itemize \beameritemnestingprefix item}##1}}%
			}%
		}%
	}
	\fi%
+	\setlength\itemsep{\fill}
+	\ifnum \@itemdepth >1
+	\vfill
+	\fi%  
	\beamer@cramped%
	\raggedright%
	\beamer@firstlineitemizeunskip%
}
\def\enditemize{\ifhmode\unskip\fi\endlist%
-	\usebeamertemplate{itemize/enumerate \beameritemnestingprefix body end}}
+       \usebeamertemplate{itemize/enumerate \beameritemnestingprefix body end}
+	\ifnum \@itemdepth >1
+	\vfil
+	\fi%  
+}
\makeatother
```
{% endraw %}

Essentially, the new code redefines the `\itemsep` length parameter as `\vfill` and adds a `\vfil` at the end of an `\itemize` environment. `\vfil` and `\vfil` are both commands to create vertical space, and this Stack Exchange [answer](https://tex.stackexchange.com/a/21028) explains the difference between them, but I still have no idea what the difference is after reading it. What matters is that the `\enumerate` environment definition looks identical to the `\itemize` one in the lines surrounding the new code (with the substitution of `\endenumerate` for `\enditemize`), which makes it easy to add it to this definition as well.

{% raw %}
```latex
\makeatletter
\def\enumerate{%
	\ifnum\@enumdepth>2\relax\@toodeep
	\else%
	\advance\@enumdepth\@ne%
	\edef\@enumctr{enum\romannumeral\the\@enumdepth}%
	\advance\@itemdepth\@ne%
	\fi%
	\beamer@computepref\@enumdepth% sets \beameritemnestingprefix
	\edef\beamer@enumtempl{enumerate \beameritemnestingprefix item}%
	\@ifnextchar[{\beamer@@enum@}{\beamer@enum@}}
\def\beamer@@enum@[{\@ifnextchar<{\beamer@enumdefault[}{\beamer@@@enum@[}}
\def\beamer@enumdefault[#1]{\def\beamer@defaultospec{#1}%
	\@ifnextchar[{\beamer@@@enum@}{\beamer@enum@}}
\def\beamer@@@enum@[#1]{% partly copied from enumerate.sty
	\@enLab{}\let\@enThe\@enQmark
	\@enloop#1\@enum@
	\ifx\@enThe\@enQmark\@warning{The counter will not be printed.%
		^^J\space\@spaces\@spaces\@spaces The label is: \the\@enLab}\fi
	\def\insertenumlabel{\the\@enLab}
	\def\beamer@enumtempl{enumerate mini template}%
	\expandafter\let\csname the\@enumctr\endcsname\@enThe
	\csname c@\@enumctr\endcsname7
	\expandafter\settowidth
	\csname leftmargin\romannumeral\@enumdepth\endcsname
	{\the\@enLab\hspace{\labelsep}}%
	\beamer@enum@}
\def\beamer@enum@{%
	\beamer@computepref\@itemdepth% sets \beameritemnestingprefix
	\usebeamerfont{itemize/enumerate \beameritemnestingprefix body}%
	\usebeamercolor[fg]{itemize/enumerate \beameritemnestingprefix body}%
	\usebeamertemplate{itemize/enumerate \beameritemnestingprefix body begin}%
	\expandafter
	\list
	{\usebeamertemplate{\beamer@enumtempl}}
	{\usecounter\@enumctr%
		\def\makelabel##1{{\hss\llap{{%
						\usebeamerfont*{enumerate \beameritemnestingprefix item}%
						\usebeamercolor[fg]{enumerate \beameritemnestingprefix item}##1}}}}}%
	\setlength\itemsep{\fill}
	\ifnum \@itemdepth >1
	\vfill
	\fi%  
	\beamer@cramped%
	\raggedright%
	\beamer@firstlineitemizeunskip%
}
\def\endenumerate{\ifhmode\unskip\fi\endlist%
	\usebeamertemplate{itemize/enumerate \beameritemnestingprefix body end}
	\ifnum \@itemdepth >1
	\vfil
	\fi%  
}
\makeatother
```
{% endraw %}

Once we've done that, now numbered lists are also evenly spaced!

![](/images/posts/Slide_Enumerate_Better.png)

## All Together now

Sticking all of the below in your preamble will greatly improve the visual appeal of your slides with zero effort required on each individual slide.

{% raw %}
```latex
% % redefine itemsep to autofill space on beamer slides
% % from https://tex.stackexchange.com/questions/369504#369597
\makeatletter
\renewcommand{\itemize}[1][]{%
	\beamer@ifempty{#1}{}{\def\beamer@defaultospec{#1}}%
	\ifnum \@itemdepth >2\relax\@toodeep\else
	\advance\@itemdepth\@ne
	\beamer@computepref\@itemdepth% sets \beameritemnestingprefix
	\usebeamerfont{itemize/enumerate \beameritemnestingprefix body}%
	\usebeamercolor[fg]{itemize/enumerate \beameritemnestingprefix body}%
	\usebeamertemplate{itemize/enumerate \beameritemnestingprefix body begin}%
	\list
	{\usebeamertemplate{itemize \beameritemnestingprefix item}}
	{\def\makelabel##1{%
			{%
				\hss\llap{{%
						\usebeamerfont*{itemize \beameritemnestingprefix item}%
						\usebeamercolor[fg]{itemize \beameritemnestingprefix item}##1}}%
			}%
		}%
	}
	\fi%
	\setlength\itemsep{\fill}
	\ifnum \@itemdepth >1
	\vfill
	\fi%  
	\beamer@cramped%
	\raggedright%
	\beamer@firstlineitemizeunskip%
}
\def\enditemize{\ifhmode\unskip\fi\endlist%
	\usebeamertemplate{itemize/enumerate \beameritemnestingprefix body end}
	\ifnum \@itemdepth >1
	\vfil
	\fi%  
}
\makeatother

\makeatletter
\def\enumerate{%
	\ifnum\@enumdepth>2\relax\@toodeep
	\else%
	\advance\@enumdepth\@ne%
	\edef\@enumctr{enum\romannumeral\the\@enumdepth}%
	\advance\@itemdepth\@ne%
	\fi%
	\beamer@computepref\@enumdepth% sets \beameritemnestingprefix
	\edef\beamer@enumtempl{enumerate \beameritemnestingprefix item}%
	\@ifnextchar[{\beamer@@enum@}{\beamer@enum@}}
\def\beamer@@enum@[{\@ifnextchar<{\beamer@enumdefault[}{\beamer@@@enum@[}}
\def\beamer@enumdefault[#1]{\def\beamer@defaultospec{#1}%
	\@ifnextchar[{\beamer@@@enum@}{\beamer@enum@}}
\def\beamer@@@enum@[#1]{% partly copied from enumerate.sty
	\@enLab{}\let\@enThe\@enQmark
	\@enloop#1\@enum@
	\ifx\@enThe\@enQmark\@warning{The counter will not be printed.%
		^^J\space\@spaces\@spaces\@spaces The label is: \the\@enLab}\fi
	\def\insertenumlabel{\the\@enLab}
	\def\beamer@enumtempl{enumerate mini template}%
	\expandafter\let\csname the\@enumctr\endcsname\@enThe
	\csname c@\@enumctr\endcsname7
	\expandafter\settowidth
	\csname leftmargin\romannumeral\@enumdepth\endcsname
	{\the\@enLab\hspace{\labelsep}}%
	\beamer@enum@}
\def\beamer@enum@{%
	\beamer@computepref\@itemdepth% sets \beameritemnestingprefix
	\usebeamerfont{itemize/enumerate \beameritemnestingprefix body}%
	\usebeamercolor[fg]{itemize/enumerate \beameritemnestingprefix body}%
	\usebeamertemplate{itemize/enumerate \beameritemnestingprefix body begin}%
	\expandafter
	\list
	{\usebeamertemplate{\beamer@enumtempl}}
	{\usecounter\@enumctr%
		\def\makelabel##1{{\hss\llap{{%
						\usebeamerfont*{enumerate \beameritemnestingprefix item}%
						\usebeamercolor[fg]{enumerate \beameritemnestingprefix item}##1}}}}}%
	\setlength\itemsep{\fill}
	\ifnum \@itemdepth >1
	\vfill
	\fi%  
	\beamer@cramped%
	\raggedright%
	\beamer@firstlineitemizeunskip%
}
\def\endenumerate{\ifhmode\unskip\fi\endlist%
	\usebeamertemplate{itemize/enumerate \beameritemnestingprefix body end}
	\ifnum \@itemdepth >1
	\vfil
	\fi%  
}
\makeatother

% % set larger itemize font sizes
% % from https://latex.org/forum/viewtopic.php?t=8515
\setbeamerfont{itemize/enumerate body}{size=\Large}
\setbeamerfont{itemize/enumerate subbody}{size=\large}
\setbeamerfont{itemize/enumerate subsubbody}{size=\normalsize}

% % redefine \[\] via redefinition of same as equation* to be LARGE
% % from https://tex.stackexchange.com/a/40531
\usepackage{etoolbox}
\BeforeBeginEnvironment{equation*}{\begingroup\LARGE}
\AfterEndEnvironment{equation*}{\endgroup}
\BeforeBeginEnvironment{align*}{\begingroup\LARGE}
\AfterEndEnvironment{align*}{\endgroup}
```
{% endraw %}

I've combined all of the LaTeX code above into a style file called [`better-beamer.sty`](https://github.com/jayrobwilliams/TeX-Misc/blob/master/better-beamer.sty) available on my GitHub. To avoid having to copy and paste this code into the preamble of every presentation you make, you can just load the style file instead! If you place the style file into the same directory as your `.tex` file, you just need to add:

```latex
\usepackage{better-beamer}
```

If you want to avoid having to copy the style file every time you make a new presentation, you can just use an absolute path to reference it in your `.tex` document. On my computer, this looks like this:

```latex
\usepackage{/Users/Rob/Dropbox/TeX/Templates/better-beamer}
```

## R Markdown

One caveat if you use R Markdown like I do. R Markdown relies on [pandoc](https://pandoc.org) to convert from `.Rmd` to `.md` to `.tex` to `.pdf` (phew). This only matters if you're a lazy typist like me and write your

```markdown
- lists
- like
- this
```

and

```markdown
- not

- like

- this.
```

When you write your lists in the former format, pandoc redefines `\itemsep` to `0pt` in any list (bulleted or numbered) environment in the the resulting LaTeX code via the following command:

{% raw %}
```latex
\providecommand{\tightlist}{%
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
```
{% endraw %}

This will cancel out our redefined list environments and get us back our original cramped lines. There's no way to disable this `\tightlist` behavior (short of removing it from the source code and compiling pandoc yourself), but it *is* very easy to neutralize thanks to the info in this Stack Exchange [answer](https://tex.stackexchange.com/a/257464). If you're using R Markdown, simply add the following to your YAML header under the `header-includes` variable.

```latex
\def\tightlist{}
```

This will come after the `\tightlist` definition in the preamble and redefine it to do nothing, leaving our properly spaced lists intact without having to add an empty line after every item. At some point I'll post my custom LaTeX template (with other aesthetic improvements) for Beamer slides via R Markdown and talk about my process for modifying the default template.