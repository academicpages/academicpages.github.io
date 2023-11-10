---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


The complete list of my publications can also be found on <a href="https://scholar.google.com/citations?user=nmgE5hkAAAAJ&hl=en&authuser=2">my Google Scholar profile.

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}