---
title: "DSXplore: Optimizing Convolutional Neural Networks via Sliding-Channel Convolutions"
collection: publications
permalink:  /publication/08-DSXplore-2021
date: 2021-05-17
venue: 'IPDPS'
paperurl: 'https://arxiv.org/pdf/2101.00745.pdf'
---
+ Propose and implement the first optimized design for exploring deep separable convolution on
CNNs; 
+ At the algorithm level, we incorporate a novel sliding-channel convolution (SCC), featured
with filter-channel overlapping to balance the accuracy performance and the reduction of computation
and memory cost;
+ At the implementation level, we build an optimized GPU-implementation tailored
for SCC by leveraging several key techniques, such as the input-centric backward propagation and the
channel-cyclic optimization; 
+ Integrate the SCC into the existing Pytorch framework as a new type of
convolution operator.
+ Project Open-source publicly at [Github](git@github.com:YukeWang96/DSXplore.git).