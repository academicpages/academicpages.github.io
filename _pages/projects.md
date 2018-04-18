---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---


{% include base_path %}

{% for post in site.projects reversed %}
  {% include publication-single.html %}
{% endfor %}
