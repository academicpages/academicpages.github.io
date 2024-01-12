---
layout: archive
title: "Computational Science and Machine Learning Lab (CSML)"
permalink: /lab/
author_profile: false
priority: 90
people:
  # Current members ordered from oldest member to newest
  - type: Current
    name: Dr. Arash Sarshar
    position: Director
    img: /images/people/ArashSarshar.jpg
    website: 'https://sarshar.dev/'
    email: arash.sarshar@csulb.edu
  - type: Current
    name: Amogh Raj
    img: /images/people/AmoghRaj.jpg
    website: ''
    email: ''
    research-interests: 'solving PDEs, machine learning'
  - type: Current
    name: Amogh Raj
    img: /images/people/AmoghRaj.jpg
    website: ''
    email: ''
    research-interests: 'solving PDEs, machine learning'
  - type: Current
    name: Amogh Raj
    img: /images/people/AmoghRaj.jpg
    website: ''
    email: ''
    research-interests: 'solving PDEs, machine learning'
---

{% include base_path %}



The Computational Science and Machine Learning Lab (CSML) is an interdisciplinary research lab at Cal State Long Beach focusing on aiding scientific computation using algorithmic innovation and machine learning methodologies.

In particular, our work concentrates on developing novel algorithms and models that can effectively meld complex data from multiple sources to improve our understanding of various scientific phenomena. We aim to contribute to the development of more accurate and reliable predictive models that can be used in a wide range of applications.



## Research Focus



Our research interests span a wide range of topics, including data-driven modeling and simulation, uncertainty quantification, and optimization. We use state-of-the-art machine learning techniques in  deep learning, reinforcement learning, and Bayesian learning to develop robust and efficient solutions to these problems. Our goal is to create novel approaches to scientific computation that bring together traditional methods and cutting-edge machine learning techniques.




## Student Mentorship



At CSML, we believe in providing our students with individual attention, clear expectations, and ongoing support and mentoring on writing, presentation, and programming skills. We are looking for students who have demonstrated strong programming skills, research or project experience, dependability, initiative, and excellent communication skills. As mentors, we strive to create a welcoming and inclusive environment for our students to learn and grow.



## Lab Members

{% assign groups = page.people | group_by : 'type' %}
{% for g in groups %}
  <h2 class="text-muted">
    {{ g.name }}
  </h2>

  <div class="row">
    {% for p in g.items %}
      <div class="d-flex col-12 col-sm-6 col-md-4 col-lg-3">
        {% include contact-card.html person=p %}
      </div>
    {% endfor %}
  </div>
{% endfor %}


<!-- {% include gallery caption="This is a sample gallery with **Markdown support**." %} -->

## Prospective Students


If you are interested in pursuing research in this exciting and rapidly growing field, we invite you to join our team at CSML. The best way to get in touch is by filling out [this short survey](https://forms.gle/YQcw92ZJorb4NmVV9).

<!-- Optionally, for an extra challenge, try to solve [this puzzle](https://github.com/elswit/dart/). Make a pull request with your solution (or just your thoughts), and we can take it from there. -->
