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
* B.S. in Information Engineering, Nanjing University, 2015
* M.S. in Optical Engineering, Nanjing University, 2017
* Ph.D in Computer Science and Engineering, The Chinese University of Hong Kong, 2021 (expected)
  
Skills
======
* Matlab, C
* Python
  * TensorFlow
  * Pytorch

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
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
  
Service
======
* Review papers for top conferences:
  * 2019: ACL 2019,ICLR 2019, DSN 2019, AAAI 2019
  * 2018: NIPS 2018, EMNLP 2018, IJCAI 2018
