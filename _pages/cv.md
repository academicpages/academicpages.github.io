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

* Ph.D. in [Educational Psychology & Educational Technology](https://education.msu.edu/cepse/epet/) @ Michigan State University, 2024 (expected)
* B.A. in [Education, Communities, and Organizations](https://education.uw.edu/programs/undergraduate/eco) @ University of Washington, Seattle, 2020
* B.S. in [Computer Science](https://www.cs.washington.edu/academics/ugrad) @ University of Washington, Seattle, 2020

# Publications
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
# Teaching
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

# Talks
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
# Awards and Honors
* [Husky 100](https://www.washington.edu/husky100/year/2020/#name=andrew-hu), University of Washington (2020)
* [Summer Research Fellowship](https://education.msu.edu/resources/academic-student-affairs/summer-research-fellowships/), Michigan State University (2022)
