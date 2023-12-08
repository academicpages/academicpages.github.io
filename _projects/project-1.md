---
title: "Two-Axis Tilting CNC Rotary Table"
excerpt: "Custom two-axis tilting rotary table with pneumatic brake<br/><img src='/images/Two-Axis_Tilting_NC_Rotary_Table_w500.png'>"
collection: projects
tags: design, machine
---

![Two-Axis Tilting Rotary Table](/images/Two-Axis_Tilting_NC_Rotary_Table_w500.png)

This two-axis rotary table is developed for integration into a multi-axis CNC milling machine. It was designed, manufactured and assembled by me, using a variety of custom machined parts and off-the-shelf components. Primary goals were to machine non-ferrous metals and plastics using 3+2 style and full 5-axis machining techniques. I have begun designing and building a full 5-axis CNC milling machine that will eventually use this rotary table. The mill structure is similar to a bridge mill, where the x-axis and rotary axes will travel underneath the y-axis and mill spindle, as shown below. 

![5-Axis CNC Bridge Mill](/images/Mill Render 1_w300.jpg)

*Milling machine concept*

This project provided many opportunities to learn more about machine design, electronics, programming, motor and gearbox sizing, servo tuning, pneumatics, fabrication and systems integration.

## Design

This two-axis tilting rotary table is designed to be compact and stiff (both moment stiffness and torsional stiffness). Primary components include:

1. Large diameter needle roller thrust bearings
2. Oversized crossed roller bearings
3. Harmonic drives (strain wave gear reducers)
4. AC servo motors with absolute shaft encoders
5. Trunnion style support bearing arrangement
6. Pneumatic brake for clamping

Shown below are several section views showing internal components and design elements:

![Two-axis trunnion 1](/images/2 Axis Trunnion Render 1_wLabels_w500.jpg)

*3D model showing 750W servo motor with absolute encoder and support bearing* 

![Two-axis trunnion 2](/images/2 Axis Trunnion Render 2_wLabels_w500.jpg)

*Integrated 200W rotary table servo motor and 80:1 harmonic drive*

![Two-axis trunnion 3](/images/2 Axis Trunnion Render 3_wLabels_w500.jpg)

*Pneumatic brake construction with large diameter piston for high clamping force*

![Two-axis trunnion 4](/images/2 Axis Trunnion Render 4_wLabels_w500.jpg)

*5 inch diameter rotary table using oversized needle roller thrust bearings for smooth motion and high stiffness*



### C-Axis Pneumatic Brake

![Two-axis rotary table brake](/images/2 Axis Trunnion Brake Explode_w600.jpg)

*Exploded view of rotary table brake components*

For simplicity and cost reasons I used brake pads commonly found in hydraulic mountain bike brake. Seven of these pads are mounted to the drive pulley of the spindle. A stainless steel brake rotor is mounted to an axially compliant but torsionally stiff [flexure](https://en.wikipedia.org/wiki/Flexure). When air is applied the piston clamps the rotor, the rotor shifts axially and clamps against the brake pads and drive pulley, locking the rotary table. A wave spring provides a returning force to unclamp the brake when air is removed from the system. This brake design provides stiff and backlash-free clamping of the rotary table due to the unique brake rotor flexure design. The rotary table can be clamped with up to 115 Nm of brake torque @ 100 psi (depends on air pressure). 

![Two-axis rotary table brake enlarged](/images/2 Axis Trunnion Brake Explode_wLabels_w600.jpg)

*Enlarged image of brake rotor and brake piston*

![Two-axis rotary table brake rotor](/images/2 Axis Trunnion Brake Rotor Explode_w600.jpg)

*Brake rotor flexure assembly*

![Two-axis rotary table brake prototype](/images/2 Axis Trunnion Brake Rotor Prototype_w600.jpg)

*C-Axis belt drive, rotary table brake pads and drive pulley*

### Compact C-Axis Motor and Drivetrain

I wanted to have the C-axis motor and drivetrain tucked inside the body of the rotary table to shield it from metal chips and coolant.

![Two-axis rotary table brake rotor](/images/2 Axis Trunnion Motor_w600.jpg)

*C-Axis motor, gearbox and belt drive*



### High Torque A-Axis Servo Motor and Harmonic Drive

The A-axis uses a rebuilt [SHF-40-100-2UH](https://www.harmonicdrive.net/products/gear-units/hollow-shaft-gear-units/shf-2uh/shf-40-100-2uh) harmonic drive from Harmonic Drive Solutions. This gear reducer also includes a very stiff preloaded crossed roller bearing to support any radial, axial or moment loads. Harmonic drives operate with very little angular backlash (< 7 arc sec [0.002 degrees]), hysteresis and excellent positional accuracy (1 arc min [0.0166 degrees]) - making them a great option for this rotary table. They offer a large gear reduction in a very small package with great mechanical efficiency and torsional stiffness. This particular unit is 100:1, with a rated torque of 265 Nm and a momentary peak torque above 1000 Nm, although the 750W servo motor would not be able to output the required torque. I was able to get this unit from a machine rebuilder on Ebay for a great price, along with a replacement crossed roller bearing from a Taiwan supplier.

![Two-axis rotary table bearing](/images/2 Axis Trunnion A-Axis Gearing_w600.jpg)

*A-Axis before assembly - Harmonic drive adaptor plate visible on left*

![Two-axis rotary table bearing](/images/2 Axis Trunnion A-Axis Bearing_w600.jpg)

*New crossed roller bearing - replacement for used harmonic drive bearing*

![Two-axis rotary table support bearing shaft shims](/images/2 Axis Trunnion A-Axis Support Shims_w600.jpg)

*Shimming alignment of secondary support bearing shaft to be co-axial with A-Axis rotation axis*
