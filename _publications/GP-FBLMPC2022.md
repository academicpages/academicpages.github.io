---
title: "Learning-Based Model Predictive Control for Improved Mobile Robot Path Following using Gaussian Processes and Feedback Linearization"
collection: publications
date: 2022-06-17
venue: 'xxx'
---

Submitted to Journal of Field Robotics on June 17, 2022. Manuscript # .
## The submitted paper is available upon request. ##

[[Videos]](https://youtu.be/tC09jJQ0OXM)

## Abstract
This paper proposes a high-performance path following algorithm that combines Gaussian Processes (GP) based learning and Feedback Linearization (FBL) with Model Predictive Control (MPC) for ground mobile robots operating in off-road terrains, referred to as GP-FBLMPC. The algorithm uses a nominal kinematic model and learns unmodeled dynamics as GP models by using observation data collected during field experiments. Extensive outdoor experiments using a Clearpath Husky A200 mobile robot show that the proposed GP-FBLMPC algorithm's performance is comparable to existing GP learning-based nonlinear MPC (GP-NMPC) methods with respect to the path following errors. The advantage of GP-FBLMPC is that it is generalizable to reducing path following errors for different paths that are not included in the GP models training process, while GP-NMPC methods only work on exactly the same path on which GP models are trained. GP-FBLMPC is also computationally more efficient than the GP-NMPC because it does not conduct iterative optimization and requires fewer GP models to make predictions over the MPC prediction horizon loop at every time step. Field tests show the effectiveness and generalization of reducing path following errors of the GP-FBLMPC algorithm. It requires little training data to perform GP modeling before it can be used to reduce path following errors for new, more complex paths on the same terrain (see video at https://youtu.be/tC09jJQ0OXM).
