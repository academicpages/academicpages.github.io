---
layout: archive
title: "News"
permalink: /news/
author_profile: false
---

{% include base_path %}

{% for post in site.news reversed %}
  <p style="display: inline;">{{ forloop.rindex }}. {% include archive-single-news.html %} </p>
{% endfor %}