---
layout: archive
title: "Online Teaching Resources"
permalink: /teaching/
author_profile: true
---

{% for textbook in site.online_textbooks %}
  <article class="archive__item">
    <h2 class="archive__item-title">
      <a href="{{ textbook.url }}">{{ textbook.title }}</a>
    </h2>
    <p class="archive__item-excerpt">
      {{ textbook.excerpt | markdownify | strip_html | truncate: 160 }}
    </p>
  </article>
{% endfor %}