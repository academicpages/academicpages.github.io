---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on [my Google Scholar profile](https://scholar.google.com/citations?user=9nZlUHkAAAAJ&hl=en).

{% include base_path %}

## Conferences and Journals
{% for post in site.publications reversed %}

{% endfor %}

## Other Publications
{% for post in site.publications reversed %}
    {% if post.tags contains 'other' %}
      {% include archive-single.html %}
	{% endif %}
{% endfor %}
