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
DPhil in Engineering Science, University of Oxford, 2018-2022<br>
M.Eng in Engineering Science, University of Oxford, 2014-2018

Work experience
======
**2021 - Present: Senior Researcher - Microsoft**<br>
I work on compressing neural networks for quick computation on edge devices - specifically I have been working on compressing Language Models, and Diffusion based networks for both language and image generation

**July - December 2021: Research Intern - Microsoft**<br>
I worked on compressing especifically superresolution models for cheap computation on edge devices - this included using a pipeline consisting of Distillation, Pruning, and Quantization

**July 2019: Graduate Engineer - Omnitek (now sold to Intel)**<br>
I worked on Quantizing Neural Networks for efficient computation on FPGAs
  
Skills
======
Python, PyTorch, C++

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  