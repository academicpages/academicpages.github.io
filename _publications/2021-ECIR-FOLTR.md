---
title: "Federated Online Learning to Rank with Evolution Strategies: A Reproducibility Study"
collection: publications
permalink: /publication/ECIR2021FOLTR
year: 2021
venue: 'Proceedings of the 43rd European Conference on Information Retrieval (ECIR)'
authors: Shuyi Wang, Shengyao Zhuang, Guido Zuccon
track: Reproducibility paper
---
---

## Abstract
Online Learning to Rank (OLTR) optimizes ranking models using implicit users’ feedback, such as clicks, directly manipulating search engine results in production. This process requires OLTR methods to collect user queries and clicks; current methods are not suited to situations in which users want to maintain their privacy, i.e. not sharing data, queries and clicks.

Recently, the federated OLTR with evolution strategies (FOLtR-ES) method has been proposed to provide a solution that can meet a number of users’ privacy requirements. Specifically, this method exploits the federated learning framework and $\epsilon$-local differential privacy. However, the original research study that introduced this method only evaluated it on a small Learning to Rank (LTR) dataset and with no conformity with respect to current OLTR evaluation practice. It further did not explore specific parameters of the method, such as the number of clients involved in the federated learning process, and did not compare FOLtR-ES with the current state-of-the-art OLTR method. This paper aims to remedy to this gap.

Our findings question whether FOLtR-ES is a mature method that can be considered in practice: its effectiveness largely varies across datasets, click types, ranker types and settings. Its performance is also far from that of current state-of-the-art OLTR, questioning whether the maintained of privacy guaranteed by FOLtR-ES is not achieved by seriously undermining search effectiveness and user experience.


[Download paper here](wang2021foltr-reproducibility.pdf)

[Code](https://github.com/ielab/foltr)

