---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.researchgate %}
  You can also find our articles on <a href="{{site.author.researchgate}}">my ResearchGate profile</a>.
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

![Light-mech](/images/光影.jpg)

