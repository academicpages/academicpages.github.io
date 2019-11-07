---
title: "Fast Image Reconstruction with an Event Camera"
collection: publications
permalink: /firenet
excerpt: 
date: 2019-11-07
venue: Coming soon
paperurl:
citation: 
header:
   teaser: firenet_thumbnail.png
---

<a href="https://cedric-scheerlinck.github.io/files/2019_firenet.pdf" target="_blank"><b>PDF</b></a>&emsp;

![firenet_banner](/images/firenet_banner.png){:class="img-responsive"}

<b>Abstract.</b> 
Event cameras are powerful new sensors able to capture high dynamic range with microsecond temporal resolution and no motion blur.
Their strength is detecting brightness changes (called events) rather than capturing direct brightness images; however, algorithms can be used to convert events into usable image representations for applications such as classification.
Previous works rely on hand-crafted spatial and temporal smoothing techniques to reconstruct images from events.
State-of-the-art video reconstruction has recently been achieved using neural networks that are large (10M parameters) and computationally expensive, re- quiring 30ms for a forward-pass at 640 × 480 resolution on a modern GPU.
We propose a novel neural network architecture for video reconstruction from events that is smaller (<b>38k</b> vs. 10M parameters) and faster (<b>10ms</b> vs. 30ms) than state-of-the-art with minimal impact to performance.
