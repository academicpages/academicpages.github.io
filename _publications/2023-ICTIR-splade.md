---
title: "Exploring the Representation Power of SPLADE Models"
collection: publications
permalink: /publication/ICTIR2023SPLADE
year: 2023
venue: 'Proceedings of the 2023 ACM SIGIR International Conference on the Theory of Information Retrieval (ICTIR ’23)'
authors: Joel Mackenziem, <strong>Shengyao Zhuang</strong>, Guido Zuccon
track: Short paper
---
---

## Abstract
The SPLADE (SParse Lexical AnD Expansion) model is a highly effective approach to learned sparse retrieval, where documents are represented by term impact scores derived from large language models.
During training, SPLADE applies regularization to ensure postings lists are kept sparse --- with the aim of mimicking the properties of natural term distributions --- allowing efficient and effective lexical matching and ranking.
However, we hypothesize that SPLADE may encode additional signals into common postings lists to further improve effectiveness.
To explore this idea, we perform a number of empirical analyses where we re-train SPLADE with different, controlled vocabularies and measure how effective it is at ranking passages.
Our findings suggest that SPLADE can effectively encode useful ranking signals in documents even when the vocabulary is constrained to terms that are not traditionally useful for ranking, such as stopwords or even random words.

[Download paper here](https://arxiv.org/pdf/2306.16680.pdf)

[Code](https://github.com/ielab/understanding-splade)
