---
layout: archive
title: "Publications"
permalink: /fr/publications/
lang: fr
author_profile: true
---

{% if author.googlescholar %}
  Vous pouvez aussi trouver mes articles sur <u><a href="{{author.googlescholar}}">, mon profil Google Scholar</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.fr.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
