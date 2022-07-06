---
title: "Ranking-Preserving Cross-Source Learning for Image Retargeting Quality Assessment"
collection: publications
permalink: /publication/2019-Ranking-Preserving-Cross-Source-Learning-for-Image-Retargeting-Quality-Assessment
excerpt: ''
date: 2019-06-20
venue: 'IEEE Transactions on Pattern Analysis and Machine Intelligence'
tags:
  - Journal Publications
citation: 'Yong-Jin Liu, Yiheng Han, Zipeng Ye, Yu-Ku Lai. Ranking-Preserving Cross-Source Learning for Image Retargeting Quality Assessment. IEEE Transactions on Pattern Analysis and Machine Intelligence. Vol. 42, No. 7, pp. 1798-1805, 2020.'
---

Abstract: Image retargeting techniques adjust images into different sizes and have attracted much attention recently. Objective quality assessment (OQA) of image retargeting results is often desired to automatically select the best results. Existing OQA methods train a model using some benchmarks (e.g., RetargetMe), in which subjective scores evaluated by users are provided. Observing that it is challenging even for human subjects to give consistent scores for retargeting results of different source images (diff-source-results), in this paper we propose a learning-based OQA method that trains a General Regression Neural Network (GRNN) model based on relative scores - which preserve the ranking - of retargeting results of the same source image (same-source-results). In particular, we develop a novel training scheme with provable convergence that learns a common base scalar for same-source-results. With this source specific offset, our computed scores not only preserve the ranking of subjective scores for same-source-results, but also provide a reference to compare the diff-source-results. We train and evaluate our GRNN model using human preference data collected in RetargetMe. We further introduce a subjective benchmark to evaluate the generalizability of different OQA methods. Experimental results demonstrate that our method outperforms ten representative OQA methods in ranking prediction and has better generalizability to different datasets.



[Download paper here](http://yongjinliu.github.io/files/2019-Ranking-Preserving-Cross-Source-Learning-for-Image-Retargeting-Quality-Assessment.pdf)

[Download source code here](http://cg.cs.tsinghua.edu.cn/people/~Yongjin/OQA%20Source%20code.zip)

[More information](https://ieeexplore.ieee.org/document/8742588)

Recommended citation: **Yong-Jin Liu**, Yiheng Han, Zipeng Ye, Yu-Ku Lai. Ranking-Preserving Cross-Source Learning for Image Retargeting Quality Assessment. IEEE Transactions on Pattern Analysis and Machine Intelligence. Vol. 42, No. 7, pp. 1798-1805, 2020.





