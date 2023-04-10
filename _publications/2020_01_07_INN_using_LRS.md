---
title: "Invertible Generative Modeling using Linear Rational Splines"
collection: publications
permalink: /publication/2020_01_07_INN_using_LRS
excerpt: 'In this paper, we explore using linear rational splines as an invertible transformations for normalizing flows.'
date: 2020-01-06
venue: 'The 23rd International Conference on Artifcial Intelligence and Statistics (AISTATS)'
---

![Alt](https://hmdolatabadi.github.io/files/publications/2020_Linear_Rational_Splines/img.png)

Normalizing flows attempt to model an arbitrary probability distribution through a set of invertible mappings. These transformations are required to achieve a tractable Jacobian determinant that can be used in high-dimensional scenarios. The first normalizing flow designs used coupling layer mappings built upon affine transformations. The significant advantage of such models is their easy-to-compute inverse. Nevertheless, making use of affine transformations may limit the expressiveness of such models. Recently, invertible piecewise polynomial functions as a replacement for affine transformations have attracted attention. However, these methods require solving a polynomial equation to calculate their inverse. In this paper, we explore using linear rational splines as a replacement for affine transformations used in coupling layers. Besides having a straightforward inverse, inference and generation have similar cost and architecture in this method. Moreover, simulation results demonstrate the competitiveness of this approach’s performance compared to existing methods.

[[arXiv]](https://arxiv.org/abs/2001.05168)
<a id="raw-url" href="https://raw.githubusercontent.com/hmdolatabadi/hmdolatabadi.github.io/master/files/bibtex/HMDolatabadi2020LRS.bib">[bibtex]</a>
[[code]](https://github.com/hmdolatabadi/LRS_NF)
[[blog-post]](https://hmdolatabadi.github.io/posts/2020/10/lrs/)
[[poster]](https://hmdolatabadi.github.io/files/publications/2020_Linear_Rational_Splines/Hadi_M_Dolatabadi_AISTATS_Poster.pdf)
