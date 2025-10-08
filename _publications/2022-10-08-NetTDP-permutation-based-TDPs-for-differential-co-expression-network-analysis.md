---
title: "NetTDP: permutation-based TDPs for differential co-expression network analysis"
collection: publications
category: manuscripts
permalink: /publication/2022-10-08-NetTDP-permutation-based-TDPs-for-differential-co-expression-network-analysis
excerpt: #
date: 2022-10-08
venue: 'Briefings in Bioinformatics'
slidesurl: #
paperurl: #
bibtexurl: #
arxivurl: #
journalurl: "https://doi.org/10.1093/bib/bbac417"
citation: 'Menglan Cai, Anna Vesely, Xu Chen, Limin Li, Jelle J. Goeman (2022). NetTDP: permutation-based true discovery proportions for differential co-expression network analysis. <i>Briefings in Bioinformatics</i> 23(6). DOI: 10.1093/bib/bbac417'
---
Existing methods for differential network analysis could only infer whether two networks of interest have differences between two groups of samples, but could not quantify and localize network differences. In this work, a novel method, permutation-based Network True Discovery Proportions (NetTDP), is proposed to quantify the number of edges (correlations) or nodes (genes) for which the co-expression networks are different. In the NetTDP method, we propose an edge-level statistic and a node-level statistic, and detect true discoveries of edges and nodes in the sense of differential co-expression network, respectively, by the permutation-based sumSome method. Furthermore, the NetTDP method could further localize the differences by inferring the TDPs for edge or gene subsets of interest, which can be selected post hoc. Our NetTDP method allows inference on data-driven modules or biology-driven gene sets, and remains valid even when these sub-networks are optimized using the same data. Experimental results on both simulation data sets and five real data sets show the effectiveness of the proposed method in inferring the quantification and localization of differential co-expression networks. The R code is available at https://github.com/LiminLi-xjtu/NetTDP.