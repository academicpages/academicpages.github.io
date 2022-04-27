---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

*2022:*
* 1.	Thomas Reese, Adam Wright, **Siru Liu**, Richard Boyce, Andrew Romero, Guilherme Del Fiol, Kensaku Kawamoto, Daniel Malone. Improving the specificity of drug-drug interaction alerts: Can it be done?, American Journal of Health-System Pharmacy. 2022. doi: 10.1093/ajhp/zxac045


{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
