---
layout: archive
title: "Experiences"
permalink: /experiences/
author_profile: true
---


{% include base_path %}

Personal details
======
* Birth  11/24/1997
* Gender  Male 
* Citizenship  Chinese

{% for post in site.experiences reversed %}
  {% include archive-single.html %}
{% endfor %}