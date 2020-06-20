---
title: 'Combining PDF Documents'
date: 2019-06-26
permalink: /posts/2019/06/combining-pdfs/
excerpt_separator: <!--more-->
tags:
  - references
  - bash
---

How many times have you found that your institution has access to a digital version of a book you need only to discover that it comes in 15 different PDF files?
<!--more-->
I use [Zotero](https://www.zotero.org/) as my reference manager and it's difficult to attach more than one file to an entry, so I've certaintly spent time in the past painstakingly combining every section of a book together before adding it to Zotero. I finally got tired of doing this by hand and wrote a short Bash script to automate this process. Now I can combine as many PDFs as I want with a single command!

# How it works

My solution relies on [Ghostscript](https://www.ghostscript.com/) to combine multiple PDF files from the command line. On a Mac you can easily install Ghostscript using [Homebrew](https://brew.sh/) by running

```bash
brew install ghostscript
```

Once you've done that you've got everything you need. Create a shell script and put the following in it

```bash
#!/bin/bash
if [[ $# -eq 0 ]]; then
  gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=output.pdf *.pdf
else
  gs -dBATCH -dNOPAUSE -q -sDEVICE=pdfwrite -sOutputFile=$1 *.pdf
fi
```

The script first checks if you've supplied an output filename as an argument, and if not uses the default name of `output.pdf`. Be aware of where you run this script as it will overwrite a file called `output.pdf` if it exists in the active directory! If you have supplied an output filename, it will use that instead of `output.pdf`.

## Running it

To actually run this script, there are two steps left:

1. Make it executable
2. Add it to your PATH

Making your script executable is relatively straightforward. Use the `chmod +x` command in Terminal on your script. I saved mine as `PDFcombine.sh` so I ran `chmod +x PDFcombine.sh`. Putting your script on your PATH just ensures that your Terminal will be able to find it when you call it to combine PDF files. It's a little more complicated so I'll just link to this [excellent StackExchange answer](https://unix.stackexchange.com/a/26059) on how to do so. On my system this script lives in a directory in my Dropbox with similar other small utilities called `Bash`, so my `.bash_profile` has these lines in it

```bash
# custom bash scripts                                                           
export PATH=$PATH:/Users/Rob/Dropbox/Methods/Bash
```

to add it to my PATH. As an added bonus Ghostscript will (usually) rotate any pages containing sideways tables or figures!

# A warning

This script will combine PDF files in the order that `ls *.pdf` returns them. By default, this will be an *alphabetic sort*, so the files 1.pdf, 2.pdf, and 10.pdf would be combined in the following order: 1.pdf, 10.pdf, 2.pdf.

You can fix this by adding leading zeroes to all filenames so that each ID string is the same length. Most digital versions of books give you filenames like this, but be sure to check, otherwise your combined PDF might require a lot of skipping around. This script can be written to perform a *natural sort* of input files, but the code to do so is more complex, so I'll cover it in a future post.