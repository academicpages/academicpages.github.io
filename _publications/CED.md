---
title: "CED: Color Event Camera Dataset"
collection: publications
permalink: /CED
excerpt: 
date: 2019-06-16
venue: Conference on Computer Vision and Pattern Recognition Workshops
paperurl:
citation: 
youtubeId: R9BiRN7f7uY
header:
   teaser: CED_thumbnail_text.png
---

<a href="https://cedric-scheerlinck.github.io/files/2019_cvprw_CED.pdf" target="_blank"><b>PDF</b></a>&emsp;
<a href="https://youtu.be/R9BiRN7f7uY" target="_blank"><b>Video</b></a>&emsp;
<a href="http://rpg.ifi.uzh.ch/CED.html" target="_blank"><b>Datasets</b></a>&emsp;
<a href="https://cedric-scheerlinck.github.io/files/2019_cvprw_CED.txt" target="_blank"><b>BibTex</b></a>

![CED_banner](/images/CED_banner.png){:class="img-responsive"}

<b>Abstract.</b> Event cameras are novel, bio-inspired visual sensors, whose pixels output asynchronous and independent timestamped spikes at local intensity changes, called 'events'.
Event cameras offer advantages over conventional frame-based cameras in terms of latency, high dynamic range (HDR) and temporal resolution.
Until recently, event cameras have been limited to outputting events in the intensity channel, however, recent advances have resulted in the development of color event cameras, such as the Color-DAVIS346.
In this work, we present and release the first *Color Event Camera Dataset (CED)*, containing 50 minutes of footage with both color frames and events.
CED features a wide variety of indoor and outdoor scenes, which we hope will help drive forward event-based vision research.
We also present an extension of the event camera simulator ESIM that enables simulation of color events.
Finally, we present an evaluation of three state-of-the-art image reconstruction methods that can be used to convert the Color-DAVIS346 into a continuous-time, HDR, color video camera to visualise the event stream, and for use in downstream vision applications.

{% include youtubePlayer.html id=page.youtubeId %}

<br />
<b>Reference:</b>
* C. Scheerlinck\*, H. Rebecq\*, T. Stoffregen, N. Barnes, R. Mahony, D. Scaramuzza, "CED: Color Event Camera Dataset", Conference on Computer Vision and Pattern Recognition Workshops (CVPRW), 2019.
