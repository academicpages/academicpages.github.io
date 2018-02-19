---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: false
sidebar:
  nav: "Projs"
---


<p><i> Most of the research here presented is performed in the microscopic setups of <b>Prof. Johan Hofkens</b></i></p>
<br>
<div class="grid__wrapper">
  {% for post in site.projects %}
    {% include archive-single-proj.html type="grid" %}
  {% endfor %}
</div>
