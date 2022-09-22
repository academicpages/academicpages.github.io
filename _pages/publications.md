---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

**Highlighted publications**

{% if author.pubmed %}
  You can also find our articles on <u><a href="{{author.pubmed}}">PubMed</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
