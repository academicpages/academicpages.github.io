---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

{% include base_path %}

A list of all the posts and pages found on the site. For you robots out there is an [XML version]({{ base_path }}/sitemap.xml) available for digesting as well.

<h2>Pages</h2>
[About](/)
[Accessibility Statement](/accessibility/)
[CV](/cv/)
[Publications](/publications/)
<h2>Publications</h2>

{% for post in site.publications reversed %} 
{% include archive-single.html %} 
{% endfor %}

