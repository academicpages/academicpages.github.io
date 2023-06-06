</br>
</br>
</br>
<p style="text-align: center;">John Ragland</p>
<p style="text-align: center;">PhD Student, Electrical and Computer Engineering, University of Washington</p>
<p style="text-align: center;">Phone: (256)-678-2268, Email: jhrag (at) uw (dot) edu</p>
<p style="text-align: center;">John-Ragland.github.io</p>

---
## Education
B.S. in Electrical and Computer Engineering, Auburn University 2015-2019 </br>
M.S. in Electrical and Computer Engineering, Auburn University 2019-2020 </br>
Ph.D. in Electrical and Computer Engineering, The University of Washington 2020-(2024) </br>

## Experience
- Graduate Teaching Assistant, May 2019 - May 2020
    - Auburn University
    - Undergraduate Signals and Systems
- Graduate Researcher, June 2020 - (present)
    - The University of Washington
- Summer Intern, June 2022 - September 2022
    - Applied Research in Acoustics

## Publications
{% for publication in publications %}
{{ publication.author }}, ({{ publication.year }}), {{ publication.title }}, *{{ publication.journal }} Vol. {{ publication.volume }}*, [link](https://doi.org/{{ publication.doi}}) </br>
{% endfor %}

## Talks
### Conference Presentations
{% for talk in talks %}
{{ talk.author }}, ({{ talk.year }}), {{ talk.title }}, *{{ talk.journal }}*, [link](https://doi.org/{{ talk.doi}}) </br>
{% endfor %}

### Invited Talks
Need to add section here that can input data from csv

## Awards

- ASA best student paper award - second place at the ASA Nashville in underwater acoustics technical committe
- Strasberg Mury ... 