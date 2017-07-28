---
title: 'Which logistic regression method in Python should I use?'
date: 2017-07-28
permalink: /posts/2017/07/logistic-regression-python/
tags:
  - Python
  - logistic regression
  - statistics
---

This question is related to my last blog post about [what people consider when choosing which Python package to use.](https://kellieotto.github.io/posts/2017/07/vetting-os/)
Say I want to use some statistical method.
I have a few options.
I could code it up from scratch myself, knowing that this might have undetected bugs and be pretty slow.
I could Google what I'm looking for and use the first thing I find; similarly, there are no guarantees.
Or, I could do my research, find all the packages that seem to offer what I'm looking for, and decide which looks best based on [how thoroughly they've documented and tested their code.](https://kellieotto.github.io/posts/2017/07/vetting-os/)

But I ran up against a problem: there are multiple ways to do logistic regression in Python that seem equally good.
I dig into a more in-depth comparison of the methods here.

# Logistic regression

We perform logistic regression when we believe there is a relationship between continuous covariates X and binary outcomes Y.
We assume that outcomes come from a distribution parameterized by B, and E(Y | X) = g^{-1}(X'B) for a link function g.

For logistic regression, the link function is g(p)= log(p/1-p).
X'B represents the log-odds that Y=1, and applying g^{-1} maps it to a probability.
We do logistic regression to estimate B.

Assuming that the model is correct, we can interpret the estimated coefficients as statistically significant or insignificant.
(I highly discourage this; I tend to believe that the model is a useful approximation to the true data-generating process.)
Otherwise, we can simply use logistic regression to predict Y given X or find the predicted probabilities that Y=1 given X.
For my purposes, I'm trying to estimate in-sample probabilities given Y and X; I'm not worried about inference on the coefficients or overfitting.

## Generalized linear models in `statsmodels`

`statsmodels` is a package that implements a variety of regression methods.
It seems like their main goal is to do inference on the estimated parameters.

The model B is estimated using the magic of one-parameter exponential families. 
There are nice formulas for the mean, variance, score function, etc for data from these distributions. 
They fit by maximum likelihood; by default, it is done using iteratively reweighted least squares.

The output of this model includes all kinds of metrics based on the likelihood. To use these measures, you must believe the distributional assumptions, namely that the data truly follow the relationship you're estimating.
That said, `statsmodels` offers a convenient `summary` method that prints out the estimated coefficients, standard errors, etc. in a table.

## Discrete choice models in `statsmodels`

`statsmodels` offers a second way to do logistic regression.
Confusing, right?
This one is part of its Discrete choice models module.
It also uses maximum likelihood to fit, but uses more general optimization methods.
The user can choose from among many common optimization methods, but the default is Newton-Raphson (which, it turns out, is equivalent to iteratively reweighted least squares for logistic regression).

The output of this method is similar to the GLM, but includes some methods specific to discrete models. 
This could be useful when we're doing prediction -- sometimes we want binary predictions (rather than probabilities), ROC curves and confusion matrices, etc.


## Scikit-learn

At first glance, I might actually learn towards using the `scikit-learn` logistic regression. 
In my experience, the package has more credibility and is more widely used than `statsmodels`. 
However, it looks like the way they frame the problem, and consequently the API, is tailored to a slightly different problem from what I'm doing.

Remember, I want to do regression. 
They frame logistic regression as a *two-class decision rule* with optional L1 or L2 penalization. 
When penalization is introduced to a method, the fitting procedure often has to rely more on optimization than distribution-related formulas. 
The solvers provided in `scikit-learn` don't include IRLS and the documentation talks a lot about penalization.

I wanted to know if I can use this function if I *don't* want to regularize?
Turns out, you can't get rid of the penalty term in the loss function. 
Instead, [you can set C=1e10](https://datascience.stackexchange.com/a/10807) or another large value to make the penalty term small.

The outputs returned look similar to those from `statsmodels`, but there's no clean `summary` method to print the estimated coefficients and model fit statistics.

# Speed comparison

I'm interested in performance, so I did a small simulation to compare the speed of these three methods.
I generated 10,000 observations with 100 independent, standard normal covariates X and an independent standard normal error e.
I set B = [0.01, 0.02, ..., 1] and set the log-odds for individual i to
B'X_i + e_i.
Then, the ith outcome is Y_i = 1 if the log-odds is at least 0.
I used `%timeit` to run the three methods on this fake data.

```python
import sklearn
import statsmodels.api as sm
import numpy as np

def gen_data():
	X = np.random.normal(size=(10000, 100))
	beta = (np.array(range(100))+1)/100
	logodds = np.dot(X, beta) + np.random.normal(size=(10000,))
	Y = np.array(logodds >= 0, dtype=int)
	return (Y, X)
	
def fit_sm_glm(Y, X):
	X = sm.add_constant(X)
	glm_mod = sm.GLM(Y, X, family=sm.families.Binomial())
	glm_res = glm_mod.fit()
	
def fit_sm_logit(Y, X):
	X = sm.add_constant(X)
	logit_mod = sm.Logit(Y, X)
	logit_res = logit_mod.fit(disp=False)
	
def fit_sklearn(Y, X):
	sk_model = sklearn.linear_model.LogisticRegression(C=1e10)
	sk_res = sk_model.fit(X, Y)
	
def test_speed(fit_function):
	(Y, X) = gen_data()
	fit_function(Y, X)
		
%timeit test_speed(fit_sm_glm)
%timeit test_speed(fit_sm_logit)
%timeit test_speed(fit_sklearn)

> 1 loop, best of 3: 1.85 s per loop
> 1 loop, best of 3: 371 ms per loop
> 1 loop, best of 3: 219 ms per loop
```
`statsmodels` GLM is the slowest by far!
The `statsmodels` logit method and `scikit-learn` method are comparable.

# Take-aways

For my purposes, it looks the `statsmodels` discrete choice model logit is the way to go.
It's significantly faster than the GLM method, presumably because it's using an optimizer directly rather than iteratively reweighted least squares.
I'm not doing prediction and am not worried about overfitting, so the fact that I can't disable the regularization in `scikit-learn` is undesirable.
However, it's the fastest of the three methods.

I'd love to know if you've done a similar comparison -- did you actually test out the different packages or did you just choose one and run with it?