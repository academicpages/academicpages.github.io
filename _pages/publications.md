---
layout: archive
title: "Research"
permalink: /publications/
author_profile: true

Rahul's research interests are aimed at answering how Machine Learning can help in realizing optimal policies across industries amidst uncertain scenarios. More specifically, he is interested in leveraging Reinforcement Learning besides conventional Machine Learning to enable policy-makers to optimize decisions under uncertainties.     

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

