---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* MS Robotics, University of Michigan - Ann Arbor (expected 2025)
* BE Information Technology, University of Mumbai (2023)

Work experience
======
* Invideo, Software Engineer Intern
  * Implemented NeRF models to generate realistic talking head avatars from a single image + text script/driving audio.
  * Duties included: Tagging issues
  * Deployed the service as an API on Modal Labs cloud-compute, as part of invideo's AI suite.

* Indian Institute of Science (IISc Bangalore), Research Intern
  * ‘Domain Adaptive Semantic Segmentation of Indian Road Scenes’ for applications in autonomous driving and navigation systems.
  * Supervisor: Dr. KVS Hari

* Nucsoft, Software Engineer Intern
  * Created an Optical Character Recognition (OCR) tool for masking sensitive data on government documents.
  * Trained and deployed the model to redact the ID numbers on Aadhaar cards (similar to Social Security numbers in the US).

* Mavericks Racing, Autonomous Driving Domain Head
  * Implemented models for monocular depth estimation, video-frame interpolation, and video super-resolution.
  * Trained a DQN agent in CarRacing 2D, an autonomous vehicle environment in OpenAI Gym.
  
Skills
======
* Skill 1
* Skill 2
  * Sub-skill 2.1
  * Sub-skill 2.2
  * Sub-skill 2.3
* Skill 3

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
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
  
Service and leadership
======
* Currently signed in to 43 different slack teams
