---
title: "Implementing Viola Jones Algorithm using Python and Numba"
excerpt: "Python and Numba-based open source implementation of Viola Jones Cascade Classifier training procedure<br/><img src='/images/thumbnail_vj.jpg'>"
collection: portfolio
---

## Viola Jones Cascade Classifier Training
This repository provides a Python implementation for training a cascade classifier using Viola-Jones algorithm. The code has been optimized using Numba's Just in Time compilation to run almost as fast as the C++ implementation provided by OpenCV. There is no efficient Python-based implementation available on Github, and this repo can be used by researchers and practitioners who want to experiment with training cascade classifiers.

For data preparation, and training and detection usage details, please check the [Github repository](https://github.com/abhishekiitm/py_viola_jones).

<img src="/images/vj_detection.jpg" width="50%"/>

Fig. Detections on the FDDB dataset