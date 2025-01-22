---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---
Full CV in PDF version [available here](../files/AtaOtaranCV_12_2024.pdf) (uploaded 12/2024).

{% include base_path %}

Education
======

<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
* {
  box-sizing: border-box;
}

body {
  background-color: white;
  font-family: Helvetica, sans-serif;
}

/* The actual timeline (the vertical ruler) */
.timeline {
  position: relative;
  max-width: 1200px;
  margin: 0 auto;
}

/* The actual timeline (the vertical ruler) */
.timeline::after {
  content: '';
  position: absolute;
  width: 6px;
  background-color: #474e5d;
  top: 0;
  bottom: 0;
  left: 50%;
  margin-left: -3px;
}

/* Container around content */
.container {
  padding: 10px 40px;
  position: relative;
  background-color: inherit;
  width: 50%;
}

/* The circles on the timeline */
.container::after {
  content: '';
  position: absolute;
  width: 25px;
  height: 25px;
  right: -17px;
  background-color: #474e5d;
  border: 4px solid #FF9F55;
  top: 15px;
  border-radius: 50%;
  z-index: 1;
}

/* Place the container to the left */
.left {
  left: 0;
}

/* Place the container to the right */
.right {
  left: 50%;
}

/* Add arrows to the left container (pointing right) */
.left::before {
  content: " ";
  height: 0;
  position: absolute;
  top: 22px;
  width: 0;
  z-index: 1;
  right: 30px;
  border: medium solid white;
  border-width: 10px 0 10px 10px;
  border-color: transparent transparent transparent white;
}

/* Add arrows to the right container (pointing left) */
.right::before {
  content: " ";
  height: 0;
  position: absolute;
  top: 22px;
  width: 0;
  z-index: 1;
  left: 30px;
  border: medium solid white;
  border-width: 10px 10px 10px 0;
  border-color: transparent white transparent transparent;
}

/* Fix the circle for containers on the right side */
.right::after {
  left: -16px;
}

/* The actual content */
.content {
  padding: 20px 30px;
  background-color: white;
  position: relative;
  border-radius: 6px;
}

/* Media queries - Responsive timeline on screens less than 600px wide */
@media screen and (max-width: 600px) {
  /* Place the timelime to the left */
  .timeline::after {
  left: 31px;
  }
  
  /* Full-width containers */
  .container {
  width: 100%;
  padding-left: 70px;
  padding-right: 25px;
  }
  
  /* Make sure that all arrows are pointing leftwards */
  .container::before {
  left: 60px;
  border: medium solid white;
  border-width: 10px 10px 10px 0;
  border-color: transparent white transparent transparent;
  }

  /* Make sure all circles are at the same spot */
  .left::after, .right::after {
  left: 15px;
  }
  
  /* Make all right containers behave like the left ones */
  .right {
  left: 0%;
  }
}
</style>
</head>
<body>

<div class="timeline">
  <div class="container left">
    <div class="content">
      <h2>2017 - 2022 </h2>
      <p>Ph.D. in Computer Science <br> Queen Mary University of London</p>
      <p>Thesis: Ankle-Actuated Human-Machine Interface for Walking in Virtual Reality</p>
      <p>Advisor: Dr. Ildar Farkhatdinov</p>
    </div>
  </div>
  <div class="container right">
    <div class="content">
      <h2> 2015 - 2017 </h2>
      <p> M.Sc. in Mechatronics <br> Sabanci University, Istanbul
      <p> GPA: 3.90/4 </p>
      <p> Thesis: Design and Control of Series Elastic Actuated Educational Devices </p>
      <p> Advisor: Prof. Volkan Patoglu </p>
    </div>
  </div>
  <div class="container left">
    <div class="content">
      <h2>2011 - 2015 </h2>
      <p> B.Sc. in Mechatronics with Minors in Mathematics <br>  Sabanci University, Istanbul </p> 
      <p> GPA: 3.58/4 (4th out of 38) </p>
      <p> Thesis: Design and Control of a Ballbot </p>
      <p> Advisor: Prof. Volkan Patoglu </p>
    </div>
  </div>
</div>

</body>
</html>


<p><details> <summary> Ph.D. in Computer Science, Queen Mary University of London, 2017 - 2022 </summary>
<ul style="list-style-type:circle">
  <li> Thesis: Ankle-Actuated Human-Machine Interface for Walking in Virtual Reality</li>
  <li> Advisor: Dr. Ildar Farkhatdinov </li>
</ul>  
</details> </p>


<p><details> <summary> M.Sc. in Mechatronics, Sabanci University, Istanbul, 2015 - 2017 </summary>
<ul style="list-style-type:circle">
  <li>  GPA: 3.90/4 </li>
  <li> Thesis: Design and Control of Series Elastic Actuated Educational Devices </li>
  <li> Advisor: Prof. Volkan Patoglu </li>
</ul>  
</details> </p>

<p><details> <summary>  B.Sc. in Mechatronics with Minors in Mathematics, Sabanci University, Istanbul, 2011 - 2015 </summary> 
<ul style="list-style-type:circle">
  <li>  GPA: 3.58/4 (4th out of 38) </li>
  <li>  Thesis: Design and Control of a Ballbot </li>
  <li>   Advisor: Prof. Volkan Patoglu </li>
</ul>  
</details> </p>

<!-- Robert College, Istanbul, 2006 - 2011 -->

<!--
*  Ph.D. in Computer Science, Queen Mary University of London, 2017 - 2022
    * Thesis: Ankle-Actuated Human-Machine Interface for Walking in Virtual Reality
    *  Advisor: Dr. Ildar Farkhatdinov
