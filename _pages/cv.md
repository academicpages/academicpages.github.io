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
* Bachelor of Science(Honours). Major in Astrophysics and Geology, Honours in Astrophysics, Monash University, 2013-2017
* PhD in Astrophysics, Monash University, 2018-2021(expected)

Work experience
======
* Feb 2017 - Current: Teaching Assistant
  * Monash University

Skills
======
* Skill 1
* Skill 2
  * Sub-skill 2.1
  * Sub-skill 2.2
  * Sub-skill 2.3
* Skill 3

Awards
======
* Australian Postgraduate Award
* MoCa Prize - Best astrophysics honours student at Monash, 2017
* J.L Williams Honours scholarship

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
