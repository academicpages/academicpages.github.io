---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

# Education
* B.S. in Computer Science @ University of Washington, Seattle, 2020
* B.A. in Education, Communities, and Organizations @ University of Washington, Seattle, 2020
* Ph.D in Educational Psychology & Educational Technology @ Michigan State University, 2024 (expected)

# Publications
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
# Talks
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
# Teaching
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
# Awards and Honors
* Husky 100, University of Washington (2020)
* Summer Research Fellowship, Michigan State University (2022)
