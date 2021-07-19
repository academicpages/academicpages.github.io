---
permalink: /
title: "Personal Profile"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am second-year PHD working on Machine Learning. 

Research interest includes Converging Speed-up of DNN, Combinatorial Problem Solving with Reinforcement Learning and General Machine Learning Application. 
Current works are about Topopligical Scheduling of Systm Memory, Material&Thickness Selection during Chip Architecture Design.

Projects:
======

Regularization Method Development
------
Design new regularization method called ‘Dreg’ which can boost the speed(nearly 50%) and improve the accuracy of
traditional deep learning especially in large batch;

Training various models(ResNet18, MobileNetV2 and VGG16) on different datasets(MNIST, CIFAR10 and CIFAR100) with
new ‘Dreg’ Method’(Pytorch, CUDA, Vim, Linux).

Memory Scheduling
------
Schedule memory and computation resources for each task based on task priority with Reinforcement Learning Agent-Pointer Network(achieve nearly 80% Recall Accuracy on huge number of task request);

Design datasets to simulate real system request for training and evaluation(Pytorch, CUDA, Vim, Linux);

Apply new method on model layers sheduling of edgetpu.

Material-Thickness Selection for Chip Configuration
------
Select material and thickness for each layer of chip with Reinforcement Learning Agent-Pointer Network(Successfully Recognize special pattern by training only 16 data points);

Modify traditional pointer network to achieve twin decoding requests for material and thickness, build connection between them for better performance(Pytorch, CUDA, Vim, Linux);

Adjust reward function for better guidance.
