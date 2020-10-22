---
title: "Strategies for Pre-training Graph Neural Networks"
collection: publications
permalink: /publication/2019-05-29-strategies
excerpt: "We investigate the effective use of pre-training strategies on graph datasets for molecular property prediction and protein function prediction.<center><img src='/images/method.jpg' height='200'></center>"
date: 2019-05-29
venue: 'International Conference on Learning Representations'
paperurl: 'https://openreview.net/forum?id=HJlWWJSFDH'
citation: 'Weihau Hu, Bowen Liu, Joseph Gomes, Marinka Zitnik, Percy Liang, Vijay S. Pande, Jure Leskovec. &quot;Strategies for Pre-training Graph Neural Networks.&quot; In <i>International Conference on Learning Representations</i> (2019).'
---
Many applications of machine learning require a model to make accurate pre-dictions on test examples that are distributionally different from training ones, while task-specific labels are scarce during training. An effective approach to this challenge is to pre-train a model on related tasks where data is abundant, and then fine-tune it on a downstream task of interest. While pre-training has been effective in many language and vision domains, it remains an open question how to effectively use pre-training on graph datasets. In this paper, we develop a new strategy and self-supervised methods for pre-training Graph Neural Networks (GNNs). The key to the success of our strategy is to pre-train an expressive GNN at the level of individual nodes as well as entire graphs so that the GNN can learn useful local and global representations simultaneously. We systematically study pre-training on multiple graph classification datasets. We find that naïve strategies, which pre-train GNNs at the level of either entire graphs or individual nodes, give limited improvement and can even lead to negative transfer on many downstream tasks. In contrast, our strategy avoids negative transfer and improves generalization significantly across downstream tasks, leading up to 9.4% absolute improvements in ROC-AUC over non-pre-trained models and achieving state-of-the-art performance for molecular property prediction and protein function prediction.

[Full Article](https://openreview.net/forum?id=HJlWWJSFDH)

Recommended citation: Weihau Hu, Bowen Liu, Joseph Gomes, Marinka Zitnik, Percy Liang, Vijay S. Pande, Jure Leskovec. “Strategies for Pre-training Graph Neural Networks”. In <i>International Conference on Learning Representations</i> (2019).
