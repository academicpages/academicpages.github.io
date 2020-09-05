---
title: "Reducing the Sim-to-Real Gap for Event Cameras"
collection: talks
type: "Talk"
permalink: /talks/ecnn
venue: "European Conference on Computer Vision (ECCV)"
date: 2020-08-23
youtubeId: 4-4dxSXwly8
header:
   teaser: 20arXiv_teaser.png
---

<a href="https://youtu.be/4-4dxSXwly8" target="_blank"><b>Video</b></a>&emsp;

{% include youtubePlayer.html id=page.youtubeId %}
<br />

<b>Abstract.</b> 
Event cameras are paradigm-shifting novel sensors that report asynchronous, per-pixel brightness changes called 'events' with unparalleled low latency.
This makes them ideal for high speed, high dynamic range scenes where conventional cameras would fail. 
Recent work has demonstrated impressive results using Convolutional Neural Networks (CNNs) for video reconstruction and optic flow with events.
We present strategies for improving training data for event based CNNs that result in 20-40% boost in performance of existing state-of-the-art (SOTA) video reconstruction networks retrained with our method, and up to 15% for optic flow networks.
A challenge in evaluating event based video reconstruction is lack of quality ground truth images in existing datasets.
To address this, we present a new **High Quality Frames (HQF)** dataset, containing events and ground truth frames from a DAVIS240C that are well-exposed and minimally motion-blurred.
We evaluate our method on HQF + several existing major event camera datasets.

[Project page](/20ecnn).
