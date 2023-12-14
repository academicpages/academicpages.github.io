---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

* **TensoRF Re-implementation**\
TensoRF introduces a novel way to model and reconstruct radiance fields by factorizing tensors into multiple compact low-rank tensor components. This allows for more efficient scene modeling and realistic rendering of 3D scenes, with advantages like super-fast convergence, a compact memory footprint, and the ability to capture vivid details. By re-implementing the TensorVMSplit-192 model for a lego scene, I was able to achieve a Peak Signal-to-Noise Ratio (PSNR) of 36.49, which exceeds the paper's reported 35.72 for the same scene. This project is the beginning of my exploratory journey into the realm of 3D computer vision and the potential of Neural Radiance Fields (NeRF) as a research direction. 

* **Base Layer Efficiency in Scalable Human-Machine Coding** [[arXiv]](https://arxiv.org/pdf/2307.02430.pdf)\
A basic premise in scalable human-machine coding is that the base layer is intended for automated machine analysis and is therefore more compressible than the same content would be for human viewing. Use cases for such coding include video surveillance and traffic monitoring, where the majority of the content will never be seen by humans. Therefore, base layer efficiency is of paramount importance because the system would most frequently operate at the base-layer rate. In this paper, we analyze the coding efficiency of the base layer in a state-of-the-art scalable human-machine image codec, and show that it can be improved. In particular, we demonstrate that gains of 20-40% in BD-Rate compared to the currently best results on object detection and instance segmentation are possible.\
**Keywords:** Human-machine Coding, Scalable Coding, Learning-based Compression 


* **Rate-Distortion Theory in Coding for Machines and its Applications** [[arXiv]](https://arxiv.org/pdf/2305.17295)\
Recent years have seen a tremendous growth in both the capability and popularity of automatic machine analysis of images and video. As a result, a growing need for efficient compression methods optimized for machine vision, rather than human vision, has emerged. To meet this growing demand, several methods have been developed for image and video coding for machines.  Unfortunately, while there is a substantial body of knowledge regarding rate-distortion theory for human vision, the same cannot be said of machine analysis. In this paper, we extend the current rate-distortion theory for machines, providing insight into important design considerations of machine-vision codecs. We then utilize this newfound understanding to improve several methods for learnable image coding for machines. Our proposed methods achieve state-of-the-art rate-distortion performance on several computer vision tasks such as classification, instance segmentation, and object detection.\
**Keywords:** Rate-Distortion Theory, Collaborative Intelligence, Image Coding, Coding for Machines, Learnable Compression, Compression for Machines, Split Computing


* **VVC+M: Plug and Play Scalable Image Coding for Humans and Machines** [[arXiv]](https://arxiv.org/pdf/2305.10453.pdf)\
Compression for machines is an emerging field, where inputs are encoded while optimizing the performance of downstream automated analysis. In scalable coding for humans and machines, the compressed representation used for machines is further utilized to enable input reconstruction. Often performed by jointly optimizing the compression scheme for both machine task and human perception, this results in sub-optimal rate-distortion (RD) performance for the machine side. We focus on the case of images, proposing to utilize the pre-existing residual coding capabilities of video codecs such as VVC to create a scalable codec from any image compression for machines (ICM) scheme. Using our approach we improve an existing scalable codec to achieve superior RD performance on the machine task, while remaining competitive for human perception. Moreover, our approach can be trained post-hoc for any given ICM scheme, and without creating a coupling between the quality of the machine analysis and human vision.\
**Keywords:** Compression for Machines, Coding for Machines, Image Coding, Scalable Coding, Learned Image Compression


* **Control of Computer Pointer Using Hand Gesture Recognition in Motion Pictures** [[arXiv]](https://arxiv.org/abs/2012.13188)\
A user interface is designed to enable computer cursor control through hand detection and gesture classification. A comprehensive hand dataset comprising 6720 image samples is collected, encompassing four distinct classes: fist, palm, pointing to the left, and pointing to the right. The images were captured from 15 individuals in various settings, including simple backgrounds with different perspectives and lighting conditions. A convolutional neural network (CNN) was trained on this dataset to accurately predict labels for each captured image and measure their similarity. The system incorporates defined commands for cursor movement, left-click, and right-click actions. Experimental results indicate that the proposed algorithm achieves a remarkable accuracy of 91.88% and demonstrates its potential applicability across diverse simple backgrounds.\
**Keywords:** Hand Gesture Recognition, Dataset, Convolutional Neural Network, Human-computer Interaction, Classification
