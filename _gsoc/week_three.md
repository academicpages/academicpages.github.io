---
title: 'Week three (Jun 12, 2023 - Jun 19, 2023)'
collection: gsoc
---

This is the third week of my GSoC journey.

GSoC project
=================
*  [GSoC project URL](https://summerofcode.withgoogle.com/programs/2023/projects/HKW6ydaI)
*  [Work Repository](https://github.com/Mustardburger/CellBox)

Tasks
=================
1. Add index to pert.csv and expr.csv files for dataloader testing.
2. Write tests for testing if Tensorflow and Pytorch dataloaders are similar.
For this test, I came up with an idea. I will add the index to each row in pert.csv and expr.csv files, then the two dataloaders behave similarly if they pick out the same rows of the data. For example, in leave-one-out (LOO) setting, choosing the drug index to be 7 leaves out all the rows where drug 7 is present. Therefore, in the **training set**, both dataloaders should only pick rows that don't have drug 7.
3. Implement the tests via pytest.
I have never written unit tests for Python before. Therefore, this is a great opportunity for me to write tests using pytest.

Relevant issues:
================
* Inconsistent drug indexing in loo_label.csv and the code ([#48](https://github.com/sanderlab/CellBox/issues/48))

Notes
=================
Check out my [personal GSoC notebook](https://docs.google.com/document/d/1fYkUNYuRcPHByWUYay6yUeTKtBuiwTGKJoztT0LajiA/edit?usp=sharing), where I keep my observations and comments in one place.
