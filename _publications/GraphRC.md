---
title: "GraphRC: Accelerating Graph Processing on Dual-addressing Memory with Vertex Merging"
collection: publications
permalink: /publication/GraphRC
excerpt: 'This paper is about a graph processing accelerator designed for RCNVM (a dual-addressing memory based on crossbar architecture).'
date: 2022-10-29
venue: 'IEEE/ACM International Conference on Computer-Aided Design (ICCAD’22)'
paperurl: 'https://doi.org/10.1145/3508352.3549408'
---
## Abstract
To be announed.
<!-- Architectural innovation in graph accelerators attracts research attention due to foreseeable inflation in data sizes and the irregular memory access pattern of graph algorithms. Conventional graph accelerators ignore the potential of Non-Volatile Memory (NVM) crossbar as a dual-addressing memory and treat it as a traditional single-addressing memory with higher density and better energy efficiency. In this work, we present GraphRC, a graph accelerator that leverages the power of dual-addressing memory by mapping in-edge/out-edge requests to column/row-oriented memory accesses. Although the capability of dual-addressing memory greatly improves the performance of graph processing, some memory accesses still suffer from low-utilization issues. Therefore, we propose a vertex merging (VM) method that improves cache block utilization rate by merging memory requests from consecutive vertices. VM reduces the execution time of all 6 graph algorithms on all 4 datasets by 24.24% on average. We then identify the data dependency inherent in a graph limits the usage of VM, and its effectiveness is bounded by the percentage of mergeable vertices. To overcome this limitation, we propose an aggressive vertex merging (AVM) method that outperforms VM by ignoring the data dependency inherent in a graph. AVM significantly reduces the execution time of ranking-based algorithms on all 4 datasets while preserving the correct ranking of the top 20 vertices. -->

[Download paper here](http://WeiCheng14159.github.io/files/publications/GraphRC.pdf)

```
@ARTICLE{GraphRC,  
  author={Wei Cheng, Chun-Feng Wu, Yuan-Hao Chang, and Ing-Chao Lin},  
  journal={IEEE/ACM International Conference on Computer-Aided Design (ICCAD’22)},   
  title={GraphRC: Accelerating Graph Processing on Dual-addressing Memory with Vertex Merging}, 
  doi={10.1145/3508352.3549408}
}
```
