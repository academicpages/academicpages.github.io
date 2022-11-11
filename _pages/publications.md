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
  {% include archive-single.html %}
{% endfor %}

<h2>POSTERS AND SYMPOSIUMS and UNPUBLISHED WORKS</h2> 
{% for post in site.nonPeerReviewedPublications reversed %}
  {% include archive-single.html %}
{% endfor %}

<h2>UNDERGRADUATE RESEARCH</h2> 
{% for post in site.miscPublications reversed %}
  {% include archive-single.html %}
{% endfor %}
