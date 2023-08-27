---
title: 'Week seven (Jul 10, 2023 - Jul 17, 2023)'
collection: gsoc
---

This is the seventh week of my GSoC journey.

GSoC project
=================
*  [GSoC project URL](https://summerofcode.withgoogle.com/programs/2023/projects/HKW6ydaI)
*  [Work Repository](https://github.com/Mustardburger/CellBox)

Tasks
=================
1. Work on the GSoC midterm evaluation
2. Fix several bugs in the Pytorch traning loop `train_torch.py`:
    * Change the model weight matrix from a `torch.tensor` to a `nn.Parameter` to enable gradient flow.
    * Add in the option of choosing `args.pert_form` that affects the loss function during backprop.
3. Replicate Figure 2A and 2B using the current Pytorch code
4. Discuss a strange numerical discrepancy issue when writing tests for Pytorch ODE solver. In particular, given identical input and parameters, Tensorflow and Pytorch ODE solvers agreed to the error of `10e-8` for the first 100 time steps, but drastically diverged from 100 to 200 time steps. This phenomenon occurs for all inputs and parameters.

Relevant issues:
================
* change-util-functions-and-models ([branch](https://github.com/Mustardburger/CellBox/tree/change-util-functions-and-models))
* Numerical instability between Tensorflow and Pytorch ([#56](https://github.com/sanderlab/CellBox/issues/56))

Notes
=================
Check out my [personal GSoC notebook](https://docs.google.com/document/d/1fYkUNYuRcPHByWUYay6yUeTKtBuiwTGKJoztT0LajiA/edit?usp=sharing), where I keep my observations and comments in one place.
