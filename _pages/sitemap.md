---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

<h1>Pages</h1>
{% for post in site.pages %}
  {% include archive-single.html %}
{% endfor %}

<h1>Other contents</h1>

{% for collection in site.collections %}
{% unless collection.output == false or collection.label == "posts" %}
  {% capture label %}{{ collection.label }}{% endcapture %}
  {% if label != written_label %}
  <h2><i>{{ label }}</i></h2>
  {% capture written_label %}{{ label }}{% endcapture %}
  {% endif %}
{% endunless %}
{% for post in collection.docs %}
  {% unless collection.output == false or collection.label == "posts" %}
  {% include archive-single.html %}
  {% endunless %}
{% endfor %}
{% endfor %}
