---
layout: archive
title: "Talks"
permalink: /talks/
author_profile: true
---

This page is under construction.

No formal talks were presented by myself.

But you can appreciate this masterpiece

![masterpiece](http://toaa2.github.io/images/proim.png)

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{https://scholar.google.com/}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.articles reversed %}
  {% include archive-single.html %}
{% endfor %}
