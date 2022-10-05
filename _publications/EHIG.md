---
title: "Generalizing Bayesian Optimization with Decision-theoretic Entropies"
collection: publications
permalink: /publications/EHIG
venue: "The 36th Conference on Neural Information Processing Systems (NeurIPS 2022)"
date: 2022-9-21
citation: 'Willie Neiswanger*, <b>Lantao Yu</b>* (equal contribution), Shengjia Zhao, Chenlin Meng, Stefano Ermon. <i>The 36th Conference on Neural Information Processing Systems</i>. <b>NeurIPS 2022</b>.'
---
[[PDF]](https://arxiv.org/pdf/2210.01383.pdf)

## Abstract
Bayesian optimization (BO) is a popular method for efficiently inferring optima of an expensive black-box function via a sequence of queries. Existing information-theoretic BO procedures aim to make queries that most reduce the uncertainty about optima, where the uncertainty is captured by Shannon entropy. However, an optimal measure of uncertainty would, ideally, factor in how we intend to use the inferred quantity in some downstream procedure. In this paper, we instead consider a generalization of Shannon entropy from work in statistical decision theory (DeGroot 1962, Rao 1984), which contains a broad class of uncertainty measures parameterized by a problem-specific loss function corresponding to a downstream task. We first show that special cases of this entropy lead to popular acquisition functions used in BO procedures such as knowledge gradient, expected improvement, and entropy search. We then show how alternative choices for the loss yield a flexible family of acquisition functions that can be customized for use in novel optimization settings. Additionally, we develop gradient-based methods to efficiently optimize our proposed family of acquisition functions, and demonstrate strong empirical performance on a diverse set of sequential decision making tasks, including variants of top-k optimization, multi-level set estimation, and sequence search.