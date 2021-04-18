---
layout: default
permalink: /teaching/
redirect_from:
  - /teaching.html
---

{% include base_path %}

{% for post in site.teaching reversed %}
  {% include teaching.html %}
{% endfor %}
