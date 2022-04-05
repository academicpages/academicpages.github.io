---
title: "Effective and Privacy-preserving Federated Online Learning to Rank"
collection: publications
permalink: /publication/ICTIR2021FPDGD
year: 2021
venue: 'Proceedings of the 2021 ACM SIGIR International Conference on the Theory
of Information Retrieval (ICTIR ’21)'
authors: Shuyi Wang, Bing Liu, <strong>Shengyao Zhuang</strong>, Guido Zuccon, <i class="fa fa-trophy" aria-hidden="true"> Best Student Paper Award </i>
track: Full paper
---
---

## Abstract
Online Learning to Rank (OLTR) has been primarily studied in the centralised setting, where a central server is responsible to index the searchable data, collect the users’ queries and search interactions, and optimize ranking models. A drawback of such a centralised OLTR paradigm is that it cannot guarantee user’s privacy as all data (both the searchable one and the one related to user interactions) is collected by the server.

In this paper, we propose a Federated OLTR method, called FPDGD, which leverages the state-of-the-art Pairwise Differentiable Gradient Descent (PDGD) and adapts it to the Federated Averaging framework. For a strong privacy guarantee, we further introduce a noise-adding clipping technique based on the theory of differential privacy to be used in combination with FPDGD.

Empirical evaluation shows FPDGD significantly outperforms the only other federated OLTR method. In addition, FPDGD is more robust across different privacy guarantee requirements than the current method: our method is therefore more reliable for real-life applications.



[Download paper here](http://arvinzhuang.github.io/files/wang2021fpdgd.pdf)

[Code](https://github.com/ielab/fpdgd-ictir2021)

