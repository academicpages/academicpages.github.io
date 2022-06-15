---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

## Primary
{% for post in site.pubsprimary reversed %}
  {% include archive-single.html %}
{% endfor %}

## Other
{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
