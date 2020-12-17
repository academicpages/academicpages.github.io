---
layout: default
title: "Projets"
excerpt: "Projets"
permalink: /projects/
author_profile: true
---

{% for post in site.projects reversed %}
  {% if post.title == title %}
    {% include projectdetailled.html %}
    {% endif %}
{% endfor %}
