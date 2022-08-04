---
title: "About me"
excerpt: "About me"
author_profile: true
lang: de
redirect_from:
  - /de/
---
Ich heiße Philippe Laporte und das ist ein Test.

{% for lang in site.languages %}
    {% if lang == site.default_lang %}
{{ lang }} (Default)
    {% else %}
{{ lang }}
    {% endif %}
{% endfor %}

{{ page.url }}
{{site.repository}}

<a href=" {{ page.url }}"> en </a> <br>
<a href=" {{site.repository}}/"> en </a><br>

[En]( {{site.repository}}/about/)

{% for lang in site.languages %}
    {% if lang == site.default_lang %}
      <a href=" {{ page.url }}">{{ lang }}</a>
    {% else %}
      <a href="/{{ lang }}{{ page.url }}">{{ lang }}</a>
    {% endif %}
{% endfor %}