---
title: "Learning-Based Model Predictive Control for Improved Mobile Robot Path Following using Gaussian Processes and Feedback Linearization"
collection: publications
date: 2021-12-02
venue: 'xxx'
---

Finalizing for a submission.

<!-- [[Video]](https://youtu.be/BhD-sUd2qAI) -->

## Abstract
This paper proposes a high-performance path following algorithm that combines Gaussian Processes (GP) based learning with Feedback Linearized Model Predictive Control (FBLMPC) for ground mobile robots operating in off-road terrains, referred to as GP-FBLMPC. The algorithm uses a baseline kinematic model and learns unmodeled dynamics as GP models by using observation data collected during field experiments. We demonstrate the effectiveness of the proposed algorithm via extensive outdoor experiments using a Clearpath Husky A200 mobile robot. The test results indicate that the proposed GP-FBLMPC algorithm's performance is comparable to GP learning-based nonlinear MPC (GP-NMPC) with respect to the path following errors. However, GP-FBLMPC is computationally more efficient than the GP-NMPC because it does not conduct iterative optimization and requires fewer GP models to make predictions over the MPC prediction horizon loop at every time step. Field tests show the algorithm requires very little training data to perform GP modeling before it can be used to reduce path following errors for new, more complex paths in the same terrain (see video at https://youtu.be/BhD-sUd2qAI). 
