---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---



<p align="center">
  <img src="https://safakhan413.github.io/images/safa.jpg?raw=true" alt="Photo" style="width: 450px;"/> 
</p>

# About Me
* I am a Ph.D. student in the [SEIEE](http://english.seiee.sjtu.edu.cn/) at [Shanghai Jiao Tong University](http://en.sjtu.edu.cn/), advised by Prof. [Lu Hongtao](http://www.cs.sjtu.edu.cn/en/PeopleDetail.aspx?id=156). [[Curriculum Vitae](https://safakhan413.github.io/files/Safa Nasir-vA.pdf)] 
* My research interests lie in the general area of machine learning, particularly in deep learning, computer vision, deepfakes, generative modeling, facial recognition.
* I am proficient with Python and javascript. I have worked as a web developer before with MEAN Stack.
* I received my Bachelor’s Degree and Master's Degree at [lahore University of Management Sciences](https://lums.edu.pk/). My Graduate research advisors is Prof. [Ihsan Ayub Qazi](https://web.lums.edu.pk/~ihsan/)


Select projects
======

{% assign sorted_portfolio = site.portfolio | sort: 'priority' %}
{% for post in sorted_portfolio %}
  {% include archive-single.html %}
{% endfor %}
