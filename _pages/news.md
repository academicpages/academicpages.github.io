---
layout: archive
title: "News"
permalink: /news/
author_profile: false
---

{% include base_path %}
{% for post in site.pages %}
  {% include archive-single.html %}
{% endfor %}
