---
title: "Random Problems with R"
collection: publications
permalink: /publication/2018-09-18-r-random-sample
excerpt: "Faulty algorithms in R's random sampling functions."
date: 2018-09-18
paperurl: 'https://arxiv.org/abs/1809.06520'
---

*with Philip B. Stark*

R (Version 3.5.1 patched) has two issues with its random sampling function- ality. First, it uses a version of the Mersenne Twister known to have a seed- ing problem, which was corrected by the authors of the Mersenne Twister in 2002. Updated C source code is available at [http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/MT2002/CODES/mt19937ar.c](http://www.math.sci.hiroshima-u.ac.jp/~m-mat/MT/MT2002/CODES/mt19937ar.c). Second, R generates random integers between $1$ and $m$ by multiplying random floats by $m$, taking the floor, and adding $1$ to the result. Well-known quantization effects in this approach result in a non-uniform distribution on ${1, \ldots, m}$. The difference, which depends on $m$, can be substantial. Because the sample function in R relies on generating random integers, random sampling in R is biased. There is an easy fix: construct random integers directly from random bits, rather than multiplying a random float by m. That is the strategy taken in Python’s `numpy.random.randint()` function, and recommended by the authors of the Mersenne Twister algorithm, among others. Example source code in Python is available at [https://github.com/statlab/cryptorandom/blob/master/cryptorandom/cryptorandom.py](https://github.com/statlab/cryptorandom/blob/master/cryptorandom/cryptorandom.py) (see functions `getrandbits()` and `randbelow_from_randbits()`).
