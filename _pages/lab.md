---
layout: archive
title: "Computational Science and Machine Learning Lab (CSML)"
permalink: /lab/
author_profile: false
---




The Computational Science and Machine Learning Lab (CSML) is an interdisciplinary research lab at Cal State Long Beach focusing on aiding scientific computation using algorithmic innovation and machine learning methodologies.

Our work concentrates on developing novel algorithms and models that can effectively meld complex data from multiple sources to improve our understanding of various scientific phenomena. We aim to contribute to the development of more accurate and reliable predictive models that can be used in a wide range of applications.



## Research Focus



Our research interests span a wide range of topics, including data-driven modeling and simulation, uncertainty quantification, and optimization. We use state-of-the-art machine learning techniques in  deep learning, reinforcement learning, and Bayesian learning to develop robust and efficient solutions to these problems. Our goal is to create novel approaches to scientific computation that bring together traditional methods and cutting-edge machine learning techniques.




## Student Mentorship



At CSML, we believe in providing our students with individual attention, clear expectations, and ongoing support and mentoring on writing, presentation, and programming skills. We are looking for students who have demonstrated strong programming skills, research or project experience, dependability, initiative, and excellent communication skills. As mentors, we strive to create a welcoming and inclusive environment for our students to learn and grow.


## Prospective Students 


If you are interested in pursuing research in this exciting and rapidly growing field, we invite you to join our team at CSML. The best way to get in touch is by filling out [this short survey](https://forms.gle/YQcw92ZJorb4NmVV9). 

## Lab Members
<nbsp>
{% include base_path %}

{% assign ordered_pages_s = site.people | sort:"order_number" %}

{% for post in ordered_pages_s %}
  {% include contact-card.html type="grid" %}
{% endfor %}

