---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}
### 2021
<b>Assessment of WRF-CHEM Simulated Dust Using Reanalysis, Satellite Data and Ground-Based Observations</b> 
<a href="https://doi.org/10.1007/s12524-021-01328-3" target="_blank"> [Paper] </a>
**Rajeev, A.**, Singh, C., Singh, S.K. et al. Assessment of WRF-CHEM Simulated Dust Using Reanalysis, Satellite Data and Ground-Based Observations. **J Indian Soc Remote Sens** (2021). .(<span style="color:red;font-weight:bold"></span>)

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
