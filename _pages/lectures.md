---
layout: archive
title: "Lectures"
permalink: /lectures/
author_profile: true
---

{% include base_path %}

{% for post in site.lectures reversed %}
  {% include archive-single.html %}
{% endfor %}