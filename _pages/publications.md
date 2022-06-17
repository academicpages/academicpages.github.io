---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
# redirect_from: 
#   - /publications/
---
{% include base_path %}

<!-- > *If you know exactly what you are going to do,*\
> *what is the point of doing it?*\
> ***Pablo Picasso*** -->

<!-- Publications
======
The full list of my publications can be found on [Google Scholar](https://scholar.google.com/citations?user=KQL8tB8AAAAJ&hl=en). -->

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
<!-- Patents
======
Estimation apparatus, estimation method, and non-transitory computer readable medium. [WO2021019634A1](https://patentimages.storage.googleapis.com/cf/ac/b0/8ce8f37ef4ba5c/WO2021019634A1.pdf)

Processing apparatus, security control method, and non-transitory computer readable medium . [WO2021186589A1](https://patentimages.storage.googleapis.com/e3/29/a4/b881c206b24569/WO2021186589A1.pdf) -->

<!-- {% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %} -->

