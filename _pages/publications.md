---
layout: archive
title: "Research"
permalink: /publications/
author_profile: true
---

You can also find my articles on <u><a href="{{https://scholar.google.com/citations?user=T-xX3w0AAAAJ&hl=en}}">my Google Scholar profile</a>.</u>

<!-- {% if author.googlescholar %} --> 

<!-- {% endif %} --> 

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
