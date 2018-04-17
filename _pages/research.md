---
layout: archive
title: "Publications"
permalink: /research/
author_profile: true
---


{% include base_path %}

{% for post in site.research reversed %}
  {% include archive-single-pub.html %}
{% endfor %}

<h1> Working Papers </h1>

{% include base_path %}

{% for post in site.research reversed %}
  {% include archive-single.html %}
{% endfor %}
