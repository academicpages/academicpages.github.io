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

<h2>JOURNAL, CONFERENCE, AND WORKSHOP PAPERS <!--AND DEMONSTRATIONS (PEER-REVIEWED)--></h2> 
{% for post in site.publications reversed %}
  {% if post.website-separation-category == "c1" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2>POSTERS AND SYMPOSIUMS AND UNPUBLISHED WORKS</h2> 
{% for post in site.publications reversed %}
  {% if post.website-separation-category == "c2" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}


<h2>UNDERGRADUATE RESEARCH</h2> 
{% for post in site.publications reversed %}
  {% if post.website-separation-category == "c3" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}
