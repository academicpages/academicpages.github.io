---
layout: archive
permalink: /publications/
author_profile: true
---

<h2>Journals</h2>
  {% for post in site.publications reversed %} 
    {% if post.pubtype == 'journal' %} 
      {% include archive-single.html %} 
    {% endif %}
  {% endfor %}

<h2>Conferences</h2>
  {% for post in site.publications reversed %} 
    {% if post.pubtype == 'conference' %} 
      {% include archive-single.html %} 
    {% endif %}
  {% endfor %}

<h2>Preprints</h2>
  {% for post in site.publications reversed %} 
    {% if post.pubtype == 'preprint' %} 
      {% include archive-single.html %} 
    {% endif %}
  {% endfor %}

<h2>Thesis</h2>
  {% for post in site.publications reversed %} 
    {% if post.pubtype == 'thesis' %} 
      {% include archive-single.html %} 
    {% endif %}
  {% endfor %}
