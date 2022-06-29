---
title: "Flexible-Rate Learned Hierarchical Bi-Directional Video Compression With Motion Refinement and Frame-Level Bit Allocation"
collection: publications
permalink: /publication/2022-06-27-flex-rate-icip2022
excerpt: 'This work presents improvements and novel additions to the recent work on end-to-end optimized hierarchical bidirectional video compression to further advance the state of-the-art in learned video compression.'
date: 2022-06-27
venue: "IEEE International Conference on Image Processing (ICIP 2022)"
paperurl: 
citation: 'Eren Cetin, M. Akin Yilmaz, A. Murat Tekalp. (2022). &quot;Flexible-Rate Learned Hierarchical Bi-Directional Video Compression With Motion Refinement and Frame-Level Bit Allocation.&quot; <i>IEEE International Conference on Image Processing (ICIP 2022)</i>.'
---
As an improvement, we combine motion estimation and prediction modules and compress refined residual motion vectors for improved rate-distortion performance. As novel addition, we adapted the gain unit proposed for image compression to flexible-rate video compression in two ways: first, the gain unit enables a single encoder model to operate at multiple rate-distortion operating points; second, we exploit the gain unit to control bit allocation among intra-coded vs. bi-directionally coded frames by fine tuning corresponding models for truly flexible-rate learned video coding.

[Download paper here](https://arxiv.org/pdf/2206.13613.pdf)

Recommended citation: 
```
@misc{https://doi.org/10.48550/arxiv.2206.13613,
  doi = {10.48550/ARXIV.2206.13613},
  url = {https://arxiv.org/abs/2206.13613},
  author = {Cetin, Eren and Yilmaz, M. Akin and Tekalp, A. Murat},
  keywords = {Image and Video Processing (eess.IV), Computer Vision and Pattern Recognition (cs.CV)},
  title = {Flexible-Rate Learned Hierarchical Bi-Directional Video Compression With Motion Refinement and Frame-Level Bit Allocation},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```