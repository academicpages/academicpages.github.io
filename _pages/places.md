---
layout: archive
title: "Places I've Been"
permalink: /places/
author_profile: true
---

{% include base_path %}


{% for post in site.places %}
  {% include archive-single.html %}
{% endfor %}
