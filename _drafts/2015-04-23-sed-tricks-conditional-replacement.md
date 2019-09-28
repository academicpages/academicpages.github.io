---
date: '2015-04-23'
slug: sed-tricks-conditional-replacement
title: 'sed tricks: conditional replacement'
---

I wanted to change the read names in a [fasta](http://en.wikipedia.org/wiki/FASTA_format) file. Basically, I wanted to run a `sed` replacement, but only on lines that start with `>`, changing lines like `>GoodInfo_LotsOfTrash` into just `>GoodInfo`, but I wanted to leave lines that didn't start with `>` alone.





I found a [nice answer](http://stackoverflow.com/questions/3333483/sed-replace-only-if-match-the-first-word-in-line):





    <code>sed '/conditional_pattern/ s/pattern/replacement/g'
    </code>





In my case, I wanted to chuck everything after an underscore `_`, so `sed '/^>/ /_.*//'`. The command line wins again.