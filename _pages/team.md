---
layout: archive
title: "Team Members"
permalink: /team/
author_profile: true
---

{% include base_path %}


{% for post in site.team %}
  {% include archive-single.html %}
{% endfor %}
