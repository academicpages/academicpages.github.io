---
title: "Bringing a Blurry Frame Alive at High Frame-Rate with an Event Camera"
author: "L. Pan, <u>C. Scheerlinck</u>, X. Yu, R. Hartley, M. Liu, Y. Dao"
collection: publications
permalink: /event-deblurring
excerpt: 
date: 2019-06-15
venue: Conference on Computer Vision and Pattern Recognition (CVPR; ORAL accept. rate 6%)
paperurl: https://arxiv.org/abs/1811.10180
citation: 
youtubeId: JcgboJ_7JAE
header:
   teaser: blurry_thumbnail.png
---

<a href="https://openaccess.thecvf.com/content_CVPR_2019/papers/Pan_Bringing_a_Blurry_Frame_Alive_at_High_Frame-Rate_With_an_CVPR_2019_paper.pdf" target="_blank"><b>PDF</b></a>&emsp;
<a href="https://youtu.be/JcgboJ_7JAE" target="_blank"><b>Video</b></a>&emsp;
<a href="https://github.com/panpanfei/Bringing-a-Blurry-Frame-Alive-at-High-Frame-Rate-with-an-Event-Camera" target="_blank"><b>Code</b></a>&emsp;
<a href="https://drive.google.com/file/d/1s-PR7GxpCAIB20hu7F3BlbXdUi4c9UAo/view" target="_blank"><b>Data</b></a>&emsp;
<a href="https://drive.google.com/open?id=11O-D7uwN9DM47JFeFSicMjdhW9fG09-1" target="_blank"><b>Slides</b></a>&emsp;
<a href="https://cedric-scheerlinck.github.io/files/2019_cvpr_blurry.txt" target="_blank"><b>BibTex</b></a>

![blurry_banner](/images/blurry_banner.png){:class="img-responsive"}

{% include youtubePlayer.html id=page.youtubeId %}
<br />

CVPR talk <a href="https://drive.google.com/file/d/1NscnUF2QxK0of4ZW7T8kneJTH1X76l2u/view" target="_blank">here</a>

<b>Abstract.</b> Event-based cameras can measure intensity changes (called '<i>events</i>') with microsecond accuracy under high-speed motion and challenging lighting conditions. With the active pixel sensor (APS), the event camera allows simultaneous output of the intensity frames. However, the output images are captured at a relatively low frame-rate and often suffer from motion blur. A blurry image can be regarded as the integral of a sequence of latent images, while the events indicate the changes between the latent images. Therefore, we are able to model the blur-generation process by associating event data to a latent image. In this paper, we propose a simple and effective approach, the <b>Event-based Double Integral (EDI)</b> model, to reconstruct a high frame-rate, sharp video from a single blurry frame and its event data. The video generation is based on solving a simple non-convex optimization problem in a single scalar variable. Experimental results on both synthetic and real images demonstrate the superiority of our EDI model and optimization method in comparison to the state-of-the-art.

**DOI:** <a href="https://doi.org/10.1109/CVPR.2019.00698" target="_blank">10.1109/CVPR.2019.00698</a>

CVF <a href="https://openaccess.thecvf.com/content_CVPR_2019/html/Pan_Bringing_a_Blurry_Frame_Alive_at_High_Frame-Rate_With_an_CVPR_2019_paper.html" target="_blank">Open Access</a>

<b>Reference:</b>
* L. Pan, C. Scheerlinck, X. Yu, R. Hartley, M. Liu, Y. Dao "Bringing a Blurry Frame Alive at High Frame-Rate with an Event Camera", Conference on Computer Vision and Pattern Recognition (CVPR), 2019, pp. 6820-6829.
