---
layout: archive
title: "Research"
permalink: /research/
excerpt: "Research"
author_profile: true
---

My research in the [Miller group](https://millergroup.caltech.edu/Miller_Group/Home.html) at Caltech is to bridge the gap between the world of quantum physics and the world of chemistry through machine learning.
The basic elements of chemistry are atoms and molecules, whose behavior is governed by quantum mechanics.
Based on the principles of the quantum mechanics, quantum chemistry methods offers a way to calculate the properties of molecules.
However, for a lot of large or medium sized molecules, it is not easy to reach the desired accuracy for the chemists within an acceptable computational cost.
Thus, we developed _Molecular-Orbital-Based Machine Learning_ (MOB-ML) [1,2,3] to obtain the molecular properties in the level of highly accurate but expensive wavefunction theory from the cheap Hartree-Fock method.

My contribution to MOB-ML includes both the physics side and the machine learning side.
On the physics side, I worked with my collaborators to design the MOB-ML to satisfy all the physical requirements of a good quantum chemistry theory, including a few permutation symmetries and size consistency. [3]
Such careful design significantly increases the transferability for various of systems including organic molecules, intermolecular interactions and transition states, etc.
On the machine learning side, I improved the Gaussian Process algorithm by the Black-box Matrix Multiplication technique, and finally scaled up the machine learning by more than 30 times without loss of learnability.

[1] Welborn, Matthew, Lixue Cheng, and Thomas F. Miller III. "Transferability in machine learning for electronic structure via the molecular orbital basis." Journal of chemical theory and computation 14, no. 9 (2018): 4772-4779.  
[2] Cheng, Lixue, Matthew Welborn, Anders S. Christensen, and Thomas F. Miller III. "A universal density matrix functional from molecular orbital-based machine learning: Transferability across organic molecules." The Journal of chemical physics 150, no. 13 (2019): 131103.  
[3] Husch, Tamara, Jiace Sun, Lixue Cheng, Sebastian JR Lee, and Thomas F. Miller III. "Improved accuracy and transferability of molecular-orbital-based machine learning: Organics, transition-metal complexes, non-covalent interactions, and transition states." The Journal of Chemical Physics 154, no. 6 (2021): 064108.  
