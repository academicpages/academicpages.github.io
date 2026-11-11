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

{% include skills.html %}

## Talks
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>

<script src="{{ base_path }}/assets/js/cv-skills.js"></script>

## Service and leadership
* Reviewing: New Perspectives in Graph Machine Learning (NPGML) workshop, NeurIPS 2025.
* De la Haute-Savoie aux grandes écoles
* Imperial College Oenology Society
