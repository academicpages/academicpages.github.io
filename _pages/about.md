---
permalink: /
title: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

## About Me 🤖
I am a postdoc at the AI-Bio Convergence Research Institute and a visiting professor at Soongsil University.

My work centers on **evaluating language models**, with a particular emphasis on **multilingual capability and reliability**.  

I develop **theoretically grounded and empirically robust evaluation frameworks** by bridging Linguistics, Translation Studies, and Computer Science.



## Latest News

{% assign now_ts = "now" | date: "%s" | plus: 0 %}
{% assign one_year_ago = now_ts | minus: 31536000 %}

<ul>
{% for post in site.posts %}
  {% assign post_ts = post.date | date: "%s" | plus: 0 %}
  {% if post_ts >= one_year_ago %}
    <li>
      <strong>{{ post.date | date: "%Y.%m" }}</strong> —
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>

<p><a href="/year-archive/">→ more</a></p>
