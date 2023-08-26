---
title: 'Final report'
collection: gsoc
---

This is the end of my GSoC journey (August 26, 2023).

GSoC project
=================
*  [GSoC project URL](https://summerofcode.withgoogle.com/programs/2023/projects/HKW6ydaI)
*  [Work Repository](https://github.com/users/cannin/projects/5)
Mentor: **Augustin Luna** and **Bo Yuan**

Final product
=================
The final product of this GSoC project is a full-fledged implementation of [CellBox](https://github.com/sanderlab/CellBox) in [Pytorch](https://github.com/Mustardburger/CellBox/tree/final). This implementation has identical functionality as the original version, verified by a range of unit tests (defined in [`test.py`](https://github.com/Mustardburger/CellBox/blob/final/test.py)) and a successful replication of Figure 2 in the original CellBox paper (specified [here](https://github.com/Mustardburger/CellBox/tree/final/manuscript_rep/Figure2)). In addition, the Pytorch implementation has many more advantages:
* It uses the more recent, up-to-date version of Pytorch (Pytorch 2.0) instead of the deprecated Tensorflow 1.15 used in the original version.
* It includes more detailed documentation for all functions, giving future users and developers a better idea on how the codebase works.
* It also includes a better written README.md with clearer instructions on how to install the package and running the first commands.
* The most unique point is that it has many unit tests that future developers can use as a performance reference when they aim to rewrite CellBox with another programming package or library. CellBox Pytorch repo also supports CI/CD with Github Actions, a next step in building reliable code.

While many next steps are available to make CellBox Pytorch even better (specified below), the goal of this project, which makes a Pytorch version of CellBox and ensures it works well, has been met.

Next steps
=================
Even though GSoC has been over, and the basic goal of this project has been achieved, there are many other next steps to be done beyond GSoC:
* Rewrite the multi-stage training schedule. Even though the current Pytorch training schedule works perfectly fine and closely resembles the original Tensorflow version, they do not utilize the most up-to-date strategies for multi-stage training. Possible strategies, such as weight decay, are interesting directions I can look into.
* Resolve the ODE numerical discrepancy issue. Even though all unit tests are passed and Figure 2 in the paper has been replicated identically, the discrepancy still persists ([#56](https://github.com/sanderlab/CellBox/issues/56)). This gives an unanswered question of why two models can still converge to pretty much the same spot while having different results from the ODE.
* CellBox Pytorch, and also the original implementation of CellBox in the original version, includes sample datasets specified in [`data`](https://github.com/sanderlab/CellBox/tree/master/data). However, the process of coming from wet lab data (such as Reverse Phase Protein Assay or RPPA) to a CellBox-compatible matrix to feed in the model has been unclear. This limits usability of CellBox for other research groups, because they don't have information on how CellBox data is processed. My next step involves working with Augustin to retrace how CellBox data is processed and including this in the README.
* Both versions of CellBox also have very specialized dataloaders that only work with datasets in [`data`](https://github.com/sanderlab/CellBox/tree/master/data). Another next step will be to build a more flexible dataloader codebase that works with a wider range of cell perturbation datasets.

Acknowledgements
=================
I would like to express my sincere gratitude to Bo Yuan and Augustin Luna for their great mentorship throughout the project. They have helped me significantly and introduced me to the field of cell perturbation biology, which CellBox is based on. Finally, I would like to thank Google Summer of Code for accepting me and allowing me to work on my first open-source project.
