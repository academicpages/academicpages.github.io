---
title: "Compression of volume-surface integral equation matrices via Tucker decomposition for magnetic resonance applications"
collection: publications
permalink: /publication/paper2
excerpt: 'In this work, we propose a method for the compression of the coupling matrix in volume-surface integral equation (VSIE) formulations. VSIE methods are used for electromagnetic (EM) analysis in magnetic resonance imaging (MRI) applications, for which the coupling matrix models the interactions between the coil and the body. We showed that these effects can be represented as independent interactions between remote elements in 3-D tensor formats, and subsequently decomposed with the Tucker model. Our method can work in tandem with the adaptive cross approximation (ACA) technique to provide fast solutions of VSIE problems. We demonstrated that our compression approaches can enable the use of VSIE matrices of prohibitive memory requirements, by allowing the effective use of modern graphical processing units (GPUs) to accelerate the arising matrix-vector products. This is critical to enable numerical MRI simulations at clinical voxel resolutions in a feasible computation time. In this article, we demonstrate that the VSIE matrix-vector products needed to calculate the EM field produced by an MRI coil inside a numerical body model with 1 mm^3 voxel resolution, could be performed in ~33 s in a GPU, after compressing the associated coupling matrix from ~80 TB to ~43 MB.'
date: 2021-06-25
venue: 'IEEE Transactions on Antennas and Propagation'
paperurl: 'https://ieeexplore.ieee.org/abstract/document/9465722'
citation: 'Giannakopoulos, Ilias I., et al. "Compression of volume-surface integral equation matrices via Tucker decomposition for magnetic resonance applications." IEEE Transactions on Antennas and Propagation (2021).'
---
