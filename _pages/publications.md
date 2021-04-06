---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

{% for pub in site.data.publications %}
  {{ pub.citation }} {% if pub.doi %}doi: <a href="http://doi.org/{{ pub.doi }}">{{ pub.doi }}</a>{% endif %} {% if pub.pmid %}pubmed: <a href="http://ncbi.nlm.nih.gov/pubmed/{{ pub.pmid }}">{{ pub.pmid }}</a>{% endif %} {% if pub.pmc %}pmc: <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/{{ pub.pmc }}">{{ pub.pmc }}</a>{% endif %} {% if pub.pdf %}pdf: <a href="{{ pub.pdf }}">pdf</a>{% endif %} {% if pub.url %} <a href="{{ pub.url }}">link</a>{% endif %}
{% endfor %}

## Other work

**SW Olesen**. Quantitative modeling for microbial ecology and clinical trials. PhD thesis, MIT (2016). [DSpace](https://dspace.mit.edu/handle/1721.1/107277); [source code](https://github.com/swo/mit-thesis)

**SW Olesen**. *Processing 16S data: an informal primer about 16S rRNA amplicon data* (Mar 2021). [file](/files/primer16s.pdf); [source code](https://github.com/swo/16s-book)

**SW Olesen**, EJ Alm. "Leveraging microbes when responding to an oil spill." [HSE NOW](http://www.spe.org/hsenow/article/leveraging-microbes-when-responding-to-a-spill) (Dec 2016).
