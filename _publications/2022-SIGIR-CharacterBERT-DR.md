---
title: "CharacterBERT and Self-Teaching for Improving the Robustness of Dense Retrievers on Queries with Typos"
collection: publications
permalink: /publication/SIGIR2022CharacterBERT-DR
year: 2022
venue: 'Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR ’22)'
authors: <strong>Shengyao Zhuang</strong>, Guido Zuccon
track: Full paper
---
---

## Abstract
Previous work has shown that dense retrievers are not robust to out-of-domain and outlier queries, i.e. their effectiveness on these queries is much poorer than what expected. In this paper, we consider a specific instance of such queries: queries that contain typos. We show that a small character level perturbation in queries (as caused by typos) highly impacts the effectiveness of dense retrievers.
We then demonstrate that the root cause of this resides in the input tokenization strategy employed by BERT. In BERT, tokenization is performed using the BERT's WordPiece tokenizer and we show that a token with a typo will significantly change the token distributions obtained after tokenization. This distribution change translates to changes in the input embeddings passed to the BERT-based query encoder of dense retrievers. We then turn our attention to devising dense retriever methods that are robust to such typo queries, while still being as performant as previous methods on queries without typos. For this, we use CharacterBERT as the backbone encoder and an efficient yet effective training method, called Self-Teaching (ST), that distills knowledge from queries without typos into the queries with typos. Experimental results show that CharacterBERT in combination with ST achieves significantly higher effectiveness on queries with typos compared to previous methods. Along with these results and the open-sourced implementation of the methods, we also provide a new passage retrieval dataset consisting of real-world queries with typos and associated relevance assessments on the MS MARCO corpus, thus supporting the research community in the investigation of effective and robust dense retrievers.

[Download paper here](https://arxiv.org/pdf/2204.00716.pdf)

[Code](https://github.com/ielab/CharacterBERT-DR)
