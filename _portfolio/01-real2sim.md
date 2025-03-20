---
layout: single
title: Real2Sim
excerpt: <i>When having a robotics pipeline that works in the real world is not enough, going back in simulation can help.
header:
  teaser: "webots_example.png"
collection: academic
tags:
  - biped
  - work
categories: biped.ai
---

A challenge of most robotics projects is the translation of algorithms that work in a simulated environment to the real world. This happens for most projects involving a physical robot with motors, as  they usually start by  implementing the perception and control pipelines in simulation so that failures don't result in >10k $ of hardware costs when the robot falls.
The sim2real problem is then to be able to transform a robot that works in simulation to one that works in the real world.

![Simulation Example](/images/webots_example.png){: .align-center}
*Simulation environment*

The challenge we faced  at biped is the opposite of that one. Our product was aimed towards visually impaired humans, giving auditory feedback to help them locate obstacles, but leaving the obstacle avoidance and joint control parts to them.

This approach was obviously tested, both with sighted humans and annotated data before pushing everything in production.  But as there was always a human brain in the middle, there was never an incentive to have a simulated environment, where we could control the  test scenarios, and have leverage on sensor noise and ground truth for the localisation of the cameras and obstacles.

This made improving our obstacle detection algorithms quite hard, as we had to directly record images with the cameras, have them annotated and compute metrics, that needed some degree of interpretation, as sensor noise / human error was always present.

To tackle this problem, I created a synthetic data generation pipeline through the [Webots](https://cyberbotics.com/) robotics simulator. I was already familiar with it from my  work on [optimizing a bipedal model](/portfolio/02_semester_biorob) and [allowing a robotic wheel-chair to climb stairs](/portfolio/01_master_lws).
This allowed to easily create simulation environments, adding various obstacles (cars, walls, houses) with a known position.

<div style="text-align: center;">
  <video controls loop style="max-width: 100%;">
    <source src="/files/webots_shoulder.webm" type="video/webm">
  </video>
</div>

*Office like environment, with a simulated shoulder movement when walking*

The cameras (Intel Realsense D430I) of our physical device could also be simulated by using  a combination of [simulated sensors](https://cyberbotics.com/doc/guide/sensors), together with a custom noise models based on the characteristics of the realsense cameras.

Adding a dummy robot, whose motion is controlled with the Keyboard and with some perturbations reproducing a human gait, permitted the creation of a simulation where we could test our algorithms in a controlled way.

<div style="text-align: center;">
  <video controls loop style="max-width: 100%;">
    <source src="/files/simulated_environment.mp4" type="video/mp4">
  </video>
</div>

*Simulated environment showcasing synthetic sensor noise*

This also reduced the costs for data annotation, as using built-in segmentation functionalities allowed the generation of ground truth for panoptic segmentation in each simulated frame.

Thanks to this, I was able to:

- Improve our ground segmentation algorithms
- Have a tool to develop a vision based localisation system
- Create a baseline dataset for a research project, with no annotation costs and full control over the experimental scenarios
- Break a gap in "explainabilty", by having a video game like experience, to showcase what our software was doing to a non technical public.
