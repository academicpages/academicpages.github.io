---
title: 'Combining PDF Documents the Smarter Way'
date: 2019-07-08
permalink: /posts/2019/07/combining-pdfs-naturally/
excerpt_separator: <!--more-->
toc: true
tags:
  - references
  - bash
---

My previous [post]({{ site.baseurl }}{% post_url 2019-06-25-combining-pdfs %}) on combining multiple PDF files had an important caveat that things would end up in the wrong order if you had files with leading ID numbers that started at 1 and ended at 12, you'd end up with PDFs combined in the order 1, 10, 11, 12, 2, 3, ..., 9.
<!--more-->
This is because the default sort in Bash is an alphabetic sort. This is just our standard alphabetic sort, but it gets tripped up when dealing with numbers. We can think of it as a type of 'greedy' algorithm because it sorts all inputs by the first character, before moving onto the second character within each subset. This behavior is fine (and desirable!) for words, but fails with numbers.

We want to use a [natural sort](https://en.wikipedia.org/wiki/Natural_sort_order), which is just an alphabetic sort that treats multi-digit numbers as numbers instead of a collection of characters. A natural sort of our files would combine them in the order 1, 2, 3, 4, 5, ..., 12, 13. That means a natural sort can handle a wider range of numbering styles!

# How it Works

This script uses the same basic idea as the first one, but sorting the input files with a natural sort requires some Bash tricks. This time around the code is

```bash
#!/bin/bash
if [[ $# -eq 0 ]]; then
  printf '%s\0' ./*.pdf | sort -zV | xargs -0 gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=output.pdf
else
  printf '%s\0' ./*.pdf | sort -zV xargs -0 gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=$1
fi
```

This looks complicated, so let's break it down into individual parts. Each part is separated by a `|`, or pipe, which directs the output from one function to the next. If you've ever used magrittr's pipes (`%>%`) in R, the concept is exactly the same.

## `printf`

The first part of the first Ghostscript line is

```bash
printf '%s\0' ./*.pdf
```

. The `printf` command is a *very* old C command, ported to Bash as a **shell builtin**. It allows you to print multiple inputs while formatting the output produced. `printf` uses **format specifiers** to tell the function how to print inputs. While it can be used to format integers and doubles, we're going to be dealing with filenames, which are strings, and denoted with `'%s'`.

When we give `printf` more than one input, we need to tell it what type of **separator** to use, otherwise it will just print all of the inputs in one giant string. If you use a **newline** (`\n`), then `printf` will produce output equivalent to `ls *.pdf`. For our purposes, we want to use a **null terminator** (`\0`) to separate inputs. You can't actually see null terminators in the printed output, but any commands you pass them to will be able to.

## `sort`

The next part of the first Ghostscript line is

```bash
sort -zV
```

This is where the magic happens that properly sorts our input files even if their numbers are missing leading zeroes. The `-z` flag tells `sort` to return the sort inputs still separated by null terminators, while the `-V` flag performs a **version sort**, the function's name for a natural sort.

## `xargs`

The final part of the first Ghostscript line is

```bash
xargs -0 gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=output.pdf
```

This is almost identical to the `gs` call in the simpler script. However, that script had `*.pdf` at the end as the "files" argument to `gs`. That won't work for us here as we had to use `printf` and `sort` first to get our document correctly sorted. `xargs` converts the standard input produced by `|` into arguments that `gs` can accept.

The `-0` flag tells the function to expect null terminators as separators instead of spaces or newlines. Without this flag, you'll get an error if any of your PDFs have spaces in their filenames. This is why we've been using null terminators as separators all along; without them our script would be helpless against filenames with spaces in them.

The command we want to use, `gs` in this case, comes *after* `xargs`. You can read this line as `gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=output.pdf files` where `files` is the naturally sorted list of PDF files produced by the first two parts of the line. And we're done!

## Putting it all Together

When you run this script, it finds all PDF files in a directory, sorts them with a natural sort, and then combines them into a single PDF document. Just like before, you can can supply an output filename.

# Running It

Just like before, we need to make our script executable and add it to our PATH in order to run it. Refer to my previous [post]({{ site.baseurl }}{% post_url 2019-06-25-combining-pdfs %}) for a reminder on how to do so. No caveats about document ID numbers this time, but you're on your own if the publisher decided to just use chapter names with no ID numbers...