---
title: "Mechatronics Device: Portable/Lightweight Gait Analysis"
excerpt: 
    "Jan 2023 – May 2023<br/>
    Developed compact and portable footwear for gait analysis to improve gait balance for patients at the Barrow Institute.<br/>
    <img src= 'https://raw.githubusercontent.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device/main/IMAGES/CAD-Design.png'>"
collection: portfolio
---

Developed compact and portable footwear for gait analysis to improve gait balance for patients at the Barrow Institute.<br/>
[Link](https://github.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device)

<br/>

# <img src="https://raw.githubusercontent.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device/main/IMAGES/SoulTech-logo.png"  width="20%" height="20%"> Portable Gait Analysis Device
The SoulTech aims to expand and apply the knowledge of the real engineering industry to develop a compact and portable embedded system for gait analysis and provide real-time therapy feedback to doctors and improve gait balance for patients at the Barrow Institute. <br />
<img src="https://raw.githubusercontent.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device/main/IMAGES/ASU-logo.png"  width="25%" height="25%">
&nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp;
<img src="https://raw.githubusercontent.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device/main/IMAGES/Barrow-Logo.png"  width="30%" height="30%"> <br />
## <br /> Proposed Concepts <br />

## Background
Gait analysis plays a crucial role in analyzing an individual's walking patterns, identifying abnormalities, and devising effective treatment plans. However, traditional methods of gait analysis often require expensive and time-consuming equipment, making them inaccessible to the average person. To address this problem, the invention of gait analysis socks or soles provides a more accessible and cost-effective solution for stakeholders and clients seeking to analyze their gait. These devices use specialized sensors to capture real-time data on an individual's walking patterns, providing valuable insights into their gait mechanics.

### Sole
<img src="https://raw.githubusercontent.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device/main/IMAGES/Concept1-Sole.png"  width="100%" height="100%">
The sole mainly consists of a conductive sensing material such as a Velostat that will act as a pressure sensor. These will be connected to copper tape to transmit the analog signal generated from the sensed pressure to a wire connected to the microcontroller. The conductive sensing materials will be placed at specific points that the foot normally comes into contact with while walking. The soles will then be covered with electrical tape to protect the sensors as well as the user's feet. The microcontroller will be placed in a separate housing with a daughterboard, vibrator, and accelerometer that will be strapped near the user's ankle. The vibrator will be used for bio-feedback purposes. <br /> 

### Socks <br />
<img src="https://raw.githubusercontent.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device/main/IMAGES/Concept2-Sock.png"  width="100%" height="100%">
Pressure-sensitive socks are made of washable and comfortable microfibre laced with Velostat (a thin pressure-sensitive material) to relay the data required to the microcontroller through copper strips. Team will try to infuse the controller, and IMU into the socks but if it's not possible, they will be attached to the sock using a detachable casing. These detachable casings will be sold separately thereby reducing the recurring costs if they break. Haptic feedback will be given using small vibration devices.

## CAD Designs
Pressure-sensitive socks are made of washable and comfortable microfibre laced with Velostat to relay the data required to the microcontroller through copper strips. These are connected to copper tape to transmit the analog signal generated from the sensed pressure to a wire connected to the microcontroller. The conductive sensing materials are placed at specific points that the foot normally comes into contact with while walking. The microcontroller is placed in a separate housing with a daughterboard, linear vibration motor, and accelerometer that is strapped near the user's ankle. These detachable casings are sold separately thereby reducing the recurring costs if they break. Haptic feedback is given using small linear vibration motor devices. The team will make sure that all embedded devices are sealed properly so that the device can be cleaned regularly.
<img src="https://raw.githubusercontent.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device/main/IMAGES/CAD-Design.png"  width="100%" height="100%">
<br />

## Requirements
### Functional Requirements
- Pressure sensing: The socks must accurately measure the pressure (weight) applied on the patient's foot with each step to determine weight distribution.
- Bio-feedback: The haptic feedback should be clear and easily distinguishable by the user to provide meaningful feedback on their gait.
- Initial contact detection: The socks should be able to detect which part of the foot made initial contact with the ground during walking.
- Stance time and stance length measurement: The socks must accurately measure the amount of time the foot is in a stance phase and the length of the stance phase.
- Stride measurement: The socks must measure the length of each stride and the number of strides taken during a given period.
- Cadence measurement: The socks must measure the rate at which the user walks to determine their cadence.
- Spatial characteristics measurement: The socks must accurately measure the distance traveled and movement angles by the user during the gait analysis.
- Durability: The socks should be able to withstand repeated use and be made of materials that are easy to clean after each use.
- Data collection and storage: The socks should have the ability to store data or transmit live data for further analysis and sharing with healthcare providers.

### Performance Requirements
- Accuracy: The socks should be able to accurately measure the pressure applied on the patient's foot during gait analysis.
- Precision: The socks should provide precise measurements of the patient's walking pattern, stance phase time, initial contact, and time shift.
- Sensitivity: The socks should be sensitive enough to detect where pressure is distributed.
- Speed: The socks should provide live data to the therapist and patient, with minimal lag time.
- Reliability: The socks should have consistent performance over time, without noticeable degradation.
- Durability: Regular wear and use should not damage the socks.
- Compatibility: Various sizes and styles of footwear should be compatible with the socks.
- Portability: The socks should be lightweight and portable, allowing for easy transport and use in a variety of settings.
- Connectivity: Data collection and analysis should be possible through wireless connections between socks and a computer or mobile device.
- Power efficiency: The socks should have a long battery life and be energy-efficient to reduce the need for frequent charging or replacement of batteries.

### Usability Requirements
- Easy to put on and take off: Socks must be designed to be easy to put on and take off so as not to cause discomfort or harm to the user. 
- Comfortable: Socks should be made of soft, breathable material to ensure maximum comfort during use.
- Secure fit: Socks must fit securely to prevent them from slipping or moving during use, which can affect the accuracy of the data collected.
- Easy to clean: socks must be easy to clean after each use to maintain good hygiene and prevent the spread of infections.
- User-friendly interface: The device must have a user-friendly interface so that both the user and the therapist can easily interpret the collected data.
- Light and portable: The device should be light and portable so that it can be easily carried and used in various situations. 
- Durability: Socks must be durable and long-lasting to withstand regular use without breaking or losing precision. 
- Compatibility: The socks must be compatible with multiple devices and software to easily integrate with existing healthcare systems.

## Block Diagram
<img src="https://raw.githubusercontent.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device/main/IMAGES/Block Diagram.png"  width="100%" height="100%">
8 Analog Input pins are used to obtain the pressure readings. Additionally, an analog pin was used for the haptic feedback with a linear vibrator motor. An in-built IMU was incorporated into the system which enabled the team to obtain precise measurements of the orientation and movement of the device. Furthermore, to enhance the user experience and enable a more user-friendly interface, Bluetooth connectivity was also implemented. This allowed for seamless smartphone communication, enabling the user to monitor and control the device. The combination of the Arduino Nano 33 IoT, pressure sensor, haptic feedback vibrator motor, accelerometer, and Bluetooth connectivity enabled team SoulTech to build a highly efficient and user-friendly system for pressure measurement and gait analysis.

## Software Diagram
<img src="https://raw.githubusercontent.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device/main/IMAGES/Softwarediag.png"  width="100%" height="100%">

As the patient walks using the Gait Analysis sock, the doctors can analyze the pressure applied, time information, and spatial characteristics of the feet. Utilizing pressure sensors, the system records the pressure distribution, initial point of contact, and angle of the foot. By employing a complementary filter that combines pressure distribution and accelerometer data (modified with homogeneous transformation), the angle of the foot on the ground can be calculated while the sensor is attached to the ankle. The IMU data can further aid in determining spatial characteristics and cadence.


## Implementation
<img src="https://raw.githubusercontent.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device/main/IMAGES/Implementation.jpg"  width="100%" height="100%">
<img src="https://raw.githubusercontent.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device/main/IMAGES/BUILD_1.jpg"  width="100%" height="100%">
<img src="https://raw.githubusercontent.com/Tatwik19/SoulTech-Portable-Gait-Analysis-Device/main/IMAGES/BUILD_3.jpg"  width="100%" height="100%">
<br />

### Calculating Gait Characteristics
- Pressure
- Stance time
- Point of contact
- Stance
- Stride Length 
- Stride Width 
- Cadence 
- Spatial Characteristics


<video controls>
  <source src="https://user-images.githubusercontent.com/96451759/234762332-7743c3fe-cdfe-4230-942c-10e17a4d2a56.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


## FUTURE WORK/RECOMMENDATIONS
Since this is currently a working prototype, future iterations can focus on improving data accuracy and integrating the device with a sock for potential use in clinical settings or commercial sales.

1. Using Advanced Microcontrollers <br />
Arduino Platform is great for straightforward tasks but fails when burdened with huge data and when accurate data is expected as its computational abilities are very limited. The team could explore more microcontrollers such as Raspberry, on the other hand, offers a better platform as it can handle larger complex data, handle multiple tasks concurrently, and  ntegrate additional functionalities, such as advanced algorithms, communication protocols, or even graphical user interfaces.

2. Implementing advanced filtering algorithms: <br />
Sophisticated filtering algorithms can improve the accuracy of gait analysis by reducing noise in data. AI techniques like machine learning and signal processing can be used to develop these algorithms, which can adjust to various data scenarios, ensuring accurate results for different patients and settings.

3. Detecting patterns and predicting future gait changes: <br />
Applying machine learning algorithms to gait data can identify recurring patterns, anomalies, and changes over time, which can help detect potential problems, monitor treatment success, and develop customized rehabilitation programs. Predicting and modeling future gait changes can also be accomplished using AI techniques like time-series analysis and recurrent neural networks. These prediction programs can anticipate issues before they arise by analyzing past gait data, allowing healthcare practitioners to intervene proactively, modify treatment plans, or offer advice to patients. This has the potential to enhance patients' long-term health and mobility.

4. Integration with other wearables and IoT devices <br />
A more thorough view of a patient's general health and activity levels can be obtained by expanding the system to incorporate data from additional wearable devices, such as smartwatches or fitness trackers. By integrating IoT devices, healthcare professionals, patients, and researchers can share data and monitor patients remotely. Better decisions, more individualized care, and greater health outcomes can all be facilitated by this connected environment.

## ACKNOWLEDGMENT
The authors would like to express their sincere appreciation to Professor Troy McDaniel, the team's mentor, and EGR 555 Mechatronic Systems class professor. His invaluable guidance, expertise, and support throughout the project were greatly appreciated. The authors would also like to extend their gratitude to Joelly Lobato De Faria and Kyle Sandoval, health practitioners at Barrow Institute, for serving as clients and main customers. Their insights, feedback, and direction provided invaluable support for the project's success.
