---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: false
---

<h2>Pages</h2>
{% for post in site.pages %}
  {% include archive-single.html %}
{% endfor %}
