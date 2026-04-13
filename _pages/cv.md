---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

# Education

- B.Tech. in Electronics and Communication (Major), Computer Science (Minor)
  - National Institute of Technology, Surat
  - Aug 2019 - May 2023
  - **GPA: 9.55/10 (3.95/4)**
  - **Gold Medalist - Ranked 1 of 156 students in Electronics Engineering**
  - Coursework: Data Structures & Algorithms, Computer Architecture, Computer Networks, Operating System, Deep Learning

# Work experience

- Aug 2023 - Present: **Software Engineer 2**, JPMorgan Chase
  - Developed a cloud-based distributed application that processes 5 million transactions daily and handles over 50,000 analytics queries per hour
  - Engineered a hot and cold data strategy using Query Federation, slashing storage costs by 30%
  - Designed a database synchronization utility for real-time geospatial analytics, automating 95% of clients' manual workflow
  - **Recognition:** Accelerated Promotion to Software Engineer 2 within first year - awarded to top 5% of global cohort

- May 2022 - July 2022: **Software Engineer Intern**, JPMorgan Chase
  - Designed an Amazon Kinesis data pipeline streaming 1 Terabyte of daily trading data to Redshift
  - Enabled 4X operational scaling for the firm's fastest-growing trading division

- May 2021 - July 2021: **Summer Research Fellow**, Indian Institute of Technology Delhi
  - Investigated Twin Augmentation in pre-trained classifiers for class imbalance in chest X-ray classification
  - Achieved 5% improvement in classification accuracy over baseline model

- Dec 2020 - Feb 2021: **Research Intern**, Indian Space Research Organization (ISRO)
  - Developed a geolocation algorithm to map Mask R-CNN outputs to geo-coordinates in satellite imagery
  - Supported research on geolocation-aware deep learning models for remote sensing

# Skills

- **Programming Languages:** Python, C++, Java
- **Web Technologies:** React, Node.js, Django, Docker, WebRTC, Sockets.IO
- **Cloud Platforms:** AWS (Kinesis, Redshift, S3, DynamoDB), GCP, Terraform
- **Databases:** MySQL, MongoDB, DynamoDB, Aurora, Redshift, PostGIS
- **AI & ML:** TensorFlow, Keras, PyTorch, Pandas, NumPy, scikit-learn, OpenCV

# Publications

  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>
  
Teaching
======
  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
Service and leadership
======
* **Microsoft Student Ambassador:** Mentored 50+ students in web development and organized 10+ programming workshops
* **Organizer, DotSlash Hackathon:** Spearheaded technical operations, developed event website, hosted live sessions on YouTube
* **7-time Hackathon Winner:** Awards from competitions at University at Buffalo, Fordham University, and other institutions
