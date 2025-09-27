---

layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:

* /resume

---

{% include base_path %}

# Education

* Ph.D. in Animal Science (in progress), Texas A&M University, College Station, TX

  * Research focus: Precision Dairy Management, machine learning applications for cattle health and efficiency (e.g., lameness detection, heat stress quantification, ketosis detection, robotic milking efficiency).
* M.S. in Animal Science, [Your University], [Year]
* B.S. in Animal Science, [Your University], [Year]

# Work experience

* 2023–Present: Graduate Research Assistant

  * Texas A&M University, Department of Animal Science
  * Duties include: Developing AI-based tools for dairy cattle management, managing on-farm data collection, statistical and machine learning modeling, conference presentations, and mentoring undergraduate students.
  * Supervisor: Dr. Paudyal

* 2023–Present: Teaching Assistant, ANSC 107 and ANSC 108 (Basic Animal Science)

  * Texas A&M University
  * Duties include: Organizing and grading coursework, supporting students with accommodations, leading lab sessions, and guest lecturing.

# Skills

* Data Analysis: Python, R, MATLAB, SQL
* Machine Learning: Scikit-learn, TensorFlow, PyTorch, XGBoost
* Computer Vision: YOLO, OpenCV, CNNs
* Statistical Modeling: Mixed models, regression, bootstrapping, time-series analysis
* Tools: GitHub, Bash, Linux, HPC/Cluster computing
* Communication: Conference presentations, technical writing, teaching experience

# Publications

  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

# Talks

  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html  %}
  {% endfor %}</ul>

# Teaching

  <ul>{% for post in site.teaching reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

# Service and leadership

* Active member, Nepalese Student Association at Texas A&M University
* Organizer and presenter, departmental seminars and workshops
* Mentor for undergraduate student researchers
* Volunteer for outreach in dairy cattle management and data science applications
