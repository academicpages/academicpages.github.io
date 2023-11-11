---
permalink: /
title: "Shengyao (Arvin) Zhuang 庄胜尧"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
I am a postdoctoral researcher at [CSIRO, Australian e-Health Research Centre](https://aehrc.csiro.au/), where I focus on developing large language model-based search engine systems in the medical domain. Before joining CSIRO, I was a Ph.D. student at the [ielab](http://ielab.io/), EECS, The University of Queensland, Australia, supervised by Professor [Guido Zuccon](http://ielab.io/people/guido-zuccon). My primary research interests lie in information retrieval, large language model-based neural rankers, and NLP in general.
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

