---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
Please see my [Google Scholar](https://scholar.google.com/citations?hl=en&user=iZnTmxMAAAAJ&view_op=list_works&sortby=pubdate) for a full list of publications. Here, I highlight some of my ongoing and recent work.

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
