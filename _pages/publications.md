---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

## Data
{% include base_path %}

{% for post in site.portfolio %}
  {% include archive-single.html %}
{% endfor %}

## Working Papers

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

## Works in Progress

**Scale of Truth: How Ideology Affects What NGO Tweets about What Is Happening in Gaza** (with Marcella Morris, Adee Weller, and Kam Williams)
  
  _Received seed grant from [Computational Social Science Datathon](https://sites.google.com/view/css-workshop-datathon), 2021_
