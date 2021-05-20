---
title: "Counterfactual Online Learning to Rank"
collection: publications
permalink: /publication/ECIR2020COLTR
excerpt: 
year: 2020
venue: '42nd European Conference on IR Research (ECIR)）'
paperurl: 'http://academicpages.github.io/files/paper1.pdf'
authors: Shengyao Zhuang, Guido Zuccon
citation:
---

Exploiting users’ implicit feedback, such as clicks, to learn rankers is attractive as it does not require editorial labelling effort, and adapts to users’ changing preferences, among other benefits. However, directly learning a ranker from implicit data is challenging, as users’ implicit feedback usually contains bias (e.g., position bias, selection bias) and noise (e.g., clicking on irrelevant but attractive snippets, adversarial clicks). Two main methods have arisen for optimizing rankers based on implicit feedback: counterfactual learning to rank (CLTR), which learns a ranker from the historical click-through data collected from a deployed, logging ranker; and online learning to rank (OLTR), where a ranker is updated by recording user interaction with a result list produced by multiple rankers (usually via interleaving).

In this paper, we propose a counterfactual online learning to rank algorithm (COLTR) that combines the key components of both CLTR and OLTR. It does so by replacing the online evaluation required by traditional OLTR methods with the counterfactual evaluation common in CLTR. Compared to traditional OLTR approaches based on interleaving, COLTR can evaluate a large number of candidate rankers in a more efficient manner. Our empirical results show that COLTR significantly outperforms traditional OLTR methods. Furthermore, COLTR can reach the same effectiveness of the current state-of-the-art, under noisy click settings, and has room for future extensions.
