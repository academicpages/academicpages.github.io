---
layout: archive
title: ""
permalink: /code/
author_profile: true
---

#  <a href="https://adsynthesizer.github.io/"> ADSynthesizer </a>

We build a realisitic Active Directory attack graph generator using metagraph abstractions.

![Alt text](https://hxnguyen.github.io/images/adsynth.png "a title")


#  <a href="http://autonetkit.org"> Autonetkit </a>

I built  the first version of Autonetkit - open source code to automatically  generate emulations of large networks with sophisticated policies. Autonetkit is now used in the Cisco VIRL lab.

![Alt text](https://hxnguyen.github.io/images/autonetkit.png "a title")


#  <a href="http://autonetkit.org](https://github.com/dinesharanathunga/mgtoolkit"> MGtoolkit </a>

Mgtoolkit is a python package for modelling and analysing  metagraphs - a special type of hypergraph. We used metagraphs for modelling network security policies.

{% include base_path %}

{% for post in site.code reversed %} 
{% include archive-single.html %} {% endfor %}
