---
title: "Reinforcement Online Learning to Rank with Unbiased Reward Shaping"
collection: publications
permalink: /publication/arxiv2021ROLTR
year: 2022
venue: 'Information Retrieval Journal (IRJ)'
authors: <strong>Shengyao Zhuang</strong>, Zhihao Qiao, Guido Zuccon
track: Journal paper
---
---

## Abstract
Online learning to rank (OLTR) aims to learn a ranker directly from implicit feedback derived from users’ interactions, such as clicks. Clicks however are a biased signal: specifically, top-ranked documents are likely to attract more clicks than documents down the ranking (position bias). In this paper, we propose a novel learning algorithm for OLTR that uses reinforcement learning to optimize rankers: Reinforcement Online Learning to Rank (ROLTR). In ROLTR, the gradients of the ranker are estimated based on the rewards assigned to clicked and unclicked documents. In order to de-bias the users’ position bias contained in the reward signals, we introduce unbiased reward shaping functions that exploit inverse propensity scoring for clicked and unclicked documents. The fact that our method can also model unclicked documents provides a further advantage in that less users interactions are required to effectively train a ranker, thus providing gains in efficiency. Empirical evaluation on standard OLTR datasets shows that ROLTR achieves state-ofthe-art performance, and provides significantly better user experience than other OLTR approaches. To facilitate the reproducibility of our experiments, we make all experiment code available at https://github.com/ielab/OLTR.

[Download paper here](https://arxiv.org/pdf/2201.01534.pdf)

[Code](https://github.com/ielab/OLTR)

