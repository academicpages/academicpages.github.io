---
title: 'Analying multiple datasets with a joint likelihood'
date: 2020-07-02
permalink: /posts/2020/07/joint/
tags:
  - notebooks
  - bayesian inference
---

Suppose you have multiple datasets that share one/two or more parameters, you want to combine the data and analyse them together to make the best possible measurement for the parameters shared by the multiple different data sets. A joint likelihood is the natural way to do such an analysis. One massive benefit of such a method is that not only this allows one to do model selection, it also gives a better measurement of the parameters than multiplying the individual posteriors would. This can also help constrain the other non-common parameters too, particularly if the additional data set can break a degeneracy.  In this example, I show how you can use a joint likelihood for a simple system involving two data sets; noisy observations of a linear model. I show how such data can be fit in a joint likelihood with bilby. Specifically, in this example the gradient is a joint parameter while the intercept is unique to each data set.

Jupyter notebook to run through the problem [here](https://github.com/nikhil-sarin/a_simple_joint_likelihood/blob/master/example_notebook.ipynb)
------
