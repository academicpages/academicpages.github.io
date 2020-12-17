---
layout: default
title: "Projets"
excerpt: "Projets"
permalink: /projectdetails/
author_profile: true
---

{% for post in site.projects reversed %}
  {% if post.title == title %}
    test {{title}}
    {% include projectdetails.html %}
  {% endif %}
{% endfor %}
