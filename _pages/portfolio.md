---
layout: archive
title: "Portfolio Projects"
permalink: /portfolio-projects/
author_profile: true
---

Here you'll find different data science projects. These projects may be related to publications (linked if they are) or are just interesting questions/problems in the data science world.

{% include base_path %}

{% for post in site.portfolio-projects %}
{% include archive-single.html %}
{% endfor %}
