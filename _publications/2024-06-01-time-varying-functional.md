---
title: "Time-varying functional connectivity as Wishart processes"
collection: publications
category: manuscripts
permalink: /publication/2024-06-01-time-varying-functional
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2024-06-01
venue: 'Imaging Neuroscience'
slidesurl: 'http://academicpages.github.io/files/slides1.pdf'
paperurl: 'http://academicpages.github.io/files/paper1.pdf'
bibtexurl: 'http://academicpages.github.io/files/bibtex1.bib'
citation: 'Kampman et al. (2024). &quot;Time-varying functional connectivity as Wishart processes.&quot; <i>Journal 1</i>. 1(1).'
---
The contents above will be part of a list of publications, if the user clicks the link for the publication than the contents of section will be rendered as a full page, allowing you to provide more information about the paper for the reader. When publications are displayed as a single page, the contents of the above "citation" field will automatically be included below this section in a smaller font.

We investigate the utility of Wishart processes (WPs) for estimating time-varying functional connectivity (TVFC), which is a measure of changes in functional coupling as the correlation between brain region activity in functional magnetic resonance imaging (fMRI).
The WP is a stochastic process on covariance matrices that can model dynamic covariances between time series, which makes it a natural fit to this task.
Recent advances in scalable approximate inference techniques and the availability of robust open-source libraries have rendered the WP practically viable for fMRI applications.
We introduce a comprehensive benchmarking framework to assess WP performance compared with a selection of established TVFC estimation methods.
The framework comprises simulations with specified ground-truth covariance structures, a subject phenotype prediction task, a test-retest study, a brain state analysis, an external stimulus prediction task, and a novel data-driven imputation benchmark.
The WP performed competitively across all the benchmarks.
It outperformed a sliding window (SW) approach with adaptive cross-validated window lengths and a dynamic conditional correlation (DCC)-multivariate generalized autoregressive conditional heteroskedasticity (MGARCH) baseline on the external stimulus prediction task, while being less prone to false positives in the TVFC null models.
