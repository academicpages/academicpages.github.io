---
title: 'Analying multiple datasets with a joint likelihood'
date: 2020-07-3
permalink: /posts/2020/07/joint/
tags:
  - notebooks
  - bayesian inference
---

Suppose you have multiple datasets that share one or two parameters, you want to combine the data and analyse them together to make the best possible measurement for the parameters shared by the two different data sets. A joint likelihood is the natural way to do this analysis. This gives a better constraint on the joint parameter and can actually help constrain the other parameters too, particularly if the other data set can break a degeneracy.  In this example, I show how you can use a joint likelihood for a simple example involving two data sets, noisy observations of a line can be fit in a joint likelihood. In this example, the gradient is a joint parameter while the intercept is unique to each data set.

Jupyter notebook to run through the problem [here](https://github.com/nikhil-sarin/a_simple_joint_likelihood/blob/master/example_notebook.ipynb)
------
