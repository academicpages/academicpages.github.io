---
title: "BERT-based Dense Retrievers Require Interpolation with BM25 for Effective Passage Retrieval"
collection: publications
permalink: /publication/ICTIR2021InterpolateDR
year: 2021
venue: 'Proceedings of the 2021 ACM SIGIR International Conference on the Theory
of Information Retrieval (ICTIR ’21)'
authors: Shuai Wang, <strong>Shengyao Zhuang</strong>, Guido Zuccon
track: Full paper
---
---

## Abstract
The integration of pre-trained deep language models, such as BERT, into retrieval and ranking pipelines has shown to provide large effectiveness gains over traditional bag-of-words models in the passage retrieval task. However, the best setup for integrating such deep language models is still unclear. 

When BERT is used to re-rank passages (i.e., BERT re-ranker), previous work has empirically shown that, while in practice BERT re-ranker cannot act as initial retriever due to BERT's high query time costs, and thus a bag-of-words model such as BM25 is required. It is not necessary to interpolate BERT re-ranker and bag-of-words scores to generate the final ranking. In fact, the BERT re-ranker scores alone can be used by the re-ranker: the BERT re-ranker score appears to already capture the relevance signal provided by BM25. 

In this paper, we further investigate the topic of interpolating BM25 and BERT-based rankers. Unlike previous work that considered the BERT re-ranker, however, here we consider BERT-based dense retrievers (RepBERT and ANCE). Dense retrievers encode queries and documents into low dimensional BERT-based embeddings. These methods overcome BERT's high computational costs at query time, and can thus be feasibly used in practice as whole-collection retrievers, rather than just as re-rankers. 

Our novel empirical findings suggest that, unlike for BERT re-ranker, interpolation with BM25 is necessary for BERT-based dense retrievers to perform effectively; and the gains provided by the interpolation are significant. Further analysis reveals why this is so: dense retrievers are very effective at encoding strong relevance signals, but they fail in identifying weaker relevance signals -- a task that the interpolation with BM25 is able to make up for.



[Download paper here](http://arvinzhuang.github.io/files/shuai2021interpolateDR.pdf)

[Code](https://github.com/ielab/InterpolateDR-ICTIR2021)

