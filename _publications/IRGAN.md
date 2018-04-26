---
title: "IRGAN: A Minimax Game for Unifying Generative and Discriminative Information Retrieval Models"
collection: publications
permalink: /publications/IRGAN
venue: "The 40th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR-17)"
date: 2017-04-11
citation: 'Jun Wang, <b>Lantao Yu</b>, Weinan Zhang, Yu Gong, Yinghui Xu, Benyou Wang, Peng Zhang and Dell Zhang. <i>The 40th International ACM SIGIR Conference on Research and Development in Information Retrieval.</i> <b>SIGIR 2017.</b> <b> <span style="color:red">Best Paper Award Honorable Mention</span> </b>'
---  
[[PDF]](https://arxiv.org/abs/1705.10513)  [[Code]](https://github.com/geek-ai/irgan)


## Abstract
This paper provides a unified account of two schools of thinking in information retrieval modelling: the generative retrieval focusing on predicting relevant documents given a query, while discriminative retrieval focusing on predicting relevancy given a query-document pair. We propose a game theoretical minimax game to iteratively optimise both models.
On one hand, the discriminative model, aiming to mine signals from labelled and unlabelled data, provides guidance to train the generative model towards fitting the underlying relevance distribution over documents given the query.
On the other hand, the generative model, acting as an attacker to the current discriminative model, generates difficult examples for the discriminative model in an adversarial way by minimising its discrimination objective.
With the competition between these two models, we show that the unified framework takes advantage of both schools of thinking: (i) the generative model learns to fit the relevance distribution over documents via the signal from the discriminative model, and (ii) the discriminative model is able to exploit the unlabelled data selected by the generative model to achieve a better estimation for document ranking.
Our experimental results have demonstrated significant performance gains as much as 23.96% on Precision@5 and 15.50% on MAP over strong baselines in a variety of applications including web search, item recommendation, and question answering.

## Best Paper Award Honorable Mention
<p align="center">
  <img src="https://lantaoyu.github.io/files/sigir17-award.jpg?raw=true" alt="Photo" style="width: 850px;"/>
</p>