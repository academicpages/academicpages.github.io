---
title: "Robotic Foosball Table"
excerpt: "ECE Capstone Project. Capable of regularly defeating skilled human opponents. <br/><br/><img src='/images/foosball1_img.png'>"
collection: portfolio
---

The Robotic Foosball Table was a five-person capstone project for the Electrical and Computer Engineering majors. We had one semester to plan, design, order parts for, assemble, and test the project. At the end of the semester, the project was presented at UVA's Capstone Symposium, where dozens of people were able to play against the table. 

The project uses a camera mounted above the table to feed images to a Raspberry Pi, which reads raw image data and extracts the location and trajectory of the moving ball using color segmentation. It uses the trajectory data to send commands to a MSP432 microcontroller, which turns those commands into electrical signals that can interact with two custom PCBs that drive the linear and rotational motors. Efficient C code enables processing images at 30 frames per second. 

Check out the code base [here](http://github.com/capstone)

<!-- ![](http://www.github.com/zacharyyahn/zacharyyahn.github.io/images/foosball3.png)
Custom 3-D printed motor mounts attach DC brushless motors to an aluminum frame.

![](http://www.github.com/zacharyyahn/zacharyyahn.github.io/images/foosball2.png)
We designed two PCBs from scratch to interface between the microcontroller and motors. 

![](http://www.github.com/zacharyyahn/zacharyyahn.github.io/images/foosball5.png)
The entire project was modeled in Fusion360.  -->
