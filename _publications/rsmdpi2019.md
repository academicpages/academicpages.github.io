---
title: "Orientation- and Scale-Invariant Multi-Vehicle Detection and Tracking from Unmanned Aerial Videos"
collection: publications
permalink: /publications/rsmdpi2019
date: 2019-09-16
venue: 'Remote Sensing'
---

[[Paper]](https://www.mdpi.com/2072-4292/11/18/2155)
[[Poster]](https://jwangjie.github.io/publications/rsmdpi2019/DLRL2019.pdf)
[[Videos]](https://github.com/jwangjie/UAV-vehicle-tracking)
[[software]](https://github.com/jwangjie/Fine-tune-YOLOv3)
[[Dataset]](https://github.com/jwangjie/UAV-Vehicle-Detection-Dataset)

**This paper proposes a deep-learning pipeline for multiple vehicle detection and tracking from UAV videos. This approach works reliably for vehicle tracking with significant orientation and scale variations.**

<div style="text-align: center">
<img src="https://jwangjie.github.io/publications/rsmdpi2019/rs2019.gif"/>
</div>

## Abstract
Along with the advancement of light-weight sensing and processing technologies, unmanned aerial vehicles (UAVs) have recently become popular platforms for intelligent traffic monitoring and control. UAV-mounted cameras can capture traffic-flow videos from various perspectives providing a comprehensive insight into road conditions. To analyze the traffic flow from remotely captured videos, a reliable and accurate vehicle detection-and-tracking approach is required. In this paper, we propose a deep-learning framework for vehicle detection and tracking from UAV videos for monitoring traffic flow in complex road structures. This approach is designed to be invariant to significant orientation and scale variations in the videos. The detection procedure is performed by fine-tuning a state-of-the-art object detector, You Only Look Once (YOLOv3), using several custom-labeled traffic datasets. Vehicle tracking is conducted following a tracking-by-detection paradigm, where deep appearance features are used for vehicle re-identification, and Kalman filtering is used for motion estimation. The proposed methodology is tested on a variety of real videos collected by UAVs under various conditions, e.g., in late afternoons with long vehicle shadows, in dawn with vehicles lights being on, over roundabouts and interchange roads where vehicle directions change considerably, and from various viewpoints where vehicles’ appearance undergo substantial perspective distortions. The proposed tracking-by-detection approach performs efficiently at 11 frames per second on color videos of 2720p resolution. Experiments demonstrated that high detection accuracy could be achieved with an average F1-score of 92.1%. Besides, the tracking technique performs accurately, with an average multiple-object tracking accuracy (MOTA) of 81.3%. The proposed approach also addressed the shortcomings of the state-of-the-art in multi-object tracking regarding frequent identity switching, resulting in a total of only one identity switch over every 305 tracked vehicles.

<div style="text-align: center">
<img src="https://jwangjie.github.io/publications/rsmdpi2019/roundabout.png"/>
</div>

## Framework 
<div style="text-align: center">
<img src="https://jwangjie.github.io/publications/rsmdpi2019/framework.png" />
</div>
This figure illustrates the framework of our proposed method for multiple vehicle tracking-by-detection. Detection: the vehicle detector was fine-tuned on YOLOv3 by a custom labeled dataset together with two other datasets. Re-Id training: deep vehicle Re-Id appearance features were extracted by training a wide residual network with the VeRi dataset. Tracking: the detected bounding boxes were used to calculate the Mahalanobis distance as the motion metric, and the pixels inside the bounding boxes were used to calculate the minimum cosine distance as the deep appearance similarity metric; the two metrics were then integrated in a weighted form to conduct data association using cascade matching.

## Dataset 
The software packages we used includes [YOLOv3](https://github.com/AlexeyAB/darknet) for vehicle detection, [Deep Cosine Metric Learning](https://github.com/nwojke/cosine_metric_learning) for vehicle Re-identification and [Deep SORT](https://github.com/Qidian213/deep_sort_yolov3) for vehicle tracking. The dataset fine-tunes the vehicle detector includes 154 images from [aerial-cars-dataset](https://github.com/jekhor/aerial-cars-dataset), 1374 images from the M0606 folder [UAVDT-Benchmark](https://sites.google.com/site/daviddo0323/projects/uavdt), and our custom-labeled 157 images. The whole dataset created following YOLOv3 labeling format can be found at [UAV-Vehicle-Detection-Dataset](https://github.com/jwangjie/UAV-Vehicle-Detection-Dataset), which is available upon request.

<div style="text-align: center">
<img src="https://jwangjie.github.io/publications/rsmdpi2019/yolo_dataset.png" 
     width="680px" height="380px"/>
</div>

The dataset used for vehicle Re-identification training is [VeRi](https://github.com/VehicleReId/VeRidataset). 
<div style="text-align: center">
<img src="https://jwangjie.github.io/publications/rsmdpi2019/veri_dataset.png" 
     width="680px" height="230px"/>
</div>


## Reference
Please cite this paper in your publications if it helps your research:

```
@article{wang2019orientation,
  title={Orientation-and Scale-Invariant Multi-Vehicle Detection and Tracking from Unmanned Aerial Videos},
  author={Wang, Jie and Simeonova, Sandra and Shahbazi, Mozhdeh},
  journal={Remote Sensing},
  volume={11},
  number={18},
  pages={2155},
  year={2019},
  publisher={Multidisciplinary Digital Publishing Institute}
}
```
