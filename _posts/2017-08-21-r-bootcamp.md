---
title: "How Well Did I Follow Pedagogy Guidelines at R Bootcamp 2017?"
date: 2017-08-21
permalink: /posts/2017/08/r-bootcamp/
tags:
  - R
  - bootcamp
  - workshop
  - Software Carpentry
---


This week I had the privilege of participating in two workshops: I was a participant at a train-the-trainer workshop to become a Software Carpentry instructor and an instructor at the R Bootcamp put on by the Statistics Department and D-Lab.
It was a unique opportunity to spend two days learning how to teach one of these bootcamps, and then to put my skills to the test a few days later.

<div class='center'>
<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Fourth annual <a href="https://twitter.com/hashtag/Statistics?src=hash">#Statistics</a> Dept and <a href="https://twitter.com/DLabAtBerkeley">@DLabAtBerkeley</a> R Bootcamp. I love watching so many people learn their first <a href="https://twitter.com/hashtag/Rstats?src=hash">#Rstats</a> <a href="https://t.co/bwV5EarPGp">pic.twitter.com/bwV5EarPGp</a></p>&mdash; Kellie Ottoboni (@kellieotto) <a href="https://twitter.com/kellieotto/status/899014319324536832">August 19, 2017</a></blockquote> <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
</div>

Software Carpentry is a nonprofit that develops curriculum for novices learning to program and puts on two day workshops to teach people their curriculum.
You don't need to be a certified instructor to teach their material, but it makes you part of their community and creates opportunities to travel and teach at workshops around the world.

[The instructor training materials are available on the Software Carpentry website.](https://swcarpentry.github.io/instructor-training/)
The training took place over two days.
It was structured in the style of a Software Carpentry programming workshop: the leaders modeled how we would run a workshop ourselves.

A few days later, I was a helper at the annual R Bootcamp.
It started four years ago as a workshop to get the new Statistics and D-Lab students up to speed on R before classes started, but demand has grown tremendously since its inception.
This year there was a waitlist to participate!

Last year, I modified the graphics lesson and made the focus `ggplot2`.
This year, I taught the graphics lesson as well as the data wrangling with `dplyr` lesson (which, coincidentally, was based off of Software Carpentry materials).
The lessons are made with R Markdown, so there is code along with slides.
[The bootcamp materials are here.](https://github.com/berkeley-scf/r-bootcamp-2017)

At the instructor training, I learned a number of useful things that I wanted to incorporate into my teaching.
How well did I manage to practice these best-practices?

## Live coding

Ideally, you know the lesson content and main ideas well enough that you can step away from them and write code at the command line as you talk through it!
It's more instructive for students to 
a) follow along as you type, rather than reading a block of code,
b) hear you talk through your thought process as you write code, and
c) watch you make mistakes and fix them rather than see only the finished product.

I tried this for the `dplyr` lesson and felt like I fumbled. 
At the beginning, it was easy enough, but once it came time to write long multi-line commands I slipped. 
I ended up copy-and-pasting or pointing to the code in the slides. 
I only live coded one plot in the graphics lesson, but this was intentional:
`ggplot` calls can be quite long to type out, and the point was to demonstrate its rich capabilities rather than the precise syntax.

## Motivating and not accidentally demotivating

Topics fall on two axes, usefulness and easiness.
Students will get demotivated if 
* you present topics that are too hard early on
* you present topics that are not useful early on
* you use language like "just do x", "actually, do x", or "x is simple". Students who don't know how to do x will think they're dumb for not knowing

Conversely, students will be more motivated to learn if you show them extremely useful but simple things and if you remind them that you yourself are not a coding god.

I tried to make the point that I learned all these tools very recently, so I'm not an expert either. 
I compared the concise syntax of `dplyr` to the long, convoluted code they'd need to write in base R to accomplish the same task.
I encouraged students to think creatively about what kind of plots they want to make and to Google how to do it if they don't know how, because that's what I do. 
One person asked how to add a second y-axis to a plot and I told him to "just google it". 
He scoffed at me, so maybe I demotivated him there. Oops.

## Cognitive load

Students can only handle a few (on average, 5-7) new concepts in their short term memory. 
Once you've taught about that many things, you should pause and have them do a *formative assessment* to test their understanding and practice using the concepts.
This helps the learner figure out what they do and don't understand, and gives them a chance to solidify their short term memory before taking on a new set of concepts.

The bootcamp structure we used was about 40 minutes of lecture and demonstration, then 20 minutes of solo or group practice. 
Looking back on it, I think that 15-20 minutes of material  would have been the right amount of cognitive load before breaking for an exercise. 
Alas, we can improve next time. 
It was especially difficult for students on the first day, as the first lessons were more dense then later ones.


# Unsolved problems

Overall, I think the R bootcamp went well.
There was low attrition and students actually seemed *more* engaged on day 2.

I personally could have done more to follow the Software Carpentry guidelines for teaching.
That said, with such a short amount of time between the instructor training and the R bootcamp, I didn't have enough time to modify the lessons to my liking and practice teaching and live coding them.

I saw a few unsolved problems in how to run a successful bootcamp.

* How do you make sure everyone has the requisite programs installed? You can't devote half of the workshop to this, but you don't want people to give up and leave either. At the R bootcamp, we had a 30 minute buffer before the program started when students could talk to the helpers and get set up. I helped a few people during this time. Others came too late, tried to get set up while the lessons had already started, fell behind, and left.
* What's the best way to help students in real time? This is especially important at the beginning of a workshop when are overwhelmed by details. The R bootcamp had 5 helpers circulating the room and used Piazza for non-critical questions. I thought this worked well for a group of 100+; [the Software Carpentry sticky note method](https://swcarpentry.github.io/instructor-training/15-practices/) probably works well for smaller groups.
* What level of background do you assume? For instance, a lot of students had trouble loading in the example datasets because they didn't understand their file directory structure. This is a common problem for people who've never used the command line. But how much time in a bootcamp for R should be devoted to learning a concept outside the scope of R?