---
title: "What's important when vetting open source packages?"
date: 2017-07-21
permalink: /posts/2017/07/vetting-os/
tags:
  - Python
  - R
  - open source
---

I'm in the early stages of creating several Python packages right now (shameless self plug -- see [permute](statlab.github.io/permute), [cryptorandom](github.com/statlab/cryptorandom), and [pscore_match](github.com/kellieotto/pscore_match)). 
I want people to *actually* use them when they're ready.
They have potential for wide use, but they have narrow functionality compared to big packages like `numpy` or `scipy`.
I could imagine that somebody looking to do a particular task in Python, like propensity score matching, would do a Google search and stumble upon my package.

Anyone can write a package and upload it to GitHub, PyPi, or R CRAN,
and more and more people are doing it as resources accessible to beginners, like Hadley's [R packages book](r-pkgs.had.co.nz), become available.
This leads to a new problem: we need to sift through packages to decide whether they suit our needs.

I went out to Twitter to find out what people think about when they're deciding whether or not to use a package.

## Documentation

The first thing that I look for in a package is documentation.
Multiple people echoed this.

The most basic level of documentation explains how to use each function, method, and class.
I simply can't use code if I don't know what the inputs and outputs should be.
This is really simple to do with docstrings in Python and with the `roxygen` package in R.

The next level of documentation is providing examples.
Examples demonstrate how to use individual pieces of code together.
They also indicate that the developer tried their code on real (or simulated) data, which is always a promising sign of conscientiousness.
In R, this is typically done with vignettes, documents with code and explanatory narrative interleaved.

The most comprehensive documentation would be a package website.
While not strictly necessary, it enables you to navigate between documentation for different pieces of the package seamlessly.
It adds a touch of professionalism that a Github repository just doesn't have.
I've been using [Sphinx](dphinx-doc.org) to convert my docstrings to a website hosted on Github.

Lack of documentation shows that the package author was hurried and raises concerns that things might not work as they seem.
Which leads to my next point...

## Tests

"Software testing proves the existence of bugs but not their absence."
Unit tests are chunks of code that use the software in various ways to determine if it behaves as expected.
If a package has no unit tests, then we can't have much confidence that there are no bugs.


<div class="center">
<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr">best sign is open source with good tests. Even if I can’t read/understand all code I should understand test suite.</p>&mdash; Jason Becker (@jsonbecker) <a href="https://twitter.com/jsonbecker/status/887838223229210624">July 20, 2017</a></blockquote>
</div>

One measure of how well you've tested your code is coverage -- what percentage of lines are run in your unit tests?
Higher coverage gives more confidence in a package.
It still doesn't mean that the code works; it just means that in those particular test cases, the lines of code that were run behaved as expected.
It's important to run multiple test cases so that the code gets exercised in more than one way.

It's great to have tests, but you actually need to run them.
A surefire way to do this is to set up a continuous integration system:
every time a change is made to the code base, all of the tests are run.
Most often I see people using [Travis CI](travis-ci.org) with Github.
It raises a flag if new contributions don't pass all the tests; that way, you can avoid merging a bad pull request.

You can even put badges for your coverage percentage and Travis build on your Github README.
This is an obvious signal to users that your package is well tested.

The more tests there are, the more confidence we have that the code works.

## Reputation 

The most important signal of a good package seems to be what people say about it -- its reputation.
This is hard to quantify, but it's communicated in a lot of ways:

- Word of mouth: Have you heard about it through Twitter or a blog? Does a colleague use it?
- Examples of use: Have you seen people using it in their research/project/analysis/product?
- Use metrics: Does it have many Github stars? Has it been downloaded much?

Even more elusive is *the author's reputation*.
If people recognize your name and know that you've contributed other useful packages, they're more likely to trust this package.
If you're new to open source, your best bet at building your reputation is to create a personal website featuring your work and to establish a presence on Github by integrating it into your everyday workflow.

<div class="center">
<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr">You can&#39;t really. Basic quality (version, doc), GitHub stars, downloads...<br>Always a gamble (and a security risk)</p>&mdash; Mastodon|Remi Rampin (@remram44) <a href="https://twitter.com/remram44/status/887815041545891840">July 19, 2017</a></blockquote>

<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr">Plus squishier things like whether author seems aware of related packages and literature, author&#39;s reputation and other contributions.</p>&mdash; James E. Pustejovsky (@jepusto) <a href="https://twitter.com/jepusto/status/887830868299042816">July 20, 2017</a></blockquote>

<blockquote class="twitter-tweet" data-conversation="none" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/seankross">@seankross</a> applies the punch in the face test -- if I could find them to punch them in the face, and I know them well enough, I&#39;ll use it</p>&mdash; Elissa Redmiles (@eredmil1) <a href="https://twitter.com/eredmil1/status/887894277497290754">July 20, 2017</a></blockquote>
</div>

## Take-aways

With packages, more is better -- more documentation, more examples, more unit tests, more downloads.

But as important as these things are, people will look at you and your package's online presence to gauge whether they should use it.
We do a similar thing when judging candidates for a position.
We make a first impression based on their appearance, their institutional or company affiliation, and the people in their network.
Academics cultivate a presence in their field by going to conferences, giving seminars, and editing in journals, so their work is more widely recognized;
similarly one needs to cultivate an online presence in the open source community to give their packages credibility.
This seems suboptimal.

As a final note, [Karthik Ram](http://inundata.org/) is working on a paper about this topic, which I'm sure will be more comprehensive than my musings!
