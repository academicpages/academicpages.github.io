</br>
</br>
</br>

# John Ragland
<p style="text-align: center;">PhD Student, Electrical and Computer Engineering, University of Washington </br> phone: (256)-678-2268, email: jhrag (at) uw (dot) edu, website: [ [John-Ragland.github.io] ](https://John-Ragland.github.io)</p>

---
## Education
**Auburn University**
B.S. in the department of Electrical and Computer Engineering, suma cum laude, 2015-2019</br>
*Honors College Scholar*</br>

**Auburn University**
M.S. in the department of Electrical and Computer Engineering, suma cum laude 2019-2020</br>
*Adviser:* Thaddeus Roppel</br>
*Thesis:* Digital Simulation and Recreation of a Vacuum Tube Guitar Amp [ [link] ](http://hdl.handle.net/10415/7112)</br>
*Emphasis:* Digital Signal Processing, Real-time Audio Processing, Physical Modeling
</br>

**University of Washington**
Ph.D. in the department of Electrical and Computer Engineering, 2020-(2024 expected)</br>
*Adviser:* Shima Abadi</br>
*Thesis:* Using coherent ambient sound to probe the ocean</br>
*Emphasis:* Digital Signal Processing, Acoustics, Machine Learning</br>

## Experience
- Graduate Teaching Assistant, May 2019 - May 2020, *Auburn University*
- Graduate Researcher, June 2020 - (present), *The University of Washington*
- Summer Intern, June 2022 - September 2022, *Applied Research in Acoustics*

## Journal Publications

{% for paper in papers|sort(attribute='year', reverse=True) %}
  {% if paper.author.startswith('(in preparation)') or paper.author.startswith('(submitted)') %}
    {{ paper.author }}, ({{ paper.year }}), {{ paper.title }}, *{{ paper.journal }}* </br>
  {% else %}
    {{ paper.author }}, ({{ paper.year }}), {{ paper.title }}, *{{ paper.journal }} Vol. {{ paper.volume }}* </br>[ [link] ](https://doi.org/{{ paper.doi }}) </br>
  {% endif %}
{% endfor %}


## Talks

### Invited Talks
{% for invite in invited|sort(attribute='year', reverse=True) %}{{ invite.address }} - {{ invite.month }}, {{ invite.year }}</br></br>
{% endfor %}

### Conference Presentations
{% for talk in talks|sort(attribute='year', reverse=True) %}
  {% if talk.author.startswith('(in preparation)')  %}
    {{ talk.author }}, ({{ talk.year }}), {{ talk.title }}, {{ talk.booktitle }}, *{{ talk.address }}* </br>
  {% else %}
    {{ talk.author }}, ({{ talk.year }}), {{ talk.title }}, {{ talk.booktitle }}, *{{ talk.address }}* [ [link] ]({{ talk.url }})</br>
  {% endif %}


{% endfor %}

## Awards

- **ASA best student paper award** - second place at the ASA Nashville in underwater acoustics technical committee, December 2022
- **The Daoma and Murray Strasberg Memorial Scholarship** - for Graduate Students in Ocean Acoustics, May 2023

## Open Source Code Contributions
- OOIPy - a python package for accessing broadband and low frequency hydrophone data that is part of the Ocean Observatories Innitiative [ [github] ](https://github.com/Ocean-Data-Lab/ooipy) [ [pypi] ](https://pypi.org/project/ooipy/)
- xrsignal (in development)- a python package that ports functionality from scipy.signal to xarray and is compatible with distributed computing [ [github] ](https://github.com/John-Ragland/xrsignal) 

## Cruise Experience
- R/V Rachel Carson, 2022, 2 days - deployed mooring with two hydrophones that was successfully recovered one week later. The goal of this deployment was to acoustically measure methane seeps in the Puget Sound.

## Media Coverage
- UW ECE spotlights, [*Listening to the ocean to measure the impact of climate change | UW Department of Electrical & Computer Engineering*](https://web.archive.org/web/20230731211310/https://www.ece.uw.edu/spotlight/listening-to-the-ocean-climate-change/)
- OOI Science Highlights, [*An Overview of Ambient Sound Using OOI Hydrophones*](https://web.archive.org/web/20230731211602/https://oceanobservatories.org/2022/11/an-overview-of-ambient-sound-using-ooi-hydrophones/)
