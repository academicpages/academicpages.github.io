---
layout: archive
title: "Code"
permalink: /code/
author_profile: true
---

#  <a href="http://autonetkit.org"> Autonetkit </a>

I helped build  the first version of Autonetkit - open source code to automatically  generate emulations of large networks with sophisticated policies. Autonetkit is now used in the Cisco VIRL lab.


#  <a href="http://autonetkit.org](https://github.com/dinesharanathunga/mgtoolkit"> Mgtoolkit </a>

Mgtoolkit is a python package for modelling and analysing  metagraphs - a special type of hypergraph. We used metagraphs for modelling network security policies.

{% include base_path %}

{% for post in site.code reversed %} 
{% include archive-single.html %} {% endfor %}
