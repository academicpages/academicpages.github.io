---
title: "Orientation- and Scale-Invariant Multi-Vehicle Detection and Tracking from Unmanned Aerial Videos"
collection: publications
permalink: /publication/rsmdpi2019
date: 2009-09-16
venue: 'Remote Sensing'

---

[[Paper]](https://www.mdpi.com/2072-4292/11/18/2155)
[[Videos]](https://github.com/jwangjie/UAV-vehicle-tracking)
[[Dataset]](https://github.com/jwangjie/UAV-Vehicle-Detection-Dataset)

## Abstract
Along with the advancement of light-weight sensing and processing technologies, unmanned aerial vehicles (UAVs) have recently become popular platforms for intelligent traffic monitoring and control. UAV-mounted cameras can capture traffic-flow videos from various perspectives providing a comprehensive insight into road conditions. To analyze the traffic flow from remotely captured videos, a reliable and accurate vehicle detection-and-tracking approach is required. In this paper, we propose a deep-learning framework for vehicle detection and tracking from UAV videos for monitoring traffic flow in complex road structures. This approach is designed to be invariant to significant orientation and scale variations in the videos. The detection procedure is performed by fine-tuning a state-of-the-art object detector, You Only Look Once (YOLOv3), using several custom-labeled traffic datasets. Vehicle tracking is conducted following a tracking-by-detection paradigm, where deep appearance features are used for vehicle re-identification, and Kalman filtering is used for motion estimation. The proposed methodology is tested on a variety of real videos collected by UAVs under various conditions, e.g., in late afternoons with long vehicle shadows, in dawn with vehicles lights being on, over roundabouts and interchange roads where vehicle directions change considerably, and from various viewpoints where vehicles’ appearance undergo substantial perspective distortions. The proposed tracking-by-detection approach performs efficiently at 11 frames per second on color videos of 2720p resolution. Experiments demonstrated that high detection accuracy could be achieved with an average F1-score of 92.1%. Besides, the tracking technique performs accurately, with an average multiple-object tracking accuracy (MOTA) of 81.3%. The proposed approach also addressed the shortcomings of the state-of-the-art in multi-object tracking regarding frequent identity switching, resulting in a total of only one identity switch over every 305 tracked vehicles.

## Reference
Please cite this paper in your publications if it helps your research:

```
@article{Wang2019group,
    title={Orientation- and Scale-Invariant Multi-Vehicle Detection and Tracking from Unmanned Aerial Videos},
    author={Wang, Jie and Simeonova, Sandra and Shahbazi, Mozhdeh},
    journal={Remote Sensing},
    year={2019},
    doi={10.3390/rs11182155},
    organization={MDPI}
    }
```
