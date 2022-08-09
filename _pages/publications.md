---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


## Published Papers
- - -

- [Unfolding-Model-Based Visualization: Theory, Method and Applications](https://jmlr.org/papers/volume22/18-846/18-846.pdf)
Yunxiao Chen, Zhiliang Ying, **Haoran Zhang**
*Journal of Machine Learning Research*, 2021, 22: 1-51.





{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
