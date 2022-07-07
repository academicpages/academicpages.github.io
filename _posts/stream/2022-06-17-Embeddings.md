---
date: 2022-06-17
tags:
- stream
- nn
title: Neural Network Embeddings
---

Embeddings are used to map high-dimensional data to low-dimensional floating-point representation. This may improve the performance because it improves the representation of the input given to the model.

A `nn.Embedding` layer is simply a linear layer from one-hot representation of categorical data to a real vector. During learning, task-specific embedding weights are learned from the supervised data. It is sometimes helpful to initialize embedding weights using a more general method such as:  Word2Vec, Doc2Vec, GloVe.