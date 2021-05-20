---
title: "How do Online Learning to Rank Methods Adapt to Changes of Intent?"
collection: publications
permalink: /publication/SIGIR2021Intent
year: 2021
venue: 'Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR)'
authors: Shengyao Zhuang, Guido Zuccon
track: Full paper
---
---

## Abstract
Online learning to rank (OLTR) uses interaction data, such as clicks, to dynamically update rankers. OLTR has been thought to capture user intent change overtime – a task that is impossible for rankers trained on statistic datasets such as in offline and counterfactual learning to rank. However, this feature has never been demonstrated and empirically studied, as previous work only considered simulated online data with a single user intent, or real online data with no explicit notion of intents and how they change over interactions. In this paper, we address this gap by study the capability of OLTR algorithms to adapt to user intent change.

Our empirical experiments show that the adaptation to intent change does vary across OLTR methods, and is also dependent on the amount of noise in the implicit feedback signal. This is an important result, as it highlights that intent change adaptation should be studied alongside online and offline performance.

Investigating how OLTR algorithms adapt to intent change is challenging as current LTR datasets do not explicitly contain the required intent data. Along with the main findings reported in this paper related to intent change, we also contribute a methodology to investigate this aspect of OLTR methods. Specifically, we create a collection for OLTR with explicit intent change by adapting an existing TREC collection to this task. We further introduce methods to model and simulate click behaviour related to intent change. We further propose novel evaluation metrics tailored to study different aspects of how OLTR methods adapt to intent change.

[Download paper here](http://arvinzhuang.github.io/files/arvin2021intentchange.pdf)

[Code](https://github.com/ielab/OLTR-intent-change)

