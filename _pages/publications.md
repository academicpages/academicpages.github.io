---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% assign years = site.data.publications | map: "year" | sort | uniq | reverse %}
{% for year in years %}
# {{ year }}
{% assign publications = site.data.publications | where: "year", year %}
<ul>
{% for paper in publications %}
  {% include publication.html %}
{% endfor %}
</ul>
{% endfor %}

