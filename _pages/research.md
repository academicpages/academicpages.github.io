---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
header:
  og_image: "research/ecdf.png"
---
<h1>DARWIN -- Delaware Advanced Research Workforce and Innovation Network<h1>
<img src="" alt="Italian Trulli">

DARWIN is a compute and storage resource supporting computational and data-intensive research at the University of Delaware and in the Delaware Region. DARWIN is funded by an NSF MRI (Major Research Instrumentation) grant.
For more information, see the

In a new avenue of research, I leverage social media data to explore
participation in extremist movements across multiple contexts, gaining insight
into the early stages of radicalization.

<nbsp>

{% include base_path %}

{% assign ordered_pages = site.research | sort:"order_number" %}

{% for post in ordered_pages %}
  {% include archive-single.html type="grid" %}
{% endfor %}
