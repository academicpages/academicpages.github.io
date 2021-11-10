---
layout: archive
title: "Research"
permalink: /publications/
author_profile: true
---

{% include base_path %}

## Working papers

{% for post in site.workings reversed %}
  {% include archive-single.html %}
{% endfor %}

## Published papers

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}