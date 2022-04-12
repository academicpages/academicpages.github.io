---
title: "Memory footprint reduction for the FFT-based volume integral equation method via tensor decompositions"
collection: publications
permalink: /publication/paper5
excerpt: 'We present a method of memory footprint reduction for FFT-based, EM VIE formulations. The arising Green's function tensors have low multilinear rank, which allows Tucker decomposition to be employed for their compression, thereby greatly reducing the required memory storage for numerical simulations. Consequently, the compressed components are able to fit inside a GPU on which highly parallelized computations can vastly accelerate the iterative solution of the arising linear system. In addition, the elementwise products throughout the iterative solver process require additional flops, thus, we provide a variety of novel and efficient methods that maintain the linear complexity of the classic elementwise product with an additional multiplicative small constant. We demonstrate the utility of our approach via its application to VIE simulations for the MRI of a human head. For these simulations, we report an order of magnitude acceleration over standard techniques.'
date: 2019-07-26
venue: 'IEEE Transactions on Antennas and Propagation'
paperurl: 'https://ieeexplore.ieee.org/abstract/document/8777311'
citation: 'Giannakopoulos, Ilias I., Mikhail S. Litsarev, and Athanasios G. Polimeridis. "Memory footprint reduction for the FFT-based volume integral equation method via tensor decompositions." IEEE Transactions on Antennas and Propagation 67.12 (2019): 7476-7486.'
---
