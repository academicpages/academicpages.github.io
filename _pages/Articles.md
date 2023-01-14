---
layout: archive
title: "Articles"
permalink: /articles/
author_profile: true
---

This page is under construction.

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{https://scholar.google.com/}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
