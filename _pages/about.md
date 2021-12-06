---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a robotics researcher working on combining machine learning with classical robotics methods for mobile robots operating in real-world environments to achieve high performance safely and effectively. I work on applying machine learning to MPC for mobile robot path following with Prof. Joshua Marshall at [Queen’s University](https://offroad.engineering.queensu.ca/). We recently proposed a high-performance path following algorithm that combines Gaussian Processes (GP) with Feedback Linearized Model Predictive Control (FBLMPC) for ground mobile robots operating in off-road terrains, referred to as [GP-FBLMPC](http://jiewang.name/publications/GP-FBLMPC2021/). Extensive outdoor experiments using a Clearpath Husky A200 mobile robot demonstrate the proposed GP-FBLMPC algorithm's performance is comparable to a GP learning-based nonlinear MPC with respect to the path following errors. However, combining MPC with feedback linearization eliminates the need for iterative nonlinear optimization, and the GP-FBLMPC algorithm needs a smaller number of GP models (two instead of three) to make disturbance predictions in the prediction horizon loop at every time step. In addition to computational efficiency, the estimated GP models are generalize to reducing path following errors for different paths. Field test results show the GP-FBLMPC algorithm requires one time drive (training data collection) on a simple path before it can reduce path following errors for new complex paths in the same field terrain. 

I received the Ph.D. degree in mechanical engineering, specializing in robotics control, from the University of Calgary, Canada. The research focused on locomotion mode selection and motion planning of a leg-tracked quadrupedal robot. By proposing an energy criterion-based approach, automatic locomotion mode transitions between tracked and legged locomotion to negotiate steps were achieved. Prior to joining the Offroad Robotics group, I worked as a Post-Doctoral Fellow at the University of Calgary. I developed and implemented perception solutions for micro aerial vehicles including visual SLAM and CNN-based multi-object detection and tracking.


**Recent News:**

[Dec. 06, 2021](http://jiewang.name/publications/GP-FBLMPC2021/): Finalizing our GP-FBLMPC algorithm [Paper](http://jiewang.name/publications/GP-FBLMPC2021/) to be submitted to IEEE/ASME Transactions on Mechatronics.

[Nov. 11, 2021](http://jiewang.name/publications/simulator2021/): A quantitative comparison of CoppeliaSim, Gazebo, MORSE and Webots robot simulator [Paper](http://jiewang.name/publications/simulator2021/) was submited. 

[Apr. 04, 2020](http://jiewang.name/posts/2020/04/gpr/): An Intuitive Tutorial to [Gaussian Processes Regression](https://github.com/jwangjie/An-Intuitive-Tutorial-to-Gaussian-Processes-Regression) posted. (104 Stars and 24 Forks on GitHub by Dec. 6, 2021)

[Feb. 03, 2020](https://offroad.engineering.queensu.ca/people/jie-wang/): I joined Offroad Robotics Lab.  
