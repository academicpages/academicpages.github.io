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
Starting to work with polyglot v.30<br><br>

{% for lang in site.languages %}
    {% if lang == site.default_lang %}
      {{ lang }} (Default)
[{{lang}}]({{lang}}{{page.url}})
    {% else %}
      {{ lang }}
[{{lang}}]({{lang}}{{page.url}})
    {% endif %}
{% endfor %}

{{ page.url }}<br>
fr{{ page.url }}<br>

<a href=" {{ page.url }}"> en </a> <br>
<a href=" {{site.repository}}/"> en </a><br>

[En]( {{site.repository}}/about/)<br>
[Fr]( {{site.repository}}/_pages/fr/about/)<br>
[Fr]( {{site.website_name}}/_pages/fr/about/)<br>

[Fr](/fr/about/)<br>
[Fr](fr/about/)<br>

[Fr](fr{{page.url}}) 
[De](de{{page.url}})<br>

{{site}}

{% for lang in site.languages %}
    {% if lang == site.default_lang %}
      {{ lang }}
      <a href="{{ page.url }}">{{ lang }}</a>
      [{{lang}}]({{page.url}})<br>
    {% else %}
      {{ lang }}
      <a href="{{ lang }}{{ page.url }}">{{ lang }}</a>
      [{{lang}}]({{lang}}{{page.url}})<br>
    {% endif %}
{% endfor %}