---
title: "Explaining Deep Neural Network Models with Adversarial Gradient Integration"
collection: publications
category: conferences
permalink: /publication/2021-08-01-adversarial-gradient-ijcai
excerpt: 'This paper proposes a method for explaining deep neural networks using adversarial gradient integration.'
date: 2021-08-01
venue: 'Proceedings of the 30th International Joint Conference on Artificial Intelligence (IJCAI-21)'
authors: 'Pan, D., Li, X., and Zhu, D.'
paperurl: 'https://www.ijcai.org/proceedings/2021/0396.pdf'
citation: 'Pan, D., Li, X and Zhu, D. (2021). &quot;Explaining Deep Neural Network Models with Adversarial Gradient Integration.&quot; <i>The proceedings of 30th International Joint Conference on Artificial Intelligence (IJCAI-21)</i>, Montreal, Canada.'
---

**Abstract:**
Deep neural networks (DNNs) have became one of the most high performing tools in a broad rangeof machine learning areas. However, the multilayer non-linearity of the network architectures preventus from gaining a better understanding of the models' predictions. Gradient based attributionmethods (e.g., Integrated Gradient (IG)) that decipher input features' contribution to the predictiontask have been shown to be highly effective yet requiring a reference input as the anchor for explainingmodel's output. The performance of DNN model interpretation can be quite inconsistent withregard to the choice of references. Here we propose an Adversarial Gradient Integration (AGI) methodthat integrates the gradients from adversarial examples to the target example along the curve of steepestascent to calculate the resulting contributions from all input features. Our method doesn't rely onthe choice of references, hence can avoid the ambiguity and inconsistency sourced from the referenceselection. We demonstrate the performance of our AGI method and compare with competing methodsin explaining image classification results. Code is available at [GitHub](https://github.com/pd90506/AGI).


