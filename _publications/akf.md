---
title: "An Asynchronous Kalman Filter for Hybrid Event Cameras"
author: "Z. Wang, Y. Ng, <u>C. Scheerlinck</u>, R. Mahony"
collection: publications
permalink: /akf
excerpt: 
date: 2020-12-08
venue: arXiv
paperurl:
citation: 
youtubeId: JRjiojUzgfVo
header:
   teaser: akf_thumbnail.png
---

<a href="https://arxiv.org/pdf/1903.06531.pdf" target="_blank"><b>PDF</b></a>&emsp;
<a href="https://youtu.be/RjiojUzgfVo" target="_blank"><b>Video</b></a>&emsp;
<a href="https://cedric-scheerlinck.github.io/files/2020_arxiv_akf.txt" target="_blank"><b>BibTex</b></a>

![blurry_banner](/images/banners/akf_banner.png){:class="img-responsive"}

{% include youtubePlayer.html id=page.youtubeId %}
<br />

<b>Abstract.</b> We present an Asynchronous Kalman Filter (AKF) to reconstruct High Dynamic Range (HDR) videos by fusing low-dynamic range images with event data.
Event cameras are ideally suited to capture HDR visual information without blur but perform poorly on static or slowly changing scenes.
Conversely, conventional image sensors measure absolute intensity of slowly changing scenes effectively but do poorly on quickly changing scenes with high dynamic range.
The proposed approach exploits advantages of hybrid sensors under a unifying uncertainty model for both conventional frames and events.
We present a novel dataset targeting challenging HDR and fast motion scenes captured on two separate sensors: an RGB frame-based camera and an event camera.
Our video reconstruction outperforms the state-of-the-art algorithms on existing datasets and our targeted HDR dataset.

<b>Reference:</b>

* Z. Wang, Y. Ng, C. Scheerlinck, R. Mahony, "An Asynchronous Kalman Filter for Hybrid Event Cameras", arXiv, December 2020.
