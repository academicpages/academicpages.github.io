---
title: "Generating Smooth and Facial-Details-Enhanced Talking Head Video: A Perspective of Pre and Post Processes"
collection: publications
permalink: /publication/2022-Generating-Smooth-and-Facial-Details-Enhanced-Talking-Head-Video-A-Perspective-of-Pre-and-Post-Processes
excerpt: ''
date: 2022-10-12
venue: 'ACMMM'
tags:
  - Conference Publications
citation: 'Tian Lv, Yu-Hui Wen, Zhiyao Sun, Zipeng Ye, and Yong-Jin Liu*. 2022. Generating Smooth and Facial-Details-Enhanced Talking Head Video: A Perspective of Pre and Post Processes. In Proceedings of the 30th ACM International Conference on Multimedia (MM '22). Association for Computing Machinery, 7079–7083. https://doi.org/10.1145/3503161.3551583'
---



Abstract: Talking head video generation has received increasing attention re-cently. So far the quality (especially the facial details) of the videos from state-of-the-art deep learning methods is limited by either the quality of training data or the performance of generators, and needs to be further improved. In this paper, we propose a data pre- and post- processing strategy based on a key observation: generating a talking head video from a multi-modal input is a challenging problem and generating a smooth video with fine facial details makes the problem even harder. Then we propose to decompose the problem solution into a main deep model, a pre- and a post-processing. The main deep model generates a reasonably good talk-ing face video, with the aid of a pre-process, which also contributes to a post-process for restoring smooth and fine facial details in the final video. In particular, our main deep model reconstructs a 3D face from an input reference frame, and then uses an AudioNet to generate a sequence of facial expression coefficients with an input audio clip. To ensure final facial details in the generated video, we sample the original texture from the reference frame in the pre-process with the aid of reconstructed 3D face and a predefined UV map. Accordingly, in the post-process, we smooth the expression coefficients of adjacent frames to alleviate jitters and apply a pre-trained face restoration module to recover the fine facial details. Experimental results and ablation study show the advantage of our proposed method.



[Download paper here](http://yongjinliu.github.io/files/2022-Generating-Smooth-and-Facial-Details-Enhanced-Talking-Head-Video-A-Perspective-of-Pre-and-Post-Processes.pdf)

[More information](https://doi.org/10.1145/3503161.3551583)

Recommended citation: Tian Lv, Yu-Hui Wen, Zhiyao Sun, Zipeng Ye, and **Yong-Jin Liu***. 2022. Generating Smooth and Facial-Details-Enhanced Talking Head Video: A Perspective of Pre and Post Processes. In Proceedings of the 30th ACM International Conference on Multimedia (MM '22). Association for Computing Machinery, 7079–7083. https://doi.org/10.1145/3503161.3551583.

