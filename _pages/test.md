---
layout: single
title: "Test for tags"
permalink: /test/
author_profile: true
---

{% include toc title="Tags" %}

Profiles of graduate students in international political economy on the 2021 job market can be found here. You can also see check them out by tag [here](#jmc_tag).


<a id='jmc_tag'></a>

{% for tag in site.tags %}
  <h1 id=tag[0]>{{ tag[0] }}</h1>
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}














