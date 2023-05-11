---
layout: archive
# title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<h1>Master Thesis</h1>
------
{% for post in site.publications reversed %}
  {% if post.pubtype == 'master_thesis' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
------

<br>
<br>
<h1>International Journals (3)</h1>
------
{% for post in site.publications reversed %}
  {% if post.pubtype == 'international_journal' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
------

<br>
<br>
<h1>Domestic Journals (1)</h1>
------
{% for post in site.publications reversed %}
  {% if post.pubtype == 'domestic_journal' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
------

<br>
<br>
<h1>International Conferences (1)</h1>
------
{% for post in site.publications reversed %}
  {% if post.pubtype == 'international_conference' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
------

<br>
<br>
<h1>Domestic Conferences (11)</h1>
------
{% for post in site.publications reversed %}
  {% if post.pubtype == 'domestic_conference' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
------

<br>
<br>
<h1>Workshops & Academics (4)</h1>
------
{% for post in site.publications reversed %}
  {% if post.pubtype == 'workshop_academic' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
------
<br>
<sup>*</sup> Equal authorship