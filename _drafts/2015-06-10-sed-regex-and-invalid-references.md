---
date: '2015-06-10'
slug: sed-regex-and-invalid-references
title: sed, regex, and invalid references
---

`sed` is a handy tool for line-by-line processing. Unfortunately it's a little older, so its regex syntax is just different enough from Perl/Python/Ruby to get me confused.





Using sed without any flags uses old-style regex. The thing that gets me here is to you need to escape `+` if you want to capture at least one repetition of the preceding expression. That means that `/[0-9]+/` will match `1+` but `/[0-9]+/` will match `1234`.





You also need to escape backreference parentheses, so if you want `a number 1` to turn into `a number "1"` you need `s_([0-9])_"1"_`, i.e., you need `(` and `)`.





Using the advanced regex flag `-r` means that you the escaping takes on the opposite meaning, so that `/[0-9]+/` now matches `1234` while `[0-9]+` matches `1+`, and the substitution above is `s_([0-9])_"1"_`, i.e., now with unescaped parentheses.