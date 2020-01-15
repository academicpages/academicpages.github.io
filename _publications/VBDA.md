---
title: "Variational Bottleneck Domain Adaptation"
collection: publications
permalink: /publications/VBDA
venue: "The 24th European Conference on Artificial Intelligence (ECAI 2020)"
date: 2019-11-20
citation: 'Yuxuan Song, <b>Lantao Yu</b>, Zhangjie Cao, Zhiming Zhou, Jian Shen, Shuo Shao, Weinan Zhang, Yong Yu. <b>ECAI 2020.</b>'
---

[[PDF]](https://arxiv.org/pdf/1911.09310.pdf)

## Abstract
Domain adaptation aims to leverage the supervision signal of source domain to obtain an accurate model for target domain, where the labels are not available. To leverage and adapt the label information from source domain, most existing methods employ a feature extracting function and match the marginal distributions of source and target domains in a shared feature space. In this paper, from the perspective of information theory, we show that representation matching is actually an insufficient constraint on the feature space for obtaining a model with good generalization performance in target domain. We then propose variational bottleneck domain adaptation (VBDA), a new domain adaptation method which improves feature transferability by explicitly enforcing the feature extractor to ignore the task-irrelevant factors and focus on the information that is essential to the task of interest for both source and target domains. Extensive experimental results demonstrate that VBDA significantly outperforms state-of-the-art methods across three domain adaptation benchmark datasets.