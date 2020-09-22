---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

My publication can also be found on <u><a href="https://scholar.google.com/citations?user=KQL8tB8AAAAJ&hl=en">google scholar</a>.</u>

<!-- {% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %} -->

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
