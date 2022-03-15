---
title: "A Framework for Graph Sampling and Random Walk on GPUs"
excerpt: "<br/> Many applications require to learn, mine, analyze and visualize large-scale graphs. These graphs are often too large to be addressed efficiently using conventional graph processing technologies. Many applications have requirements to analyze, transform, visualize and learn large scale graphs. These graphs are often too large to be addressed efficiently using conventional graph processing technologies. Recent literatures convey that graph sampling/random walk could be an efficient solution. In this paper, we propose, to the best of our knowledge, the first GPU-based framework for graph sampling/random walk. First, our framework provides a generic API which allows users to implement a wide range of sampling and random walk algorithms with ease. Second, offloading this framework on GPU, we introduce warp-centric parallel selection, and two optimizations for collision migration. Third, towards supporting graphs that exceed GPU memory capacity, we introduce efficient data transfer optimizations for out-of-memory sampling, such as workload-aware scheduling and batched multi-instance sampling. In its entirety, our framework constantly outperforms the state-of-the-art projects. First, our framework provides a generic API which allows users to implement a wide range of sampling and random walk algorithms with ease. Second, offloading this framework on GPU, we introduce warp-centric parallel selection, and two novel optimizations for collision migration. Third, towards supporting graphs that exceed the GPU memory capacity, we introduce efficient data transfer optimizations for out-of-memory and multi-GPU sampling, such as workload-aware scheduling and batched multi-instance sampling. Taken together, our framework constantly outperforms the state of the art projects in addition to the capability of supporting a wide range of sampling and random walk algorithms.
<br />

[Paper](https://arxiv.org/abs/2009.09103) <br />
[Source code](https://github.com/concept-inversion/C-SAW) <br />

 <img src='/images/csaw.png'>"
collection: portfolio
---
