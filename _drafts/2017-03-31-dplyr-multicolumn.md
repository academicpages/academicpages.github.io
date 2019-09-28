---
date: '2017-03-31'
slug: dplyr-multicolumn
title: Operating over many columns with dplyr
---

[dplyr](https://cran.r-project.org/web/packages/dplyr/vignettes/introduction.html) is awesome. It's totally changed the way I work in R. [tidyr](https://rpubs.com/bradleyboehmke/data_wrangling), in conjunction with dplyr, is also awesome. It's totally changed the way I think about my data.

I had this problem recently: I had a wide data table with one ID (representing individual people) and many columns (representing properties of each person). It made sense to compare these properties: they were things like, "Does this person have disease X?", "Disease Y?", etc. So the records look like:

_person 1; person 1 doesn't have disease X; person 1 does have disease 2; etc._

The tidy data philosophy encourages "gathering" these disparate columns into multiple rows:

_person 1; disease X; doesn't have_
_ person1; disease Y; does have_

I wanted to ask, how many diseases does each person have? dplyr provides a nice way to do this with the tidied data via the _group_by_ and _summarize_ functions. Unfortunately, my table was too big to comfortably tidy it: I had millions of rows and around a dozen columns. I wanted a way to more efficiently do this summation without having to leave dplyr.

I found only one [StackOverflow question](http://stackoverflow.com/questions/32978458/dplyr-mutate-rowwise-max-of-range-of-columns/43144545) that was closely related. After some work, I was able to generalize the first answer to solve my problem. The results are in my response to that question and in [this gist](https://gist.github.com/swo/9f4c296cb481a57dd734d1dbfed19b34). (The question is couched in frames of taking the maximum over multiple columns, but the logic is the same.) This requires some fancy footwork with [lazy evaluation](https://cran.r-project.org/web/packages/lazyeval/vignettes/lazyeval.html), formulas, and the _interp_ function.