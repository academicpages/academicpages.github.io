---
layout: archive
title: "Recent Publications"
permalink: /publications/
author_profile: true
---

{% if author.location %}
  You can also find my articles on <u><a href="{{author.location}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
