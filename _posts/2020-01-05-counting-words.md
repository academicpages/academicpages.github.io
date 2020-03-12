---
title: 'Counting Words in a Snap'
date: 2020-01-05
permalink: /posts/2020/01/counting-words/
excerpt_separator: <!--more-->
tags:
  - grading
  - bash
---

14 pt periods. 1.05" margins. 2.1 spaced lines. [Times Newer Roman](https://timesnewerroman.com/). I've seen them all, and I'm tired of trying to catch them. So, I've stopped assigning papers in terms of page length and switched to word counts. Unfortunately, counting words is more time-intensive than counting pages.
<!--more-->
To Save myself a little time and a lot of boredom I wrote a short shell script to give me the word count for every PDF file in a directory. My method is easiest to implement for PDFs, so I require students to submit their assignments as PDFs. As an added bonus, our learning managment system lets me set assignments to only accept files with a `.pdf` extension so I don't have to deal with students submitting Word docs instead.

## Setup

While the `ps2ascii` utility that we'll use in a minute comes standard with Mac OS and most Linux distributions, we want the most recent version to make sure our script can handle any special characters it encounters. It comes packaged with [Ghostscript](https://www.ghostscript.com/), so install the latest version with [Homebrew](https://brew.sh/):

```bash
brew install ghostscript
```

Once you've done that, you've got everything you need.

## The Code

Next, we need to write a bit of code. Create a text file and put the following in it:

```bash
#!/bin/bash
find . -type f -iname "*.pdf" -print0 | while IFS= read -r -d $'\0' LINE
do
    ps2ascii "$LINE" | wc -w  > "${LINE/%.pdf/-wc.txt}"
done
```

Save it with whatever name you want (I used `PDFcount`), and give it either a `.sh` file extension or no extension.

The script first finds all `.pdf` files in the current directory and then prints them out with the `-print0` flag to separate file names with null terminators instead of newlines.[^1] We then pipe this list of file names to `read` which splits them at each instance of the internal field separator `IFS` which is set to the null terminator with `-d $'\0'` (`-r` tells `read` not to split lines on backslashes) and stores the result in `LINE`.

The loop then executes for each instance of `LINE` (each filename). It first converts the `.pdf` file to plain text using `ps2ascii` and then pipes the resulting text to `wc` with the `-w` flag to count the total number of words. Finally, it writes the output of `wc -` (the number of words in the document) to a file with `>`. It uses Bash parameter substitution to create a file with the same names as the input file in `$LINE` but with `-wc.txt` instead of `.pdf` on the end of it.

Note the `%` in the parameter substitution. The syntax for parameter substitution is `${variable/pattern/replacement}`. By default, Bash substitutes the *first* occurrence of the pattern and then stops. If one of my students had submitted a file called `FinalPaper.pdf.pdf` then the script would output a file called `FinalPaper-wc.txt.pdf`, which wouldn't be a plain text file. The `%` at the start of the pattern means that it will only match at the suffix of the variable, meaning the actual file extension.`

## Running It

To run this script, all you need to do is make it executable and add it to your PATH, which I walk through in detail in a [previous post]({{ site.baseurl }}{% post_url 2019-06-25-combining-pdfs %}). Then, just open a terminal window, navigate to the directory with the files you want word counts for, and type:

```bash
PDFcount
```

The script will create one text file for each `.pdf` file it finds in the directory while leaving the originals untouched.

[^1]: This lets our script handle filenames with spaces, or really any weird characters, as null terminators are the only characters not allowed in file names on Unix-likes.