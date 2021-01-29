---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

Select publications indexed here. You can also find my articles on <a href="https://scholar.google.com/citations?hl=en&user=k5NnEvgAAAAJ&view_op=list_works&sortby=pubdate">my Google Scholar profile</a>.

<img align="center" src="/images/chart.jpg" width="10">

{% if author.googlescholar %}
  Full publication history is available at <a href="{{author.googlescholar}}">my Google Scholar profile</a>.
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
