---
title: "Attempting capture shock with discontinuous Galerkin method"
excerpt: "<img src='/images/MachNum_2504_V1.jpg'>"
collection: portfolio
---
by Zhicheng Kai, Weihao Liu, Haoran Shi, Andrew Wang Su, and Yuhao Zhou (in no particular order)

The Discontinuous Galerkin (DG, \cite{fish2007first}) method is a popular Finite Element Method (FEM) that treats the computational domain as smaller, non-overlapping subdomains with polynomial approximations to represent the states. However, with these discontinuities, oscillations may appear in higher-order DG methods, such as the Gibbs phenomenon \cite{gottlieb1997gibbs}, making well-fit limiters necessities. 

In this project, we applied the Runge-Kutta Discontinuous Galerkin (RKDG, \cite{cockburn2001runge}) method for shock capturing, which is promising for implementing the Finite Volume Method (FVM) limiters to the DG codes% without requiring the development of new limiters
. The $p$-order states are first interpolated to $p=1$, equivalent to the second-order FVM states. Then, a second-order FVM limiter is implemented to the states with oscillations. Once active, it will reconstruct limited states and project them backward to order $p$.
