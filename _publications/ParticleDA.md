---
title: "Meteotsunamis and other anomalous “tidal surge” events in western Europe in summer 2022"
collection: publications
permalink: /publications/ParticleDA
excerpt: ''
date: 2023-03-21
venue: 'Geoscientific Model Development'
paperurl: 'https://doi.org/10.5194/gmd-2023-38'
citation: 'Giles, D. Giles, M. M. Graham, M. Giordano, T. Koskela, A. Beskos and S. Guillas: ParticleDA.jl v.1.0: A real-time data assimilation software platform. Geoscientific Model Development Discussions, in review, 2023'
---
<!-- This paper is about the number 1. The number 2 is left for future work. -->

[Download paper here]( https://doi.org/10.5194/gmd-2023-38)

## Abstract 
Digital twins of physical and human systems informed by real-time data, are becoming ubiquitous across weather forecasting, disaster preparedness, and urban planning, but researchers lack the tools to run these models effectively and efficiently, limiting progress. One of the current challenges is to assimilate observations in highly nonlinear dynamical systems, as the practical need is often to detect abrupt changes. We developed a software platform to improve the use of real-time data in highly nonlinear system representations where non-Gaussianity prevents the use of more standard Data Assimilation. Optimal Particle filtering data assimilation (DA) techniques have been implemented within an user-friendly open source software platform in Julia – ParticleDA.jl. To ensure the applicability of the developed platform in realistic scenarios, emphasis has been placed on numerical efficiency, scalability and optimisation for high performance computing frameworks. Furthermore, the platform has been developed to be forward model agnostic, ensuring that it is applicable to a wide range of modelling settings, for instance unstructured and non-uniform meshes in the spatial domain or even state spaces that are not spatially organised. Applications to tsunami and numerical weather prediction demonstrate the computational benefits in terms of lower errors, lower computational costs (due to ensemble size and the algorithm's overheads being minimised) and versatility thanks to flexible I/O in a high level language Julia.

Recommended citation: Giles, D., Graham, M. M., Giordano, M., Koskela, T., Beskos, A., and Guillas, S.: ParticleDA.jl v.1.0: A real-time data assimilation software platform, Geosci. Model Dev. Discuss. [preprint], in review, 2023.
