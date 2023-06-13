---
layout: archive
type: "Research"
title: "Research"
permalink: /publications/
author_profile: true
---

{% include base_path %}
# Research
{% for post in site.publications reversed %}
{% include archive-single.html %}
{% endfor %}
