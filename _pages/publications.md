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

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

“Rising Food Prices: The Case of Childhood Poverty in a Developed Economy,” NCUR Proceedings, 2017
“The Hope of Mankind,” The Journal of Student Leadership, 2017
