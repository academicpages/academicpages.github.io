---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

Carmona Díaz, G. M., Villada Zapata, J., Piñeres, J. D., & Jiménez Leal, W. (2021). Persuasión moral en el marco del posconflicto en Colombia: un estudio sobre la calidad de los argumentos y la experticia de la fuente. Acta Colombiana de Psicología, 24(2), 144-155.