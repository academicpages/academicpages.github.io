---
title: "Location-directed image modeling and its application to image interpolation"
collection: publications
permalink: /publication/location-interp
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2018-10-25
venue: '2018 25th IEEE International Conference on Image Processing (ICIP)'
paperurl: 'http://academicpages.github.io/files/paper1.pdf'
citation: '<b>Lantao Yu</b>, Michael Orchard. <b>ICIP 2018.</b>'
---
[PDF](http://academicpages.github.io/files/paper1.pdf)

## Abstract

This paper explores the development and the use of a complex-valued, multi-resolution image representation to model and exploit local image structures in image-processing applications. Our approach distinguishes itself from prior approaches by constructing and exploiting the direct relationship between the locations of local structures and representation coefficients. Coefficients of our representation have magnitudes that measure the image energy within a specific region in both space and frequency, and phases that carry information about the distance of that energy from a local reference position. Our work proposes to model relationships, both across spatial regions and across different frequency bands, among the field of coefficient magnitudes, and among the field of coefficient phases. To illustrate the advantages of modeling these relationships, we present an algorithm for interpolating a natural image by a factor of two, both horizontally and vertically. Relationships among magnitudes and phases of available bands of coefficients are exploited to estimate local edge parameters (e.g. location, orientation, sharpness) that provide information about higher-frequency coefficients that are not available in the original image. Our work produces PSNR results that are competitive with state-of-the-art single image interpolation algorithms around edges and preserves both edge sharpness and contour smoothness.
