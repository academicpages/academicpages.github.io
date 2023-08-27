---
title: 'Week eleven (Aug 7, 2023 - Aug 14, 2023)'
collection: gsoc
---

This is the eleventh week of my GSoC journey.

GSoC project
=================
*  [GSoC project URL](https://summerofcode.withgoogle.com/programs/2023/projects/HKW6ydaI)
*  [Work Repository](https://github.com/Mustardburger/CellBox)

Tasks
=================
1. After a simple bug fix, where the argument `shuffle=True` should have been set to `shuffle=False` for the test dataloader so that the prediction rows align with the indices specified in `random_pos.csv`, Figure 2C generated from 500 CellBox Pytorch models now resembles very closely the figure in the original paper, even capturing some outliers in the original scatterplot.
2. Meet Dr. Chris Sander and Augustin in person during trip to Boston.

Relevant issues:
================
* Blogs about Pytorch having suboptimal convergence when compared with TensorFlow model ([this](https://discuss.pytorch.org/t/suboptimal-convergence-when-compared-with-tensorflow-model/5099) and [this]https://stackoverflow.com/questions/73600481/400-higher-error-with-pytorch-compared-with-identical-keras-model-with-adam-op)

Notes
=================
Check out my [personal GSoC notebook](https://docs.google.com/document/d/1fYkUNYuRcPHByWUYay6yUeTKtBuiwTGKJoztT0LajiA/edit?usp=sharing), where I keep my observations and comments in one place.
