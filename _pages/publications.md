---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
<h2>Peer-Reviewed Books</h2>


{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.peer_reviewed_books reversed %}
  
  {% include archive-single.html %}
{% endfor %}

<h2>Peer-Reviewed Articles</h2>

{% for post in site.peer_reviewed_articles %}
   {% include archive-single.html %}
{% endfor %}

<h2>Non-refereed Publications</h2>

{% for post in site.non_refereed_publications %}
  {% include archive-single.html %}
{% endfor %}

<h2>Work in progress</h2>

{% for post in site.in_progress %}
  {% include archive-single.html %}
{% endfor %}
<h2>Book Reviews</h2>
{% for post in site.book_reviews %}
  {% include archive-single.html %}
{% endfor %}