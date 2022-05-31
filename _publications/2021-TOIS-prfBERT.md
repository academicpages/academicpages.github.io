---
title: "Pseudo Relevance Feedback with Deep Language Models and Dense Retrievers: Successes and Pitfalls"
collection: publications
permalink: /publication/arxiv2021prfBERT
year: 2022
venue: 'Transactions on Information Systems (TOIS)'
authors: Hang Li, Ahmed Mourad, <strong>Shengyao Zhuang</strong>, Bevan Koopman, Guido Zuccon
track: Journal paper
---
---

## Abstract

Pseudo Relevance Feedback (PRF) is known to improve the effectiveness of bag-of-words retrievers. At the same time, deep language models have been shown to outperform traditional bag-of-words rerankers. However, it is unclear how to integrate PRF directly with emergent deep language models. In this article, we address this gap by investigating methods for integrating PRF signals into rerankers and dense retrievers based on deep language models. We consider text-based and vector-based PRF approaches, and investigate different ways of combining and scoring relevance signals. An extensive empirical evaluation was conducted across four different datasets and two task settings (retrieval and ranking).

Text-based PRF results show that the use of PRF had a mixed effect on deep rerankers across different datasets. We found that the best effectiveness was achieved when (i) directly concatenating each PRF passage with the query, searching with the new set of queries, and then aggregating the scores; (ii) using Borda to aggregate scores from PRF runs.

Vector-based PRF results show that the use of PRF enhanced the effectiveness of deep rerankers and dense retrievers over several evaluation metrics. We found that higher effectiveness was achieved when (i) the query retains either the majority or the same weight within the PRF mechanism, and (ii) a shallower PRF signal (i.e., a smaller number of top-ranked passages) was employed, rather than a deeper signal. Our vector-based PRF method is computationally efficient; thus this represents a general PRF method others can use with deep rerankers and dense retrievers.

[Download paper here](https://arxiv.org/pdf/2108.11044.pdf)

[Code](https://github.com/hanglics/Neural-Relevance-Feedback-Public/tree/master/Vector_Based_PRF)
