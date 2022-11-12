---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

{% if author.semanticscholar %}
  You can also find my articles on my [Semantic Scholar profile]({{ author.semanticscholar }}).
{% endif %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
