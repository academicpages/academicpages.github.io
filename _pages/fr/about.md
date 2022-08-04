---
title: "About me"
excerpt: "About me"
author_profile: true
lang: fr
---
Mon nom est Philippe Laporte et ceci est un test

{% for lang in site.languages %}
    {% if lang == site.default_lang %}
{{ lang }} (Default)
    {% else %}
{{ lang }}
    {% endif %}
{% endfor %}