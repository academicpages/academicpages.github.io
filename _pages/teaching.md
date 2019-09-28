---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

{% include base_path %}

{% for x in site.data.teaching %}
  - {{ x.title }}. {{ x.venue }}. {% if x.inviter %}Invited by {{ x.inviter }}.{% endif %} ({{ x.date }})
{% endfor %}
