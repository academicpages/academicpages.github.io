---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}
<style>
  h1 {
    text-align: center;
  }
</style>

# Peer-reviewed publications

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

# Non-archived (posters, conference presentations)

{% for post in site.posters reversed %}
  {% include archive-single.html %}
{% endfor %}