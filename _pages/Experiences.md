---
layout: archive
title: ""
permalink: /experiences/
author_profile: true
---


{% include base_path %}

Software development
======
* a b c

Research
======
* d e f

Engineering projects
======
* g h i

{% for post in site.experiences reversed %}
  {% include archive-single.html %}
{% endfor %}