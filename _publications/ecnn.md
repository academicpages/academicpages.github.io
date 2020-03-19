---
title: "How To Train Your Event Camera Neural Network"
author: "T. Stoffregen\\*, <u>C. Scheerlinck</u>\\*, D. Scaramuzza, T. Drummond, N. Barnes, L. Kleeman, R. Mahony"
collection: publications
permalink: /ecnn
excerpt: 
date: 2020-03-18
venue: arXiv
paperurl:
citation: 
header:
   teaser: ecnn_thumbnail.png
---

<a href="https://cedric-scheerlinck.github.io/files/coming_soon.txt" target="_blank"><b>PDF</b></a>&emsp;
<a href="https://cedric-scheerlinck.github.io/files/2020_arxiv_ecnn.txt" target="_blank"><b>BibTex</b></a>

![ecnn_banner](/images/ecnn_banner.png){:class="img-responsive"}

<b>Abstract.</b> 
Event cameras are paradigm-shifting novel sensors that report asynchronous, per-pixel brightness changes called 'events' with unparalleled low latency.
This makes them ideal for high speed, high dynamic range scenes where conventional cameras would fail.
Recent work has demonstrated impressive results using Convolutional Neural Networks (CNNs) for video reconstruction and optic flow with events.
We present strategies for improving training data for event based CNNs that result in 25-40% boost in performance of existing state-of-the-art (SOTA) video reconstruction networks retrained with our method, and up to 80% for optic flow networks.
A challenge in evaluating event based video reconstruction is lack of quality groundtruth images in existing datasets.
To address this, we present a new <b>High Quality Frames (HQF)</b> dataset, containing events and groundtruth frames from a DAVIS240C that are well-exposed and minimally motion-blurred.
We evaluate our method on HQF + several existing major event camera datasets.

<br />
<b>Reference:</b>
* T. Stoffregen\*, C. Scheerlinck\*, D. Scaramuzza, T. Drummond, N. Barnes, L. Kleeman, R. Mahony, "How To Train Your Event Camera Neural Network", arXiv, 2020.
