---
layout: archive
title: "CV"
description: "CV of Hamidreza Montazeri Hedesh: education, research, open-source software, experience, teaching and service."
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

You can download a PDF copy of my complete CV [here](/files/cv.pdf).

## Education
---
* **Ph.D. in Electrical Engineering**, Northeastern University, Boston, USA (Sep 2021 – Present)
    * **GPA:** 3.81
    * **Thesis:** Scalable Method for Stability and Robustness Verification of Systems with NN Feedback using Positivity Constraints.
* **M.Sc. in Aerospace Engineering**, Sharif University of Technology (Sep 2017 – June 2020)
    * **Control Courses GPA:** 3.75
    * **Thesis:** Coupled Attitude-Orbit Dynamics and Control of a Solar Sail via Center-of-Mass Manipulation.
* **B.Sc. in Aerospace Engineering**, Sharif University of Technology (Sep 2012 – June 2017)
    * **Thesis:** Attitude Control of an Under-Actuated Satellite by Two Reaction Wheels.

## Research & Impact
---
* **Novel Neural Network Bounding:** Designed global & local NN bounding (depth‑agnostic) methods, enabling $$\sim 10\times$$ faster bound computation and tight, input‑aware sector envelopes for controllers.
* **Scalable Verification Pipeline:** Built a scalable robust stability verification pipeline for NN‑in‑the‑loop systems under positivity constraints, achieving up to $$\sim 10^4\times$$ speedup over state-of-the-art baselines.
* **Safe-by-Design NN Controllers:** Designed neural network controllers for systems with time delays and model uncertainty: the architecture enforces the required stability sector on the controller's gain at the origin by construction, and a sector-regularized imitation-learning loss pushes the trained controller to stay inside the sector.
* **Sim-to-Real Gap:** Validated learning-enabled control frameworks through extensive simulation and hardware-informed experiments, bridging the gap between theoretical guarantees and real-world robotic performance.
* **Tool Integration:** Implemented state‑of‑the‑art verification (AutoLiRPA, JAX‑Verify) and bridged them with classical control toolchains (MPC/robust analysis) for reproducible experiments using MATLAB/Python integration.
* **Crowd Dynamics & Fluid Analogy:** Modeled large-scale population motion as continuum flow dynamics and designed optimal egress control policies, highlighting transferable techniques for airflow and transport phenomena.
* **Space Robotics Optimization:** Derived coupled attitude–orbit dynamics of a solar sail via center-of-mass manipulation, including interplanetary path optimization using SNOPT.

