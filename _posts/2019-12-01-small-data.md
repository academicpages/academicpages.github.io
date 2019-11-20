---
title: 'Small Data'
date: 2019-12-01
permalink: /posts/2019/12/small-data/
tags:
  - ?
---

[Work In Progress]
Hello reader, this article is the short version of a [Stanford course](http://web.stanford.edu/~rjohari/teaching/notes/). 
I wrote its after an extensive 

# 1-Small Intro
---

The amount of data we collect is gargantuous (Facebook posts, tweets, medical tests...) and it often arriving faster than we can store and analyze it. 
> "Big" data can't be analyzed on a single machine.
On the contrary, small data can be analyzed and collected on a single machine (even though we now have 64GB of RAM at home).

This article aims at mastering the skills that will help you for "small" data analysis and thus for any data analysis.

# 2-Linear Regression
---

## Summerizing a sample
How can we summerize a sample? We first use simple statistics:
+ Sample mean
+ Sample median (more robust to outliers)
+ Sample standard deviation
All of them can be computed in one shot using pandas:
```python
import pandas as pd

df = pd.read_csv("some_data.csv")
df.describe()
>>>
```

## Modeling relationships
We focus on modelizing relationships between observations. 

+ Let $Y=(Y_1, ..., Y_n)$ be the outcome, or target
+ Let $X$ be the features where rows are $X_i=(X_{i1}, ..., X_{ip})$
Our goal is to find a functional relationship such that
$$Y_i \approx f(X_i)$$
