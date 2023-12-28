---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

# The National Flood Insurance Program, Racial and Ethnic Disparity, and the Pursuit of Environmental Justice. With Jing Ai

# The Demographics of Property Insurance: Evidence from the Homeowners Insurance Market. With Jing Ai and Charles Nyce

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.research reversed %}
  {% include archive-single.html %}
{% endfor %}
