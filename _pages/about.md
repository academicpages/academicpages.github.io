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

<ul>
{% for post in site.posts limit:5 %}
  <li>
    <strong>{{ post.date | date: "%Y.%m" }}</strong> —
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ul>

<p><a href="/year-archive/">→ more</a></p>
