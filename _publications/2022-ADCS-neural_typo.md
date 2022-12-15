---
title: "Robustness of Neural Rankers to Typos: A Comparative Study"
collection: publications
permalink: /publication/ADCS2022NeuralTypo
year: 2022
venue: 'Proceedings of the 26th Australasian Document Computing Symposium (ADCS ’22)'
authors: <strong>Shengyao Zhuang</strong>, Xinyu Mao, Guido Zuccon (<i class="fa fa-trophy" aria-hidden="true"> Best Paper Award </i>)
track: Short paper
---
---

## Abstract
Recent advances in passage retrieval have seen the introduction of pre-trained language models (PLMs) based neural rankers. While generally very effective, little attention has been paid to the robustness of these rankers. In this paper, we study the effectiveness of state-of-the-art PLM rankers in presence of typos in queries, as an indication of the rankers’ robustness. As of PLM rankers, we consider the two most promising directions explored in previous work: dense retrievers vs. sparse retrievers. We find that both types of rankers are very sensitive to queries with typos. We then apply an existing augmentation-based typos-aware training technique with the aim of creating typo-robust dense and sparse retrievers. We find that this simple technique only works for dense retrievers, while it hurts effectiveness when used on sparse retrievers.

[Download paper here](https://ielab.io/publications/adcs2022-typos/adcs2022-comparative-study.pdf)
