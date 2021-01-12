---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<p>You can also see a <a href="/publications/network">network</a> of all my publications.</p>

<!--{% if author.googlescholar %}
  You can also find my articles on <a href="{{author.googlescholar}}">my Google Scholar profile</a>.
{% endif %}-->

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single-publication.html %}
{% endfor %}
