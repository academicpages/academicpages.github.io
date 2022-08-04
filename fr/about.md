---
title: "About me"
excerpt: "About me"
author_profile: true
lang: fr
redirect_from:
  - /fr/
---
Mon nom est Philippe Laporte et ceci est un test

{% for lang in site.languages %}
    {% if lang == site.default_lang %}
[{{lang}} (Default)]({{lang}}{{page.url}})
    {% else %}
[{{lang}}]({{lang}}{{page.url}})
    {% endif %}
{% endfor %}