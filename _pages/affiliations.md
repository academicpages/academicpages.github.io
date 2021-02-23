---
layout: archive
title: "Affiliations"
permalink: /affiliations/
author_profile: true
---

{% include base_path %}

{% for post in site.affiliations reversed %}
  {% include archive-single.html %}
{% endfor %}
