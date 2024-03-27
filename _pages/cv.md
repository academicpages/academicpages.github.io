---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}
<style>
  h3 {
    margin-top: 10px;
  }
  .page__title {
    text-align: center;
  }
</style>
<link rel="stylesheet" href="/assets/css/terms-taught.css"/>

# Education

* Ph.D. in [Educational Psychology & Educational Technology](https://education.msu.edu/cepse/epet/) @ Michigan State University, 2025 (expected)
* B.A. in [Education, Communities, and Organizations](https://education.uw.edu/programs/undergraduate/eco) @ University of Washington, Seattle, 2020
* B.S. in [Computer Science](https://www.cs.washington.edu/academics/ugrad) @ University of Washington, Seattle, 2020

# Publications
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

# Posters & Conference Presentations
  <ul>{% for post in site.posters reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

# Teaching
  <ul>
  {% for post in site.teaching reversed %}
    {% if post.course_overview %}
      {% include archive-single-cv.html %}
    {% endif %}
  {% endfor %}
  </ul>

# Research Assistantships

  <ul>{% for post in site.research reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

# Talks and Panels
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
  
# Awards and Honors
* Outstanding Reviewer Award, [SIGCSE Technical Symposium](https://sigcse2024.sigcse.org/) (2024) 
* [Summer Research Fellowship](https://education.msu.edu/resources/academic-student-affairs/summer-research-fellowships/), Michigan State University College of Education (2022, 2023)
* [Dean's Scholar Award](https://education.msu.edu/resources/academic-student-affairs/recruitment-scholarships-fellowships/), Michigan State University College of Education (2020-2026)
* [Husky 100](https://www.washington.edu/husky100/year/2020/#name=andrew-hu), University of Washington (2020)

# Service
* MSU Ignite speaker selection committee (2024)
  * Reviewed candidate talks for a general audience research presentation series, and coached the accepted presenters.
* [JET Lab](https://msujet.org/) meeting leader (2023-present)
  * Changed the structure of our lab meetings to center students presenting their work and getting feedback, as well as building community by inviting guests with similar interests.
* Student representative for EPET (2022-2023)
  * Attended faculty meetings, raised student concerns to faculty, helped onboard first year PhD students.