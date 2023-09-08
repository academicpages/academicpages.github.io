---
layout: archive
title: ""
permalink: /Publications/
author_profile: true
---
# Journal Papers
## Journal Papers
### Journal Papers
### 2024
======
1. B.S. in GitHub, GitHub University, 2012.
2. M.S. in Jekyll, GitHub University, 2014
3. Ph.D in Version Control Theory, GitHub University, 2018 (expected)
---


---


{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

