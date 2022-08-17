---
layout: archive
title: "Publications"
permalink: /publications/
my_number: 5
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include publication.html %}
{% endfor %}

