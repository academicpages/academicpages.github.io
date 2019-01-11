---
title: "A Real-time UAV-Based Intelligent Tracking System"
collection: research
type: "IVM Lab"
permalink: /research/research-tracking
venue: "Shanghai Jiao Tong University"
date: 2018-03-22
location: "City, Country"
---

[[Code]](https://github.com/AlexXiao95/YOLO_TRACKING),
[[Poster]](https://alexxiao95.github.io/research/tracking/tracking_poster.pdf)

## Introduction

In this project, we will focus on achieving a real-time tracking system which integrates state-of-art object detection algorithm and multi object tracking algorithm into single one system. This can take us one step further to realizing a fully automatic and highly intelligent security system. We also apply the system on UAV to achieve the real-time multi object tracking on UAV video streaming.

Thanks to the rapid development of computation power, the performance of object detectors has improved dramatically in the last two decades. Among them, YOLO and SSD are two recent popular object detection framework. They are both one-staged detection which can get the location and class of object at the same time. More important is that they can both achieve real-time detection and also keep a high detection accuracy.

Multi object tracking has been a challenging field mainly due to noisy detection sets and frequently switches caused by occlusion and similar appearance among nearby objects. Most of the state-of-the- art methods focus on data association techniques. The majority of them are offline algorithms. In order to achieve real-time, we need our tracking algorithm to be online.

## Framework

<div style="text-align: center">
<img src="https://alexxiao95.github.io/research/tracking/framework.png" width = "600">
</div>

The system can be roughly divided into two mainly part, which are object detection part and multi object tracking part. First, we will use the WIFI to stream the video from the drone to the computer. Then we apply object detection frame by frame. For every object in one frame, we extract the appearance feature and motion feature and send these information into multi object tracking part.