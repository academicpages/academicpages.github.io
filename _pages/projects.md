---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
redirect_from:
  - /projects
  - /projects.html
---
    
    {% include base_path %}
    
    {% for post in site.projects reversed %}
    {% include archive-single.html %}
    {% endfor %}