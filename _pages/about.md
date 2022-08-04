---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
lang: en
redirect_from: 
  - /about/
  - /about.html
---
My name is Philippe Laporte. I am a Ph.D. student at the University of Montréal (Canada).<br>
I currently do research in Nuclear Medicine, 
where I try to improve segmentation techniques for dynamical PET images in a preclinical context.<br><br>
Starting to work with polyglot v.8<br><br>

{% for lang in site.languages %}
{{ lang }}
{% endfor %}
{{ site.title }}