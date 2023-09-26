---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my articles on <a href="https://scholar.google.com/citations?user=n0WbtPYAAAAJ&hl=en">my Google Scholar profile</a>.

{% include base_path %}

<h2>Journal Articles</h2>
{% for post in site.publications reversed %}
  {% if post.type == 'journal' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2>Conference Articles</h2>
{% for post in site.publications reversed %}
  {% if post.type == 'conference' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}