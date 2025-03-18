---
title: "Sparsely Actuated Modular Metamaterials for Shape Changing Interfaces"
excerpt: " Shape changing interfaces are robotic devices that can show notifications, physicalize data and provide a tangible entity to interact with and they can easily blend into everyday environments. This project proposes using sparsely actuated metamaterial systems for designing nature-inspired shape-changing interfaces. We explore the advantages of having the internal flexibility of the metamaterial structure as a design parameter for achieving multi degree-of-freedom curvilinear patterns through sparsely placed actuators. This project aims to help designers with design and simulation the presented structures to help improve the iterative fabrication process.
<br/> <img src='/images/MetamatGif3.gif'>  "
collection: projects
---

<br/><img src='/images/Teaser5.png'>

**[Link to related github repository](https://github.com/aotaran/MetamaterialDesignAndSimulation)**

Lets see what we mean by "sparsely actuated", "modular" and "metamaterials" using the video below. The metamaterials are the blue and white pieces that are combination of rigid (PLA/ABS) and flexible (TPU) 3d printed parts. They are basically mechanisms that define deformation pattern of the shape changing interface. They can be modularly extended by adding multiple metamaterials together, attaching shapes to them and finally used as a shape changing interface by attaching them servo motors and actuating them.  

<figure class="video_container">
  <video controls="true" allowfullscreen="true" width="100%">
    <source src="/videos/ButterflyVideo.mp4" type="video/mp4" width="100%">
  </video>
</figure>

By changing the width and length of the flexible sections in the design we can control the flexibility across the whole structure. When use an actuator to drive a joint the actuation is not propagated completely to neighboring cells, which makes sense and increasing the flexibility causes actuation to stay more localized. The implication of this is that although the underlying mechanism is single degree of freedom, flexibility of joints provides additional degrees of freedom and we can attach actuators on different locations to control the local deformations. This is what we call sparse actuation. And this allows us achieve diverse curvilinear patterns with multiple actuators. Taking inspiration from how multiple muscles deform flexible bodies in nature, we can easily achieve applications like below using sparsely actuated metamaterials.  

<figure class="video_container">
  <video controls="true" allowfullscreen="true" width="100%">
    <source src="/videos/MetamaterialAppsShort.mp4" type="video/mp4" width="100%">
  </video>
</figure>

The question is, how to reduce the number of fabrication iterations for achieving such shape changing interfaces. For this, we present a design and simulation tool to help designers in the decision making process. You can find more details about the tool in our paper, or in the project GitHub page. Below is a sample run of the design and simulation tool for making the gripper application (sped up by 4x).

<figure class="video_container">
  <video controls="true" allowfullscreen="true" width="100%">
    <source src="/videos/GripperDesign4x.mp4" type="video/mp4" width="100%">
  </video>
</figure>

**Related Academic work**

<sub> <ins> Ata Otaran </ins>, Yu Jiang and Jürgen Steimle</sub> \
<sub> [Sparsely actuated modular metamaterials for shape-changing interfaces](https://dl.acm.org/doi/10.1145/3689050.3704942)  </sub> \
<sub> **International Conference on Tangible, Embedded, and Embodied Interaction (TEI)** 2025 </sub>
