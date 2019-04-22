---
title: "Multi-Agent Adversarial Inverse Reinforcement Learning"
collection: publications
permalink: /publications/MAAIRL
venue: "The 36th International Conference on Machine Learning (ICML-19)"
date: 2018-4-12
citation: '<b>Lantao Yu</b>, Jiaming Song, Stefano Ermon. The 36th International Conference on Machine Learning. <i>The 36th International Conference on Machine Learning</i>. <b>ICML 2019</b>.'
---



## Abstract
Domain adaptation aims to leverage the supervision signal of source domain to obtain an accurate model for target domain, where the labels are not available. To leverage and adapt the label information from source domain, most existing methods employ a feature extracting function and match the marginal distributions of source and target domains in a shared feature space. In this paper, from the perspective of information theory, we show that representation matching is actually an \textit{insufficient} constraint on the feature space for obtaining a model with good generalization performance in target domain. We then propose variational bottleneck domain adaptation (VBDA), a new domain adaptation method which improves feature transferability by explicitly enforcing the feature extractor to ignore the irrelevant factors and focus on the information that is essential to the task of interest for both source and target domains. Extensive experimental results demonstrate that VBDA significantly outperforms state-of-the-art methods across three domain adaptation benchmark datasets.