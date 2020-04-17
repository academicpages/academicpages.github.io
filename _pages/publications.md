---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles in [my Google Scholar](https://scholar.google.com/citations?user=y3yJm98AAAAJ&hl=en). 

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
