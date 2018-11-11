---
layout: archive
title: <Ccenter>Publications</Center>
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

---
layout: archive
title: <Ccenter>Submitted</Center>
permalink: /submitted/
author_profile: true
---

---
layout: archive
title: <Ccenter>under preparation</Center>
permalink: /publication-underp/
author_profile: true
---
