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

<!-- Published (Journal) -->
<h2>Published (Journal)</h2>
{% assign journal_pubs = site.publications | where: "type", "journal" %}
{% for post in journal_pubs reversed %}
  {% include archive-single.html %}
{% endfor %}

<!-- Published (Conference) -->
<h2>Published (Conference)</h2>
{% assign conference_pubs = site.publications | where: "type", "conference" %}
{% for post in conference_pubs reversed %}
  {% include archive-single.html %}
{% endfor %}

<!-- Submitted -->
<h2>Submitted</h2>
{% assign submitted_pubs = site.publications | where: "type", "submitted" %}
{% for post in submitted_pubs reversed %}
  {% include archive-single.html %}
{% endfor %}