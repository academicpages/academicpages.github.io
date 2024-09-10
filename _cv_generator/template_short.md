# John Ragland PhD
<p style="text-align: center;">Post-Doctoral Scholar, School of Oceanography, University of Washington </br> phone: (256)-678-2268, email: jhrag (at) uw (dot) edu, website: [ [John-Ragland.github.io] ](https://John-Ragland.github.io)</p>

---
## Education
**University of Washington**
Ph.D. in the department of Electrical and Computer Engineering, 2020-2024</br>
*Adviser:* Shima Abadi</br>
*Thesis:* Using coherent ambient sound to probe the ocean</br>
*Emphasis:* Ambient noise interferometry, Ocean basin tomography</br>

**Auburn University**
M.S. in the department of Electrical and Computer Engineering, suma cum laude 2019-2020</br>
*Adviser:* Thaddeus Roppel</br>
*Thesis:* Digital Simulation and Recreation of a Vacuum Tube Guitar Amp [ [link] ](http://hdl.handle.net/10415/7112)</br>
*Emphasis:* Digital Signal Processing, Real-time Audio Processing, Physical Modeling

**Auburn University**
B.S. in the department of Electrical and Computer Engineering, suma cum laude, 2015-2019</br>
*Honors College Scholar*</br>

## Experience
- Post-Doctoral Scholar, July 2024 - (present), *University of Washington*
- Graduate Researcher, June 2020 - June 2024, *The University of Washington*
- Summer Intern, June 2022 - September 2022, *Applied Research in Acoustics*
- Graduate Teaching Assistant, May 2019 - May 2020, *Auburn University*

## Journal Publications

{% for paper in papers|sort(attribute='year', reverse=True) %}
  {% if paper.author.startswith('(in preparation)') or paper.author.startswith('(submitted)') %}
    {{ paper.author }}, ({{ paper.year }}), {{ paper.title }}, *{{ paper.journal }}* </br>
  {% else %}
    {{ paper.author }}, ({{ paper.year }}), {{ paper.title }}, *{{ paper.journal }} Vol. {{ paper.volume }}* </br>[ [link] ](https://doi.org/{{ paper.doi }}) </br>
  {% endif %}
{% endfor %}

## Invited Talks
{% for invite in invited|sort(attribute='year', reverse=True) %}{{ invite.address }} - {{ invite.month }}, {{ invite.year }}</br>
{% endfor %}

## Awards
- **ASA best student paper award** - second place at the ASA Nashville in underwater acoustics technical committee, December 2022
- **The Daoma and Murray Strasberg Memorial Scholarship** - for Graduate Students in Ocean Acoustics, May 2023

## Cruise Experience
- R/V Rachel Carson, 2022, 2 days - deployed mooring with two hydrophones that was successfully recovered one week later. The goal of this deployment was to acoustically measure methane seeps in the Puget Sound.