---
title: "Autoregressive Stylized Motion Synthesis with Generative Flow"
collection: publications
permalink: /publication/2021-Autoregressive-Stylized-Motion-Synthesis-with-Generative-Flow
excerpt: ''
date: 2021-06-19
venue: 'CVPR'
tags:
  - Conference Publications
citation: 'Yu-Hui Wen, Zhipeng Yang, Hongbo Fu, Lin Gao, Yanan Sun, Yong-Jin Liu*. Autoregressive Stylized Motion Synthesis with Generative Flow. In IEEE Conference on Computer Vision and Pattern Recognition (CVPR 21), pages 13612-13621, 2021.'
---

Abstract: Motion style transfer is an important problem in many computer graphics and computer vision applications, including human animation, games, and robotics. Most existing deep learning methods for this problem are supervised and trained by registered motion pairs. In addition, these methods are often limited to yielding a deterministic output, given a pair of style and content motions. In this paper, we propose an unsupervised approach for motion style transfer by synthesizing stylized motions autoregressively using a generative flow model M. M is trained to maximize the exact likelihood of a collection of unlabeled motions, based on an autoregressive context of poses in previous frames and a control signal representing the movement of a root joint. Thanks to invertible flow transformations, latent codes that encode deep properties of motion styles are efficiently inferred by M. By combining the latent codes (from an input style motion S) with the autoregressive context and control signal (from an input content motion C), M outputs a stylized motion which transfers style from S to C. Moreover, our model is probabilistic and is able to generate various plausible motions with a specific style. We evaluate the proposed model on motion capture datasets containing different human motion styles. Experiment results show that our model outperforms the state-of-the-art methods, despite not requiring manually labeled training data.



[Download paper here](http://yongjinliu.github.io/files/2021-Autoregressive-Stylized-Motion-Synthesis-with-Generative-Flow.pdf)

[Download source code here](https://github.com/wenyh1616/StyleMotion)

[More information](https://openaccess.thecvf.com/content/CVPR2021/html/Wen_Autoregressive_Stylized_Motion_Synthesis_With_Generative_Flow_CVPR_2021_paper.html)

Recommended citation: Yu-Hui Wen, Zhipeng Yang, Hongbo Fu, Lin Gao, Yanan Sun, **Yong-Jin Liu***. Autoregressive Stylized Motion Synthesis with Generative Flow. In IEEE Conference on Computer Vision and Pattern Recognition (CVPR 21), pages 13612-13621, 2021.

