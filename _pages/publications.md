---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
{% include base_path %}

[comment]: <> (You can also find my articles on <a href="https://scholar.google.com/citations?user=EMExrOMAAAAJ&hl=en"> Google Scholar profile</a>.)

## Peer-reviewed

{% for post in site.publications reversed %}
  {% if post.preprint != true %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

## Pre-prints
{% for post in site.publications reversed %}
  {% if post.preprint %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
