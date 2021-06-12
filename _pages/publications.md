---
layout: archive
title: "Papers and Preprints"
permalink: /publications/
author_profile: false
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% for post in site.publications reversed %}
  {% include archive-simple.html %}
{% endfor %}

**Preprints

{% for post in site.publications reversed %}
  {% include archive-simple.html %}
{% endfor %}
