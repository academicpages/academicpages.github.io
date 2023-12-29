---
layout: archive
title: "Working Papers"
permalink: /research/
author_profile: true
---

### The National Flood Insurance Program, Racial and Ethnic Disparity, and the Pursuit of Environmental Justice. 
*With Jing Ai*
### Abstract: 
Flood insurance by the NFIP is the most important risk management infrastructure in the 
U.S. to protect vulnerabilities and build resilience to increasing natural disasters. Racial 
and ethnic minorities comprise the most vulnerable populations. We examine disparities 
in insurance outcomes for these groups. Using a combined dataset of nationwide flood 
insurance policies and claims, and census tract level demographics, we find that 
minorities tend to pay higher premium, obtain less coverage per premium dollar, and 
have a lower likelihood of getting claims paid. They also have lower insurance take up 
rates. To aid identification, we utilize an exogenous shock of losing the Minority Tract 
designation. We also find that while social vulnerability leads to less favorable insurance 
outcomes, being racial/ethnic minority exacerbates the effects. More nuanced effects 
across minority groups are also identified. Our results add to the discussions on 
discrimination by institutions and have significant public policy implications.

### The Demographics of Property Insurance: Evidence from the Homeowners Insurance Market. 
*With Jing Ai and Charles Nyce*
### Abstract:
We provide evidence that there is a disparate impact on minorities of the availability of private 
market property insurance in Florida. We show that demographic factors explain reduced private 
market penetration. Results are largely consistent between the two measures of residual market 
(Citizens’) market presence (policy count, total exposure) and across the fixed effects models 
with or without the spatial lag. In general, we find that while risk exposure does seem to be 
contribute significantly to Citizens’ presence, supporting its purpose as a last resort insurer, both 
its market share and property risk exposure are significantly higher in minority concentrated 
census block groups.

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.research reversed %}
  {% include archive-single.html %}
{% endfor %}
