---
title: "Internship project"
excerpt: "organization:Shahid Beheshti University, Department of Computer Science and Engineering, Robotics Laboratory<br/>summer 2021<br/>SBU omni-directional control<br/>"
collection: portfolio
---

in this project with a precise model of the real robot in the Webots simulator, we tried to implement control, obstacle avoidance, wall following and localization algorithms to create a complete motion control for the robot to be ready for use.

The challenge in this project was that sonar sensors cone have a blind area and the way they were put on the triangular shaped robot made it hard to detect conrners, three proposals were given to solve this problem, either to add Lidar sensor or replace with sonar sensors, or to add more sonar sensors or reconfigure the placement of the existing sensors, and finally to add a platform on top that has a rotational motor which makes the existing sonar sensors rotate and watch and collect data from their surroundings without blind areas. Although these were all good solutions and totally feasible in an efficient way. The approach at the end was not reorganize any of the existing sensors at all and instead using the motion control to rotate the whole body of the robot in order to make the detection of the corners possible. The downsides of this solution was energy inefficiency and performance decrease, not to mention, the motors decay will increase due to the fact that there are so many sudden change in the direction and motors' torque. of course we considered smoothing out the sharpness with low level control and we did, but at the end, it didn't make much of a difference. So we advised the mechanical engineers to reconsider their sensor configurations and consider this analysis and the available options.

read more about the project: (in Persian) [report[FA].pdf](https://raw.githubusercontent.com/ph504/ph504.github.io/master/files/internship-1400-08-03.pdf)

[source code](https://github.com/ph504/ABB_handwriter)