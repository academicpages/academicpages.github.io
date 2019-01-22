---
title: 'Random Problems with R'
date: 2019-01-22
permalink: /posts/2019/01/random-problems-with-r/
tags:
  - hypothesis testing
  - statistics
  - simulation
  - sampling
  - p-values
---

I gave a lightning talk at the SF R Ladies meet-up about a problem with R's sampling algorithm. [Check out my slides here!](https://kellieotto.github.io/files/2019-01-22-sampling.pdf)

As part of my dissertation, I dug into the pseudo-random number generators and sampling algorithms used by common statistical packages. Along the way, I found an issue with the way R generates pseudo-random integers using the `sample()` function. I'll give an example where we'd like to generate integers uniformly on an interval, but sample produces 2x as many odd numbers as even ones. [Our short paper on the problem is on arXiv.](https://arxiv.org/pdf/1809.06520v1.pdf)