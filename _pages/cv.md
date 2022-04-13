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
* Diploma in Electrical and Computer Engineering (ECE), National Technical University of Athens (NTUA), 2016
* Ph.D in Computer Science, Technical University of Darmstadt, 2022

Work experience
======
* March 2016-now: Research Assistant
  * TU Darmstadt
  * Under the supervision of Prof. Max Mühlhäuser

* October 2015-March 2016: Resesarch partner
  * University of Athens (UoA)
  * Under the supervision of Prof. Aggelos Kiayias
  
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
  
Service and leadership
======
* USENIX Security Artifact Evaluation Committee (2022-)
* Invited reviewer for journals (EMSE, ACM CSUR, etc.)
