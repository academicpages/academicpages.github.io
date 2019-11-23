---
title: 'Small Data'
date: 2019-12-01
permalink: /posts/2019/12/small-data/
tags:
  - ?
---

[Work In Progress]

# Small Intro
---

Hello reader, this article is the short version of a [Stanford course](http://web.stanford.edu/~rjohari/teaching/notes/). 
I wrote it after an extensive reading of this course so that you don't have to.

The amount of data we collect is gargantuous (Facebook posts, tweets, medical tests...) and it often arriving faster than we can store and analyze it. 
> "Big" data can't be analyzed on a single machine.
On the contrary, small data can be analyzed and collected on a single machine (even though we now have 64GB of RAM at home).

This article aims at mastering the skills that will help you for "small" data analysis and thus for any data analysis.

<br>
# 1 Linear Regression
---

Let's focus on data from [child.iq](http://www.stat.columbia.edu/~gelman/arm/examples/child.iq/).

## 1-1 Summerizing a sample
How can we summerize a sample? We first use simple statistics:
+ Sample mean
+ Sample median (more robust to outliers)
+ Sample standard deviation

All of them can be computed in one shot using pandas:
<script src="https://gist.github.com/Vincent-Maladiere/92c2cf07035962f50e23a72b57299208.js"></script>

## 1-2 Modeling relationships
We focus on modelizing relationships between observations. 

+ Let $Y=(Y_1, ..., Y_n)$ be the outcome, or target.
+ Let $X$ be the features where rows are $X_i=(X_{i1}, ..., X_{ip})$.

Our goal is to find a functional relationship such that

$$Y_i \approx f(X_i)$$

To answer the question *how is* `kid_score` *related to the other variables?*

<script src="https://gist.github.com/Vincent-Maladiere/a5bfd0162e30fca9596d89b1a4b3e2d8.js"></script>

We have:
+ continuous variables: `kid_score` and `mom_iq` (they can be constrained, as `mom_iq` can't be negative)
+ categorical variables: `mom_hs` is $0$ if the mother did attend high school, o.w. 1. `mom_work` range from $1$ to $4$
  + $1=$ did not work in the first 3 years of child's life
  + $2=$ worked in 2nd or 3d year
  + $3=$ worked part-time in first year
  + $4=$ worked full-time in first year

We also use model for:
+ Associations and correlations
+ Predictions
+ Causal relationships

## 1-3 Linear regression model

We first focus on modeling linear relationship between outcomes and covariates.
We look for coefficients 

$$\hat{\beta} = [\hat{\beta}_0, ..., \hat{\beta}_p]^T$$ 

such that

$$Y_i \approx \hat{\beta}_0 + \hat{\beta}_1 X_{i1} + ... + \hat{\beta}_p X_{ip} = X_i \hat{\beta}$$

A picture of our $Y$, $X$ and $\hat{\beta}$:
<script src="https://gist.github.com/Vincent-Maladiere/20d422af2c70e8e8598e31986f249711.js"></script>

Let's build a simple regression model of `kid_score` against `mom_iq`.
<script src="https://gist.github.com/Vincent-Maladiere/62e8ed53b3407f53f5ac28d2ac36f1d4.js"></script>

That is to say, `kid_score = mom_iq x 0.61 + 25.8`.
Let's plot our model

<script src="https://gist.github.com/Vincent-Maladiere/afb6f817f3d671558621d9c0f94af28f.js"></script>

<br>
So, how to choose $\hat{\beta}$?
We focus on *ordinary least square* (OLS).
We choose $\hat{\beta}$ so that

$$SSE=sum\;of\;squared\;errors=\sum^n_{i=1}(Y_i-\hat{Y}_i)^2=\|Y-X\hat{\beta}\|^2$$

is minimized, where

$$\hat{Y_i}=X_i\hat{\beta}=\hat{\beta}_0+\sum^p_{j=1}\hat{\beta}_j X_{ij}$$

is the *fitted* value of the $i$'th observation.

+ Is the resulting model a good fit?
+ Does it make sense to use a linear model?
+ Is minimizing SSE the right objective?

We start down this road by working through the algebra of *linear regression*.

## 1-4 Ordinary least squares: Solution

The vector $\hat{\beta}$ that minimizes SSE is given by

$$\hat{\beta}=(X^TX)^{-1}X^TY$$

<details>
<summary>The key here is that $X^TX$ is invertible, whereas $X$ may not be.</summary>
$$X^TXq=0 \implies q^TX^TXq=0 \implies (Xq)^TXq=0 \implies \|Xq\|^2=0 \implies Xq=0$$
So $q = 0$ and thus the null space of $X^TX = \{0\}$.
Since $X^TX$ is a square matrix, this means that $X^TX$ is invertible.

<br>
_______________________________________________________________________________________
<br><br>
</details>

<details>
<summary>We also need to proove that $\hat{\beta}$ is the only solution.</summary>
<br>
We proove that 
$$X^T\hat{r}=0 \implies \hat{\beta} = argmin_{\beta}\|Y-\beta X|$$ where $\hat{r}=Y-X\hat{\beta}$ is the vector of residual.
That is to say: the residual vector from $\hat{\beta}$ is orthogonal to every column of X.

Let's consider any vector $\gamma$, we have
$$Y-X\gamma = \hat{r}+X(\hat{\beta}-\gamma)$$
Since $\hat{r}$ is orthogonal to $X$, we get
$$\|Y-X\gamma\|^2=\|\hat{r}\|^2+\|X(\hat{\beta}-\gamma)\|^2$$
this is minimized when $X(\hat{\beta}-\gamma)=0$ and since $X$ has rank $p+1$, 
the unique solution is $\gamma=\hat{\beta}$

<br>
_______________________________________________________________________________________
<br>
</details>


## 1-5 Residuals and $R^2$

<details>
<summary>We show why $R^2=\frac{\sum^n_{i=1}(\hat{Y}_i-\hat{\bar{Y}})^2}{\sum^n_{i=1}(Y_i-\bar{Y})^2}$</summary>
<br>
Let $\hat{r}=Y-\hat{Y}=Y-X\hat{\beta}$ be the vector of residuals.
We know that $\hat{r}$ is orthogonal to every column of $X$ (in particular to 1st column of $X$).
This means that the sum of residuals is $0$, thus
$$\sum^n_{i=1}\hat{r}_i=\sum^n_{i=1}(Y_i-\hat{Y}_i)=0 \implies \bar{Y}=\hat{\bar{Y}}$$

Since $\hat{r}$ is orthogonal to every column of $X$, we use the Pythagorean theorem to get:
$$\|Y\|^2=\|\hat{r}\|^2+\|\hat{Y}\|^2$$
using equality of sample means we get:
$$\|Y\|^2-n\bar{Y}^2=\|\hat{r}\|^2+\|\hat{r}\|^2-n\hat{\bar{Y}}^2$$
hence
$$R^2=\frac{\sum^n_{i=1}(\hat{Y}_i-\hat{\bar{Y}})^2}{\sum^n_{i=1}(Y_i-\bar{Y})^2}$$

_______________________________________________________________________________________
</details>
<br>

Note that both nominator and denominator are sample variance of $Y$ and $\hat{Y}$, so when $R^2$ is large, much of the outcome sample variance is "explained" by the fitted value, with $0 \leq R^2 \leq 1$. 

<script src="https://gist.github.com/Vincent-Maladiere/b3bd0d25d76896892fa681f9dd73057f.js"></script>

Let's plot the residuals for our model against fitted values $\hat{Y}_i$ (not the original outcomes $Y_i$)

![residuals against fitted values](https://vincent-maladiere.github.io/images/residuals_vs_fitted.png)

<details>
<br>
<summary>Hat tip to [Emre Can](https://emredjan.github.io/blog/2017/07/11/emulating-r-plots-in-python/) for his very neat implementation and overview of plotting techniques..</summary>
<script src="https://gist.github.com/Vincent-Maladiere/6fb9b7c2ae87822ddc68ca12125aa421.js"></script>
_______________________________________________________________________________________
</details>
<br>

