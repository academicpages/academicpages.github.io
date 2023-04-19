---
layout: archive
title: "Research and Publications"
permalink: /publications/
author_profile: true
---
### Active Material and Intelligent Structures Lab, UM - SJTU JI Dec 2019 - Sept 2021
#### Research Assistant & Assistant Lab Manager, Supervisor: Dr. Yanfeng Shen
#### Design of Ultra-Compliant and Flexible Sensing System with Convolutional Neural Network
* Fabricated the neural skin, including coating piezoelectric sensing powder on cross-finger flexible printed circuits 
* Assisted in polarization of composite piezoelectric material in electromagnetic vibration actuator
* Applied convolutional neural network (CNN) to the sensing system to predict detective pulse signals
* The research paper was published in EI international conference proceedings of the ASME’s 2021 International 
Mechanical Engineering Congress and Exposition (IMECE.

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
