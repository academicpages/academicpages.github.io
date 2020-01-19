---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

In this page, you can find information related to my studies, publications and talks, among other things. 

## Research interests
My research interests include Human-Computer Interaction (HCI), 3D graphics and artificial intelligence. 

## Education
* **B.S. in Computer Science, University of Castilla~La Mancha**
  * **Date**: July 2018.
  * **Final Degree Project**: AsgAR: Graphical representation generator system for the visualization of programs and algorithms
  using Mixed Reality.
  * **Advisors**: Dr. Carlos González Morcillo and PhD. Santiago Sánchez Sobrino.

## Publications
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
## Talks
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
