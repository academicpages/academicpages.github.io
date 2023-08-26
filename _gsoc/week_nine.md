---
title: 'Week nine (Jul 24, 2023 - Jul 31, 2023)'
collection: gsoc
---

This is the ninth week of my GSoC journey.

GSoC project
=================
*  [GSoC project URL](https://summerofcode.withgoogle.com/programs/2023/projects/HKW6ydaI)
*  [Work Repository](https://github.com/users/cannin/projects/5)
Mentor: **Augustin Luna** and **Bo Yuan**

Tasks
=================
1. Try out a different Pytorch ODE solver ([package](https://github.com/rtqichen/torchdiffeq)) and compare it with the current CellBox ODE solvers in Tensorflow and Pytorch. Preliminary results showed with the same input and parameters, all 3 solvers led to very different results.
2. Recheck a bug of implementing the mask on CellBox adjacency matrix. Gradients are not supposed to flow through the mask, but CellBox Pytorch did.
3. Retrain 500 models with different seeds using the original Tensorflow code and replicate Figure 2C to ensure current method for replicating Figure 2C is correct. This method will then be used on CellBox Pytorch.

Relevant issues:
================
* ([torchdiffeq](https://github.com/rtqichen/torchdiffeq))

Notes
=================
Check out my [personal GSoC notebook](https://docs.google.com/document/d/1fYkUNYuRcPHByWUYay6yUeTKtBuiwTGKJoztT0LajiA/edit?usp=sharing), where I keep my observations and comments in one place.
