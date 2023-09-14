---
title: "Typos-aware Bottlenecked Pre-Training for Robust Dense Retrieval"
collection: publications
permalink: /publication/arxiv2023ToRoDER
year: 2023
venue: 'Proceedings of the 1st International ACM SIGIR Conference on Information Retrieval in the Asia Pacific (SIGIR-AP '23)'
authors: <strong>Shengyao Zhuang</strong>, Linjun Shou, Jian Pei, Ming Gong, Houxing Ren, Guido Zuccon and Daxin Jiang.
track: Full paper
---
---

## Abstract
Current dense retrievers (DRs) are limited in their ability to effectively process misspelled queries, which constitute a significant portion of query traffic in commercial search engines. The main issue is that the pre-trained language model-based encoders used by DRs are typically trained and fine-tuned using clean, well-curated text data. Misspelled queries are typically not found in the data used for training these models, and thus misspelled queries observed at inference time are out-of-distribution compared to the data used for training and fine-tuning. Previous efforts to address this issue have focused on fine-tuning strategies, but their effectiveness on misspelled queries remains lower than that of pipelines that employ separate state-of-the-art spell-checking components. 

To address this challenge, we propose ToRoDer (TypOs-aware bottlenecked pre-training for RObust DEnse Retrieval), a novel pre-training strategy for DRs that increases their robustness to misspelled queries while preserving their effectiveness in downstream retrieval tasks. ToRoDer utilizes an encoder-decoder architecture where the encoder takes misspelled text with masked tokens as input and outputs bottlenecked information to the decoder. The decoder then takes as input the bottlenecked embeddings, along with token embeddings of the original text with the misspelled tokens masked out. The pre-training task is to recover the masked tokens for both the encoder and decoder.

Our extensive experimental results and detailed ablation studies show that DRs pre-trained with ToRoDer exhibit significantly higher effectiveness on misspelled queries, sensibly closing the gap with pipelines that use a separate, complex spell-checker component, while retaining their effectiveness on correctly spelled queries

[Download paper here](https://arxiv.org/pdf/2304.08138.pdf)
