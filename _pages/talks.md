---
layout: archive
title: "Talks and presentations"
permalink: /talks/
author_profile: true
---

{% for talk in site.data.talks %}
  - {{ talk.type }}: "{{ talk.title }}". {% if talk.authors %}{{ talk.authors }}.{% endif %} {{ talk.place }} ({{ talk.date }})
{% endfor %}
