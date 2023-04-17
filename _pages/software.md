---
layout: archive
title: "Software"
permalink: /software/
author_profile: true
---

{% include base_path %}

{% for post in site.publications reversed %}
  {% if post.softwarename %}
    {% include archive-single-software.html %}
  {% endif %}
{% endfor %}
