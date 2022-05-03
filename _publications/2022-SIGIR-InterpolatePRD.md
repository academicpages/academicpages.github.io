---
title: "To Interpolate or not to Interpolate: PRF, Dense and Sparse Retrievers"
collection: publications
permalink: /publication/SIGIR2022InterpolatePRF
year: 2022
venue: 'Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR ’22)'
authors: Hang Li, Shuai Wang, <strong>Shengyao Zhuang</strong>, Ahmed Mourad, Xueguang Ma, Jimmy Lin, Guido Zuccon
track: Short paper
---
---

## Abstract
Current pre-trained language model approaches to information retrieval can be broadly divided into two categories: sparse retrievers
(to which belong also non-neural approaches such as bag-of-words
methods, e.g., BM25) and dense retrievers. Each of these categories
appears to capture different characteristics of relevance. Previous
work has investigated how relevance signals from sparse retrievers
could be combined with those from dense retrievers via interpolation. Such interpolation would generally lead to higher retrieval
effectiveness

In this paper we consider the problem of combining the relevance signals from sparse and dense retrievers in the context of
Pseudo Relevance Feedback (PRF). This context poses two key challenges: (1) When should interpolation occur: before, after, or both
before and after the PRF process? (2) Which sparse representation
should be considered: a zero-shot bag-of-words model (BM25), or
a learnt sparse representation? To answer these questions we perform a thorough empirical evaluation considering an effective and
scalable neural PRF approach (Vector-PRF), three effective dense
retrievers (ANCE, TCTv2, DistillBERT), and one state-of-the-art
learnt sparse retriever (uniCOIL). The empirical findings from our
experiments suggest that, regardless of sparse representation and
dense retriever, interpolation both before and after PRF achieves
the highest effectiveness across most datasets and metrics.

[Download paper here](https://arxiv.org/pdf/2205.00235.pdf)
