---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

My research falls into two main areas: understanding patterns of rebel behavior before, during, and after civil conflict, and developing new tools to improve the study of peace and conflict. One strand of research explores how the territories that ethnic groups inhabit shape rebel group formation and condition their relationship with the state. This interest in rebel behavior also informs projects on the evolution of government repression and rebel killings of civilians over the course of a conflict.

My other main research agenda uses advanced methods to allow us to ask new questions in the study of peace and conflict. By using Bayesian item response theory to measure the strength of peace agreements as a latent variable, I free researchers from post-treatment bias caused by using the duration of agreements as a proxy for their strength. In another project, I use visual imagery contained in Salafi jihadist propaganda videos to detect similiarties in videos produced by different groups, allowing researchers to estimate collaboration networks with a broader clandestine movement. Other work uses over two billion observations of international trade data to develop new measures of economic interdependence and methods to detect disruptions of regular economic exchange between states.

<nbsp>

{% include base_path %}

{% assign ordered_pages = site.research | sort:"order_number" %}

{% for post in ordered_pages %}
  {% include archive-single.html type="grid" %}
{% endfor %}
