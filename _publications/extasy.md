---
title: "ExTASY: Scalable and flexible coupling of MD simulations and advanced 
sampling techniques"
collection: publications
permalink: /publication/extasy
excerpt: 'This paper is about a framework enabling advanced molecular sampling
techniques on HPCs'
date: 2016-10-27
venue: 'IEEE 12th International Conference on e-Science (e-Science), 2016'
paperurl: 'http://ieeexplore.ieee.org/abstract/document/7870921/'
citation: 'Balasubramanian, Vivekanandan, Iain Bethune, Ardita Shkurti, Elena 
Breitmoser, Eugen Hruska, Cecilia Clementi, Charles Laughton, and Shantenu Jha. 
"Extasy: Scalable and flexible coupling of md simulations and advanced sampling
techniques." In e-Science (e-Science), 2016 IEEE 12th International Conference 
on, pp. 361-370. IEEE, 2016.'
---

## Abstract:

For many macromolecular systems the accurate sampling of the relevant regions on
the potential energy surface cannot be obtained by a single, long Molecular 
Dynamics (MD) trajectory. New approaches are required to promote more efficient 
sampling. We present the design and implementation of the Extensible Toolkit for
Advanced Sampling and analYsis (Ex-TASY) for building and executing advanced 
sampling workflows on HPC systems. ExTASY provides Python based “templated 
scripts” that interface to an interoperable and high-performance pilot-based run
time system, which abstracts the complexity of managing multiple simulations. 
ExTASY supports the use of existing highly-optimised parallel MD code and their 
coupling to analysis tools based upon collective coordinates which do not 
require a priori knowledge of the system to bias. We describe two workflows 
which both couple large “ensembles” of relatively short MD simulations with 
analysis tools to automatically analyse the generated trajectories and identify
molecular conformational structures that will be used on-the-fly as new starting
points for further “simulation-analysis” iterations. One of the workflows 
leverages the Locally Scaled Diffusion Maps technique; the other makes use of 
Complementary Coordinates techniques to enhance sampling and generate 
start-points for the next generation of MD simulations. We show that the ExTASY 
tools have been deployed on a range of HPC systems including ARCHER (Cray CX30),
Blue Waters (Cray XE6/XK7), and Stampede (Linux cluster), and that good strong 
scaling can be obtained up to 1000s of MD simulations, independent of the size 
of each simulation. We discuss how ExTASY can be easily extended or modified by 
end-users to build their own workflows, and ongoing work to improve the 
usability and robustness of ExTASY.