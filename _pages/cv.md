---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## Experience

{% include experience.html %}

## Education

{% include education.html %}

## Skills
* Programming
  * Python (with PyTorch, Tensorflow)
  * C++/C
  * R
  * Matlab
  * Lisp
* Cloud computing Platforms
  * AWS
  * Microsoft Azure
* Dev tools
  * Git/Github
* Misc
  * Latex
* Languages
  * French
  * English
  * German

## Talks
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>

## Service and leadership
* Reviewing: New Perspectives in Graph Machine Learning (NPGML) workshop, NeurIPS 2025.
* De la Haute-Savoie aux grandes écoles
* Imperial College Oenology Society
