---
title: "High Frame Rate Video Reconstruction based on an Event Camera"
author: "L. Pan, R. Hartley, <u>C. Scheerlinck</u>, M. Liu, X. Yu, Y. Dai"
collection: publications
permalink: /medi
excerpt: 
date: 2020-11-09
venue: IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI)
paperurl: https://doi.org/10.1109/TPAMI.2020.3036667
citation: 
youtubeId: JcgboJ_7JAE
header:
   teaser: medi_thumbnail.png
---

<a href="https://arxiv.org/pdf/1903.06531.pdf" target="_blank"><b>PDF</b></a>&emsp;
<a href="https://youtu.be/JcgboJ_7JAE" target="_blank"><b>Video</b></a>&emsp;
<a href="https://github.com/panpanfei/Bringing-a-Blurry-Frame-Alive-at-High-Frame-Rate-with-an-Event-Camera" target="_blank"><b>Code</b></a>&emsp;
<a href="https://drive.google.com/file/d/1s-PR7GxpCAIB20hu7F3BlbXdUi4c9UAo/view" target="_blank"><b>Data</b></a>&emsp;
<a href="https://cedric-scheerlinck.github.io/files/2019_arxiv_medi.txt" target="_blank"><b>BibTex</b></a>

![blurry_banner](/images/banners/blurry_banner.png){:class="img-responsive"}

{% include youtubePlayer.html id=page.youtubeId %}
<br />

<b>Abstract.</b> Event-based cameras measure intensity changes (called 'events') with microsecond accuracy under high-speed motion and
challenging lighting conditions. With the active pixel sensor (APS), event cameras allow simultaneous output of intensity frames.
However, the output images are captured at a relatively low frame rate and often suffer from motion blur. A blurred image can be
regarded as the integral of a sequence of latent images, while events indicate changes between the latent images. Thus, we are able to
model the blur-generation process by associating event data to a latent sharp image. Based on the abundant event data alongside low
frame rate, easily blurred images, we propose a simple yet effective approach to reconstruct high-quality and high frame rate sharp
videos. Starting with a single blurred frame and its event data, we propose the <b>Event-based Double Integral (EDI)</b> model and solve it
by adding regularization terms. Then, we extend it to <b>multiple Event-based Double Integral (mEDI)</b> model to get more smooth results
based on multiple images and their events. Furthermore, we provide a new and more efficient solver to minimize the proposed energy
model. By optimizing the energy function, we achieve significant improvements in removing blur and the reconstruction of a high
temporal resolution video. The video generation is based on solving a simple non-convex optimization problem in a single scalar
variable. Experimental results on both synthetic and real sequences demonstrate the superiority of our <b>mEDI</b> model and optimization
method compared to the state of the art.

**DOI:** <a href="https://doi.org/10.1109/TPAMI.2020.3036667" target="_blank">10.1109/TPAMI.2020.3036667</a>

<b>Reference:</b>
* L. Pan, R. Hartley, C. Scheerlinck, M. Liu, X. Yu, Y. Dai, "High Frame Rate Video Reconstruction based on an Event Camera", IEEE Transactions on Pattern Analysis and Machine Intelligence, November 2020.
