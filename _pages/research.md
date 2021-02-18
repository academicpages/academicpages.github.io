---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
type: grid
---

{% include base_path %}

{% for post in site.research reversed %}
  {% include archive-single-res.html %}
{% endfor %}
