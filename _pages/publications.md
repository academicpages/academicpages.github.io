---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

{% if site.author.googlescholar %}
 <!-- <button class="btn--warning"> You can also find my publications on <a href="{{ author.googlescholar }}">Google Scholar</a>. </button>  -->
 > <b>You can also find my publications on <a href="{{ author.googlescholar }}">Google Scholar</a>. 
 <br> 
 (* denotes equal contribution)</b>
{% endif %}
<!-- <h2>(* denotes equal contribution) </h2>  -->


<!-- {% if author.googlescholar %}
  You can also find my articles on <u><a href="{{ author.googlescholar }}">my Google Scholar profile</a>.</u>
{% endif %} -->

<ol class="leftpad" reversed>

<h2 style="color:#7700DD"> 2021 - 2023 </h2>
<!-- <h3 style="color:#7700DD">JOURNAL, CONFERENCE, AND WORKSHOP PAPERS </h3>  -->
<!--AND DEMONSTRATIONS (PEER-REVIEWED)-->
{% for post in site.publications reversed %}
  {% if post.website-separation-category == "c1" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2 style="color:#7700DD"> 2019 - 2020 </h2>
<!-- <h3 style="color:#7700DD">POSTERS AND SYMPOSIUMS </h3>  -->
<!--AND UNPUBLISHED WORKS-->
{% for post in site.publications reversed %}
  {% if post.website-separation-category == "c2" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}


<h2 style="color:#7700DD">UNDERGRADUATE RESEARCH</h2> 
{% for post in site.publications reversed %}
  {% if post.website-separation-category == "c3" %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

</ol>