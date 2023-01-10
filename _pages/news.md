---
layout: archive
title: "In the News"
permalink: /news/
author_profile: true
---

{% include base_path %}

{% for post in site.news reversed %}
  {% include archive-single.html %}
{% endfor %}
