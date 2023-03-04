---
layout: archive
permalink: /posts/
title: "Blog posts"
author_profile: true
redirect_from:
  - /wordpress/blog-posts/
---

{% include base_path %}
{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}
