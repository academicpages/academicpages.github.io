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
* M.A., Health Economics, Wuhan University, 2025 (Expected)
* B.A., Finance, Wuhan University, 2021
* B.E., Priting Engineer, Wuhan University, 2021

Skills
======
* Latex, Stata, R, Python, Matlab, sql

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
