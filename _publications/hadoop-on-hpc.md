---
title: "Hadoop on HPC: Integrating Hadoop and Pilot-Based Dynamic Resource Management"
collection: publications
permalink: /publication/hadoop-on-hpc
date: 2016-05-25
venue: '2016 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW)'
paperurl: 'http://ieeexplore.ieee.org/document/7530058/'
citation: 'Andre Luckow, Ioannis Paraskevakos, George Chantzialexiou, Shantenu Jha 
Hadoop on HPC: Integrating Hadoop and Pilot-Based Dynamic Resource Management 
2016 IEEE International Parallel and Distributed Processing Symposium Workshops (IPDPSW).'
---

## Abstract:

High performance distributed computing environments have traditionally been designed to meet the compute demands of scientific applications, supercomputers have historically been producers and not consumers of data. The Apache Hadoop ecosystem has evolved to address many of the traditional limitations of HPC platforms. There exist a whole class of scientific applications that need the collective capabilities of traditional high-performance computing environments and the Apache Hadoop ecosystem. For example, the scientific domains of bio-molecular dynamics, genomics and high-energy physics need to couple traditional computing with Hadoop/Spark based analysis. We investigate the critical question of how to present both capabilities to such scientific applications. Whereas this questions needs answers at multiple levels, we focus on the design of middleware that might support the needs of both. We propose extensions to the Pilot-Abstraction so as to provide a unifying resource management layer. This provides an important step towards integration and thereby interoperable use of HPC and Hadoop/Spark, and allows applications to efficiently couple HPC stages (e.g. simulations) to data analytics. Many supercomputing centers have started to officially support Hadoop environments either in a dedicated environment or in hybrid deployments using tools, such as myHadoop. However, this typically involves many intrinsic, environment-specific details that need to be mastered, and often swamp conceptual questions like: How best to couple HPC and Hadoop application stages? How to explore runtime trade-offs (data localities vs. data movement)? This paper provides both conceptual understanding and practical solutions to questions central to the integrated use of HPC and Hadoop environments. Our experiments are performed on state-of-the-art production HPC environments and provide middleware for multiple domain sciences.

