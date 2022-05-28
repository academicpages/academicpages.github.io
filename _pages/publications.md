---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
This page is not routinely maintained, and a more up to date list of publications is available <a href="https://nikhil-sarin.github.io/files/nikhil_cv.pdf" style="color: blue; text-decoration: underline;text-decoration-style: dotted;">here</a>. As of May 2022, I have 10 first-author publications and 8 other publications where I have made significant contributions. I am an author on numerous other publications as a member of the LIGO Scientific Collaboration. For a full list of publications I am an author on see  <a href="https://ui.adsabs.harvard.edu/search/p_=0&q=author%3A%22Sarin%2C%20Nikhil%22&sort=date%20desc%2C%20bibcode%20desc" style="color: blue; text-decoration: underline;text-decoration-style: dotted;">here</a>.

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
