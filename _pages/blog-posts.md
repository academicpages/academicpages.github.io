---
layout: archive
title: "Blog"
permalink: /blog/
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.posts reversed %}
  {% include archive-blogs.html %}
{% endfor %}
