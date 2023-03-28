---
layout: archive
title: "Gallery"
permalink: /gallery/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{https://scholar.google.com/citations?user=1q1nLY8AAAAJ&hl=en&oi=ao}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.gallery reversed %}
  {% include archive-single.html %}
{% endfor %}

