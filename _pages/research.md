---
permalink: /research/
title: "Research"
---


I have had the opportunity to work on a number of interesting research projects during my Ph.D. My research combines system design, signal processing, computer vision, and machine learning methods to investigate security and privacy threats on emerging computing platforms and then proposes methods for securing modern mobile and IoT devices and protecting users’ privacy. My research has shown multiple new privacy leakages resulting from sensor data available on mobile devices, introduced secure and usable authentication mechanisms for mobile users and IoT devices, proposed usable authorization protocols for mobile developers, demonstrated attacks and defenses against IoT anomaly detection systems, and built secure communication system between humans and cameras through mobile devices. Here is a summary of some of my efforts.


Identifying Privacy Risks in Commodity Mobile Devices
=====================================================
My research presents three novel permissionless sensor-based side-channels on mobile devices and shows that leakages through these channels seriously threaten users’ privacy.

First, I demonstrated that modern stylus pencils, a popular accessory used to write, draw, and make selections on smartphones and tablets, have embedded magnets that trigger fluctuations in on-device magnetometer readings when a user interacts with the device using the pencil. I specifically focused on Apple Pencil and developed <a href='/files/S3.pdf'>S3</a> attack to show that a benign malicious app running in the background on a target user’s device can infer what the user is writing from the fluctuations in the permissionless magnetometer sensor’s data. This attack has practical significance as it does not rely on information about the pencil tip position, since iOS does not allow third-party apps running in the background to access this information. To account for the extensive changes in pencil's position and orientation while a user is writing, through the interplay of signal processing, computer vision, and machine learning techniques, I designed a novel 6-dimensional particle filter-based tracking algorithm to track the pencil’s tip movement using the magnetic field data to identify users’ writing. Through a comprehensive user study, I demonstrated that S3 stealthily infers letters, numbers, shapes, words, and sentences while a user is interacting with the pencil. This work was presented at UbiComp 2021.

Following S3, my collaborators and I presented a second attack, iStelan, a new side-channel that reveals users’ touch events from permissionless magnetometer sensor data. We exploit the revealed touch event patterns to fingerprint the type of app a user is using, and model touch events to identify users’ touch event types performed on different apps. This work will appear at PoPETs 2023.

In a more recent work, I developed LocIn attack to show that apps’ access to 3D spatial maps collected by mixed reality devices (e.g., HoloLens, iPad Pro with LiDAR) allows adversaries to infer users’ indoor environment, i.e., semantic location, without explicit user permission or any prior knowledge about the user. I designed my attack based on the observation that indoor environments are uniquely characterized by their semantic context (e.g., objects and surfaces in the environment). However, unlike pixel arrays in images, a 3D spatial map is a set of unordered points with non-uniform density, making detecting objects and surfaces in the environment challenging. Therefore, I introduced a new multi-task learning representation for location inference that unifies the geometric and contextual patterns embedded in the spatial map to infer a user’s location. I evaluated LocIn on three popular MR devices and showed that it can accurately infer a user’s location and is robust against varying size and sparsity of the spatial maps. This work is currently under submission at a top-tier security venue.




Enabling Usable Authentication on Commodity Mobile and IoT Devices
==================================================================






