---
layout: archive
title: "Selected Publications"
permalink: /publications/
author_profile: true
---

[Full List by Research Themes](/allpubs/){: .btn .btn-outline }
[Full List in Chronological Order](/allpubs_year/){: .btn .btn-outline }

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
