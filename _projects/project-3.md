---
title: "Automatic labeling of object detection datasets"
excerpt: <img src="/images/projects/project_auto.png" >
collection: projects
permalink: /publication/automatic_labeling
date: 2021-11-30
status: 'done'
---

Introduction
---
This project describes a method for automatically annotating a dataset for object detection to solve the difficult manual annotation problem. The method involves manually annotating 1/10 of the dataset using LabelImg, training a Faster-RCNN model using the annotated data, and then testing the model on the remaining dataset to generate prediction boxes in the form of XML text and visualization images. Finally, the automatic annotations are adjusted manually to improve accuracy. Compared to fully manual annotation, this method greatly reduces the workload.