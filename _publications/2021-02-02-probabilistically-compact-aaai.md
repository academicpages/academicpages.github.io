---
title: "Improving adversarial robustness via probabilistically compact loss with logit constraints"
collection: publications
category: conferences
permalink: /publication/2021-02-02-probabilistically-compact-aaai
excerpt: 'This paper proposes a method to improve adversarial robustness using probabilistically compact loss with logit constraints. (Equal contribution)'
date: 2021-02-02
venue: 'Proceedings of the Thirty-Fifth AAAI Conference on Artificial Intelligence (AAAI-21)'
authors: 'Li, X., Li, X., Pan, D., and Zhu, D. (Equal contribution)'
paperurl: 'https://ojs.aaai.org/index.php/AAAI/article/view/17030'
citation: 'Li, X., Li, X., Pan, D. and Zhu, D. (2021). &quot;Improving adversarial robustness via probabilistically compact loss with logit constraints.&quot; <i>The proceedings of Thirty-Five AAAI Conference on Artificial Intelligence (AAAI-21)</i>, virtual conference. (Equal contribution)'
---

This paper proposes a novel method to improve adversarial robustness of neural networks using probabilistically compact loss with logit constraints. Authors contributed equally to this work.

**Abstract:**
Convolutional neural networks (CNNs) have achieved state-of-the-art performance on various tasks in computer vision. However, recent studies demonstrate that these models are vulnerable to carefully crafted adversarial samples and suffer from a significant performance drop when predicting them. Many methods have been proposed to improve adversarial robustness (e.g., adversarial training and new loss functions to learn adversarially robust feature representations). Here we offer a unique insight into the predictive behavior of CNNs that they tend to misclassify adversarial samples into the most probable false classes. This inspires us to propose a new Probabilistically Compact (PC) loss with logit constraints which can be used as a drop-in replacement for cross-entropy (CE) loss to improve CNN's adversarial robustness. Specifically, PC loss enlarges the probability gaps between true class and false classes meanwhile the logit constraints prevent the gaps from being melted by a small perturbation. We extensively compare our method with the state-of-the-art using large scale datasets under both white-box and black-box attacks to demonstrate its effectiveness. The source codes are available at https://github.com/xinli0928/PC-LC.