---
date: '2015-12-31'
slug: faces-of-if
title: Faces of "if"
---

The _if_-_else _statement (a.k.a., conditional statement, conditional expression, etc.) is a basic feature of programming languages. In the languages I first learned (BASIC, C, Python), I thought _if-else_ was a monolithic thing. Many languages have an _elseif_ statement, and some languages (e.g., C, Ruby) have a _[switch](http://www.tutorialspoint.com/ansi_c/c_control_statements.htm)_ or _[case](http://ruby-doc.org/docs/keywords/1.9/Object.html#method-i-case)_ statement that takes care of complicated _if-elseif-elseif-elseif..._ situations. All of these are just syntactic sugar for a chain of _if-else_ statements, which reinforced my idea that _if-else_ was monolithic.

I was very confused when, while learning about Haskell, that [Haskell's _if_](https://wiki.haskell.org/Keywords#if) always has an _else_. The idea, in Haskell, is that everything that happens in the program is about the [movement of information](https://en.wikipedia.org/wiki/Functional_programming), not the [execution of actions](https://en.wikipedia.org/wiki/Imperative_programming). It doesn't make sense to say that variable _X_ should be _foo_ if _Y_ is true, but it's not anything if _Y_ is false.

I was, at first, confused to see that Racket has an `[if](http://docs.racket-lang.org/reference/if.html)` and a `[when](http://docs.racket-lang.org/reference/when_unless.html)`, which are different things. In this case, `if` is like Haskell's _if_, which always comes with an _else_, while `when` is an _if_ that never has an else.

When looking at some of [my work-a-day Python code](https://github.com/swo/slime2), I discovered that I use Python's _if_ both as `if` and `when`. For example, some of my _if_ statements look like:


    if switcher_thingy:
      output_variable = value_when_switch_is_true
    else:
      output_variable = value_when_switch_is_false


I would use this kind of _if-else_ when, say, I wanted to use either a default value or compute a new value from scratch. Other _if_ statements look like:


    if some_switch_about_program_execution:
      take_some_action()


I would use this kind of _if-else_ when, say, I wanted to output some extra when the program is running in a verbose mode, or I would shuffle entries in an array when I wanted to randomize the data.

The first kind of _if_ is exactly what Racket's `if` is for. The second is exactly what Racker's `when` is for. Maybe it seems excessive to put more syntax into the program, but I think it's helpful to understand that `if` is basically a function that takes a Boolean and two other values, and returns one of those two values, while `when` is a subroutine that takes an action only when some boolean is true.