---
layout: archive
title: "Script Portafolio"
permalink: /publications/
excerpt: 'In this section scripts are made in both R and Python, you will see the results are not the same even if you work with the same data, since each of these programs has a different internal resolution.'
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
