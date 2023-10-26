---
title: "A Setwise Approach for Effective and Highly Efficient Zero-shot Ranking with Large Language Models"
collection: publications
permalink: /publication/arxiv2023Setwise
year: 2023
venue: 'Arxiv Preprint'
authors: <strong>Shengyao Zhuang</strong>, Honglei Zhuang, Bevan Koopman and Guido Zuccon.
track: Full paper
---
---

## Abstract
Large Language Models (LLMs) demonstrate impressive effectiveness in zero-shot document ranking tasks. Pointwise, Pairwise, and Listwise prompting approaches have been proposed for LLM-based zero-shot ranking. Our study begins by thoroughly evaluating these existing approaches within a consistent experimental framework, considering factors like model size, token consumption, latency, among others. This first-of-its-kind comparative evaluation of these approaches allows us to identify the trade-offs between effectiveness and efficiency inherent in each approach. We find that while Pointwise approaches score high on efficiency, they suffer from poor effectiveness. Conversely, Pairwise approaches demonstrate superior effectiveness but incur high computational overhead. To further enhance the efficiency of LLM-based zero-shot ranking, we propose a novel Setwise prompting approach. Our approach reduces the number of LLM inferences and the amount of prompt token consumption during the ranking procedure, significantly improving the efficiency of LLM-based zero-shot ranking. We test our method using the TREC DL datasets and the BEIR zero-shot document ranking benchmark. The empirical results indicate that our approach considerably reduces computational costs while also retaining high zero-shot ranking effectiveness.

[Download paper here](https://arxiv.org/pdf/2310.09497.pdf)

[Code](https://github.com/ielab/llm-rankers)
