---
title: Why do I need an object-oriented programming language?
date: 2015-12-18
permalink: /posts/2015/12/object-oriented-language
---

This post is a story that has been told many times and in many places, but I've
told it in person enough time to want to tell it in writing.

My first programming language was QBasic. At programming camp I was a Basic
master. In college I was a physics major and somehow managed to do large
amounts of simulations and plotting with Mathematica. I'm in an engineering PhD
program now, and I think many of my peers learned Matlab in the same way I
learned Mathematica, and they never left.

For my Master's work I had to learn Fortran to interface with our existing
codebase. When a postdoc suggested I write a program that did something that,
in words, sounded very simple, I hesitated: Could he give me that script? I
wasn't keen on writing it in Fortran or in Mathematica. He gave me a look and
suggested I learned Python. I look a week off from work and read through
[Learning Python](https://books.google.com/books/about/Learning_Python.html?id=4pgQfXQvekcC&source=kp_cover&hl=en)
cover-to-cover. It was one of the best investments I've ever made. Sometime in
there I learned a little C.

In my PhD work, I tried to just use python and bash. And then people kept using
R around me, so I learned some R. And then some of my coworkers only coded in
Perl, so I had to learn some Perl. Some things about Perl drove me crazy (e.g.,
[internal iterators](http://perldoc.perl.org/functions/each.html)), which led
me to search for the ultimate blend of Python and Perl. I found Ruby,
which introduced me to even more concepts.

After a quick foray into Common Lisp, I'm keen on Racket. Depending on your
perspective, I might be going down the rabbit hole, climbing into an ivory
tower, or running far into left field. I'll quote [an amusing
essay](http://www.paulgraham.com/avg.html) by Paul Graham, who imagines a
programmer working in Blub, a hypothetical intermediate programming language,
where "intermediate" means between low-power languages like awk or bash and
high-power languages like Lisp. Blub might be R, or it might be Perl, or it
might be Python without ever using objects. He says:

> As long as our hypothetical Blub programmer is looking down the power
> continuum, he knows he's looking down. Languages less powerful than Blub are
> obviously less powerful, because they're missing some feature he's used to.
> But when our hypothetical Blub programmer looks in the other direction, up
> the power continuum, he doesn't realize he's looking up. What he sees are
> merely weird languages. He probably considers them about equivalent in power
> to Blub, but with all this other hairy stuff thrown in as well. Blub is good
> enough for him, because he thinks in Blub.

My officemate told me that she doesn't like "over-coded" Python, which after some discussion we decided she meant Python that uses objects. I read her this quote, and she said, "Yup, that's me."

The idea of writing your own dialects of languages is very attractive, and
Matthew Butterick's [writing on that topic](http://practicaltypography.com/why-racket-why-lisp.html) has led me to
Racket. We'll see where that goes.

*Addenum*: Racket was a lot of fun, but as a scientist, you need to use the
languages other people are using, so you can leverage their packages. That
means Python and R for me.
