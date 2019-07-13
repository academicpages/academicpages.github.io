---
layout: archive
title: "Conferences Attended"
permalink: /test
author_profile: true
---


{% for post in site.conferences reversed %}
  {% include archive-single-conf-2.html %}
{% endfor %}
