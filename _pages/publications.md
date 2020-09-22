---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

Select publications indexed here. You can also find my articles on <a href="https://scholar.google.com/citations?user=k5NnEvgAAAAJ&hl=en">my Google Scholar profile</a>.

{% if author.googlescholar %}
  You can also find my articles on <a href="{{author.googlescholar}}">my Google Scholar profile</a>.
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
