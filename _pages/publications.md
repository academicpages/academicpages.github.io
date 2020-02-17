---
layout: archive
title: "Recent Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  You can also find my articles on <u><a href="https://dblp.uni-trier.de/pers/hd/a/Alexopoulos:Nikolaos">my DBLP profile</a></u> and <u><a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
