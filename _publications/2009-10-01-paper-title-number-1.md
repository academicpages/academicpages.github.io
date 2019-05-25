---
title: "A comparative evaluation of systems for scalable linear algebra-based analytics"
collection: publications
permalink: /publication/2009-10-01-paper-title-number-1
excerpt: 
date: 2018-09-01
venue: 'Proceedings of the VLDB Endowment'
paperurl: 'http://thomas9t.github.io/files/SLAB.pdf'
citation: ''
---

The growing use of statistical and machine learning (ML) algorithms to analyze large datasets has given rise to new systems to scale such algorithms. But implementing new scalable algorithms in low-level languages is a painful process, especially for enterprise and scientific users. To mitigate this issue, a new breed of systems expose high-level bulk linear algebra (LA) primitives that are scalable. By composing such LA primitives, users can write analysis algorithms in a higher-level language, while the system handles scalability issues. But there is little work on a unified comparative evaluation of the scalability, efficiency, and effectiveness of such "scalable LA systems." We take a major step towards filling this gap. We introduce a suite of LA-specific tests based on our analysis of the data access and communication patterns of LA workloads and their use cases. Using our tests, we perform a comprehensive empirical comparison of a few popular scalable LA systems: MADlib, MLlib, SystemML, ScaLAPACK, SciDB, and TensorFlow using both synthetic data and a large real-world dataset. Our study has revealed several scalability bottlenecks, unusual performance trends, and even bugs in some systems. Our findings have already led to improvements in SystemML, with other systems' developers also expressing interest. All of our code and data scripts are available for download at https://adalabucsd.github.io/slab.html.

Recommended Citation: Anthony Thomas and Arun Kumar. 2018. A comparative evaluation of systems for scalable linear algebra-based analytics. Proceedings of the VLDB Endowment 11, 13 (September 2018), 2168-2182. DOI: https://doi.org/10.14778/3275366.3284963

[Download paper here](http://thomas9t.github.io/files/SLAB.pdf)
