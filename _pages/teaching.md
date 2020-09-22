---
layout: archive
title: "Media"
permalink: /media/
author_profile: true
---
My primary research interests lie at the interface of Optimization and Machine Learning with applications in Healthcare and Finance. Specifically, I work on designing novel Optimization algorithms for Machine Learning problems using tools from Robust and Discrete Optimization.

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
