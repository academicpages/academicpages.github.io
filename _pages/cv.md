---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* B.Eng. in Computer Science, Beijing University of Posts and Telecommunications, 2023 (expected)

<!--
* B.S. in GitHub, GitHub University, 2012
* M.S. in Jekyll, GitHub University, 2014
* Ph.D in Version Control Theory, GitHub University, 2018 (expected)
-->

<!--
Work experience
======
* Summer 2015: Research Assistant
  * Github University
  * Duties included: Tagging issues
  * Supervisor: Professor Git

* Fall 2015: Research Assistant
  * Github University
  * Duties included: Merging pull requests
  * Supervisor: Professor Hub
-->

Research Experience
======
* July, 2022 - October, 2022(expected): Research intern / Visiting student
  * University of British Columbia
  * This research is under the Mitacs Globalink Research Internship program, jointly supported by Mitacs(Canada) and China Scholarship Council(China). The research project is in its infancy.
  * Explored approximation algorithms in dynamic graph processing, for example can we develop a pathing style algorithm similar to SSSP (perhaps approximate) that is functional with deletes?
  * Explored dynamic-only algorithms in dynamic graph processing instead of converting from static to dynamic, for example can we extend algorithms like pagerank to incorporate more metadata (like timestamps themselves) into one form of weight?
  * Advisor: [Prof. Matei Ripeanu](https://people.ece.ubc.ca/matei/)
* October, 2020 - Present: Research intern
  * Beijing University of Posts and Telecommunications
  * Paper(expected): ”Interactive Realistic Real-time Animation on Mobile Platforms”
  * Explored real-time realistic animation plugins embedded into graphics rendering pipelines that can be plugged into almost any existing rendering pipeline, rather than targeting output inference results (offsets) like existing deep learning frameworks. Through our pipeline, we reduce CPU-GPU transfer and synchronization time, and improve execution efficiency through specialized and fine-grained implementation.
  * Explored adaptive tetrahedral mesh generation to reduce computation for large 3D characters to ensure responsiveness (frame rate). According to the importance of the character triangle mesh to animation, the tetrahedral mesh is adaptively divided to reduce the amount of calculation, and the neural network method is used to infer the deformation of the tetrahedral mesh, so that even a large 3D model can be obtained within a few milliseconds next frame.
  * Advisor: [Mengwei Xu](https://xumengwei.github.io/)
* November, 2019 - September, 2020: Research intern
  * Peking University
  * Paper: ”Multi-view fusion based moving target tracking using IR-UWB devices”
  * Explored high-precision moving target tracking based on multiple IR-UWB devices. Firstly, the dynamic components are extracted by static elimination, then the multi-path interference is eliminated by Gaussian blurring, and finally the multi-view distance information is integrated to achieve high-precision moving target tracking. The error between the estimated center position of the human body and the real trajectory is always within 20cm.
  * Advisor: [Daqing Zhang](http://www-public.tem-tsp.eu/~zhang_da/DaqingZhang.html)

Honors and Awards
======
* China Computer Federation Student Member, August, 2020 - Present
* Mitacs Globalink Research Internship award, February, 2022
* First-class Scholarship, Beijing University of Posts and Telecommunications, December, 2021
* Beijing University of Posts and Telecommunications: Cultural and Sports Activists, December, 2021
* National Conference on Pervasive Computing (PCC 2020) Best Paper Award, China Computer Federation, October, 2020
* National Olympiad in Informatics, China(CCF NOI 2018) Bronze medal, China Computer Federation, July, 2018

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Skills
======
* Language: proficient in C/C++, Python; competent in Java.
* Knowledge: proficient in data structures and algorithms; competent to software and system development; Understand Linux, Windows
* Tool: competent in Latex, Git.

<!--  
Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* Currently signed in to 43 different slack teams
-->
