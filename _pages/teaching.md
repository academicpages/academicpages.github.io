---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

{% include base_path %}

{% for post in site.teaching reversed %}
  {% if post.academic_term %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
