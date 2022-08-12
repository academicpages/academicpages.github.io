---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.researchgate %}
  You can also find my articles on <u><a href="{{site.author.researchgate}}">my ResearchGate profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}



