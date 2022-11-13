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

[Download pdf from IEEE](https://doi.org/10.1109/TCSI.2022.3193031)

[Download pdf from this site](http://WeiCheng14159.github.io/files/publications/CNN_CLIP-Q.pdf)

```
@article{
	title = {An Efficient Implementation of Convolutional Neural Network With CLIP-Q Quantization on FPGA},
	volume = {69},
	doi = {10.1109/TCSI.2022.3193031},
	number = {10},
	journal = {IEEE Trans. Circuits Syst. I},
	author = {Cheng, Wei and Lin, Ing-Chao and Shih, Yun-Yang},
	pages = {4093--4102}
}
```