* M.Sc. in Mechatronics, Sabanci University, Istanbul, 2015 - 2017
    * GPA: 3.90/4
    * Thesis: Design and Control of Series Elastic Actuated Educational Devices
    * Advisor: Prof. Volkan Patoglu
* B.Sc. in Mechatronics with Minors in Mathematics, Sabanci University, Istanbul, 2011 - 2015
    * GPA: 3.58/4 (4th out of 38)
    * Thesis: Design and Control of a Ballbot
    * Advisor: Prof. Volkan Patoglu 
-->
    
Academic Work Experience
======
* Postdoctoral researcher at HCI Group in Saarland University, Saarbrücken February 2022 - October 2024
  * Teaching Assistant at HCI Course for Winter semesters of '22 and '23: Organization of 200 student courses for two semesters including tutorials, homeworks and exams, 2022 - 2024
  * Supervision of three thesis projects and five project-based seminar groups, 2022 - 2024
* Teaching assistance on MSc and BSc level courses for 12 semesters, 2015 - 2021
  * Topics included linear algebra, robotics, computer-aided design and Python programming
* TUBITAK (Scientific and Technological Research Council of Turkey) funded project member, September '15 - June '17
  * Implementation of a SEA for a gait rehabilitation robot
  
Non-teaching part-time work experience
======
* Developer for a virtual 3D laboratory learning environment for biomechanics courses at QMUL as a part of the Humanoid project, July-December 2021
* Research engineer for developing a VR locomotion interface as a part of an EU funded project, May-July 2021
* Research assistant in NCNR Project on user interfaces for robot teleoperation, 2019 and 2021

Skills
======
* Programming
  * MATLAB & Simulink
  * C++ & C#
  * Python
  * ROS
* 3D Design & visualisation
  * Solidworks, Inventor
  * Blender
  * Unity
  * Gazebo
* Embedded controllers
  * TI C2000 series
  * BeagleBone
  * Arduino
* Data acquisition devices
  * NI-DAQ
  * Quanser
  * dSPACE
* FEA software
  * Ansys
  * Comsol

    
Publications
======
<div class="wordwrap">Please can also find my publications <a href="https://aotaran.github.io/publications/">here</a> or on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
<!-- 
- (Forthcoming) Otaran A., Jiang Y., & Steimle J., "Sparsely actuated modular metamaterials for shape-changing interfaces", International Conference on Tangible, Embedded, and Embodied Interaction (TEI), 2025
- (Forthcoming) Sabnis N., Otaran A., Wittchen D., Didion J., Steimle J., \& Strohmeier P. "Foot Pedal Control: The Role of Vibrotactile Feedback in Performance and Perceived Control", International Conference on Tangible, Embedded, and Embodied Interaction (TEI), 2025
- Otaran, A., Farkhatdinov, I. Exploring User Preferences for Walking in Virtual Reality Interfaces Through an Online Questionnaire. Human Computer Interaction International (HCII), 2024
- Artin Saberpour Abadian, Ata Otaran, Martin Schmitz, Marie Muehlhaus, Rishabh Dabral, Diogo Luvizon, Azumi Maekawa, Masahiko Inami, Christian Theobalt, and Jürgen Steimle. 2023. Computational Design of Personalized Wearable Robotic Limbs. In Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology (UIST '23).
- Otaran A. and Farkhatdinov I., "Haptic Ankle Platform for Interactive Walking in Virtual Reality," in IEEE Transactions on Visualization and Computer Graphics (TVCG), 2021
- Otaran A. and Farkhatdinov I., "Walking-in-Place Foot Interface for Locomotion Control and Telepresence of Humanoid Robots," 2020 IEEE-RAS 20th International Conference on Humanoid Robots (Humanoids), 2021, pp. 453-458
- Otaran, A., Tokatli, O., & Patoglu, V. (2021). Physical Human-Robot Interaction Using HandsOn-SEA: An Educational Robotic Platform with Series Elastic Actuation. IEEE Transactions on Haptics (TOH).
- Otaran, A., & Farkhatdinov, I. (2021, March). A Short Description of an Ankle-Actuated Seated VR Locomotion Interface. In 2021 IEEE Conference on Virtual Reality and 3D User Interfaces Abstracts and Workshops (VRW) (pp. 64-66). IEEE.
- Otaran, A., & Farkhatdinov, I. (2019, July). Modeling and Control of Ankle Actuation Platform for Human-Robot Interaction. In Annual Conference Towards Autonomous Robotic Systems (pp. 338-348). Springer, Cham.
- Caliskan, U., Apaydin, A., Otaran, A., & Patoglu, V. (2018, October). A series elastic brake pedal to preserve conventional pedal feel under regenerative braking. In 2018 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) (pp. 1367-1373). IEEE.
- Otaran, A., Tokatli, O., & Patoglu, V. (2018, June). HandsOn-Computing: Promoting Algorithmic Thinking Through Haptic Educational Robots. In International Conference on Human Haptic Sensing and Touch Enabled Computer Applications (pp. 564-574). Springer, Cham.
- Otaran, A. (2017). Design, control and evaluation of educational devices with series elastic actuation (MSc dissertation).
- Otaran, A., Tokatli, O., & Patoglu, V. ”Hands-On Learning with a Series Elastic Educational Robot”, in the Proceedings of the EuroHaptics as Lecture Notes in Computer Science, 2016.

-->
