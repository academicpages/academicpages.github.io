---
layout: archive
title: "Selected publications"
permalink: /publications/
author_profile: true
---

Here are listed some of my recent research outputs. For my full list of publications, see my [Google Scholar page](https://researchportal.helsinki.fi/en/organisations/past-present-sustainability-paes).

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
