---
layout: category
title: "BASIC"
permalink: /categories/basic/
taxonomy: basic
---

{% include base_path %}
{% assign posts = site.categories.basic %}
<div class="category-posts">
  <h2 class="archive__subtitle">{{ page.title }}</h2>
  {% for post in posts %}
    {% include archive-single.html %}
  {% endfor %}
</div>
