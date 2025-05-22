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
* University of Pennsylvania, Summa Cum Laude (2016-2020)
  * B.S.E. in Chemical Engineering
  * B.A. in Physics (Concentration in Advanced Theory and Experimental Techniques)
* California Institute of Technology (2020-Present)
  * Ph.D. Candidate in Chemical Engineering

Experience
======
* Goddard Group, Caltech (2022-Present)
* Miller Group, Caltech (2020-2022)
* QuantumScape Corp (2019)
* Rappe Group, University of Pennsylvania (2016-2020)

Awards
======
* NSF Graduate Research Fellow (2020)
* Barry Goldwater Fellowship Honorable Mention (2018)

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

Skills
======

Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
