---
title: "Automated Medium Refreshment for Cells Growth"
excerpt: "Circuit Based Automation Project<br/><img src='/images/Total View.jpg' width = '300'>"
collection: portfolio
---
This project aims to automate laboratory tasks such as media refreshment while also preventing risks of contamination by reducing contact with human. 
A set of peristaltic pumps, a Raspberry Pi, stepper drivers, and a flow sensor was used to formulate the machine and the gantry was created with collaboration with other Ph.D students. 

<table style="width:100%; text-align:center; border: none;">
  <tr>
    <td style="border: none;">
      <img src='/images/Pump.jpg' width='300' alt='Peristaltic Pump Setup'/>
    </td>
    <td style="border: none;">
      <img src='/images/Circuit.jpg' width='300' alt='Circuit Image'/>
    </td>
  </tr>
  <tr>
    <td style="border: none;">
    Peristaltic Pump Setup</td>
    <td style="border: none;">
    Circuit Image</td>
  </tr>
</table>


The machine supports two types of operations:
1. A continuous refreshment of media at a fixed flowrate 

    A PID control mechanism is used where the flow rate reading from the sensor is used to control the stepper driver for desired speed. 

2. A medium refreshment for a fixed volume

    The flowrate reading from the sensors are integrated at a set speed for the motor until the desired volume of media is refreshed. 
<p align= "center">
    <video width="300" controls>
    <source src="/images/Media Refreshment.mp4" type="video/mp4">
    </video>
    <br>
    Video for Media Refreshment
</p>
