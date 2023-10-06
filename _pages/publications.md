---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: false
---


<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-RWRZQTY3DB"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-RWRZQTY3DB');
</script>

{% include base_path %}

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}


Selected publications
======



{% for post in site.highlightedPublications reversed %}
  <p>{{ forloop.rindex }}. {% include archive-single-highlightedPublications.html %} </p>
{% endfor %}


Full publication list
======


{% for post in site.publications reversed %}
  <p>{{ forloop.rindex }}. {% include archive-single.html %} </p>
{% endfor %}