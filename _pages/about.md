---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
lang: en
redirect_from: 
  - /about/
  - /about.html
  - /_pages/about/
---
My name is Philippe Laporte. I am a Ph.D. student at the University of Montréal (Canada).<br>
I currently do research in Nuclear Medicine, 
where I try to improve segmentation techniques for dynamical PET images in a preclinical context.<br><br>
Starting to work with polyglot v.21<br><br>

{% for lang in site.languages %}
    {% if lang == site.default_lang %}
{{ lang }} (Default)
    {% else %}
{{ lang }}
    {% endif %}
{% endfor %}

{{ page.url }}<br>
{{site.repository}}<br>
{{ site.repository }}<br>
{{site.website_name}}<br>
{{ site.website_name }}<br>

<a href=" {{ page.url }}"> en </a> <br>
<a href=" {{site.repository}}/"> en </a><br>

[En]( {{site.repository}}/about/)<br>
[Fr]( {{site.repository}}/_pages/fr/about/)<br>
[Fr]( {{site.website_name}}/_pages/fr/about/)<br>
[Fr](/_pages/fr/about/)<br>
[Fr](_pages/fr/about/)<br>
[Fr]( /_pages/fr/about/)<br>
[Fr]( _pages/fr/about/)<br>

{% for lang in site.languages %}
    {% if lang == site.default_lang %}
      <a href=" {{ page.url }}">{{ lang }}</a>
    {% else %}
      <a href="/{{ lang }}{{ page.url }}">{{ lang }}</a>
    {% endif %}
{% endfor %}