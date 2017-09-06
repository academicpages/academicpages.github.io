---
layout: archive
title: "Resources"
permalink: /resources/
author_profile: true
---

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
