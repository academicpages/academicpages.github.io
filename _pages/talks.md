--- 
layout: archive 
title: "Talks and presentations" 
permalink: /talks/ 
author_profile: true 
--- 

{% if site.talkmap_link == true %}
  [See a map of all the places I've given a talk!](/talkmap.html)
{% endif %} 

{% for post in site.talks reversed %} 
  {% include archive-single.html %} 
{% endfor %}
