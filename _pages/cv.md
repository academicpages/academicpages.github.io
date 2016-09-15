---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /wordpress/cv/
---


{% include base_path %}
{% capture written_label %}'None'{% endcapture %}


Education
======
* B.S. in Github, Github University, 2010
* M.S. in Jekyll, Github University, 2012

Publications
======
  {% for post in site.articles %}
    {% include archive-single-cv.html %}
  {% endfor %}

Talks
======
  {% for post in site.talks %}
    {% unless post.talk_type == "Conference proceedings talk" %}
      {% include archive-single-talk-cv.html %}
    {% endunless %}
  {% endfor %}
