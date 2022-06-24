---
title: "Barehanded Music: Real-time Hand Interaction for Virtual Piano"
collection: publications
permalink: /publication/2016-Barehanded-Music-Real-time-Hand-Interaction-for-Virtual-Piano
excerpt: ''
date: 2016-02-27
venue: 'I3D'
tags:
  - Conference Publications
citation: 'Hui Liang, Jin Wang, Qian Sun, Yong-Jin Liu*, Junsong Yuan, Jun Luo, Ying He (2016) Barehanded Music: Real-time Hand Interaction for Virtual Piano. Proceedings of ACM Symposium on Interactive 3D Graphics and Games (I3D '16), pp. 87-94, 2016.'
---



Abstract: This paper presents an efficient data-driven approach to track fingertip and detect finger tapping for virtual piano using an RGB-D camera. We collect 7200 depth images covering the most common finger articulation for playing piano, and train a random regression forest using depth context features of randomly sampled pixels in training images. In the online tracking stage, we firstly segment the hand from the plane in contact by fusing the information from both color and depth images. Then we use the trained random forest to estimate the 3D position of fingertips and wrist in each frame, and predict finger tapping based on the estimated fingertip motion. Finally, we build a kinematic chain and recover the articulation parameters for each finger. In contrast to the existing hand tracking algorithms that often require hands are in the air and cannot interact with physical objects, our method is designed for hand interaction with planar objects, which is desired for the virtual piano application. Using our prototype system, users can put their hands on a desk, move them sideways and then tap fingers on the desk, like playing a real piano. Preliminary results show that our method can recognize most of the beginner's piano-playing gestures in realtime for soothing rhythms.



[Download paper here](http://yongjinliu.github.io/files/2016-Barehanded-Music-Real-time-Hand-Interaction-for-Virtual-Piano.pdf)

[More information](http://dl.acm.org/citation.cfm?id=2856411&CFID=589992092&CFTOKEN=51550633)

Recommended citation: Hui Liang, Jin Wang, Qian Sun, **Yong-Jin Liu***, Junsong Yuan, Jun Luo, Ying He (2016) Barehanded Music: Real-time Hand Interaction for Virtual Piano. Proceedings of ACM Symposium on Interactive 3D Graphics and Games (I3D '16), pp. 87-94, 2016.

