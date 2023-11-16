---
layout: archive
title: "Publication"
permalink: /publication/
author_profile: true
redirect_from:
  - /publications
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publication reversed %}
  {% include archive-single.html %}
{% endfor %}
