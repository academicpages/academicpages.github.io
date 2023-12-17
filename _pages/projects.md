---
layout: archive
title: "Projects"
permalink: /Projects/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

## Walkability and Well-Being: An Urban Analysis

Explore the intricate relationship between community walkability and various facets of well-being in urban environments, with a focus on New York City.

**Objective:**
Investigate correlations between walkability and well-being indicators, such as concentrated poverty rates and student obesity rates.

**Methodology:**
Collected data on NYC walkability, poverty, and obesity. Utilized Python, Pandas, and Matplotlib for preprocessing and visualization. Merged datasets for comprehensive analysis.

**Results:**
No significant correlation between walkability and poverty. Identified higher obesity rates in less walkable NYC neighborhoods.