## Open-Source Software
---
* **[nnsector](https://github.com/hmon91/nnsector):** Python and MATLAB library that computes global and local sector bounds of feedforward neural networks for absolute-stability analysis of neural feedback loops; supports PyTorch models.
* **[nnstab](https://github.com/hmon91/nnstab):** Python and MATLAB library that certifies exponential stability of positive feedback loops with a neural network controller and finds the largest certified region of attraction, using Metzler and Hurwitz tests instead of semidefinite programming.
* More on the [Software]({{ base_path }}/software/) page.

## Work Experience
---
* **Graduate Research & Teaching Assistant**, Northeastern University (Sep 2021 – Present)
    * Supported autonomous experimentation environments (Quanser, Franka Emika) and reproducible computational pipelines.
    * Research in control, estimation, and learning-enabled autonomy.
* **Control Systems Engineer**, Safatco (Dec 2019 – Oct 2020)
    * Reverse engineered and developed electromagnetic servo valves for fuel control systems.
    * performed SolidWorks modeling, precision measurement, and tolerance validation.
* **R&D Engineer**, Sharif Technology Services (Satellite-building Project) (Apr 2018 – Oct 2019)
    * Built and configured Hardware-in-the-Loop (HIL) and Software-in-the-Loop (SIL) testbeds to support system integration.
    * Developed digital models for satellite attitude and position estimation using EKF and UKF.
    * Designed and executed sensor calibration procedures for magnetometers, gyroscopes, and magnetorquers.
* **R&D Engineering Intern**, Sharif Technology Services (Satellite Reaction Wheel Project) (Jan 2017 – May 2017)
    * Conducted R&D for a satellite reaction wheel; drafted verification and calibration procedures.

## Selected Projects
---
### Robotics, AI & Control

* **Autonomous Lab Deployment:** Installed and calibrated multi-camera sensing systems in the Quanser autonomous lab, enabling real-time 6-DoF pose estimation for aerial and ground robots and supporting hardware-in-the-loop autonomy experiments.

* **Sensor Fusion & Control Integration:** Integrated perception, EKF/UKF state estimation, and feedback control pipelines in a robotics testbed to enable reliable autonomous flight and driving experiments.

* **Quadrotor Real-Time Control:** Designed and deployed controller–observer architectures for quadrotor dynamics on Arduino hardware, achieving real-time stabilization under noisy sensing conditions.

* **Ground-Effect Aerodynamic Modeling:** Conducted CFD-based analysis of quadrotor rotor–ground interaction using Fluent/Gambit to inform control performance limits with physics-based insights.

* **Dual-Arm Manipulation:** Configured and coordinated two Franka Emika robotic arms for interactive manipulation tasks (Tic-Tac-Toe), demonstrating synchronized multi-robot control.

* **Safe Imitation Learning:** Implemented imitation learning of an MPC controller for nonlinear inverted pendulum dynamics, verifying closed-loop stability before deployment.

* **Safe Multi-Agent Control:** Designed learning-based controllers for a network of quadrotors using a scalable NN-in-the-loop verification framework to provide formal stability guarantees.

* **Learning-Enabled Robotics:** Developed control frameworks integrating neural-network feedback with model-based dynamics to enable trustworthy deployment of learned robotic policies.

* **Certified Autonomous Driving Control:** Formulated vehicle lateral control under neural-network feedback using IQC-based parametrization to achieve formally certified performance bounds.



### Neural Network Verification & Learning-Enabled Systems

* **Neural Network Sector Bounding:** Developed global and local sector-bounding methods for feedforward neural networks, enabling depth-agnostic and input-aware certification tighter and faster than prior approaches.

* **Scalable Stability Verification:** Built a positivity-based stability and robustness verification pipeline for NN-controlled dynamical systems, achieving up to $$10^4\times$$ computational speedup over state-of-the-art.

* **Exact MILP Certification:** Formulated mixed-integer (MILP) encodings of ReLU networks for exact closed-loop stability verification of nonlinear feedback systems.

* **Relaxation Analysis for NN Verification:** Designed continuous relaxations of mixed-integer NN formulations to analyze tractability–accuracy trade-offs in verification.

* **Reachability & ROA Analysis:** Performed reachability and region-of-attraction analysis of nonlinear systems with NN feedback using IQC-based formulations to provide formal safety guarantees.

* **Cross-Platform Verification Pipelines:** Integrated AutoLiRPA and JAX-Verify with Lyapunov and MPC analysis via MATLAB–Python pipelines for reproducible certification workflows.

* **Time-Delay Neural Stability:** Verified uncertain retarded neural-network feedback loops using positive Lur’e frameworks to extend stability certification to time-delay systems.

* **System-of-Systems Robustness:** Developed verification methods for AI-enabled systems-of-systems under time delays and parametric uncertainty to strengthen safety guarantees in autonomous settings.



### Spacecraft, Orbital Mechanics & GNC

* **Solar Sail Trajectory Control:** Derived and controlled coupled attitude–orbit dynamics of a solar sail via center-of-mass manipulation using constrained nonlinear optimization (SNOPT) for interplanetary trajectory design.

* **Under-Actuated Satellite Control:** Designed nonlinear attitude control for a satellite with only two reaction wheels, achieving stability under actuation constraints.

* **Fuel Sloshing Stability Analysis:** Modeled and controlled satellite attitude considering internal fuel sloshing effects to improve robustness of stability analysis.

* **Nonlinear Spacecraft Momentum Control:** Implemented feedback linearization for nonlinear 6-DOF spacecraft attitude dynamics to enable precise momentum-transfer control.

* **High-Fidelity GNC Simulation:** Built integrated 6-DOF spacecraft GNC simulations with EKF/UKF and disturbance modeling for mission-level validation.

* **Orbital Mission Modeling:** Developed ground-track, eclipse, visibility, repeated-track, and CR3B simulation tools for comprehensive spacecraft mission analysis.

* **Satellite Estimation Systems:** Developed EKF/UKF-based attitude and position estimation pipelines for integrated spacecraft simulations and testbeds.

* **Reaction Wheel Engineering:** Engineered verification and calibration procedures for satellite reaction-wheel hardware during aerospace manufacturing.



### Aircraft & Fluid Dynamics

* **Aircraft 6-DOF Modeling:** Developed nonlinear aircraft guidance and control simulations in MATLAB/Simulink for robustness analysis under disturbances.

* **Turbulence Robustness Analysis:** Performed statistical analysis of aircraft encountering clear-air turbulence with measurement noise modeling to quantify control degradation.

* **Wing-Box Structural Simulation:** Built finite-element models of aircraft wing-box structures using Abaqus/ANSYS for stress and modal analysis.

* **Re-Entry Aerodynamic Simulation:** Conducted CFD simulations of re-entry vehicle aerodynamics using Fluent/Gambit to characterize high-speed flow behavior.

* **Thermofluid System Modeling:** Modeled internal fluid flow systems using conservation laws to analyze pressure drop and heat transfer regimes numerically.



### Networked & Data-Driven Dynamical Systems

* **Sparse System Identification:** Applied SINDy and Sum-of-Squares methods to discover governing nonlinear equations from data and certify stability properties.

* **Ocean Dynamics Identification:** Developed data-driven pipelines to model oceanic transport dynamics from drifter measurements as spatiotemporal systems.

* **Networked Epidemic Control:** Designed centralized and decentralized vaccination strategies for SIS epidemic models using graph-theoretic optimization.

* **Adaptive Networked Control:** Integrated adaptive identification with safe control for distributed dynamical systems to improve scalability of autonomy frameworks.

* **Distributed Estimation:** Developed distributed adaptive estimation algorithms for sensor networks with partially unknown nonlinear dynamics.

* **Crowd Flow & Egress Optimization:** Modeled crowd dynamics via fluid analogies and designed optimal evacuation strategies under uncertainty.



### Mechanical & Industrial Systems

* **Gas Turbine Servo-Valve Redesign:** Reverse-engineered and redesigned an electromagnetic servo-valve for industrial fuel control systems.

* **Fuel-Nozzle Test Rig Development:** Designed and built a combustion-component test rig to improve experimental validation capability.

* **Industrial Bearing Modeling:** Modeled and validated industrial bearing geometries in SolidWorks with tolerance analysis for manufacturing precision.



### Computational & Systems Programming

* **Autonomous Game Engine:** Implemented an automatic Reversi (Othello) game in C with rule-based decision logic and structured state representation.

* **Kalman Filtering Frameworks:** Implemented multiple Kalman-filter-based estimation frameworks for nonlinear aerospace systems to improve robustness under noisy sensing.




## Technical Skills
---
* **Robotics & Perception:** 6-DoF rigid-body dynamics, robotic arms, real-time control, multi-camera sensing, sensor calibration, EKF/UKF.
* **Machine Learning:** Imitation Learning, Reinforcement Learning, PyTorch, TensorFlow, AutoLiRPA, JAX-Verify.
* **Control & Optimization:** Nonlinear Control, MPC, Robust Control, Reachability Analysis, Lyapunov Methods, SNOPT, CVX.
* **Programming:** Python, MATLAB, C, Julia.
* **Simulation Tools:** Simulink, Fluent, Gambit, SolidWorks, Abaqus, ANSYS.

## Teaching & Mentorship
---
* **Teaching Assistant:**
    * *Embedded Design Enabling Robotics* (Spring 2026)
    * *Linear Systems Analysis* (Fall 2025)
    * *Electrical Engineering Class & Lab* (Spring 2025)
    * *Classical Control* (Spring 2023)
* **Mentorship:** Capstone project "Robotic Gloves for Teaching Piano" (Summer 2024).

## Professional Service
---
* **Leadership:** Founder & President of Northeastern ECE Ph.D. Council.
* **Reviewer:** IEEE CDC, ACC, Control Systems Letters, IFAC CPHS.
* **Memberships:** IEEE, Society for Risk Analysis (SRA).
