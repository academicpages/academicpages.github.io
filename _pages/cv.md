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
* B.A. in [Education, Communities, and Organizations](https://education.uw.edu/programs/undergraduate/eco) @ University of Washington, Seattle, 2020
* B.S. in [Computer Science](https://www.cs.washington.edu/academics/ugrad) @ University of Washington, Seattle, 2020
* Ph.D in [Educational Psychology & Educational Technology](https://education.msu.edu/cepse/epet/) @ Michigan State University, 2024 (expected)

# Publications
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
# Teaching
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

# Talks
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
# Awards and Honors
* Husky 100, University of Washington (2020)
* Summer Research Fellowship, Michigan State University (2022)
