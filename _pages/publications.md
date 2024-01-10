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

<h1>International Journals (2)</h1>
------
{% for post in site.publications reversed %}
  {% if post.pubtype == 'international_journal' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
------

<br>
<br>
<h1>International Conferences (3)</h1>
------
{% for post in site.publications reversed %}
  {% if post.pubtype == 'international_conference' %}
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
<h1>Domestic Conferences (14)</h1>
------
{% for post in site.publications reversed %}
  {% if post.pubtype == 'domestic_conference' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
------

<br>
<br>
<h1>Workshops (4)</h1>
------
{% for post in site.publications reversed %}
  {% if post.pubtype == 'workshop' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
------

<br>
<br>
<h1>Lecture Presentations (3)</h1>
------
{% for post in site.publications reversed %}
  {% if post.pubtype == 'lecture' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
------
<br>
<sup>*</sup> Equal authorship