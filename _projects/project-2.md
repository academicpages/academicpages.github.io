---
title: "Segmentation model of sugarcane seedlings in a field based on satellite remote sensing"
excerpt: <img src="/images/project_dragon_fruit.png" >
collection: projects
permalink: /publication/dragon_furit
date: 2021-10-11
status: 'done'
---

Introduction
---
Farmers must accurately and promptly identify sugarcane leaf diseases with identical symptoms. RGB images have a beneficial function in disease identification. Nevertheless, complex backgrounds and identical symptoms can significantly reduce the recognition accuracy and robustness. To overcome these challenges, the SLViT hybrid network is presented, in which the transformer encoder is converted to a flexible plug-in (LViT) that is subsequently integrated into several locations of a lightweight CNN architecture (SHDC). SLViT is initially trained on the publicly available disease dataset Plant Village before being moved to the self-created sugarcane leaf disease dataset SLD10k, which consists of seven classes and 10,309 images. The ablation experiments demonstrate that all the adjustments to SLViT have contributed positively to its overall performance. SLViT outperforms six SOTA models and three custom-designed leaf-disease recognition models on Plant Village in terms of speed (1,832 FPS), weight (2 MB), consumption (50 M), and precision (98.84 %). SLViT also outperformed MobileNetV3_small on the SLD10k dataset with an accuracy bonus of 1.87 % and a size reduction of 66.3 %. The experiment also reveals that SLViT has absorbed the advantages of both the lightweight CNN and the noise-resistant transformer. This study demonstrates the applicability of SLViT for sugarcane leaf diagnosis in the field.