---
title: "Robotics Dynamics and Force Control Package"

excerpt: 
    "April 2024<br/>
    Developed Robotics Package, integrating manipulator dynamics, force control, and Interactive GUI."
# excerpt: "Short description of portfolio item number 1<br/><img src='/images/500x300.png'>"
collection: portfolio
---

Developed Robotics Package, integrating manipulator dynamics, force control, and Interactive GUI.<br/>
[Link](https://github.com/thulsonASU/robot_sim)


# robot_sim


Welcome to Robo_SIM – a MATLAB package developed to explore and implement advanced dynamics and force control techniques for robotic manipulators. This package is designed for educational and research purposes, integrating core concepts in manipulator dynamics, force control methods, and interactive GUI features to provide an accessible and comprehensive tool for robotics simulations.

## Features
* **Dynamics Simulation**

  * Derives and outputs governing equations of motion for robotic systems.
  * Simulates system dynamics, providing plots for joint positions (q), velocities (q_dot), and 
 accelerations (q_ddot) over time for given inputs.

* **Force Control Methods**
  * **Compliance Control:** Implements PD control with gravity compensation, enabling indirect force control through compliance with external interactive forces. Visualizes desired vs. actual end-effector positions and contact forces.
  * **Impedance Control:** This method uses inverse dynamics control to achieve indirect force control under environmental interactions. It plots desired vs. actual end-effector positions and end-effector contact forces over time.

* **Interactive GUI**
  * A user-friendly graphical interface facilitates intuitive interaction with the package, allowing users to configure, simulate, and analyze robotic manipulator behavior easily.


MATLAB/SIMULINK Robotic Simulator for a user-defined DH table

![DHGUI](https://raw.githubusercontent.com/thulsonASU/robot_sim/main/images/DHGUI_3R.png)

![DySimGUI](https://raw.githubusercontent.com/thulsonASU/robot_sim/main/images/DySimGUI_3R.png)

![LQRGUI](https://raw.githubusercontent.com/thulsonASU/robot_sim/main/images/LQRGUI_3R.png)

![PlotGUI](https://raw.githubusercontent.com/thulsonASU/robot_sim/main/images/PlotGUI_3R.png)