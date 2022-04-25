---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% if site.teaching.size > 0 %}
  {% for post in site.publications reversed %}
    {% include archive-single.html %}
  {% endfor %}
{% else %}
  
<p style = "display:flex; justify-content:center;" ><img src="/images/sadness.gif" ></p>

<h3 style = "justify-content: center; display: flex;">Awww...Dont cry!</h3> 

<p style = "justify-content: center; display: flex;">I am going to add content here soon.</p>
{% endif %}

