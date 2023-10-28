---
title: "The Harris Corner Detector"
date: 2023-10-26
---

# Harris Corner Detector
The Harris Corner Detector is one of the oldest interest point detectors in the toolkit of computer vision. First introduced in the 1988 paper "A Combined Corner and Edge Detector" by Chris Harris and Mike Stephens as an improvement on the Moravec corner algorithm (cite), the algorithm stands as one of the easiest interest point detectors to implement for the aspiring computer vision scienctist. In this blog post, we will implement the algorithm piece by piece to see how it works with parameters. 
![dime_building](https://github.com/LandonSwartz/landonswartz.github.io/assets/50836209/b6447321-db32-4fa2-b3d7-3490c2338194)
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



