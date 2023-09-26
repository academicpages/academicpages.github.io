---
title: "Selecting which Dense Retriever to use for Zero-Shot Search"
collection: publications
permalink: /publication/SIGIRAP2023ModelSelection
year: 2023
venue: 'Proceedings of the 1st International ACM SIGIR Conference on Information Retrieval in the Asia Pacific (SIGIR-AP ’23)'
authors: Ekaterina Khramtsova, <strong>Shengyao Zhuang</strong>, Mahsa Baktashmotlagh, Xi Wang and Guido Zuccon.
track: Full paper
---
---

## Abstract
We propose the new problem of choosing which dense retrieval model to use when searching on a new collection for which no labels are available, i.e. in a zero-shot setting. Many dense retrieval models are readily available. Each model however is characterized by very differing search effectiveness -- not just on the test portion of the datasets in which the dense representations have been learned but, importantly, also across different datasets for which data was not used to learn the dense representations. This is because dense retrievers typically require training on a large amount of labeled data to achieve satisfactory search effectiveness in a specific dataset or domain. Moreover, effectiveness gains obtained by dense retrievers on datasets for which they are able to observe labels during training, do not necessarily generalise to datasets that have not been observed during training. This is however a hard problem: through empirical experimentation we show that methods inspired by recent work in unsupervised performance evaluation with the presence of domain shift in the area of computer vision and machine learning are not effective for choosing highly performing dense retrievers in our setup. The availability of reliable methods for the selection of dense retrieval models in zero-shot settings that do not require the collection of labels for evaluation would allow to streamline the widespread adoption of dense retrieval. This is therefore an important new problem we believe the information retrieval community should consider.

[Download paper here](https://arxiv.org/pdf/2309.09403v1.pdf)
