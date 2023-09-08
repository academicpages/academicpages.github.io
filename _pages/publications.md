---
layout: archive
title: ""
permalink: /Publications/
author_profile: true
---
# Journal Papers
## 2024

## Prior to RPI (2023)

1. S. Akin, C. Nath, MBG. Jun, “[Selective surface metallization of 3D-printed polymers by cold spray-assisted electroless deposition](https://pubs.acs.org/doi/10.1021/acsaelm.3c00893)", ACS Applied Electronic Materials, 2023. 
3. M.S. in Jekyll, GitHub University, 2014
4. Ph.D in Version Control Theory, GitHub University, 2018 (expected)
---


---


{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

