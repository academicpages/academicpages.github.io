---
title: 'My Racket epiphany: the do-it-again macro'
date: '2016-02-19'
slug: do-it-again
---

I'm a computation PhD student, so do a lot of menial data processing. I have one file in such-and-such format and arrangement and another file in the the same arrangement, and I need to read them both in, process them somehow, and then spit out a result that depends on the two together.

Imagine I need to read column _X_ from file 1 and column _Y_ from file 2. I often find myself writing some lines of code like:


    
    result1 = process_file_with_parameter(file1, parameter1)
    result2 = process_file_with_parameter(file2, parameter2)



I hate this. I hate repeating code. All I want in my heart of hearts is to write something like:


    
    result1 = process_file_with_parameter(file1, parameter1)
    do_that_again("1", "2")



This `do_that_again` isn't really a function, since it's taking in some _code_ and turning that into other code. It _can't_ be a function, since a function can't take `"1"`, `"2"`, and `file1` and turn that into `file2`, since the raw code `file1` simply isn't available to a function. Whether you call by reference or call by value, you're not calling by, whatever, raw code.

This annoyance was the first time I got why I would really want to write my own macro. A macro is like a function, but it works on the raw code words, not on what the code words represent in the course of evaluating the program.

At this point, I read and re-read a lot of the [Racket documentation](https://docs.racket-lang.org/guide/macros.html) and Greg Hendershott's excellent [Fear of Macros](http://www.greghendershott.com/fear-of-macros/). When I got confused and need a break, I delighted in [this account](http://www.hashcollision.org/brainfudge/) of writing a [brainfuck](https://en.wikipedia.org/wiki/Brainfuck) interpreter in Racket.

I wrote this in Racket. It's not elegant, and I'm sure there are things that could break it, and I'm sure there are better ways to do it, and in that way it's beautiful. Basically, I read in the thing to be re-evaluated and the pattern and replacement. I turn the thing to be re-evaluated into a set of strings, replace the pattern with the replacement, turn them back into whatever they were, and put that new piece of code just after the first one.


    
    #lang racket
    
    ; to use the match function in a syntax transformer
    (require (for-syntax racket/match))
    
    ; a helper function that does the replacement on whatever the input code is
    (define-for-syntax (replace-words from words to)
      (map (lambda (word)
             (let ([sfrom (regexp (syntax->datum from))]
                   [sto (syntax->datum to)]
                   [dword (syntax->datum word)])
               (cond
                 ; I'm sure there's a more elegant way to say: whatever you are, become a string,
                 ; do this thing, then go back to being whatever you were
                 [(string? dword) (regexp-replace sfrom dword sto)]
                 [(number? dword) (string->number (regexp-replace sfrom (number->string dword) sto))]
                 [(symbol? dword) (string->symbol (regexp-replace sfrom (symbol->string dword) sto))])))
             words))
    
    ; here's the meat!
    (define-syntax (do-again-with stx)
      ; match the expression, "from" replacement string, and "to" replacement string
      (match (syntax->list stx)
        [(list _ expr from to)
         (datum->syntax stx
                        ; do more than one thing...
                        `(begin
                          ; the original thing...
                          ,expr
                          ; then then the thing with the replacement
                          ,(replace-words from (syntax->list expr) to)))]))
    
    ; print two lines: "it's 1" and "it's 2"
    (do-again-with (displayln "it's 1") "1" "2")
    
    ; define a variable foo1 as "bar1" and foo2 as "bar2"
    (do-again-with (define foo1 "bar1") "1" "2")



I thought that was pretty cool.
