---
title: "Implicit multirate gark methods"
collection: publications
permalink: /publication/implicit-gark
excerpt: 'Multirate, Time integration, Implicit methods, Stability analysis'
venue: 'Journal of Scientific Computing'
date: '2021-01-01'
paperurl: 'https://arxiv.org/pdf/1910.14079.pdf'
---
This work considers multirate generalized-structure additively partitioned Runge–Kutta (MrGARK) methods for solving stiff systems of ordinary
differential equations (ODEs) with multiple time scales. These methods treat different partitions of the system with different timesteps for a more targeted and
efficient solution compared to monolithic single rate approaches. With implicit
methods used across all partitions, methods must find a balance between stability
and the cost of solving nonlinear equations for the stages. In order to characterize
this important trade-off, we explore multirate coupling strategies, problems for assessing linear stability, and techniques to efficiently implement Newton iterations
for stage equations. Unlike much of the existing multirate stability analysis which
is limited in scope to particular methods, we present general statements on stability and describe fundamental limitations for certain types of multirate schemes.
New implicit multirate methods up to fourth order are derived, and their accuracy
and efficiency properties are verified with numerical tests.

[Preprint](https://arxiv.org/pdf/1910.14079.pdf) / [Paper](https://link.springer.com/article/10.1007/s10915-020-01400-z)
