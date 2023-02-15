---
layout: archive
title: "Posters"
permalink: /posters/
author_profile: true
---

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
