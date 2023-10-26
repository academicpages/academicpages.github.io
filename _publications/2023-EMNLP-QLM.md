---
title: "Open-source Large Language Models are Strong Zero-shot Query Likelihood Models for Document Ranking"
collection: publications
permalink: /publication/emnlp2023QLM
year: 2023
venue: 'In Findings of the Association for Computational Linguistics: EMNLP 2023'
authors: <strong>Shengyao Zhuang</strong>, Bing Liu, Bevan Koopman and Guido Zuccon.
track: Short paper
---
---

## Abstract
In the field of information retrieval, Query Likelihood Models (QLMs) rank documents based on the probability of generating the query given the content of a document. Recently, advanced large language models (LLMs) have emerged as effective QLMs, showcasing promising ranking capabilities. This paper focuses on investigating the genuine zero-shot ranking effectiveness of recent LLMs, which are solely pretrained on unstructured text data without supervised instruction fine-tuning. Our findings reveal the robust zero-shot ranking ability of such LLMs, highlighting that additional instruction fine-tuning may hinder effectiveness unless a question generation task is present in the finetuning dataset. Furthermore, we introduce a novel state-of-the-art ranking system that integrates LLM-based QLMs with a hybrid zeroshot retriever, demonstrating exceptional effectiveness in both zero-shot and few-shot scenarios. We make our codebase publicly available at https://github.com/ielab/llm-qlm.


[Download paper here](https://arxiv.org/pdf/2310.13243.pdf)

[Code](https://github.com/ielab/llm-qlm)
