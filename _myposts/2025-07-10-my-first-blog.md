---
layout: post
title: "我的第一篇自定义博客"
date: 2025-07-10
excerpt: 这是摘要内容，显示在列表中。
---
正文内容从这里开始……



{% assign posts = site.myposts | sort: 'date' | reverse %}
{% assign years = "" | split: "" %}

{% for post in posts %}
  {% assign year = post.date | date: "%Y" %}
  {% unless years contains year %}
    <h2>{{ year }}</h2>
    {% assign years = years | push: year %}
  {% endunless %}

  <div class="post-entry">
    <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
    <p><small>{{ post.date | date: "%B %d, %Y" }}</small></p>
    <p>
      {% if post.excerpt %}
        {{ post.excerpt | strip_html | truncatewords: 40 }}
      {% else %}
        {{ post.content | strip_html | truncatewords: 40 }}
      {% endif %}
    </p>
    <hr>
  </div>
{% endfor %}
