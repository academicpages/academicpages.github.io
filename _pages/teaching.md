---
permalink: /teaching/
title: "Teaching"
excerpt: "Teaching"
redirect_from: 
  - /teaching.html
---

This semester I'm teaching [CS 4110](https://www.cs.cornell.edu/courses/cs4110/2020fa).

In the past I've taught the following courses:
<ul>
{% for course in site.data.courses reversed %}

{% if course.semester == "Fall" %}
{% assign sem = "fa" %}
{% else %}
{% assign sem = "sp" %}
{% endif %}

<li> <a href="https://www.cs.cornell.edu/courses/cs{{ course.number }}/{{ course.year }}{{ sem }}/">CS {{ course.number }}</a> ({{ course.year }} {{ course.semester }})</li>
{% endfor %}
</ul>
