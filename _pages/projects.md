---
layout: default
title: "Projets"
excerpt: "Projets"
permalink: /projects/
author_profile: true
---

{% for post in site.projects  %}
  {% include project.html %}
{% endfor %}
