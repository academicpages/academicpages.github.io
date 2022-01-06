---
title: "Improving Query Representations for Dense Retrieval with Pseudo Relevance Feedback: A Reproducibility Study"
collection: publications
permalink: /publication/ECIR2021ANCEPRF
year: 2022
venue: 'Proceedings of the 44th European Conference on Information Retrieval (ECIR ’22)'
authors: Hang Li, <strong>Shengyao Zhuang</strong>, Ahmed Mourad, Xueguang Ma, Jimmy Lin, Guido Zuccon
track: Reproducibility paper
---
---

## Abstract
Pseudo-Relevance Feedback (PRF) utilises the relevance signals from the top-k passages from the first round of retrieval to perform a second round of retrieval aiming to improve search effectiveness. A recent research direction has been the study and development of PRF methods for deep language models based rankers, and in particular in the context of dense retrievers. Dense retrievers, compared to more complex neural rankers, provide a trade-off between effectiveness, which is often reduced compared to more complex neural rankers, and query latency, which also is reduced making the retrieval pipeline more efficient. The introduction of PRF methods for dense retrievers has been motivated as an attempt to further improve their effectiveness.

In this paper, we reproduce and study a recent method for PRF with dense retrievers, called ANCE-PRF. This method concatenates the query text and that of the top-k feedback passages to form a new query input, which is then encoded into a dense representation using a newly trained query encoder based on the original dense retriever used for the first round of retrieval. While the method can potentially be applied to any of the existing dense retrievers, prior work has studied it only in the context of the ANCE dense retriever.

We study the reproducibility of ANCE-PRF in terms of both its training (encoding of the PRF signal) and inference (ranking) steps. We further extend the empirical analysis provided in the original work to investigate the effect of the hyper-parameters that govern the training process and the robustness of the method across these different settings. Finally, we contribute a study of the generalisability of the ANCE-PRF method when dense retrievers other than ANCE are used for the first round of retrieval and for encoding the PRF signal.

[Download paper here](https://arxiv.org/pdf/2112.06400.pdf)

[Code](https://github.com/ielab/APR)

