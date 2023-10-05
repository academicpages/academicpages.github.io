---
layout: archive
title: "Research"
permalink: /publications/
author_profile: true
---

You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>

<!-- {% if author.googlescholar %} --> 

<!-- {% endif %} --> 

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
