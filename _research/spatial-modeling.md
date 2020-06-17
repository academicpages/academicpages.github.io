---
title: "Spatial Modeling"
layout: single-portfolio
excerpt: "Models for spatially correlated data<br/><img src='/images/research/gp-bma.png' width='500' height='500'>"
collection: research
order_number: 50
author_profile: true
---

In this set of projects, I present methodological advances for the study of spatial data in political science. These type of data are common across all substantive areas of political science and include topics such as regulatory regimes in neighboring states, terrorist attacks within provinces, and public opinion across congressional districts. Within political science, these data are commonly analyzed using models from spatial econometrics. In this set of projects, I present an alternative model commonly used in other disciplines and address the problem of specifying spatial dependence structures.

### Working Papers

Rob Williams. "Gaussian Process Models for Spatial Data."

> Gaussian process models are a class of models for spatial data that are common in environmental sciences and public health, but less well known in political science. They offer many benefits over the more commonly used family of spatial econometric autoregressive models for the types of data that political scientists frequently encounter. I demonstrate these advantages by conducting Monte Carlo simulations comparing Gaussian process models to simultaneous and conditional autoregressive models. I also show that in certain cases, the two classes of models yield substantively different results, echoing findings from other disciplines.

Rob Williams. "Addressing Uncertainty in the Choice of Covariance Function in Gaussian Process Modeling with Bayesian Model Averaging." Presented at the Annual Meeting of the Society for Political Methodology, Provo, UT, July 2018. [[Poster]](/files/pdf/research/PolMeth 2018 Poster.pdf)

> While Gaussian process and spatial econometric models control for spatial dependence, they both require researchers to specify certain parameters *a priori*. The true covariance function or adjacency structure is unknown to the researcher, and so there is always some amount of uncertainty in their choice. Using model fit statistics to select the dependence structure with the best fit is insufficient as the actual data generating process may not match a specific dependence structure. I propose using Bayesian model averaging to combine estimates from multiple models, each using a likely dependence structure. Monte Carlo simulations show that Bayesian model averaging correctly identifies the covariance structure used to generate simulated data and corrects for the inclusion of misspecified models, but at the cost of a loss of efficiency.

