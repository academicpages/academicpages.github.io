---
title: "Bringing a Blurry Frame Alive at High Frame-Rate with an Event Camera"
collection: publications
permalink: /event-deblurring
excerpt: 
date: 2019-06-15
venue: Conference on Computer Vision and Pattern Recognition (CVPR; ORAL accept. rate 6%)
paperurl: https://arxiv.org/abs/1811.10180
citation: 
youtubeId:
header:
   teaser: blurry_thumbnail.png
---

<a href="https://arxiv.org/pdf/1811.10180.pdf" target="_blank"><b>PDF</b></a>&emsp;
<a href="https://cedric-scheerlinck.github.io/files/2019_cvpr_blurry.txt" target="_blank"><b>BibTex</b></a>

<b>Abstract.</b> Event-based cameras can measure intensity changes (called '<i>events</i>') with microsecond accuracy under high-speed motion and challenging lighting conditions. With the active pixel sensor (APS), the event camera allows simultaneous output of the intensity frames. However, the output images are captured at a relatively low frame-rate and often suffer from motion blur. A blurry image can be regarded as the integral of a sequence of latent images, while the events indicate the changes between the latent images. Therefore, we are able to model the blur-generation process by associating event data to a latent image. In this paper, we propose a simple and effective approach, the <b>Event-based Double Integral (EDI)</b> model, to reconstruct a high frame-rate, sharp video from a single blurry frame and its event data. The video generation is based on solving a simple non-convex optimization problem in a single scalar variable. Experimental results on both synthetic and real images demonstrate the superiority of our EDI model and optimization method in comparison to the state-of-the-art.

<br />
<b>Reference:</b>
* L. Pan, C. Scheerlinck, X. Yu, R. Hartley, M. Liu, Y. Dao "Bringing a Blurry Frame Alive at High Frame-Rate with an Event Camera," Conference on Computer Vision and Pattern Recognition, 2019.
