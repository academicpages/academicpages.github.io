---
title: "Image Super-resolution"
excerpt: "Spatial Resolution Enhancement in Images with Linear and Learning-based Techniques<br/>
- Figure: Original and Reconstructed Images (Scale Factor in order: 2, 3, 4)<br/>
<img src='/images/org-c(1).png'/><img src='/images/x2-c(1).png'/><img src='/images/x3-c(1).png'/><img src='/images/x4-c(1).png'/>"
collection: projects
---

Super-resolution (SR) techniques aim to increase the spatial resolution of a low-resolution (LR) image which is acquired by an imaging device. According to the image observation model for still images, a high-resolution (HR) continuous scene is first captured by the device and digitalized by an analog-to-digital converter. After the analog-to-digital conversion, the HR image passes through a degradation system which consists of the geometric transformation, blurring effects, downsampling, and noise addition. A general formulae to define the degradation system in the image acquisition systems can be defined as follows:

$\textbf{I}^{\textit{LR}} = A H C \textbf{ I}^{\textit{HR}} + N$
