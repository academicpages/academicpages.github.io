---
title: "Lecture 4: base R vs. tidyverse"
collection: ps811
type: "Graduate course"
venue: "Department of Political Science at the University of Wisconsin-Madison"
permalink: /ps811/ps811-lecture-4-r-vs-tidy
date: 2020-08-27
---

The goal of this lesson is to show you the differences between base R and tidyverse, how you can achieve the same results using either language, and the advantages and disadvantages of both.

While my predecessors are tidyverse zealots, I am not. When it comes to learning R, I don't feel the need to force anyone into learning it one way or the other. People may disagree with this philosophy! Ultimately, I want you to be able to build confidence and feel comfortable whenever you encounter R. And, the fact is, many people use both base R and tidyverse so it is best to know both. In PS 812, for example, you will be using primarily base R functions. So forcing you to learn only tidyverse at this point feels impractical and incompatible with your broader learning goals.

Throughout this course, I will try to specify when I am using base R and when I am using tidyverse. There are some functions that I find much easier (and more intuitive) in base R, and others that I prefer written in tidyverse. But just know this: if there's a way to write it in tidyverse, there's a way to write in base R, and vice versa.

So why tidyverse? Tidyverse is faster. Some of the code is more compact, more practical. However, there are commands that are faster to write and easier to remember in base R, even if it doesn't process faster than its tidyverse equivalent. Processing time is dependent on the amount of data you have, so if you only have a few thousand observations, it might not make much of a difference, but it will probably make a difference if you have tens or hundreds of thousands of observations.

