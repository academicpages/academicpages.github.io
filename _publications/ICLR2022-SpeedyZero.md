---
title: "SpeedyZero: Mastering Atari Games with Limited Data and Time"
collection: publications
permalink: /publication/ICLR2022-SpeedyZero
excerpt: 'Many recent breakthroughs of deep reinforcement learning (RL) are mainly built upon large-scale distributed training of model-free methods using millions to billions of samples. On the other hand, state-of-the-art model-based RL methods can achieve human-level sample efficiency but often take a much longer over all training time than model-free methods. However, high sample efficiency and fast training time are both important to many real-world applications. We develop SpeedyZero, a distributed RL system built upon a state-of-the-art model-based RL method, EfficientZero, with a dedicated system design for fast distributed computation. We also develop two novel algorithmic techniques, Priority Refresh and Clipped LARS, to stabilize training with massive parallelization and large batch size. SpeedyZero maintains on-par sample efficiency compared with EfficientZero while achieving a 14.5X speedup in wall-clock time, leading to human-level performances on the Atari benchmark within 35 minutes using only 300k samples. In addition, we also present an in-depth analysis on the fundamental challenges in further scaling our system to bring insights to the community.'
date: 2023-02-01
venue: 'ICLR'
paperurl: 'https://sites.google.com/view/speedyzero'
citation: 'Mei, Yixuan, Jiaxuan Gao, Weirui Ye, Shaohuai Liu, Yang Gao, and Yi Wu. "SpeedyZero: Mastering Atari with Limited Data and Time." In The Eleventh International Conference on Learning Representations. 2022.'
---
This paper is about the number 2. The number 3 is left for future work.

[Download paper here](https://openreview.net/forum?id=Mg5CLXZgvLJ)

BibTex:
'''
@inproceedings{mei2022speedyzero,
  title={SpeedyZero: Mastering Atari with Limited Data and Time},
  author={Mei, Yixuan and Gao, Jiaxuan and Ye, Weirui and Liu, Shaohuai and Gao, Yang and Wu, Yi},
  booktitle={The Eleventh International Conference on Learning Representations},
  year={2022}
}
'''
