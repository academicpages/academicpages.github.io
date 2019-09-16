---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## Education

- **PhD**, Biological Engineering, MIT (2016)
    - Thesis: *Quantitative modeling for microbial ecology and clinical trials*
    - Advisor: Eric Alm
- **MPhil**, Chemistry, University of Cambridge (2012)
- **MASt**, Applied Mathematics & Theoretical Physics, University of Cambridge (2011)
- **BA**, Physics, Williams College (2010)

## Awards

## Experience

* Summer 2015: Research Assistant
  * Github University
  * Duties included: Tagging issues
  * Supervisor: Professor Git

* Fall 2015: Research Assistant
  * Github University
  * Duties included: Merging pull requests
  * Supervisor: Professor Hub

## Publications

{% for post in site.data.publications %}
  {{ post.citation }}
  {% if post.doi %}doi: <a href="http://doi.org/{{ post.doi }}">{{ post.doi }}</a>{% endif %}
  {% if post.pmid %}pubmed: <a href="http://ncbi.nlm.nih.gov/pubmed/{{ post.pmid }}">{{ post.pmid }}</a>{% endif %}
{% endfor %}


Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>

Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

## Service, leadership, and community

### Scientific community & diversity

- **President**, Postdoctoral Association (PDA), Harvard Chan School (2018)
- **Member**, Dean's Advisory Committee on Diversity and Inclusion, Harvard Chan School (2016--2018)
- **Diversity Co-Chair**, Graduate Student Board, MIT Biological Engineering (2013--2016)
    - Developed new programming for events exploring student diversity
    - Co-designed and conducted first departmental diversity climate survey

### Scientific communication

- **Discussion leader & participant**, Science Policy Initiative, MIT (2012--2016)
    - Team member for visits to executive agencies and Congressional offices
    - Engaged in 30-hour Science Policy Bootcamp

### Conflict management
