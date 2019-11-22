---
title: "Infomax Neural Joint Source-Channel Coding via Adversarial Bit Flip"
collection: publications
permalink: /publications/IABF
venue: "The 34th AAAI Conference on Artificial Intelligence (AAAI 2020)"
date: 2019-11-20
citation: 'Yuxuan Song, Minkai Xu, <b>Lantao Yu</b>, Hao Zhou, Shuo Shao, Yong Yu. <i>AAAI 2020.</i>'
---

[[PDF]](https://lantaoyu.github.io/files/AAAI-SongS.6530.pdf)

## Abstract
Although Shannon theory states that it is asymptotically optimal to separate the source and channel coding as two independent processes, in many practical communication scenarios this decomposition is limited by the finite bit-length and computational power for decoding. Recently, neural joint source-channel coding (NECST) is proposed to sidestep this problem. While it leverages the advancements of amortized inference and deep learning to improve the encoding and decoding process, it still cannot always achieve compelling results in terms of  compression and error correction performance due to the limited robustness of its learned coding networks. In this paper, motivated by the inherent connections between neural joint source-channel coding and discrete representation learning, we propose a novel regularization method called Infomax Adversarial-Bit-Flip (IABF) to improve the stability and robustness of the neural joint source-channel coding scheme. More specifically, on the encoder side, we propose to explicitly maximize the mutual information between the codeword and data; while on the decoder side, the amortized reconstruction is regularized within an adversarial framework. Extensive experiments conducted on various real-world datasets evidence that our IABF can achieve state-of-the-art performances on both compression and error correction benchmarks and outperform the baselines by a significant margin. 