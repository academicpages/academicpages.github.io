---
layout: archive
title: "Conferences Attended"
permalink: /test
author_profile: true
---


  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>

  <ul>{% for post in site.conferences reversed %}
  {% include archive-single-talk-cv.html %}
{% endfor %}</ul>
