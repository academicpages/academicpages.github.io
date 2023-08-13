---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

I have been always fascinated by web search engines. What intrigues me the most is how they continue to augment our abilities to find relevant information when navigating the growing information space — from query expansion when we fail to express ourselves to tailoring the retrieved results to meet our personal preferences. 

I am currently investigating ways to help users answer complex information needs beyond the use of Search Engine Result Pages (SERPs). I am broadly interested in understanding how users interact with search engines and how we can use that understanding to design user-centered information retrieval systems. 

Inspired by the progress made in web search engines, I previously investigated the potential of using personalization technology in educational library settings as part of [my minor thesis](https://www.dropbox.com/s/gci7ke6ar8rwzc3/MarwahAlaofi-MinorThesis.pdf?dl=0) at [Monash University](https://www.monash.edu). I proposed, developed and evaluated an approach that creates student models which capture their academic interests and respond to their queries with search results re-ranked according to their individual academic interests - I had fun working with users and got interesting results :)


{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
