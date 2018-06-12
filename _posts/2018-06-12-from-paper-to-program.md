---
title: 'From Paper to Program: Challenges of Implementing Permutation Tests'
date: 2018-06-12
permalink: /posts/2018/06/from-paper-to-program/
tags:
  - hypothesis testing
  - statistics
  - simulation
  - sampling
  - p-values
---

I gave a talk about a short book I'm writing at [the 4th Conference of the  International Society of Nonparametric Statistics](http://www.isnps2018.it). [Please check out my slides!](https://kellieotto.github.io/files/2018-06-12-isnps.pdf)

As the field of data science grows and computational resources abound, it is increasingly common for people to analyze their data using permutation tests. Introductory statistics textbooks often teach parametric statistics exclusively; when they do teach permutation tests, they are often portrayed as being model-free. In fact, permutation tests do require assumptions, and this approach to teaching omits crucial considerations. Without appropriate pedagogical material about issues of implementation, people are more likely to misuse permutation tests. To fill this gap, we are developing a short open access textbook. Topics from the book include: how controlling for covariates can improve statistical power, illustrated using clinical trial data with multiple time points and study sites; how to design a permutation test for a complex experiment, illustrated with a study to assess gender bias in teaching evaluations; and computational limitations of sampling algorithms and pseudorandom number generators for big data. These examples are written in accessible language, shown using real-world data, and accompanied by R and Python code. Our materials should supplement, not replace, instruction of permutation test theory, and will enable intermediate statistics students, data scientists, and domain researchers to design the best nonparametric tests for their observational or experimental studies.
