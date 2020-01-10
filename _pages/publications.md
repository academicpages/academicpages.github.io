---
layout: archive
title: <center>Publications</center>
permalink: /publications/
author_profile: false
sidebar:
  nav: "sidenav"
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

**In-preparation** <br/>
**Alcide Zhao** et, Impacts of global air pollution are policy-controlled tug-of-wars, aiming at **Nature Climate Change** <br/>
Pandey, A.K., Stevenson, D.S., **Zhao, A**., et al., Evaluating Nitrogen dioxide in UKCA using OMI satellite retrievals over South and East Asia, aiming at **Atmospheric Chemistry and Physics**. <br/>

**In review** <br/>
Zhongyang Hu, Andreas Dietz1, **Alcide Zhao**, et al.,, Snow Moving to Higher Elevations: Analyzing Three Decades of Snowline Dynamics in the Alps, submitted to **Geophysical Research Letters** (2nd round review). <br/>
Stevenson, D.S., **Zhao, A**., et al., Trends in global tropospheric hydroxyl radical and methane lifetime since 1850 from AerChemMIP, submitted to **Atmospheric Chemistry and Physics**. <br/>

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
