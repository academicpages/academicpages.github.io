---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


* **Conditional and Residual Methods in Scalable Coding for Humans and Machines** [[PDF]](https://arxiv.org/pdf/2305.02562v1.pdf)\
Anderson de Andrade, Alon Harell, Yalda Foroutan, Ivan V. Bajić, ICME, 2023.

* **Control of Computer Pointer Using Hand Gesture Recognition in Motion Pictures** [[PDF]](https://arxiv.org/pdf/2012.13188.pdf)\
  Yalda Foroutan, Ahmad Kalhor, Saeid Mohammadi Nejati, Samad Sheikhaei, arXiv, 2020.

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{https://scholar.google.com/citations?hl=en&user=mkzIURcAAAAJ&view_op=list_works&sortby=pubdate}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
