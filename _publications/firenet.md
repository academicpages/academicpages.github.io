---
title: "Fast Image Reconstruction with an Event Camera"
author: "<u>C. Scheerlinck</u>, H. Rebecq, D. Gehrig, N. Barnes, R. Mahony, D. Scaramuzza"
collection: publications
permalink: /firenet
excerpt: 
date: 2020-03-02
venue: Winter Conference on Applications of Computer Vision (WACV)
paperurl:
citation: 
youtubeId: QaGYFtR2-X8
header:
   teaser: firenet_thumbnail.png
---

<a href="https://cedric-scheerlinck.github.io/files/2019_firenet.pdf" target="_blank"><b>PDF</b></a>&emsp;
<a href="https://youtu.be/QaGYFtR2-X8" target="_blank"><b>Video</b></a>&emsp;
<a href="https://github.com/cedric-scheerlinck/rpg_e2vid/tree/cedric/firenet" target="_blank"><b>Code</b></a>&emsp;
<a href="https://drive.google.com/file/d/1nBCeIF_Us-rGhCjdU5q1Ch-yrFckjZPa/view?usp=sharing" target="_blank"><b>Model</b></a>&emsp;
<a href="https://youtu.be/WyZxsNTVouA" target="_blank"><b>Talk</b></a>&emsp;
<a href="https://docs.google.com/presentation/d/1uedxAvh0E9LA5ZkID_cRvfQFqFeRheWsPM6OksaQld0/edit?usp=sharing" target="_blank"><b>Poster</b></a>&emsp;
<a href="https://cedric-scheerlinck.github.io/files/2020_wacv_firenet.txt" target="_blank"><b>BibTex</b></a>

![firenet_banner](/images/firenet_banner.png){:class="img-responsive"}

{% include youtubePlayer.html id=page.youtubeId %}
<br />

<b>Abstract.</b> 
Event cameras are powerful new sensors able to capture high dynamic range with microsecond temporal resolution and no motion blur.
Their strength is detecting brightness changes (called events) rather than capturing direct brightness images; however, algorithms can be used to convert events into usable image representations for applications such as classification.
Previous works rely on hand-crafted spatial and temporal smoothing techniques to reconstruct images from events.
State-of-the-art video reconstruction has recently been achieved using neural networks that are large (10M parameters) and computationally expensive, requiring 30ms for a forward-pass at 640 × 480 resolution on a modern GPU.
We propose a novel neural network architecture for video reconstruction from events that is smaller (<b>38k</b> vs. 10M parameters) and faster (<b>10ms</b> vs. 30ms) than state-of-the-art with minimal impact to performance.

FireNet can be run using this
<a href="https://github.com/cedric-scheerlinck/rpg_e2vid/tree/cedric/firenet" target="_blank"><b>code</b></a>
and
<a href="https://drive.google.com/file/d/1nBCeIF_Us-rGhCjdU5q1Ch-yrFckjZPa/view?usp=sharing" target="_blank"><b>model</b></a>.

Datasets:
* <a href="http://rpg.ifi.uzh.ch/davis_data.html" target="_blank"><b>Event Camera Dataset</b></a>
* <a href="http://rpg.ifi.uzh.ch/E2VID.html" target="_blank"><b>High Speed and HDR</b></a>
* <a href="https://drive.google.com/drive/folders/1Jv73p1-Hi56HXyal4SHQbzs2zywISOvc" target="_blank"><b>DVS Image Reconstruction Dataset</b></a>

CVF <a href="http://openaccess.thecvf.com/content_WACV_2020/html/Scheerlinck_Fast_Image_Reconstruction_with_an_Event_Camera_WACV_2020_paper.html" target="_blank">Open Access</a> page with PDF.

<b>Reference:</b>
* C. Scheerlinck, H. Rebecq, D. Gehrig, N. Barnes, R. Mahony, D. Scaramuzza, "Fast Image Reconstruction with an Event Camera", Winter Conference on Applications of Computer Vision (WACV), 2020, pp. 156-163.
