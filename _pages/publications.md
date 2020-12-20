---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
{% include base_path %}

[comment]: <> (You can also find my articles on <a href="https://scholar.google.com/citations?user=EMExrOMAAAAJ&hl=en"> Google Scholar profile</a>.)


{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
