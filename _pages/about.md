---
permalink: /
title: "Shengyao (Arvin) Zhuang 庄胜尧"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a Ph.D. student in the [ielab](http://ielab.io/), School of Information Technology and Electrical Engineering, The University of Queensland, supervised by Prof. [Guido Zuccon](http://ielab.io/people/guido-zuccon).
My primary research interests lie in information retrieval, large language model-based neural rankers, and NLP in general. Currently, I am working as a postdoctoral researcher at [CSIRO Australian e-Health Research Centre](https://aehrc.csiro.au/), where I focus on developing LLM-based search engine systems in the medical domain.
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

