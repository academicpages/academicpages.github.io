---
layout: single
title: "3D vision for a robotised wheelchair able to cross obstacles"
excerpt: "Obstacle detection and crossing for a legged-wheeled robot, motivated selection of a depth
sensor and real world experiments<br/><img src='/images/lws_cover.png'>"
collection: portfolio
category: student-project
---



<!-- Introduction of the project -->
This project was part a collaboration between EPFL (Biorob laboratory) and C. Cazali, aiming to develop a robotised wheelchair with an hybrid legged-wheeled locomotion and obstacle crossing capabilities.

<!-- Problematic -->
From previous students works, a model was implemented in simulation, with obstacle crossing working in a 2D space (xz), with a ground truth knowledge of the obstacles positions and dimensions.
My project aimed to extend this to a 3D navigation scenario, using on-board depth imagery for the obstacle perception. I was then to review and select a physical sensor, in view of real world experiments. This represented 14 weeks of full time work.

<!-- My approach -->

After extending the obstacle crossing to handle 3D navigation cases, I reviewed the state of the art for obstacle perception, and highlighted the need for a mapping strategy to aggregate the sensor's measures over time. As this is a well researched topic, I looked at the available open sources implementations, and selected the [elevation mapping approach](https://github.com/ANYbotics/elevation_mapping) developed by ETH Zürich and Anybotics, which was the more adapted to our use case.
I then interfaced the simulated sensory data with the mapping algorithms using [ROS](https://www.ros.org/), creating a 2.5D map of the environment around the robot from the sensory input.

 <video width="640" height="480" controls>
  <source src="/files/demo_lws.mp4" type="video/mp4">
</video>
After that, I solved the challenges inherent to our application, handling self-occlusion, low confidence measures and computing the obstacle representation required by the crossing algorithms while minimizing the time lag. This allowed the robot to clear multiple obstacle crossing scenarios, relying solely on real time perception for the obstacle estimation.

<figure>
<img src="/images/lws_stairsrgbd.png" alt="Sensor measure in an outdoor scene" style="width:900px;height:300px;">
<figcaption>Sensor measure in an outdoor scene</figcaption>
</figure>
Next, I chose the physical sensor after reviewing the available depth sensing technologies in regards to outdoor use, driver availability and budget. After the purchase of a 2nd generation refurbished kinect, with depth sensing based on Time-of-Flight technology and a complimentary RGB image, I adapted existing calibration scripts for [OpenCV 4](https://opencv.org/opencv-4-0/). I then tested the now calibrated sensor on outdoor scenes, and interfaced it with the rest of the project.

I then experimented with visual and motor odometry, laying the fundations for future work regarding the localisation of the robot.

<!-- Challenges -->

<!-- Results -->

With this work, I was able to provide a proof of concept on the solutions for obstacle perception with on-board imagery, combining and adapting multiple state of the art approaches to the LWS project.
