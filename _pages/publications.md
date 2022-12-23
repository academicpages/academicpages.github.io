---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

  You can also find my articles on [my Google Scholar profile.](https://scholar.google.com/citations?user=0lB9-GcAAAAJ&hl=en&authuser=1)
  
{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
