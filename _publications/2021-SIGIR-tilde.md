---
title: "TILDE: Term Independent Likelihood moDEl for Passage Re-ranking"
collection: publications
permalink: /publication/SIGIR2021TILDE
year: 2021
venue: 'Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR)'
authors: Shengyao Zhuang, Guido Zuccon
---
---

##Abstract

Deep language models (deep LMs) are increasingly being used for full text retrieval or within cascade retrieval pipelines as later-stage re-rankers. A problem with using deep LMs is that, at query time, a slow inference step needs to be performed – this hinders the practical adoption of these powerful retrieval models, or limits sensibly how many documents can be considered for re-ranking.

We propose the novel, BERT-based, Term Independent Likelihood moDEl (TILDE), which ranks documents by both query and document likelihood. At query time, our model does not require the inference step of deep language models based retrieval approaches, thus providing consistent time-savings, as the prediction of query terms’ likelihood can be pre-computed and stored during index creation. This is achieved by relaxing the term dependence assumption made by the deep LMs. In addition, we have devised a novel bi-directional training loss which allows TILDE to maximise both query and document likelihood at the same time during training. At query time, TILDE can rely on its query likelihood component (TILDE-QL) solely, or the combination of TILDE-QL and its document likelihood component (TILDE-DL), thus providing a flexible trade-off between efficiency and effectiveness. Exploiting both components provide the highest effectiveness at a higher computational cost while relying only on TILDE-QL trades off effectiveness for faster response time due to no inference being required.

TILDE is evaluated on the MS MARCO and TREC Deep Learning 2019 and 2020 passage ranking datasets. Empirical results show that, compared to other approaches that aim to make deep language models viable operationally, TILDE achieves competitive effectiveness coupled with low query latency.

[Download paper here](http://arvinzhuang.github.io/files/arvin2021tilde.pdf)

[Code](https://github.com/ielab/TILDE)

