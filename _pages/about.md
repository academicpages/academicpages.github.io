---
permalink: /
title: "Shengyao (Arvin) Zhuang 庄胜尧"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a Ph.D. student in the [ielab](http://ielab.io/), School of Information Technology and Electrical Engineering, The University of Queensland, supervised by A/Prof. [Guido Zuccon](http://ielab.io/people/guido-zuccon).

I am working on improving effectiveness, efficiency, and robustness for pre-trained deep language model based information retrieval systems.
<hr>

{% include base_path %}
{%- assign publications = site.publications | sort:"year" | reverse | group_by:"year" -%}

<h1>Publications</h1>
{% for year in publications %}
  <h2>{{ year.name }}</h2>
  <ul>
  {%- for post in year.items -%}
    {% include archive-single.html %}
  {%- endfor -%}
 </ul>
{% endfor %}

