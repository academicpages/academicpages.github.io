---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---
hello
{% include base_path %}

{% for post in site.teaching reversed %}
  {% include archive-single.html %}
{% endfor %}
