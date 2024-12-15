---
title: "Mastering Atari Games with Limited Data"
collection: publications
permalink: /publication/Neurips2021-EfficientZero
excerpt: 'Reinforcement learning has achieved great success in many applications. However, sample efficiency remains a key challenge, with prominent methods requiring millions (or even billions) of environment steps to train. Recently, there has been significant progress in sample efficient image-based RL algorithms; however, consistent human-level performance on the Atari game benchmark remains an elusive goal. We propose a sample efficient model-based visual RL algorithm built on MuZero, which we name EfficientZero. Our method achieves 194.3% mean human performance and 109.0% median performance on the Atari 100k benchmark with only two hours of real-time game experience and outperforms the state SAC in some tasks on the DMControl 100k benchmark. This is the first time an algorithm achieves super-human performance on Atari games with such little data. EfficientZero's performance is also close to DQN's performance at 200 million frames while we consume 500 times less data. EfficientZero's low sample complexity and high performance can bring RL closer to real-world applicability. We implement our algorithm in an easy-to-understand manner and it is available at the following URL. We hope it will accelerate the research of MCTS-based RL algorithms in the wider community.'
date: 2021-09-01
venue: 'Neurips 2021'
paperurl: 'https://arxiv.org/pdf/2111.00210'
citation: 'Ye, Weirui, Shaohuai Liu, Thanard Kurutach, Pieter Abbeel, and Yang Gao. "Mastering atari games with limited data." Advances in Neural Information Processing Systems 34 (2021): 25476-25488.'
---

[Download paper here](https://arxiv.org/pdf/2111.00210.pdf)

BibTex:
'''
@article{ye2021mastering,
  title={Mastering atari games with limited data},
  author={Ye, Weirui and Liu, Shaohuai and Kurutach, Thanard and Abbeel, Pieter and Gao, Yang},
  journal={Advances in Neural Information Processing Systems},
  volume={34},
  pages={25476--25488},
  year={2021}
}
'''
