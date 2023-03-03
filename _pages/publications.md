---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
redirect_from:
  - /publications/
  - /publications.html
---

## Locations of key files/directories
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{include base_path}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

I am a Principal Researcher at the <a href="https://www.bankofcanada.ca/">Bank of Canada</a>
and a visiting research scholar at the <a href="https://www.maxwell.syr.edu/">Maxwell School</a> at Syracuse University. I am a Research Fellow at the <a href="https://www.iza.org/"> Institute of Labor Economics (IZA)</a>.

My main research interests are International Economics and International Migration.
