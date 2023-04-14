---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

**Highlighted publications**


You can also find our articles on <u><a href="https://pubmed.ncbi.nlm.nih.gov/?term=rachel+knevel">PubMed</a>.</u>


{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
