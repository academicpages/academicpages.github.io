---
layout: archive
title: "News"
permalink: /news/
author_profile: false
---

{% include base_path %}

News List
=====

<ul>
  {% for post in site.news %}
    <li>{{ post.title }}</li>
  {% endfor %}
</ul>


{% for post in site.news reversed %}
  <p style="display: inline;">{{ forloop.rindex }}. {% include archive-single-news.html %} </p>
{% endfor %}