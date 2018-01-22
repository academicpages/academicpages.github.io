---
title: "Growing Tree Structured Cascade"
collection: teaching
permalink: /projects/2014-spring-teaching-1
startdate: 2017-June-01
startmonth: March
enddate: 2017-September-01
endmonth: September
---

In this project we describe a way to determine the optimal tree structured cascade configuration.

## Cascading Architecture

Consider a binary classification problem in which the datalabels are imbalanced ( # 0's >> #1's). Often, in these sort of problems classifying a datapoint with its correct label '1' is much harder task than classifying a datapoint correctly with label '0'. So, computationally we want to design a model which puts little effort is labelling datapoint as '0' and more effort effort in labelling datapoint as '1'. Cascading Architeture, first discussed in [1] addresses this. 
{% include image.html url="/images/linearcascade.png" width=450 align="right" %}

In this architeture we have a bunch of classifiers $ n $ with increasing capacity ( 1< 2 < .. < n). $P_{i}(x)$ is the probability that datapoint $x$ is '1' by $i^{th}$ classifier. The datapoint is passed throught all classifiers which are ordered accoring to their capacity. If a classifier labels the point as '0' with probability > 0.5, Cascading model is gonna classify it as 0. A point is gonna labelled as '1' only when all the $ n $ classifiers output with probability > 0.5.

## Heading 2

hi
## References
[1]Paul Viola and Michael Jones. Rapid object detection using a boosted cascade of simple features. In Computer Vision and Pattern Recognition, 2001. CVPR 2001. Proceedings of the 2001 IEEE Computer Society Conference on, volume 1, pages I–I. IEEE, 2001.
