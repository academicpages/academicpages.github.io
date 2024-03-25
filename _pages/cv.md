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
* Ph.D. in Medicine, 2023
  * Division of Radiology and Biomedical Engineering, Graduate School of Medicine, The University of Tokyo, Tokyo, Japan
  * Supervisor: Professor Osamu Abe
* Special Research Student, 2020
  * NARA Institute of Science and Technology (NAIST), Nara, Japan
  * Duties included: Building open biomedical corpus, analysing privacy risk of sharing AI models
  * Supervisor: Professor Eiji Aramaki
* B.S. in Medicine, 2015
  * Department of Medicine, The University of Tokyo, Tokyo, Japan

Work experience
======
* Department of Computational Diagnostic Radiology and Preventive Medicine, the University of Tokyo Hospital, 2023--
* Department of Radiology, the University of Tokyo Hospital, 2021--2022
* Department of Radiology, Toranomon Hospital, 2019--2020
* Department of Radiology, SHOWA University Northern Yokohama Hospital, 2018
* Department of Radiology, SHOWA University Hospital, 2018
* Department of Radiology, SHOWA University Fujigaoka Hospital, 2017
* Department of Radiology, SHOWA University Hospital, 2017

Skills
======
* Diagnostic Radiology
* Natural Language Processing
* Passed LPIC Essentials
* Passed Fundamental Information Technology Engineer Examination

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
