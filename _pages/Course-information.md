---
layout: archive
title: "Course information"
permalink: /Course-information/
author_profile: true
---

{% if site.author.course_info %}
  <div class="wordwrap">For more information about the course, please visit <a href="https://adav-course-2024.netlify.app/course_info/">the course information page</a>.</div>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
