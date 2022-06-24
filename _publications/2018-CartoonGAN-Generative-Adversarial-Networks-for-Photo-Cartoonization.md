---
title: "CartoonGAN: Generative Adversarial Networks for Photo Cartoonization"
collection: publications
permalink: /publication/2018-CartoonGAN-Generative-Adversarial-Networks-for-Photo-Cartoonization
excerpt: ''
date: 2018-06-18
venue: 'CVPR'
tags:
  - Conference Publications
citation: 'Yang Chen, Yu-Kun Lai, Yong-Jin Liu. CartoonGAN: Generative Adversarial Networks for Photo Cartoonization. In IEEE Conference on Computer Vision and Pattern Recognition (CVPR 18), pages 9465-9474, 2018.'
---



Abstract: In this paper, we propose a solution to transforming photos of real-world scenes into cartoon style images, which is valuable and challenging in computer vision and computer graphics. Our solution belongs to learning based methods, which have recently become popular to stylize images in artistic forms such as painting. However, existing methods do not produce satisfactory results for cartoonization, due to the fact that (1) cartoon styles have unique characteristics with high level simplification and abstraction, and (2) cartoon images tend to have clear edges, smooth color shading and relatively simple textures, which exhibit significant challenges for texture-descriptor-based loss functions used in existing methods. In this paper, we propose CartoonGAN, a generative adversarial network (GAN) framework for cartoon stylization. Our method takes unpaired photos and cartoon images for training, which is easy to use. Two novel losses suitable for cartoonization are proposed: (1) a semantic content loss, which is formulated as a sparse regularization in the high-level feature maps of the VGG network to cope with substantial style variation between photos and cartoons, and (2) an edge-promoting adversarial loss for preserving clear edges. We further introduce an initialization phase, to improve the convergence of the network to the target manifold. Our method is also much more efficient to train than existing methods. Experimental results show that our method is able to generate high-quality cartoon images from real-world photos (i.e., following specific artists' styles and with clear edges and smooth shading) and outperforms state-of-the-art methods.



[Download paper here](http://yongjinliu.github.io/files/2018-CartoonGAN-Generative-Adversarial-Networks-for-Photo-Cartoonization.pdf)

[Download source code here](https://github.com/FlyingGoblin/CartoonGAN)

[More information](https://ieeexplore.ieee.org/document/8579084)

[Model](http://cg.cs.tsinghua.edu.cn/people/~Yongjin/CartoonGAN-Models.rar)

Recommended citation: Yang Chen, Yu-Kun Lai, **Yong-Jin Liu**. CartoonGAN: Generative Adversarial Networks for Photo Cartoonization. In IEEE Conference on Computer Vision and Pattern Recognition (CVPR 18), pages 9465-9474, 2018.

