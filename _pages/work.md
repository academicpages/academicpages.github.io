---
layout: archive
title: "Working experiences"
permalink: /work/
author_profile: true
---


{% include base_path %}


{% for post in site.work reversed %}
      {% include archive-single.html %}
{% endfor %}
