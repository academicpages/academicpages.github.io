---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
Listed below are only publications for which I have made significant contributions.  I am an author on numerous other publications as a member of the LIGO Scientific Collaboration. For a full list of publications I am an author on see [here](https://ui.adsabs.harvard.edu/search/p_=0&q=author%3A%22Sarin%2C%20Nikhil%22&sort=date%20desc%2C%20bibcode%20desc)

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
