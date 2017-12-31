---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: false
---

{% include base_path %}


{% for post in site.portfolio %}
  {% include archive-single.html %}
{% endfor %}
