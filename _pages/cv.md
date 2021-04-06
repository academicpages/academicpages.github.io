---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

## Experience

- **Research Analyst**, [CNA](https://www.cna.org/) (2020--)
    - Implemented a [Vaccine Vulnerability Index](https://www.cna.org/centers/ipr/phpr/vaccination-tool) for DHS [CISA](https://en.wikipedia.org/wiki/Cybersecurity_and_Infrastructure_Security_Agency)
    - Executed an infectious disease threat assessment for the Greater Houston Region
    - Conceptualized portions of New York City Emergency Management's Urban Risk Index
    - Supported COVID-19 after-action reviews for Virginia's Departments of Health and Emergency Management
- **Consultant**
    - Epidemiology consultant, [Biobot Analytics](https://www.biobot.io/) (2020--)
    - Scientific consultant, [OpenBiome](https://www.openbiome.org/) (2020--)
    - Epidemiology consultant, Epic Games (2020)
    - Epidemiology consultant, National Basketball Association (2020--)
- **Scientific Director**, [OpenBiome](https://www.openbiome.org/) (2019--2020)
- **Postdoctoral Associate**, Harvard Chan School of Public Health (2016--2018)
    - Research focus: Epidemiology of antibiotic use and resistance
    - Advisor: [Yonatan Grad](https://www.hsph.harvard.edu/yonatan-grad/)

## Education

- **PhD**, Biological Engineering, MIT (2016)
    - Thesis: *Quantitative modeling for microbial ecology and clinical trials* ([MIT Dspace](https://dspace.mit.edu/handle/1721.1/107277))
    - Advisor: [Eric Alm](https://be.mit.edu/directory/eric-alm)
- **MPhil**, Chemistry, University of Cambridge (2012)
    - Thesis: *Coarse-grained models of chiral assemblies* ([pdf](/files/olesen-2012-thesis.pdf))
    - Advisor: [David Wales](https://en.wikipedia.org/wiki/David_J._Wales)
- **MASt**, Applied Mathematics & Theoretical Physics, University of Cambridge (2011)
- **BA** *magna cum laude* with Highest Honors, Physics, Williams College (2010)

## Awards

- Kocaeli International Travel Award, Harvard Chan School (2017)
    - Funds one-week exchange program with Kocaeli University, Turkey
- NSF Graduate Research Fellowship (2013--2016)
- Presidential Fellow, MIT (2012--2013)
    - Fully funds first year of graduate student for 120 students
- Herchel Smith Fellowship, Williams College (2010--2012)
    - Fully funds 2 years of graduate study at the University of Cambridge
- Howard P. Stabler Prize in Physics, Williams College (2010)
- Barry M. Goldwater Scholarship (2009)

## Publications

{% for pub in site.data.publications %}
  - {{ pub.citation }}{% if pub.doi %} doi: <a href="http://doi.org/{{ pub.doi }}">{{ pub.doi }}</a>{% endif %}{% if pub.pmid %} pubmed: <a href="http://ncbi.nlm.nih.gov/pubmed/{{ pub.pmid }}">{{ pub.pmid }}</a>{% endif %} {% if pub.url %} <a href="{{ pub.url }}">link</a>{% endif %}
{% endfor %}

## Talks & posters

{% for talk in site.data.talks %}
  - {{ talk.type }}: "{{ talk.title }}". {% if talk.authors %}{{ talk.authors }}.{% endif %} {{ talk.place }} ({{ talk.date }})
{% endfor %}

## Teaching

{% for x in site.data.teaching %}
  - {{ x.title }}. {{ x.venue }}. {% if x.inviter %}Invited by {{ x.inviter }}.{% endif %} ({{ x.date }})
{% endfor %}

## Service, leadership, and community

- **President**, [Postdoctoral Association](https://www.hsph.harvard.edu/pda/) (PDA), Harvard Chan School (2018)
    - Led a consolidation of PDA council for >15 officers to 4
    - Initiated a Training Evaluation Initiative to create a common administrator-trainee language for negotiations
- **Member**, Dean's Advisory Committee on Diversity and Inclusion, Harvard Chan School (2016--2018)
- **Communication Fellow**, MIT [Biological Engineering Communication Lab](https://mitcommlab.mit.edu/be/) (2013--2016)
    - Co-founding Fellow and mentor to junior Fellows
    - Coached >100 undergraduate, graduate, and postdoc clients
    - Co-led creation of the [CommKit](https://mitcommlab.mit.edu/be/use-the-commkit/): online, content-specific communication guide
- **Diversity Co-Chair**, Graduate Student Board, MIT Biological Engineering (2013--2016)
    - Developed new programming for events exploring student diversity
    - Co-designed and conducted first departmental diversity climate survey
- **Discussion leader & participant**, MIT [Science Policy Initiative](https://mitspi.squarespace.com/) (2012--2016)
    - Team member for visits to executive agencies and Congressional offices
    - Engaged in 30-hour Science Policy Bootcamp
