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

<div class="cv-edu-inline" aria-label="Universities">
  <span class="cv-edu-chip"><img src="{{ base_path }}/images/orgs/imperial.jpg" alt="">Imperial College London · BSc 2019</span>
  <span class="cv-edu-chip"><img src="{{ base_path }}/images/orgs/oxford.jpg" alt="">Oxford · MSc 2020</span>
  <span class="cv-edu-chip"><img src="{{ base_path }}/images/orgs/harvard.jpg" alt="">Harvard · ME 2022</span>
</div>

* BSc in Mathematics, Imperial College London, 2019
* MSc in Mathematical Sciences, University of Oxford, 2020
* ME in Computational Science and Engineering, Harvard University, 2022

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
