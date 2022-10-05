---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

I am a fourth-year Ph.D. student advised by [Prof. Guoliang Fan](https://ceat.okstate.edu/ece/faculty/guoliang-fan.html) in the [School of Electrical & Computer Engineering](https://ceat.okstate.edu/ece/) of the Oklahoma State University (OSU). Before studying at OSU, I worked as a software testing engineer in China for seven years.

Research Interests
======
My research focus on indoor localization and navigation by camera pose estimation from room layouts and image outer corners (IOCs), which invloves camera pose estimation with an optimized Perspective-n-Lines (PnL) method, deep learning, data fusion. 

* Indoor localization by geometric method: Propose a new method, PnL-IOC, based on the traditional PnL methods and introducing room layouts and IOCs.
* Indoor localization by deep learning: Propose a probabilistic Perspective-n-Lines layer for indoor camera pose estimation by using room layouts and IOCs.
* Indoor navigation: Propose a data fusion method, which can fusion indoor image data and room layout and IOCs to implement navigation.  
 

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
