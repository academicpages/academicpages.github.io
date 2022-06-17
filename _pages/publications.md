---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
{% include base_path %}


{% if page.author and site.data.authors[page.author] %}
  {% assign author = site.data.authors[page.author] %}{% else %}{% assign author = site.author %}
{% endif %}

<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">

[<i class="ai ai-google-scholar ai-1x fa-align-center"></i>]({{ author.googlescholar }}){:target="_blank"}{:rel="noopener noreferrer"}&nbsp;[Google Scholar]({{ author.googlescholar }}){:target="_blank"}{:rel="noopener noreferrer"}
&emsp;[<i class="ai ai-researchgate ai-1x"></i>]({{ author.researchgate }}){:target="_blank"}{:rel="noopener noreferrer"}&nbsp; [ResearchGate]({{ author.researchgate }}){:target="_blank"}{:rel="noopener noreferrer"}
&emsp;[<i class="ai ai-orcid ai-1x"></i>]({{ author.orcid }}){:target="_blank"}{:rel="noopener noreferrer"}&nbsp;[ORCID]({{ author.orcid }}){:target="_blank"}{:rel="noopener noreferrer"}
&emsp;[<i class="ai ai-dblp ai-1x"></i>]({{ author.dblp }}){:target="_blank"}{:rel="noopener noreferrer"}&nbsp;[dblp]({{ author.dblp }}){:target="_blank"}{:rel="noopener noreferrer"}
&emsp;[<i class="ai ai-scopus ai-1x"></i>]({{ author.scopus }}){:target="_blank"}{:rel="noopener noreferrer"}&nbsp;[Scopus]({{ author.scopus }}){:target="_blank"}{:rel="noopener noreferrer"}
&emsp;[<i class="ai ai-semantic-scholar ai-1x"></i>]({{ author.semantic-scholar }}){:target="_blank"}{:rel="noopener noreferrer"}&nbsp;[Semantic Scholar]({{ author.semantic-scholar }}){:target="_blank"}{:rel="noopener noreferrer"}
&emsp;[<i class="ai ai-publons ai-1x"></i>]({{ author.publons }}){:target="_blank"}{:rel="noopener noreferrer"}&nbsp;[Publons]({{ author.publons }}){:target="_blank"}{:rel="noopener noreferrer"}


<h2>Book Chapters</h2>
{% assign writtenYear = 'None' %}
{% for post in site.publications reversed %}
{% if post.pubtype == 'book' %}
{% capture year %}{{ post.date | default: "1900-01-01" | date: "%Y" }}{% endcapture %}
{% if year != writtenYear %}
<h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
{% capture writtenYear %}{{ year }}{% endcapture %}
{% endif %}
{% include archive-single-pubs.html %}
{% endif %}
{% endfor %}

<h2>International Journal Articles</h2>
{% assign writtenYear = 'None' %}
{% for post in site.publications reversed %}
{% if post.pubtype == 'journals' %}
{% capture year %}{{ post.date | default: "1900-01-01" | date: "%Y" }}{% endcapture %}
{% if year != writtenYear %}
<h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
{% capture writtenYear %}{{ year }}{% endcapture %}
{% endif %}
{% include archive-single-pubs.html %}
{% endif %}
{% endfor %}

<h2>International Conference Papers</h2>
{% assign writtenYear = 'None' %}
{% for post in site.publications reversed %}
{% if post.pubtype == 'conferences' %}
{% capture year %}{{ post.date | default: "1900-01-01" | date: "%Y" }}{% endcapture %}
{% if year != writtenYear %}
<h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
{% capture writtenYear %}{{ year }}{% endcapture %}
{% endif %}
{% include archive-single-pubs.html %}
{% endif %}
{% endfor %}

<h2>International Workshop Papers</h2>
{% assign writtenYear = 'None' %}
{% for post in site.publications reversed %}
{% if post.pubtype == 'workshops' %}
{% capture year %}{{ post.date | default: "1900-01-01" | date: "%Y" }}{% endcapture %}
{% if year != writtenYear %}
<h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
{% capture writtenYear %}{{ year }}{% endcapture %}
{% endif %}
{% include archive-single-pubs.html %}
{% endif %}
{% endfor %}

<h2>International Conference Abstracts</h2>
{% assign writtenYear = 'None' %}
{% for post in site.publications reversed %}
{% if post.pubtype == 'abstract' %}
{% capture year %}{{ post.date | default: "1900-01-01" | date: "%Y" }}{% endcapture %}
{% if year != writtenYear %}
<h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
{% capture writtenYear %}{{ year }}{% endcapture %}
{% endif %}
{% include archive-single-pubs.html %}
{% endif %}
{% endfor %}

<h2>Theses</h2>
{% assign writtenYear = 'None' %}
{% for post in site.publications reversed %}
{% if post.pubtype == 'thesis' %}
{% capture year %}{{ post.date | default: "1900-01-01" | date: "%Y" }}{% endcapture %}
{% if year != writtenYear %}
<h2 id="{{ year | slugify }}" class="archive__subtitle">{{ year }}</h2>
{% capture writtenYear %}{{ year }}{% endcapture %}
{% endif %}
{% include archive-single-pubs.html %}
{% endif %}
{% endfor %}
