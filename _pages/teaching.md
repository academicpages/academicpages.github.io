---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

I am a dedicated and enthusiastic instructor and my teaching philosophy is grounded in my experience, interests, and passions. In the classroom I value adaptability to student needs, clear communication with consistent review, data driven insights, and a commitment to service and inclusion. My role as an instructor is to inspire students through my academic work and equip them to achieve their personal academic goals, within and beyond our classroom. 
## Advising and mentoring

While a graduate student at WSU I voluntarily mentored three high-performing undergraduate students, initiating novel research projects with each based on their interests. 

I served as the External Examiner for Bashiru Salifu, who earned a Master of Philosophy in Indigenous Studies from the University of Tromsø (June 2020), with an *Excellent* rating for their thesis, *[Climate Change Impact and Traditional Coping Mechanisms of Borana Pastoralists in Southern Ethiopia](https://hdl.handle.net/10037/18690)*.

## Teaching experience
{% include base_path %}


{% for post in site.teaching reversed %}
  {% if post.path contains 'teaching' %}
     {% include archive-single.html %}
  {% endif %}
{% endfor %}  
