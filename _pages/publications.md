---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

{% for post in site.data.publications %}
  {{ post.citation }}
  {% if post.doi %}doi: <a href="http://doi.org/{{ post.doi }}">{{ post.doi }}</a>{% endif %}
  {% if post.pmid %}pubmed: <a href="http://ncbi.nlm.nih.gov/pubmed/{{ post.pmid }}">{{ post.pmid }}</a>{% endif %}
{% endfor %}

# Other work

**SW Olesen**. Quantitative modeling for microbial ecology and clinical trials. PhD thesis, MIT (2016). [DSpace](https://dspace.mit.edu/handle/1721.1/107277); [source code](https://github.com/swo/mit-thesis)

**SW Olesen**. *[Processing 16S data](https://leanpub.com/primer16s/): an informal primer about 16S rRNA amplicon data*. Leanpub (2016).

**SW Olesen**, EJ Alm. "Leveraging microbes when responding to an oil spill." [HSE NOW](http://www.spe.org/hsenow/article/leveraging-microbes-when-responding-to-a-spill) (Dec 2016).
