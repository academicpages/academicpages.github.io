---
layout: archive
title: "News"
permalink: /news/
author_profile: true
---

{% include base_path %}


{% for post in site.news %}
  {% include archive-single.html %}
{% endfor %}
