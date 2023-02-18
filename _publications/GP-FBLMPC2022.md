---
title: "Learning-based model predictive control for improved mobile robot path following using Gaussian processes and feedback linearization"
collection: publications
permalink: /publications/GP-FBLMPC2022/
date: 2023-01-31
venue: 'Journal of Field Robotics'
---

[[Paper]](https://onlinelibrary.wiley.com/doi/full/10.1002/rob.22165)
[[Videos]](https://youtu.be/tC09jJQ0OXM)
<!-- [[software]](https://github.com/jwangjie/Fine-tune-YOLOv3)
[[Dataset]](https://github.com/jwangjie/UAV-Vehicle-Detection-Dataset) -->

**This paper proposes a high-performance path following algorithm that combines Gaussian Processes (GP) based learning and Feedback Linearization (FBL) with 
Model Predictive Control (MPC) for ground mobile robots operating in off-road terrains.**

<div style="text-align: center">
<img src="https://jwangjie.github.io/publications/gpfblmpc2023/husky.png" 
     width="580px" height="380px"/>
</div>

## Abstract
This paper proposes a high‐performance path following algorithm that combines Gaussian processes (GP) based learning and feedback linearization (FBL) with 
model predictive control (MPC) for ground mobile robots operating in off‐road terrains, referred to as GP‐FBLMPC. The algorithm uses a nominal kinematic model 
and learns unmodeled dynamics as GP models by using observation data collected during field experiments. Extensive outdoor experiments using a Clearpath Husky 
A200 mobile robot show that the proposed GP‐FBLMPC algorithm's performance is comparable to existing GP learning‐based nonlinear MPC (GP‐NMPC) methods with 
respect to the path following errors. The advantage of GP‐FBLMPC is that it is generalizable in reducing path following errors for different paths that are 
not included in the GP models training process, while GP‐NMPC methods only work well on exactly the same path on which GP models are trained. GP‐FBLMPC is 
also computationally more efficient than the GP‐NMPC because it does not conduct iterative optimization and requires fewer GP models to make predictions over 
the MPC prediction horizon loop at every time step. Field tests show the effectiveness and generalization of reducing path following errors of the GP‐FBLMPC 
algorithm. It requires little training data to perform GP modeling before it can be used to reduce path‐following errors for new, more complex paths on the 
same terrain.

<!-- <div style="text-align: center">
<img src="https://jwangjie.github.io/publications/gpfblmpc2023/gpfblmpc_diagram.png"/>
</div> -->

<div style="text-align: center">
<img src="https://jwangjie.github.io/publications/gpfblmpc2023/gpfblmpc_diagram.png" 
     width="680px" height="680px"/>
</div>

## Field tests
### The Husky A200 robot is driven autonomously to follow the infinite path in sand terrain.
<div style="text-align: center">
<img src="https://jwangjie.github.io/publications/gpfblmpc2023/inf_ground.gif" />
</div>


<div style="text-align: center">
<img src="https://jwangjie.github.io/publications/gpfblmpc2023/inf_drone.gif" />
</div>

### The robot is driven autonomously to follow the track path in sand terrain.
<div style="text-align: center">
<img src="https://jwangjie.github.io/publications/gpfblmpc2023/track_ground.gif" />
</div>


<div style="text-align: center">
<img src="https://jwangjie.github.io/publications/gpfblmpc2023/track_drone.gif" />
</div>

### The robot is driven autonomously to follow the infinite3 path in grass terrain.
<div style="text-align: center">
<img src="https://jwangjie.github.io/publications/gpfblmpc2023/inf_grass.gif" />
</div>


<div style="text-align: center">
<img src="https://jwangjie.github.io/publications/gpfblmpc2023/inf8_grass.gif" />
</div>

## Reference
Please cite this paper in your publications if it helps your research:

```

```
