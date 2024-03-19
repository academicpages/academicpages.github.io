---
layout: archive
title: "Journal articles"
permalink: /publications/
author_profile: true

## to be put under when needed:
# #<sup>*</sup> Equal authorship
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% if post.type == "journal" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h1 style="margin-top: 100px;">In preparation</h1>
{% for post in site.publications reversed %}
  {% if post.type == "preprint" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h1 style="margin-top: 100px;">Other</h1>
{% for post in site.publications reversed %}
  {% if post.type == "other" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
