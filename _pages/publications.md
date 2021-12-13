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

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

<span style="font-size:1em; color:gray;background-color: #F0F0F0;height: 4em; width: 57em; display:inline-block; vertical-align: middle; padding-top: 22px;padding-left: 8px;text-align: left"><b>Conference Papers</b></span><br/>

<!-- <img style="float: left;" src="/images/cvpr.jpg" width="25%">  -->
<span style="font-size:0.9em;padding-left: 8px;text-align: justify"> [1]<span style="color:white">a</span><b>KORSAL: Key-point Detection based Online Real-Time Spatio-Temporal Action Localization</b><br />
  &nbsp; &nbsp; &thinsp; &thinsp; &thinsp; Kalana Abeywardena, Shechem Sumanthiran, <span style="color:blue">Sakuna Jayasundara</span>, Sachira Karunasena, Peshala Jayasekara and Ranga Rodrigo <br />
 &nbsp; &nbsp; &thinsp; &thinsp; &thinsp; International Conference on Pattern Recognition (ICPR 2022)  [Under review] <br/>
