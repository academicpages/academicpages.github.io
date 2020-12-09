---
title: "Reducing the Sim-to-Real Gap for Event Cameras"
author: "T. Stoffregen\\*, <u>C. Scheerlinck</u>\\*, D. Scaramuzza, T. Drummond, N. Barnes, L. Kleeman, R. Mahony"
collection: publications
permalink: /20ecnn
excerpt: 
date: 2020-08-23
venue: European Conference on Computer Vision (ECCV)
paperurl:
citation: 
youtubeId: 4-4dxSXwly8
header:
   teaser: 20arXiv_teaser.png
---

<a href="https://arxiv.org/pdf/2003.09078.pdf" target="_blank"><b>PDF</b></a>&emsp;
<a href="https://youtu.be/4-4dxSXwly8" target="_blank"><b>Video</b></a>&emsp;
<a href="https://drive.google.com/drive/folders/18Xdr6pxJX0ZXTrXW9tK0hC3ZpmKDIt6_?usp=sharing" target="_blank"><b>Dataset</b></a>&emsp;
<a href="https://github.com/TimoStoff/event_cnn_minimal" target="_blank"><b>Code</b></a>&emsp;
<a href="{{ "/files/2020_eccv_ecnn.txt" | relative_url }}" target="_blank"><b>BibTex</b></a>

![ecnn20_banner](/images/banners/20arXiv_banner.png){:class="img-responsive"}

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

**DOI:** <a href="https://doi.org/10.1007/978-3-030-58583-9_32" target="_blank">10.1007/978-3-030-58583-9_32</a>

<b>Reference:</b>
* T. Stoffregen\*, C. Scheerlinck\*, D. Scaramuzza, T. Drummond, N. Barnes, L. Kleeman, R. Mahony, "Reducing the Sim-to-Real Gap for Event Cameras", European Conference on Computer Vision (ECCV), 2020.

\* Equal contribution.
<br />
