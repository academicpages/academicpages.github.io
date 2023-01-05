---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

{% if author.googlescholar != "" %}
  You can also find my articles on <a href="{{author.googlescholar}}">my Google Scholar profile</a>.
{% endif %}