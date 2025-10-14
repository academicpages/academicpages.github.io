---
title: "On the Learning Property of Logistic and Softmax Losses for Deep Neural Networks"
collection: publications
category: conferences
permalink: /publication/2020-02-01-learning-behavior-aaai
excerpt: 'This paper analyzes the learning behavior of logistic and softmax losses in deep neural networks.'
date: 2020-02-01
venue: 'Proceedings of the Thirty-Fourth AAAI Conference on Artificial Intelligence (AAAI-20)'
authors: 'Li, X., Li, X., Pan, D., and Zhu, D.'
paperurl: 'https://ojs.aaai.org/index.php/AAAI/article/view/5907'
citation: 'Li, X, Li, X, Pan, D. and Zhu, D (2020). &quot;On the learning property of logistic and softmax losses for deep neural networks.&quot; <i>Thirty-Fourth AAAI Conference on Artificial Intelligence (AAAI-20)</i>, New York, USA.'
---

**Abstract:**
Deep convolutional neural networks (CNNs) trained with logistic and softmax losses have made significant advancement in visual recognition tasks in computer vision. When training data exhibit class imbalances, the class-wise reweighted version of logistic and softmax losses are often used to boost performance of the unweighted version. In this paper, motivated to explain the reweighting mechanism, we explicate the learning property of those two loss functions by analyzing the necessary condition (e.g., gradient equals to zero) after training CNNs to converge to a local minimum. The analysis immediately provides us explanations for understanding (1) quantitative effects of the class-wise reweighting mechanism: deterministic effectiveness for binary classification using logistic loss yet indeterministic for multi-class classification using softmax loss; (2) disadvantage of logistic loss for single-label multi-class classification via one-vs.-all approach, which is due to the averaging effect on predicted probabilities for the negative class (e.g., non-target classes) in the learning process. With the disadvantage and advantage of logistic loss disentangled, we thereafter propose a novel reweighted logistic loss for multi-class classification. Our simple yet effective formulation improves ordinary logistic loss by focusing on learning hard non-target classes (target vs. non-target class in one-vs.-all) and turned out to be competitive with softmax loss. We evaluate our method on several benchmark datasets to demonstrate its effectiveness.

