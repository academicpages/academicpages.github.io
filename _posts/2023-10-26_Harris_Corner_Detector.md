---
title: "Implementing the Harris Corner Detector"
date: 2023-10-26
permalink: /posts/2023/10/HarrisCorner/
tags:
  - ComputerVision
  - Corners
  - Harris Corner Detector
---
# Implementing the Harris Corner Detector

##  The Harris Corner Detector
The Harris Corner Detector is one of the oldest interest point detectors in the toolkit of computer vision. First introduced in the 1988 paper "A Combined Corner and Edge Detector" by Chris Harris and Mike Stephens as an improvement on the Moravec corner algorithm (cite), the algorithm stands as one of the easiest interest point detectors to implement for the aspiring computer vision scienctist. In this blog post, we will implement the algorithm piece by piece to see how it works with parameters. 
![dime_building](https://github.com/LandonSwartz/landonswartz.github.io/assets/50836209/d4be9d33-a4d4-4006-910f-c13c4bdb30e6)

## Overview
The algorithm is a simple:
1. Convert the image to grayscale
2. Find the gradients (spatial derivatives) with respect to x and y
3. Set up the structure tensor based on the gradients
4. Calculate the Harris response
5. Perform non-maximal suppression for optimal values

We'll be implementing the algorithm in python for ease of use and simplicity. The focus here is learning the algorithm by building the parts of the algorithm from the ground up, not the building blocks themselves. We'll be utilizing the latest and greatest of built-in functions in OpenCV and numpy. 

### Convert the image to grayscale
Finding the gradients in the x and y direction is can be an expensive processing step for each channel of an RGB image. Therefore, the traditional harris corner detector usually starts with converting the RGB image into a grayscale image to only deal with one channel for calculations. 
```
def load_image(self, image_path):
        self.image = cv2.imread(image_path)
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
```

### Find the gradients
Computing the gradients of an image requires a special kind of process that some may be familar with if you have any experience with neural networks and convolutions where you convolve two 3x3 kernels with an image to calculate the approximations of the deriviates in both the x and y direction. The best way to understand it is to see the results in action. 
![image_gradients](https://github.com/LandonSwartz/landonswartz.github.io/assets/50836209/3118c840-a654-451a-b550-d22127b83c5f)

As you can see from the image above, Ix (the gradient in the x / hortizontal direction) finds the edges in the hortizontal direction of the image. Iy finds the edges in the vertical direction of the image. That is where the _"Combined Corner and Edge Detection"_ part of the method comes into play. Traditionally, we apply a guassian filter before finding the gradients to remove any noise from the image (especially back in the early 1990's and before Iphones when everyone had a 4K camera in their pocket).
```
def apply_gaussian_blur(self):
        self.blurred_image = cv2.GaussianBlur(self.gray_image, (self.window_size, self.window_size), 0)

    def compute_gradients(self):
        self.Ix = cv2.Sobel(self.blurred_image, cv2.CV_64F, 1, 0, ksize=self.window_size)
        self.Iy = cv2.Sobel(self.blurred_image, cv2.CV_64F, 0, 1, ksize=self.window_size)
```
Because gradients play such a huge role in computer vision, it is important we dive a little deeper into the inner workings of them. We use an operator called the Sobel operator to find gradients traditionally (remember gradients is just spatial derirvatives, so rate of change of pixels in an area). Take $G_x$ and $G_y$ as the gradients and $A$ as the original image. 

$$G_x = \begin{bmatrix} +1 & 0 & -1 \\\ +2 & 0 & -2 \\\ +1 & 0 & -1 \end{bmatrix} * A$$

$$G_y = \begin{bmatrix} +1 & +2 & +1 \\\ 0 & 0 & 0 \\\ +1 & +2 & +1 \end{bmatrix} * A$$

### Structure Tensor Construction
The Structure Tensor, or the second-moment matrix, is a matrix consisting of the gradients of a function. For our purposes, it describes the distribution of the gradients of an image in the a specific neighborhood around a point. We describe it as below:

$$ M = \Sigma_{(x, y) \in W} \begin{bmatrix} I^2_x & I_xI_y \\\ I_xI_y & I^2_y \end{bmatrix} $$

where Ix and Iy are the previous found image gradients and W is the neighborhood of the pixel we are looking. 

