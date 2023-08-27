---
title: 'Week four (Jun 19, 2023 - Jun 26, 2023)'
collection: gsoc
---

This is the fourth week of my GSoC journey.

GSoC project
=================
*  [GSoC project URL](https://summerofcode.withgoogle.com/programs/2023/projects/HKW6ydaI)
*  [Work Repository](https://github.com/Mustardburger/CellBox)

Tasks
=================
1. (Per Augustin's request): Learn Github Actions to automate testing process.
2. Reimplement linear regression model (LinReg) using Pytorch
I decided to start off with the LinReg model first because it is simpler to implement than CellBox, and it is a good test case to ensure the training loop in Pytorch works as expected.
Reimplementing this model takes several steps:
* Create the new `model_torch.py` file. I plan to keep the PertBio base class, but I change it to inherit nn.Module and change many of its variables.
* Rewrite the LinReg Pytorch model. This object inherits PertBio and will include a forward funtion that defines a forward pass through the model.
* Rewrite the loss function and the optimizer, turning it into its Pytorch counterpart.
3. Rewrite the training loop.
After the new Pytorch model is defined, I will reimplement part of the training loop. The Pytorch model will be trained, but the loop at this point will not have features such as early stopping or saving screenshots.

Relevant issues:
================
* LinReg has no self.train_y0 ([#50](https://github.com/sanderlab/CellBox/issues/50))

Notes
=================
Check out my [personal GSoC notebook](https://docs.google.com/document/d/1fYkUNYuRcPHByWUYay6yUeTKtBuiwTGKJoztT0LajiA/edit?usp=sharing), where I keep my observations and comments in one place.
