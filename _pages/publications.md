---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---
  {% if site.author.googlescholar %}
  You may also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a> or <a href="https://smeisler.github.io/files/StevenMeisler_CV.pdf">my CV</a>.
  {% endif %}
  
  The list below is compiled from my Google Scholar profile (as of April 1st, 2024) using [google-scholar-for-github-pages](https://github.com/cmccomb/google-scholar-for-github-pages). Please note that author lists are cut-off after the 10th author due to how Google Scholar exports author lists. Please refer to the Google Scholar links for full citations. If you would like PDFs of any of these papers, please reach out! Works under review or in press may not be reflected on this list - please see <a href="https://smeisler.github.io/files/StevenMeisler_CV.pdf">my CV</a> for a more comprehensive list.
  
### Submitted Preprints
{% include publications link=true venue_search="rxiv" %}

### Published Articles
{% include publications link=true venue_exclude="bioRxiv;PsyArXiv;arXiv" venue_search_exclude="rxiv;Rxiv;arXiv" %}
