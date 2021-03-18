---
title: "Image Super-resolution"
excerpt: "Spatial Resolution Enhancement in Images with Linear and Learning-based Techniques<br/>
- Figure: Original and Reconstructed 'comic' Images (Scale Factor in order: 2, 3, 4)<br/>
<img src='/images/org-c(1).png'/><img src='/images/x2-c(1).png'/><img src='/images/x3-c(1).png'/><img src='/images/x4-c(1).png'/>"
collection: projects
---

Super-resolution (SR) techniques aim to increase the spatial resolution of a low-resolution (LR) image, which is acquired by an imaging device. According to the image observation model for still images, a high-resolution (HR) continuous scene is first captured by the device and digitalized by an analog-to-digital converter. After the analog-to-digital conversion, the HR image passes through a degradation system, which consists of the geometric transformation, blurring effects, downsampling, and noise addition. A general formula to define the degradation system in the image acquisition systems can be defined as follows:
<p align="center">
  <b>$\textbf{I}^{\textit{LR}} = A H C \textbf{ I}^{\textit{HR}} + N$</b><br>
</p>
                         
where $\textbf{I}^{\textit{LR}}$ is the LR image, $\textbf{I}^{\textit{HR}}$ is the HR image, C is the geometric transformation matrix, H is the blur matrix, A is the downsampling operator, and N is the noise. The ultimate goal of the SR techniques is to eliminate these degradation effects and estimate the HR image. SR is an ill-posed problem due to the downsampling operation and also an inverse problem since the input image $\textbf{I}^{\textit{HR}}$ of the degradation system is the desired output of the SR system. To solve this problem, many techniques have been discussed in the literature, which can be mainly divided into two categories based on the LR input number: Single-Input SR (SISR) techniques and Multi-Input SR (MISR) techniques. Since SR is an ill-posed problem, the mapping from the LR space to the HR space requires multiple input images with different geometric alignments or nonlinearity to estimate the lost information of the HR image.

In this project, I first implemented Irani-Peleg's IBP algorithm, an MISR technique, and compared it with a convolutional neural network (CNN) implementation. Later, I implemented a sub-pixel CNN and analyzed it with different parameters and loss functions. I used AWS for training process. During my reseach journey, I found some interesting results on the limitation of SR and on the checkerboard artifacts.
* Limitation of SR:
<p align="center">
  <img src='/images/SR-power.png'/><br/>
  <br/>First Row: Sub-pixel CNN, Second Row: Bicubic Interpolation<br/>
  Fig. 1: FFT-Error Results of ’comic’ Image<br/>
</p>
Figure 1 shows the absolute difference between the reconstructed ’comic’ image and the original image in frequency domain for different scale factors and algorithms. The width of the dark blue region shows the super-resolution power of the algorithms. Although the sub-pixel CNN is only of three layers, its super-resolution power is almost double the bicubic interpolation, which cannot recover any lost frequency component.

* Checkerboard Artifacts
<p align="center">
  <br/><img src='/images/ca.png'/><br/>
  <br/>First Row: Sub-pixel CNN with Perceptual Loss, Second Row: Sub-pixel CNN with Pixel-wise L2-Norm Loss<br/>
  Fig. 2: FFT-Error Results<br/>
</p>
The checkerboard artifacts occur in an image due to pixel replication during the upscaling process. That is, lower resolution images are duplicated in order to fill the area in the SR space. In Figure 2, the high frequency components that are associated with the checkerboard artifacts can be seen inside the red rectangles. These frequency components are related to the frequency of the squares and their harmonics. They are high frequency components since the squares repeat themselves in a short period. 

Checkerboard artifacts can be eliminated with an ideal low-pass filter. The radius of the filter should be carefully chosen. 
<p align="center">
  <br/><img src='/images/cali.png'/><img src='/images/casiz.png'/><br/>
  <br/>Left: Image before Low-pass Filtering, Right: Image after Low-pass Filtering<br/>
  Fig. 3: Reconstructed 'butterfly' Images<br/>
</p>
