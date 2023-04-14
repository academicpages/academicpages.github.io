---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


You can find my articles on <u><a href="{{site.googlescholar}}">my Google Scholar profile</a>.</u>

Some selected publications:

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
