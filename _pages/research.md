---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<h2>Journal Articles</h2>
<br><strong>Making the environment like a cool thing: Exploring generation Z and millennials engagement with climate change video on YouTube</strong><br>Seelig, M., Shata, A., **Yang, Z.**, Sd, D., Gao, Y., Hu, H. & Yang, J.<br>
<i>Environment and Behavior</i> <b>(Submitted for Review)</b>
<br> <strong>Abstract:</strong> Past research has not discovered why Generation Z and Millennials modestly engage in pro-environmental behaviors. Guided by Entertainment-education and Environmental self-efficacy, the present study employed a sequential mixed method utilizing qualitative and quantitative techniques to gauge younger generations' reception of climate videos shared on YouTube and if their climate knowledge increases and empowers them to change environmental behaviors. Our findings show that messages containing a positive narrative arouse less resistance to change than a negative narrative, and conceivably, this influences their everyday behaviors leading to favorable environmental outcomes better at persuading the adoption of pro-environmental behaviors. Yet, while participants believe they possess the self-efficacy to engage in specific behaviors expected of them, they are more concerned about external responses, such as the lack of government and other power structures' efforts to combat the escalating climate crisis.<br>

<br><strong>Making the environment like a cool thing: Exploring generation Z and millennials engagement with climate change video on YouTube</strong><br>Seelig, M., Shata, A., **Yang, Z.**, Sd, D., Gao, Y., Hu, H. & Yang, J.<br>
<i>Environment and Behavior<i> (<b>Submitted for Review</b>)
<p style="text-align:justify"><b> <i>Abstract: </i></b>Past research has not discovered why Generation Z and Millennials modestly engage in pro-environmental behaviors. Guided by Entertainment-education and Environmental self-efficacy, the present study employed a sequential mixed method utilizing qualitative and quantitative techniques to gauge younger generations' reception of climate videos shared on YouTube and if their climate knowledge increases and empowers them to change environmental behaviors. Our findings show that messages containing a positive narrative arouse less resistance to change than a negative narrative, and conceivably, this influences their everyday behaviors leading to favorable environmental outcomes better at persuading the adoption of pro-environmental behaviors. Yet, while participants believe they possess the self-efficacy to engage in specific behaviors expected of them, they are more concerned about external responses, such as the lack of government and other power structures' efforts to combat the escalating climate crisis.</p><br>



<h2>Book Chapter</h2>
{% for post in site.publications reversed %}
  {% if post.pubtype == 'chapter' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}

<h2>Conference Presentations</h2>
{% for post in site.publications reversed %}
  {% if post.pubtype == 'conference' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}

