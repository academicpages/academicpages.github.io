---
title: 'Week ten (Jul 31, 2023 - Aug 7, 2023)'
collection: gsoc
---

This is the tenth week of my GSoC journey.

GSoC project
=================
*  [GSoC project URL](https://summerofcode.withgoogle.com/programs/2023/projects/HKW6ydaI)
*  [Work Repository](https://github.com/users/cannin/projects/5)
Mentor: **Augustin Luna** and **Bo Yuan**

Tasks
=================
1. Correct mask has been fixed for CellBox Pytorch, and 500 models are being retrained with the updated model.
2. Check some blogs about other people's complaining different behaviour and suboptimal training performance of Pytorch compared with Tensorflow (for example, [this](https://discuss.pytorch.org/t/suboptimal-convergence-when-compared-with-tensorflow-model/5099) and [this]https://stackoverflow.com/questions/73600481/400-higher-error-with-pytorch-compared-with-identical-keras-model-with-adam-op). Overall, people tend to see a similar trend where Pytorch and Tensorflow models converge differently despite identical hyperparams and inputs. But the causes are very varied.
3. Implement a unit test to compare the output of Pytorch and Tensorflow CellBox models after one feedforward loop (without backprop) with indentical input and weight initializations.

Relevant issues:
================
* Blogs about Pytorch having suboptimal convergence when compared with TensorFlow model ([this](https://discuss.pytorch.org/t/suboptimal-convergence-when-compared-with-tensorflow-model/5099) and [this]https://stackoverflow.com/questions/73600481/400-higher-error-with-pytorch-compared-with-identical-keras-model-with-adam-op)

Notes
=================
Check out my [personal GSoC notebook](https://docs.google.com/document/d/1fYkUNYuRcPHByWUYay6yUeTKtBuiwTGKJoztT0LajiA/edit?usp=sharing), where I keep my observations and comments in one place.
