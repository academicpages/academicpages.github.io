---
layout: page
title: "Publications"
permalink: /publications/
author_profile: true
years: [2024,2023,2022,2021,2020,2019,2018,2017,2016]
nav: true
nav_order: 1
---

<!-- _pages/publications.md -->
<div class="publications">

{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f MyPublications -q @*[year={{y}}]* %}
{% endfor %}

</div>
