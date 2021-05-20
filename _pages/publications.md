---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}
{%- assign publications = site.publications | sort:"year" | reverse | group_by:"year" -%}
{% for year in publications %}
  <h2>{{ year.name }}</h2>
  <ul>
  {%- for publication in year.items -%}
  {% include archive-single.html %}
  </ul>
  {%- endfor -%}

{% endfor %}
