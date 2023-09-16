---
title: "Dynamic Mechanical Analysis Automation"
excerpt: "Creating an Automated Setup for Vibrational Experiments <br/><img src='/images/DMA_MAE.png' width = '300'>"
collection: portfolio
---
This project aims to automate the setup procedure for running Dynamic Mechanical Analysis tests on magneto-active elastomers for determining the viscoelastic properties. The design of the orginal DMA setup has also been completely revamped when creating this new setup. The original setup had several problems that needed to be addressed:
1. The callibration of the force sensor with respect to the sample was done manually which took too much time.
2. The sample had to be placed between the two steel plates that allowed magnetic field to be applied but made the sample hard to place. 
3. The setup was not optimized for the natural frequency which limited the range of experiments that could be perfomred in the lab.

 In order to address the first problems, I created a MATLAB application capable of controlling the setup. While applications using LabView or C++ had better documentations and resources, MATLAB was used to consider accessibility as it was the prominent software in the lab. 
 
 Optimal settings have been preset for the oscilloscope and the Lock-in amplifier in order to optimize the duration for the time constant while still accounting for accuracy. Different setting for the app and algorithm has been documented in the github link below: \
Github Link to Software:  [DMA Setup](https://github.com/hwkwon1114/MAE-DMA)

<img src='/images/DMA_MATLAB.png' width = '370'><img src='/images/DMA_MATLAB2.png' width = '370'>

In order to address the second problem, the design of the setup was completely revamped to a vertical setup from the original horizontal alignment. The magnetic plates were separated from the platform that holds to the sample, preventing samples from dropping and overall reducing the time to place the sample. THe magnetic plates' rods were designed based on the research article [Yoshikazu Ishikawa and Sōshin Chikazumi 1962 Jpn. J. Appl. Phys. 1 155](https://iopscience.iop.org/article/10.1143/JJAP.1.155#references), which provided ideal angles and rod widths to create the strongest electromagnets. 

<img src='/images/Magnet_Design.png' width = '500'>

Lastly, Eigenfrequency and Frequency Domain has been tested on variations of the design in order to increase the natural frequency of the setup. 

<img src='/images/DMA_COMSOL2.png' width = '500'>
