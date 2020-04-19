---
title: "Fast Image Reconstruction with an Event Camera"
collection: talks
type: "Talk"
permalink: /talks/wacv20
venue: "Winter Conference on Applications of Computer Vision (WACV)"
date: 2020-03-02
youtubeId: WyZxsNTVouA
location: "Snowmass Village, Colorado"
header:
   teaser: firenet_thumbnail.png
---

<a href="https://youtu.be/WyZxsNTVouA" target="_blank"><b>Video</b></a>&emsp;
<a href="https://docs.google.com/presentation/d/1uedxAvh0E9LA5ZkID_cRvfQFqFeRheWsPM6OksaQld0/edit?usp=sharing" target="_blank"><b>Poster</b></a>&emsp;

{% include youtubePlayer.html id=page.youtubeId %}
<br />

<b>Abstract.</b> 
Event cameras are powerful new sensors able to capture high dynamic range with microsecond temporal resolution and no motion blur.
Their strength is detecting brightness changes (called events) rather than capturing direct brightness images; however, algorithms can be used to convert events into usable image representations for applications such as classification.
Previous works rely on hand-crafted spatial and temporal smoothing techniques to reconstruct images from events.
State-of-the-art video reconstruction has recently been achieved using neural networks that are large (10M parameters) and computationally expensive, requiring 30ms for a forward-pass at 640 × 480 resolution on a modern GPU.
We propose a novel neural network architecture for video reconstruction from events that is smaller (<b>38k</b> vs. 10M parameters) and faster (<b>10ms</b> vs. 30ms) than state-of-the-art with minimal impact to performance.

FireNet [project page](/firenet).
