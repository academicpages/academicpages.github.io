---
layout: default
title: "Projets"
excerpt: "Projets"
permalink: /
author_profile: true
---

{% for post in site.projects reversed %}
  {% include project.html %}
{% endfor %}
