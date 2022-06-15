---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

## Peer-Reviewed International Journal Publications 
### As primary author
{% for post in site.pubs_journal_primary reversed %}
  {% include archive-single.html %}
{% endfor %}

### Co-authored
{% for post in site.pubs_journal_coauth reversed %}
  {% include archive-single.html %}
{% endfor %}

## Peer-Reviewed  International  Conference 
### As primary author
{% for post in site.pubs_conf_primary reversed %}
  {% include archive-single.html %}
{% endfor %}

### Co-authored
{% for post in site.pubs_conf_coauth reversed %}
  {% include archive-single.html %}
{% endfor %}
