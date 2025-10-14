---
title: "Learning Compact Features via In-Training Representation Alignment"
collection: publications
category: conferences
permalink: /publication/2023-02-01-learning-compact-aaai
excerpt: 'This paper presents a method for learning compact features through in-training representation alignment.'
date: 2023-02-01
venue: 'Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence (AAAI-23)'
authors: 'Li, X., Li, X., Pan, D., Qiang, Y., and Zhu, D.'
paperurl: 'https://ojs.aaai.org/index.php/AAAI/article/view/26044'
citation: 'Li, X., Li, X., Pan, D., Qiang, Y., Zhu, D. (2023). &quot;Learning Compact Features via In-Training Representation Alignment.&quot; <i>In the Proceedings of Thirty-Seventh AAAI Conference on Artificial Intelligence (AAAI-23)</i>.'
---

**Abstract:**
Deep neural networks (DNNs) for supervised learning can be viewed as a pipeline of the feature extractor (i.e., last hidden layer) and a linear classifier (i.e., output layer) that are trained jointly with stochastic gradient descent (SGD) on the loss function (e.g., cross-entropy). In each epoch, the true gradient of the loss function is estimated using a mini-batch sampled from the training set and model parameters are then updated with the mini-batch gradients. Although the latter provides an unbiased estimation of the former, they are subject to substantial variances derived from the size and number of sampled mini-batches, leading to noisy and jumpy updates. To stabilize such undesirable variance in estimating the true gradients, we propose In-Training Representation Alignment (ITRA) that explicitly aligns feature distributions of two different mini-batches with a matching loss in the SGD training process. We also provide a rigorous analysis of the desirable effects of the matching loss on feature representation learning: (1) extracting compact feature representation; (2) reducing over-adaption on mini-batches via an adaptively weighting mechanism; and (3) accommodating to multi-modalities. Finally, we conduct large-scale experiments on both image and text classifications to demonstrate its superior performance to the strong baselines.
