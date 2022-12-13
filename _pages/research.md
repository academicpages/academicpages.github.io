---
permalink: /research/
title: "Research"
---


I have had the opportunity to work on a number of interesting research projects during my Ph.D. My research combines system design, signal processing, computer vision, and machine learning methods to investigate security and privacy threats on emerging computing platforms and then proposes methods for securing modern mobile and IoT devices and protecting users’ privacy. Here is a summary of some of my research efforts

<!---
My research has shown multiple new privacy leakages resulting from sensor data available on mobile devices, introduced secure and usable authentication mechanisms for mobile users and IoT devices, proposed usable authorization protocols for mobile developers, demonstrated attacks and defenses against IoT anomaly detection systems, and built secure communication system between humans and cameras through mobile devices. Here is a summary of some of my efforts.

--->

## Enabling Usable Authentication on Commodity Mobile and IoT Devices [MobiCom'20, S&P'23]

<div style="text-align: justify">
<b>I developed two systems, <a href='/files/FaceRevelio.pdf'>FaceRevelio</a> and IoTCupid to enable reliable and secure user and device authentication to protect users’ private information (e.g., contacts, messages, credit card details) on commodity mobile and allow secure communication between IoT devices.</b>

 <a href='/files/FaceRevelio.pdf'>FaceRevelio</a> is a novel liveness detection system that protects facial authentication mechanisms on commodity smartphones from spoofing attacks, without requiring effort from the users or any external hardware. It leverages the smartphone screen as a light source and illuminates different portions of the screen with random lighting patterns for a short duration (∼1 second) to simulate multiple lighting conditions. The reflection of the light from the screen is recorded and then used to extract stereo images of the face and its 3D surface through a photometric stereo technique. The reconstructed 3D surface differentiates a real human face from its 2D counterpart and defends against spoofing attacks. This work was presented at MobiCom 2020.
</div>
 
 <p align="center">
 <a href='https://youtu.be/zGlbclBXQ8Y'><img src="/files/facerevelio_teaser.png"
     alt="FaceRevelio - Teaser Video"
     style="display:block;
        margin-left: auto;
        margin-right: auto;" /></a>
 <br>
 <em>MobiCom 2020 - FaceRevelio Teaser Video</em>
 </p>
 
More recently, I developed, IoTCupid, a new secure, and usable decentralized group pairing system for IoT devices with heterogeneous sensing modalities. My work demonstrates that two devices can use the time interval between the subsequent occurrences of a commonly observed event type (e.g., coffee-machine-on events sensed by the microphone and power meter) as proof of co-presence and use them as evidence to establish a symmetric key. IoTCupid proposes a novel group key establishment protocol that enables dynamic group generation among devices and is resilient to man-in-the-middle, offline brute force and denial of key exchange attacks. This work was recently accepted to IEEE S&P and will be available online soon.
 
<b>Impact: </b> My work on liveness detection has gained recognition from both academia and industry, and a patent has been approved for it. Our work on IoT device pairing has encouraged the integration of secure and usable pairing mechanisms in emerging decentralized IoT systems such as Thread/OpenThread. To this end, the tools and algorithms I have developed allow developers to implement effective systems for improving users’ security and privacy. 

## Identifying Privacy Risks in Commodity Mobile Devices [UbiComp'21, PoPETs'23]

<b>My research presents three novel permissionless sensor-based side-channels on mobile devices and shows that leakages through these channels seriously threaten users’ privacy.</b>

First, I developed <a href='/files/S3.pdf'>S3</a> attack to demonstrate that modern stylus pencils, a popular accessory used to write, draw, and make selections on smartphones and tablets, have embedded magnets that trigger fluctuations in on-device magnetometer readings when a user interacts with the device using the pencil. I specifically focused on Apple Pencil and showed that a benign malicious app running in the background on a target user’s device can infer what the user is writing from the fluctuations in the permissionless magnetometer sensor’s data. To account for the extensive changes in pencil's position and orientation while a user is writing, through the interplay of signal processing, computer vision, and machine learning techniques, I designed a novel tracking algorithm to track the pencil’s tip movement using the magnetic field data to identify users’ writing. This work was presented at UbiComp 2021.

 <p align="center">
 <a href='https://youtu.be/W3cb42cPugI'><img src="/files/s3_teaser.png"
     alt="S3 - Teaser Video"
     style="display:block;
        margin-left: auto;
        margin-right: auto;" /></a>
 <br>
 <em>UbiComp 2021 - S3 Presentation</em>
 </p>

