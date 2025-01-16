---
layout: archive
title: "News"
permalink: /news/
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

{% for post in site.news reversed %}
  <p style="display: inline;"> {% include archive-single-news.html %} </p>
{% endfor %}