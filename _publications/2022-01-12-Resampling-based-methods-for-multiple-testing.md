---
title: "2022-01-12-Resampling-based-methods-for-multiple-testing"
collection: publications
category: thesis
permalink: /publication/2022-01-12-Resampling-based-methods-for-multiple-testing
excerpt: #
date: 2022-01-12
venue: "Department of Statistical Sciences, University of Padua"
slidesurl: #
paperurl: 'http://annavesely.github.io/files/thesis_Anna_Vesely.pdf'
bibtexurl: #
arxivurl: #
journalurl: #
citation: 'Anna Vesely (2022). Resampling-based methods for multiple testing on high-dimensional data <i>PhD thesis, Department of Statistical Sciences, University of Padua</i>. URL: https://www.research.unipd.it/handle/11577/3449435'
---
We consider the problem of testing multiple hypotheses in high-dimensional settings, arguing that more tools are needed to support an exploratory approach, where researchers may test many subsets of hypotheses and make a selection post hoc. We focus on resampling-based methods, that rely on minimal assumptions and tend to be more powerful than parametric approaches, especially in presence of multiple hypotheses. In this framework, we provide two general and flexible procedures: a method to make confidence statements on the proportion of true discoveries (TDP), and a method to make inference on predictor variables in linear regression.

First, we propose a general closed testing procedure for sum-based global tests. It provides lower confidence bounds for the TDP, simultaneously over all subsets of hypotheses; these simultaneous inferences come for free, i.e., without any adjustment of the alpha-level, whenever a global test is used. Our method allows for an exploratory approach, as simultaneity ensures control of the TDP even when the subset of interest is selected post hoc. It adapts to the unknown joint distribution of the data through permutation testing. Any sum test may be employed, depending on the desired power properties. We present an iterative shortcut for the closed testing procedure, based on the branch and bound algorithm, which converges to the full closed testing results, often after few iterations; even if it is stopped early, it controls the TDP. The feasibility of the method for high dimensional data is illustrated on brain imaging data, then we compare the properties of different choices for the sum test through simulations.

Subsequently, we propose a multiple testing method for hypotheses on coefficients in high-dimensional linear regression. It allows to construct asymptotically valid resampling-based tests for any subset of hypotheses, which can be used in closed testing procedures, as well as the above-mentioned shortcut. The approach is presented in two ways: an exact method, and an approximate method that is less computationally intensive. We show that, to build test statistics for any set of hypotheses, it is sufficient to define test statistics for individual hypotheses, relying on a variable selection procedure, and then combine these through a suitable function. The resulting method is extremely flexible, allowing different selection procedures and several combining functions. The performance of the proposed exact and approximate methods is illustrated through simulations.