Following S3, my collaborators and I presented a second attack, iStelan, a new side-channel that reveals users’ touch events from permissionless magnetometer sensor data. We exploit the revealed touch event patterns to fingerprint the type of app a user is using, and model touch events to identify users’ touch event types performed on different apps. This work will appear at PoPETs 2023.

In a more recent work, I developed LocIn attack to show that apps’ access to 3D spatial maps collected by mixed reality devices (e.g., HoloLens, iPad Pro with LiDAR) allows adversaries to infer users’ indoor environment, i.e., semantic location, without explicit user permission or any prior knowledge about the user. I introduced a new multi-task learning representation for location inference that unifies the geometric and contextual patterns embedded in the spatial map to infer a user’s location. I evaluated LocIn on three popular MR devices and showed that it can accurately infer a user’s location and is robust against varying size and sparsity of the spatial maps. This work is currently under submission at a top-tier security venue.

<b>Impact: </b> My findings on privacy leakages in mobile devices have encouraged the development of defenses against sensor-based side-channel attacks. We reported our findings from S3 and iStelan to Apple’s product security team. The security team acknowledged our findings and they are currently investigating our attacks further. I have also released a labeled version of the ARKitScenes, a dataset of raw unlabeled 3D spatial maps collected by Apple devices, along with tools for generating scene understanding labels. These tools will enable further investigation of privacy leakages via spatial maps and possible defenses to prevent them. 

## Online Hate and Harassment against Marginalized Populations

<b>Recently, I leveraged my experience in evaluating users’ perception of mobile security and privacy threats through user studies to understand how specific user populations are exposed to digital risks, specifically online hate and harassment.</b>
 
I specifically focused on online hate and harassment against refugees, a vast population displaced from their home countries due to social and political turmoil. Refugees’ increasing online presence, in order to adapt to their new homes, has heightened their exposure to toxic content attacks, a form of online hate and harassment. Therefore, I investigated the types of toxic content attacks that target refugees and how these attacks affect refugees’ security and privacy actions, goals, and barriers they face in responding to toxic content. My mixed-method approach of thematic analysis, refugee liaison interviews, and an online survey with refugees revealed diverse assault contexts and how intersecting identities intensify attacks against refugees. This work is currently under submission at a top-tier security conference



## Secure and Usable Remote Authorization [USENIX Security'22]

Within the context of smartphone access control, my collaborators and I explored the security and usability of Android’s authorization APIs and showed that existing mobile app developers rarely use them correctly to implement secure authorization since using them requires extensive cryptography expertise. To this end, we developed <a href=/files/SARA.pdf>SARA</a>, a secure android remote authorization library to allow developers to integrate secure authorization into their apps easily. We designed and conducted a user study with Android developers to evaluate the usability and practicality of SARA compared to the existing Android APIs and demonstrated that developers could quickly implement secure remote authorization with a few lines of code using SARA. In the spirit of open science, and to ensure our work benefits the entire Android community, we have publicly released SARA <a href='https://github.com/purseclab/SARA-Secure-Android-Remote-Authorization'>[SARA GitHub]</a>. This work led to a collaboration with Google’s Android Security team, and a proposal based on our findings was funded by Google’s ASPIRE Research Award, where I am the lead graduate student mentoring 4 Ph.D. and 1 undergraduate students.


## Human-Camera Communication [MobiSys'18, InfoCom'20]
In my research, I have also investigated how surveillance cameras can digitally associate people in public spaces with their smartphones without knowing the phones’ IP/MAC addresses to enable widespread applications ranging from security surveillance to business intelligence while protecting users’ privacy. We introduced a new communication system between cameras (server) and humans (client) that leverages a person’s context features (e.g., walking velocity, WiFi signal strength around them) as its address. I developed a context feature extraction and selection algorithm that extracts features, from camera videos and users’ smartphone sensor data, capable of distinguishing a specific person from a group of people in the camera view. Through this, a public camera can broadcast a message with a target user’s context address which is only accepted by a user’s phone if its context address matches the phone’s sensor data.


## Personalized Federated Learning [FL-ICML'2021]
In a recent collaboration, I leveraged insights from statistical learning theory and optimization literature to improve the generalizability and accuracy of collaborative models learnt in federated learning. In later work, we leveraged our understanding of existing federated learning approaches to propose 9 new performance and fairness metrics more suitable for evaluating personalized learning algorithms compared to standard average accuracy metrics.








