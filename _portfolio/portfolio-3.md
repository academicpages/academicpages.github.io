---
title: "Flexible-Rate Bidirectional Video Compression with Motion Refinement"
excerpt: "A learned bidirectional video compression network proposed for my Bachelor's Thesis."
collection: portfolio
---

Video content has been becoming more prevalent in the last decade by capturing 80% of the
online data. As this is the case, more efficient video compression methods are helpful to provide a
better service for people who stream online video content with a limited bandwidth. For that reason,
our aim is to develop a learned bidirectional video compression framework that achieves superior or
competitive rate-distortion performance compared to other works in the literature of video
compression. To achieve the desired results, we employ additional modules such as bidirectional
motion prediction, motion refinement, learned frame fusion and achieve flexible bitrate using a single
model with learned quantization parameters. Testing our network on UVG dataset, a common
benchmark, we achieve competitive or superior results at high bitrates when we compare our results
with other learned video compression networks such as DVC [1](https://openaccess.thecvf.com/content_CVPR_2019/papers/Lu_DVC_An_End-To-End_Deep_Video_Compression_Framework_CVPR_2019_paper.pdf), Scale-Space Flow [2](https://openaccess.thecvf.com/content_CVPR_2020/papers/Agustsson_Scale-Space_Flow_for_End-to-End_Optimized_Video_Compression_CVPR_2020_paper.pdf), RLVC [3](https://ieeexplore.ieee.org/abstract/document/9288876),
and LHBDC [4](https://arxiv.org/pdf/2112.09529) in terms of PSNR and MS-SSIM scores. On the other hand, the model achieves
slightly worse rate-distortion performance at low bitrates compared to LHBDC [4](https://arxiv.org/pdf/2112.09529) and the traditional
SVT-HEVC codec at very slow preset in terms of PSNR and MS-SSIM. In the following report,
further details of the proposed network are provided extensively with visual results that demonstrate
the effect of main modules.

For further information, please refer to the [report](/files/flexible-rate-hierarchical/Flexible-Rate-Hierarhical-Video-Compression.pdf) I have prepared for my BSc thesis.

The code for the proposed network can be found in [Github](https://github.com/erenovic/Bidirectional-Video-Compression-with-Motion-Refinement).

<img src='/files/flexible-rate-hierarchical/bachelors_thesis_architecture.png' alt='bidirectional video compression network architecture' width='600' height='700'>

