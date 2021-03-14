---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## Education

* Ph.D in Architecture and Civil Engineering, Granada University, 2017  
  (Department of Urbanism and Spatial Planning)
* M.Sc. in Urbanism, Spatial Planning and Environment, Granada University, 2010
* M.Sc. in Geographic Information Systems, UNIGIS - Girona University, 2010
* B.Sc. in Environmental Sciences, Granada University, 2008

## Publications

  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

## Teaching

  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

## Talks

  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
