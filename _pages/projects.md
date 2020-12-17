---
layout: default
title: "Projets"
excerpt: "Projets"
permalink: /projects/
author_profile: true
---

{% include base_path %}
{% for post in site.projects reversed %}
  {% capture year %}{{ post.date | date: '%Y' }}{% endcapture %}
  {% if year != written_year %}
    <h2 id="{{ year | %Y }}" class="archive__subtitle">{{ year }}</h2>
    {% capture written_year %}{{ year }}{% endcapture %}
  {% endif %}
    {% include project.html %}
{% endfor %}
