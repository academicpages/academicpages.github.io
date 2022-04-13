---
layout: archive
permalink: /posts/
title: "Blog posts"
author_profile: true
---

{% include base_path %}
{% capture written_year %}'None'{% endcapture %}
{% for post in site.posts %}
  {% include archive-single.html %}
{% endfor %}
