---
layout: single
title: "Job Market Candidates 2021"
permalink: /test-toc/
toc: true
toc_label: "JM tags"
author_profile: true
---

Profiles of graduate students in international political economy on the 2021 job market can be found here. You can also see check them out by tag [here](#jmc_tag).

# Job Market Candidates by tags
<a id='jmc_tag'></a>


{% for tag in site.tags %}
  <div class="toc">
    <ul>
      <li><a href="{ tag[0] }">{{ tag[0] }}</a></li>
    </ul>
  </div>
  <h1 id="{ tag[0] }">{{ tag[0] }}</h1>
{% endfor %}


{% for tag in site.tags %}
  <h3>{{ tag[0] }}</h3>
  <ul>
    {% for post in tag[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %} 	
