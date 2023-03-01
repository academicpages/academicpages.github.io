---
title: "Compensation of Model Errors in Electrocardiographic Imaging Using Bayesian Estimation"
collection: publications
permalink: #
excerpt: 'In most studies, Bayesian Maximum A Posteriori (MAP) estimation deals only with the measurement noise and ignores the forward model errors. We incorporated model uncertainty in the MAP formulation to improve the inverse reconstructions of epicardial potentials.'
date: 2021-09-13
venue: 'Computing in Cardiology'
paperurl: 'https://ieeexplore.ieee.org/abstract/document/9662933'
citation: 'F. Aldemir and Y. S. Dogrusoz, "Compensation of Model Errors in Electrocardiographic Imaging Using Bayesian Estimation," 2021 Computing in Cardiology (CinC), Brno, Czech Republic, 2021, pp. 1-4, doi: 10.23919/CinC53138.2021.9662933.'
---

Abstract:

Bayesian Maximum a Posteriori (MAP) estimation has been successfully applied to electrocardiographic imaging (ECGI). However, in most studies, MAP deals only with the measurement noise and ignores the forward model errors. In this study, we incorporated model uncertainty in the MAP formulation to improve the inverse reconstructions. Measured electrograms (EGM) from the University of Utah were used to form training and test datasets. Body surface potential (BSP) measurements were simulated at 30 dB SNR. The inverse problem was solved using MAP estimation. The training dataset was used to define the prior probability function (pdf). Both the measurement noise and model error were assumed to be uncorrelated with the EGMs. Model error was introduced as shift in the heart position and scaling of the heart size. Three model error pdfs were considered: no compensation (model error is assumed as zero in the solution); model error is modeled as independent and identically distributed (IID) and correlated across leads (CORR). For IID and CORR, pdf was estimated based on all geometry disturbances. Results were evaluated using spatial (sCC) and temporal (tCC) correlation coefficients. These results showed that including model errors in the MAP formulation, even in a simple form such as the IID, improved the reconstructions over ignoring them.
