---
title: "Dealing with Typos for BERT-based Passage Retrieval and Ranking"
collection: publications
permalink: /publication/EMNLP2021typo
year: 2021
venue: 'In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP)'
authors: <strong>Shengyao Zhuang</strong>, Guido Zuccon
track: Short paper
---
---

## Abstract
Passage retrieval and ranking is a key task in open-domain question answering and information retrieval. Current effective approaches mostly rely on pre-trained deep language model-based retrievers and rankers. These methods have been shown to effectively model the semantic matching between queries and passages, also in presence of keyword mismatch, i.e. passages that are relevant to a query but do not contain important query keywords.

In this paper we consider the Dense Retriever (DR), a passage retrieval method, and the BERT re-ranker, a popular passage re-ranking method. In this context, we formally investigate how these models respond and adapt to a speciﬁc type of keyword mismatch – that caused by keyword typos occurring in queries. Through empirical investigation, we ﬁnd that typos can lead to a signiﬁcant drop in retrieval and ranking effectiveness. We then propose a simple typos-aware training framework for DR and BERT re-ranker to address this issue. Our experimental results on the MS MARCO passage ranking dataset show that, with our proposed typos-aware training, DR and BERT re-ranker can become robust to typos in queries, resulting in signiﬁcantly improved effectiveness compared to models trained without appropriately accounting for typos.

[Download paper here](https://arxiv.org/pdf/2108.12139.pdf)

[Code](https://github.com/ielab/typos-aware-BERT)
