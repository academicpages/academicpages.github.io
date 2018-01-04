---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: false
sidebar:
  nav: "Projs"
---

{% include base_path %}


{% for post in site.projects %}
  {% include archive-single.html %}
{% endfor %}
