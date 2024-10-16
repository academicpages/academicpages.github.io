---
layout: archive
title: "Papers"
permalink: /papers/
author_profile: true
---
{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}
{% include base_path %}

<!-- Publications -->
{% for post in site.publications reversed %} 
  {% include archive-single-new.html %}
{% endfor %}

---

<!-- The site.workshops can also be added if wanted -->