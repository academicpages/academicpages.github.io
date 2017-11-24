---
<!-- layout: archive -->
title: "Publications [(Google Scholar Profile)](https://scholar.google.com/citations?user=Ixg9n-EAAAAJ&hl=en)"
permalink: /publications/
author_profile: true
---

<!-- [[Google Scholar Profile]](https://scholar.google.com/citations?user=Ixg9n-EAAAAJ&hl=en) -->
{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications %}
  {% include archive-single.html %}
{% endfor %}
