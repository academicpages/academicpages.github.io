---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% assign categories = site.publication_category %}

{% for category in categories %}
  <h2>{{ category[1].title }}</h2>
  <ul>
    {% for post in site.publications reversed %}
      {% if post.category == category[0] %}
        {% include archive-single.html %}
      {% endif %}
    {% endfor %}
  </ul>
{% endfor %}
