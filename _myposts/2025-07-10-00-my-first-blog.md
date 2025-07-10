---
title: "hellokitty!"
date: 2025-07-10
permalink: /myposts/2025/07/10/hellokitty/
tags:
    - hellokitty
---

Hello! Welcome to my personal homepage.

```

---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
```
