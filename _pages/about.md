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
* I am a data science professional, converting insights to revenue by leveraging my background in machine learning and software development. Also, a Ph.D. candidate at [SEIEE](http://english.seiee.sjtu.edu.cn/) [Shanghai Jiao Tong University](http://en.sjtu.edu.cn/), advised by Prof. [Lu Hongtao](http://www.cs.sjtu.edu.cn/en/PeopleDetail.aspx?id=156). 
<!-- [[Curriculum Vitae](https://safakhan413.github.io/files/Safa, Nasir - Deep Learning.pdf)]  -->
* My research interests lie in the general area of machine learning, particularly in deep learning, computer vision, deepfakes, generative modeling, facial recognition and Vision Tranformers.
* My toolkit consists of Python, SQL, Node.js, Javascript, Java and Ruby
* Prior experience with web development with Ruby on Rails and Node.js gave me a deep understanding of end to end web development pipeline and RESTful APIs.
* I received my Bachelor’s Degree and Master's Degree at [lahore University of Management Sciences](https://lums.edu.pk/). My Graduate research advisors is Prof. [Ihsan Ayub Qazi](https://web.lums.edu.pk/~ihsan/)
* In Progress AWS Solution Architect Certification


Select projects
======

{% assign sorted_portfolio = site.portfolio | sort: 'priority' %}
{% for post in sorted_portfolio %}
  {% include archive-single.html %}
{% endfor %}
