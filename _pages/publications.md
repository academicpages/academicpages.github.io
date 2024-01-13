---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}
  "Caution! This page is under construction. I am adding more zeros to the code and less confusion to the layout. Thanks for your patience. Please come back in a while.
{% for post in site.publications reversed %}
  #{% include archive-single.html %}
{% endfor %}
