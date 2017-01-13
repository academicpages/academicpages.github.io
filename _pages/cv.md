---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /wordpress/cv/
---

{% include base_path %}

Education
======
* B.S. in Github, Github University, 2012
* M.S. in Jekyll, Github University, 2014
* Ph.D in Version Control Theory, Github University, 2017 (expected)

Work experience
======
* Summer 2015: Research Assistant
  * Github University
  * Duties included: Rejecting pull requests
  * Supervisor: Professor Git

* Fall 2015: Research Assistant
  * Github University
  * Duties included: Rejecting pull requests
  * Supervisor: Professor Hub

Skills
======
* Skill 1
* Skill 2
  * Sub-skill 2.1
  * Sub-skill 2.2
  * Sub-skill 2.3
* Skill 3

Publications
======
  {% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}
 
<br/>
Talks
======
  {% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}
   
<br/>
Teaching
======
  {% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}
