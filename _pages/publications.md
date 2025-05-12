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
  {% unless post.hidden %}
    {% include archive-single.html %}
  {% endunless %}
{% endfor %}

![Light-mech](/images/光波.png)

