---
title: 'An Introduction to Analysis of Variance (ANOVA)'
date: 2022-08-03
permalink: /posts/2022/08/what-is-anova/
tags:
  - statistics
  - analysis of variance
  - categorical variables
---

This post gives a brief introduction to the basics of analysis of variance and how it works. A discussion of sums of squares is provided in addition to an overview of the oneway analysis of variance model.

# What is Analysis of Variance (ANOVA)?

Analysis of variance (ANOVA) is a popular statistical method developed
by Ronald Fisher. ANOVA was initially used by Fisher to understand
variability in crop yield, but its applications are not limited to crop
science. In fact, ANOVA is easily applied to data from any field
provided certain assumptions (discussed below) are satisfied.

Generally speaking, ANOVA is used to determine if there are meaningful
differences in the means means of a response variable across various
“treatment” groups. At its core, ANOVA is done by determining if the
variability among various groups unlikely to occur solely because of
random chance.

## What are Sums of Squares?

ANOVA works by determining if variability in the response variable $y$ is due to significant differences between treatment groups or random chance. We can measure variability in the response variable by computing the *sum of squares*. Simply put, the *sum of squares* is a measure of distance between each observed response $y_{ij}$ and the overall mean of all observations $\bar{\bar{y}}$.

Consider the overall (total) sum of squares $\textrm{SST} = \sum_{i=1}^{k}\sum_{j=1}^{n_i}(y_{ij}-\bar{\bar{y}})^2.$

It can be shown that the total sum of squares (SST) can be partitioned
as follows:

$$
\textrm{SST} = \sum_{i=1}^{k}\sum_{j=1}^{n_i}(y_{ij}-\bar{\bar{y}})^2 = \sum_{i=1}^{k}n_i(\bar{y}_{i.}-\bar{\bar{y}})^2 + \sum_{i=1}^{k}\sum_{j=1}^{n_i}(y_{ij}-\bar{y}_{i.})^2,
$$

where we define the sums of squares on the right side of the equality as
the sum of squares between groups (SSB), and sum of squares within
groups (SSW), respectively. Specifically, we have

$$
\textrm{SSB} = \sum_{i=1}^{k}n_i(\bar{y}_{i.}-\bar{\bar{y}})^2 \quad \textrm{and} \quad \textrm{SSW} = \sum_{i=1}^{n}(y_{ij}-\bar{y}_{i.})^2,
$$

where $\bar{y}_{i.}$ denotes the mean of the response variable ($y$) for all observations corresponding to group $i$.

So, we have $\textrm{SST} = \textrm{SSB} + \textrm{SSW}$.

Each of the partitioned sums of squares can be viewed in the following way:

* SST measures the total variability from each individual response to the overall mean of the responses (across all groups).
* SSB is a measure of variability in the average response from group to group ("between" groups).
* SSW is a measure of the variability for each response within its respective group (variability left over after adjusting for group).
