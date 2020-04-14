---
title: "Greedy kernel change-point detection"
collection: publications
permalink: /publication/ieee-kernel-2019
excerpt: 'A novel non-parametric and model-free off-line change-point detection method based on a kernel mapping is presented.'
date: 2010-10-01
venue: 'IEEE Transactions on Signal Processing'
paperurl: # 'http://academicpages.github.io/files/paper2.pdf'
citation: 'Truong, C., Oudre, L., & Vayatis, N. (2019). Greedy kernel change-point detection. IEEE Transactions on Signal Processing, 67(24).'
---
[[doi]](https://doi.org/10.1109/TSP.2019.2953670) [[pdf]](http://deepcharles.github.io/files/ieee-kernel-2019.pdf)

**Abstract.** We consider the problem of detecting abrupt changes in the underlying stochastic structure of multivariate signals. A novel non-parametric and model-free off-line change-point detection method based on a kernel mapping is presented. This approach is sequential and alternates between two steps: a greedy detection to estimate a new breakpoint and a projection to remove its contribution to the signal. The resulting algorithm is able to segment time series for which no accurate model is available: it is computationally more efficient than exact kernel change-point detection and more precise than window based approximations. The proposed method also offers some theoretical consistency properties. For the special case of a linear kernel, an even faster implementation is provided. The proposed strategy is compared to standard parametric and nonparametric procedures on a real-world data set composed of 262 accelerometer recordings.