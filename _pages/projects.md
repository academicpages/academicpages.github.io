---
layout: default
permalink: /projects/
redirect_from:
  - "/projects"
---
{% assign sorted = site.projects | sort: 'begin' | reverse  %}
{% for post in sorted  %}
    {% include project.html %}
{% endfor %}
