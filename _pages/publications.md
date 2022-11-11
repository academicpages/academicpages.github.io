---
layout: archive
title: "Publications"
permalink: /publications
author_profile: true
redirect_from:
  - /publications
---



{% include base_path %}

## ["ContextCLIP: Contextual Alignment of Image-Text pairs on CLIP visual representations"](https://drive.google.com/file/d/1iMxrjVp2EfqCN2c2F6aG8h8lKPRNZlMb/view?usp=share_link)


{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
