---
title: 'Bob Keohane'
date: 2021-07-14
permalink: /posts/2021/07/bob-keohane/
tags:
  - development
  - category1
  - category2
---

---
Bob Keohane: <!--more-->
---

Excerpt with multiple paragraphs

Here's another paragraph in the excerpt.


  {% for tag in page.tags %}
    {% capture tag_name %}{{ tag }}{% endcapture %}
    <a href="/tag/{{ tag_name }}"><code class="highligher-rouge"><nobr>{{ tag_name }}</nobr></code>&nbsp;</a>
  {% endfor %}


<!--more-->

[image](gsipe-workshop.github.io/evergiven.jpeg)

Headings are cool
======

You can have many headings
======

Aren't headings cool?
------
