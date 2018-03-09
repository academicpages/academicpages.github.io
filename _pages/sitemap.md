---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

{% for post in site.pages %}
  {% include archive-single.html %}
{% endfor %}
