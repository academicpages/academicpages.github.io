---
layout: archive
title: "People"
permalink: /people/
show_date: false
author_profile: true
---

{% include base_path %}

{% for post in site.people %}
  {% include archive-single.html %}
{% endfor %}
