---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

{% include base_path %}

{% for post in site.teaching reversed %}
  {% unless post.course_overview %}
    {% include archive-single.html %}
  {% endunless %}
{% endfor %}
