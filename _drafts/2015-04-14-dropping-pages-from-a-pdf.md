---
date: '2015-04-14'
slug: dropping-pages-from-a-pdf
title: Dropping pages from a pdf
---

When I got a journal article through Illiad, there was an annoying first page about copyright law. After futzing around with Preview for a while, I downloaded the command-line tool `pdftk`.





I'm on Mac OSX, and I use [macports](https://www.macports.org/), so just





    <code>sudo port install pdftk
    </code>





My `foo.pdf` was 10 pages, so to get pages 2-10 I just did





    <code>pdftk foo.pdf cat 2-10 output out.pdf
    </code>





Bonus: I wrote a script that reads the output from the `dump_data` command. One of those lines is `NumberOfPages`, so I parsed that number and put that into the `cat` command so I wouldn't have to look it up myself.