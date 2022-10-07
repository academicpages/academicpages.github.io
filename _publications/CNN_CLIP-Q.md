---
title: "An Efficient Implementation of Convolutional Neural Network With CLIP-Q Quantization on FPGA"
collection: publications
permalink: /publication/CNN_CLIP-Q
excerpt: 'This paper is about a hardware-software codesigned CNN accelerator based on the CLIP-Q network quantization algorithm.'
date: 2022-07-09
venue: 'IEEE Transactions on Circuits and Systems I: Regular Papers'
paperurl: 'https://doi.org/10.1109/TCSI.2022.3193031'
---
## Abstract
Convolutional neural networks (CNNs) have achieved tremendous success in the computer vision domain recently. The pursue for better model accuracy drives the model size and the storage requirements of CNNs as well as the computational complexity. Therefore, Compression Learning by InParallel Pruning-Quantization (CLIP-Q) was proposed to reduce a vast amount of weight storage requirements by using a few quantized segments to represent all weights in a CNN layer. Among various quantization strategies, CLIP-Q is suitable for hardware accelerators because it reduces model size significantly while maintaining the full-precision model accuracy. However, the current CLIP-Q approach did not consider the hardware characteristics and it is not straightforward when mapped to a CNN hardware accelerator. In this work, we propose a software-hardware codesign platform that includes a modified version of CLIP-Q algorithm and a hardware accelerator, which consists of 5 × 5 reconfigurable convolutional arrays with input and output channel parallelization. Additionally, the proposed CNN accelerator maintains the same accuracy of a full-precision CNN in Cifar-10 and Cifar-100 datasets.

[Download paper here](http://WeiCheng14159.github.io/files/publications/CNN_CLIP-Q.pdf)

```
@ARTICLE{CNN_CLIP-Q,
  author={Cheng, Wei and Lin, Ing-Chao and Shih, Yun-Yang},  
  journal={IEEE Transactions on Circuits and Systems I: Regular Papers},   
  title={An Efficient Implementation of Convolutional Neural Network With CLIP-Q Quantization on FPGA},   
  year={2022},  
  volume={69},  
  number={10},  
  pages={4093-4102},  
  doi={10.1109/TCSI.2022.3193031}
}
```