---
title: "3D Gaussian Splatting Representation Compression"
excerpt: "Application of Learned Image/Video Compression Methods on 3D Gaussian Splatting"
collection: portfolio
---

3D Gaussian splatting has recently gained immense popularity due to its high parallelizability and efficiency,
allowing 3D scenes to be rendered faster than neural radiance field-based methods while maintaining compa-
rable quality. However, representing a scene with 3D Gaussian splatting requires a large number of Gaussian
primitives, from hundreds of thousands to several millions, resulting in high storage complexity. To address
this issue, we investigate the use of learned entropy models from the image compression literature and resid-
ual coding for Gaussian attribute compression. We also explore enhancements to the 3D Gaussian splatting
algorithm using a Markov Chain Monte Carlo framework and investigate methods to reduce the number
of Gaussian primitives through learned primitive masking and importance-based pruning. Our experiments
show that optimizing Gaussian primitives with the Markov Chain Monte Carlo framework significantly im-
proves the visual quality of novel view synthesis. Additionally, learned primitive masking and importance-
based pruning can reduce the number of Gaussian primitives by up to half without notable quality loss. We
demonstrate that learned entropy modeling, combined with a hyperprior network, can integrate seamlessly
into optimized Gaussian primitives, reducing their size by up to 10 times without degrading visual quality.
As the integration does not require any modification in Gaussian primitives, it is an easy method to adopt.
Further investigation of hierarchy generation and residual coding reveals that hierarchy structure with octree
representation and weighted averaging does not allow for higher compression efficiency, indicating a more
complex Gaussian attribute prediction scheme might be required to increase storage efficiency. These find-
ings highlight the potential for further storage improvements in 3D Gaussian splatting while maintaining
high visual quality, paving the way for scalable rendering techniques.

For further information, please refer to the [report](/files/3dgs-compression/3D-GS-Compression.pdf) and the [presentation](/files/3dgs-compression/3D-GS-Compression.pptx) I have prepared for my MSc semester thesis.

The details of the implementation can be accessed in [Github](https://github.com/erenovic/GSCompression).

<img src='/files/3dgs-compression/3dgs-compression.png' alt='3D Gaussian Splatting Representation Compression' width='600' height='700'>

