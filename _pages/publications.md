---
layout: archive
title: "Publications"
author_profile: true
---


- &quot;Planted matching problems on random hypergraphs.&quot;, Adomaityte, U. and Toshniwal, A. and Sicuro, G. and Zdeborová, L. (2022). Physical Review E 
[[paper](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.106.054302) [arxiv](https://arxiv.org/abs/2209.03423)]

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
