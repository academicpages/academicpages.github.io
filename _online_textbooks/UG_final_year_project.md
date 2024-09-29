---
title: "Final Year Project: Space Station Design"
excerpt: "An introduction to multibody dynamics and the use of symbolic computation in modelling them."
mathjax: true
---

{% marginfigure 'mf-id-1' 'assets/imgs/HQ_Final_Logo_for_light_theme.png' 'Logo for SpaceHQ.
We like to think of ourseleves as a ragtag group of outliers trying to figure out how we
can build larger structures in space. An example challenge is how we can go from 
modular stations such as ISS, as seen on the left of our logo, to rotating wheel
space stations, on the right of our logo.' %}

## Who this page serves?
This is likely only useful for QMUL's final year undergraduate students in who are taking
[EMS690U final year project](https://www.qmul.ac.uk/modules/items/ems690u-integrated-design-project.html)
under my supervision. It will make little to no sense for anyone else (inlcuding those from QMUL) as
there will be a lot covered in the in-person workshops. This is merely to augment to that; it is not
meant as a standalone piece.

## Project Areas
The core thesis of the project is that large (or even ultra-large) space structures
could help us inspirational or useful things. Human habitation and space-based astronomy
are classic examples of the former whereas 
former whereas in-space manufacturing or tackling
overcome existential risks/threats 
### In-Space Manufacturing (e.g., Organs, Electronics, and Pharmaceuticals Drugs)
**<u>Domain</u>**:: Commercial Businesses backed by either venture capital and/or
space agencies.

[3-D printing artificial organs](https://www.nasa.gov/missions/station/iss-research/3d-bioprinting/)
would be a boon to those on the donor organs wait-list. ISS astronauts are also working on this technology
to if these
[artificial organs can withstand the space environment](https://www.space.com/international-space-station-3d-printed-hearts-astronauts-deep-space-travel).

**<u>Existing Players</u>**
- **Semiconductors and Electronics**
    -  [Space Forge](https://www.spaceforge.com)
- **Pharmaceuticals Drugs** 
   - [Varda Space](https://www.varda.com)
   - [BioOrbit](https://www.bioorbit.space/)


### Large Space Stations (Modular or Monolithic)
**<u>Domain</u>**: National space agencies have built space stations so far.
Commercial entities are now trying to get a piece of the pie.

{% marginnote 'table-2-id' '*Table 1*: A table of space stations launched and planned.' %}
<div class="table-wrapper">
  <table class="booktabs">
    <thead>
      <tr>
        <th colspan="4" class="cmid">Space Stations</th>
      </tr>
      <tr>
        <th class="l">Funding</th>
        <th>Name (Year)</th>
        <th class="r">Capacity</th>
        <th class="r">Type/Comments</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td rowspan="18">Govt. funded</td>
        <td><a href="https://en.wikipedia.org/wiki/Salyut_1">Salyut 1</a> (1971)</td>
        <td class="r">3</td>
        <td class="r">Monolithic</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Salyut_2">Salyut 2</a> (1973)</td>
        <td class="r">2</td>
        <td class="r">Monolithic, military. Debris collision failure</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Salyut_3">Salyut 3</a> (1974-1975)</td>
        <td class="r">2</td>
        <td class="r">Monolithic, military</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Salyut_4">Salyut 4</a> (1974-1977)</td>
        <td class="r">3</td>
        <td class="r">Monolithic</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Salyut_5">Salyut 5</a> (1976-1977)</td>
        <td class="r">2</td>
        <td class="r">Monolithic, military</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Salyut_6">Salyut 6</a> (1977-1982)</td>
        <td class="r">3</td>
        <td class="r">Semi-modular</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Salyut_7">Salyut 7</a> (1982-1991)</td>
        <td class="r">3</td>
        <td class="r">Semi-modular</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Skylab">Skylab</a> (1973-1979)</td>
        <td class="r">3</td>
        <td class="r">Monolithic</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Almaz">Almaz</a> (1973-1976)</td>
        <td class="r">2-3</td>
        <td class="r">Monolithic, military</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Mir">Mir</a> (1986-2001)</td>
        <td class="r">3</td>
        <td class="r">Modular</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/International_Space_Station">International Space Station</a> (2000-present)</td>
        <td class="r">7</td>
        <td class="r">Modular, international</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Tiangong-1">Tiangong-1</a> (2011-2018)</td>
        <td class="r">3</td>
        <td class="r">Monolithic prototype</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Tiangong-2">Tiangong-2</a> (2016-2019)</td>
        <td class="r">2</td>
        <td class="r">Monolithic prototype</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Tiangong_space_station">Tiangong Space Station</a> (2021-present)</td>
        <td class="r">3</td>
        <td class="r">Modular</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Lunar_Gateway">Lunar Gateway</a> (planned 2024)</td>
        <td class="r">4</td>
        <td class="r">Modular, lunar orbit</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Russian_Orbital_Service_Station">ROSS</a> (planned 2027)</td>
        <td class="r">4</td>
        <td class="r">Modular, Russian national</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Indian_Space_Station">Indian Space Station</a> (planned 2035)</td>
        <td class="r">3</td>
        <td class="r">Likely modular, details TBA</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Tiangong_space_station#Future_expansion">China's next-gen station</a> (planned, date TBA)</td>
        <td class="r">6</td>
        <td class="r">Likely modular, expanded Tiangong</td>
      </tr>
      <tr>
        <td colspan="4" style="border-bottom: 2px solid;"></td>
      </tr>
      <tr>
        <td rowspan="8">Private</td>
        <td><a href="https://en.wikipedia.org/wiki/Axiom_Station">Axiom Station</a> (planned 2025)</td>
        <td class="r">4</td>
        <td class="r">Modular, initially ISS-attached</td>
      </tr>
      <tr>
        <td><a href="https://vast.space/">Vast-1</a> (planned 2025)</td>
        <td class="r">4</td>
        <td class="r">Single module prototype</td>
      </tr>
      <tr>
        <td><a href="https://vast.space/">Haven-1</a> (planned 2027)</td>
        <td class="r">8</td>
        <td class="r">Larger follow-up to Vast-1</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Starlab_Space_Station">Starlab</a> (planned 2028)</td>
        <td class="r">4</td>
        <td class="r">Single-launch station</td>
      </tr>
      <tr>
        <td><a href="https://explorationcompany.space/">The Exploration Company's Nyx</a> (planned 2028)</td>
        <td class="r">4</td>
        <td class="r">Modular, expandable design</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Orbital_Reef">Orbital Reef</a> (status uncertain)</td>
        <td class="r">10</td>
        <td class="r">Modular, project paused in 2023</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Voyager_Station">Voyager Station</a> (conceptual)</td>
        <td class="r">400</td>
        <td class="r">Rotating wheel design, highly speculative</td>
      </tr>
      <tr>
        <td><a href="https://en.wikipedia.org/wiki/Orbital_Reef">Orbital Reef</a> (planned 2027)</td>
        <td class="r">10</td>
        <td class="r">Duplicate entry, remove</td>
      </tr>
    </tbody>
  </table>
</div>

<!--
| **Funding**  | **Name (Year)**                                                                                                       | **Capacity** | **Type/Comments**                              |
| ------------ | --------------------------------------------------------------------------------------------------------------------- | ------------ | ---------------------------------------------- |
|              | [Salyut 1](https://en.wikipedia.org/wiki/Salyut_1) (1971)                                                             | 3            | Monolithic                                     |
|              | [Salyut 2](https://en.wikipedia.org/wiki/Salyut_2) (1973)                                                             | 2            | Monolithic, military. Debris collision failure |
|              | [Salyut 3](https://en.wikipedia.org/wiki/Salyut_3) (1974-1975)                                                        | 2            | Monolithic, military                           |
|              | [Salyut 4](https://en.wikipedia.org/wiki/Salyut_4) (1974-1977)                                                        | 3            | Monolithic                                     |
|              | [Salyut 5](https://en.wikipedia.org/wiki/Salyut_5) (1976-1977)                                                        | 2            | Monolithic, military                           |
|              | [Salyut 6](https://en.wikipedia.org/wiki/Salyut_6) (1977-1982)                                                        | 3            | Semi-modular                                   |
|              | [Salyut 7](https://en.wikipedia.org/wiki/Salyut_7) (1982-1991)                                                        | 3            | Semi-modular                                   |
| Govt. funded | [Skylab](https://en.wikipedia.org/wiki/Skylab) (1973-1979)                                                            | 3            | Monolithic                                     |
|              | [Almaz](https://en.wikipedia.org/wiki/Almaz) (1973-1976)                                                              | 2-3          | Monolithic, military                           |
|              | [Mir](https://en.wikipedia.org/wiki/Mir) (1986-2001)                                                                  | 3            | Modular                                        |
|              | [International Space Station](https://en.wikipedia.org/wiki/International_Space_Station) (2000-present)               | 7            | Modular, international                         |
|              | [Tiangong-1](https://en.wikipedia.org/wiki/Tiangong-1) (2011-2018)                                                    | 3            | Monolithic prototype                           |
|              | [Tiangong-2](https://en.wikipedia.org/wiki/Tiangong-2) (2016-2019)                                                    | 2            | Monolithic prototype                           |
|              | [Tiangong Space Station](https://en.wikipedia.org/wiki/Tiangong_space_station) (2021-present)                         | 3            | Modular                                        |
|              | [Lunar Gateway](https://en.wikipedia.org/wiki/Lunar_Gateway) (planned 2024)                                           | 4            | Modular, lunar orbit                           |
|              | [ROSS](https://en.wikipedia.org/wiki/Russian_Orbital_Service_Station) (planned 2027)                                  | 4            | Modular, Russian national                      |
|              | [Indian Space Station](https://en.wikipedia.org/wiki/Indian_Space_Station) (planned 2035)                             | 3            | Likely modular, details TBA                    |
|              | [China's next-gen station](https://en.wikipedia.org/wiki/Tiangong_space_station#Future_expansion) (planned, date TBA) | 6            | Likely modular, expanded Tiangong              |
|              |                                                                                                                       |              |                                                |
|              | [Axiom Station](https://en.wikipedia.org/wiki/Axiom_Station) (planned 2025)                                           | 4            | Modular, initially ISS-attached                |
|              | [Vast-1](https://vast.space/) (planned 2025)                                                                          | 4            | Single module prototype                        |
|              | [Haven-1](https://vast.space/) (planned 2027)                                                                         | 8            | Larger follow-up to Vast-1                     |
| Private      | [Starlab](https://en.wikipedia.org/wiki/Starlab_Space_Station) (planned 2028)                                         | 4            | Single-launch station                          |
|              | [The Exploration Company's Nyx](https://explorationcompany.space/) (planned 2028)                                     | 4            | Modular, expandable design                     |
|              | [Orbital Reef](https://en.wikipedia.org/wiki/Orbital_Reef) (status uncertain)                                         | 10           | Modular, project paused in 2023                |
|              | [Voyager Station](https://en.wikipedia.org/wiki/Voyager_Station) (conceptual)                                         | 400          | Rotating wheel design, highly speculative      |
-->


### Large Space Telescopes (25 metres or more)
**<u>Domain</u>**: Space agencies and commercial


### In-Space Servicing/Repair/Refuelling Systems
**<u>Domain</u>**: Commercial

### Space-based Geoengineering
**<u>Domain</u>**: Commercial

### Debris Removal
**<u>Domain</u>**: Commercial
**<u>Existing Players</u>**


-[ClearSpace](http://clearspace.today)

## Project Blurb (for Inspiration Only)
There is a rapidly growing number of man-made satellites in Earth’s orbit, fulfilling
a wide range of tasks. As satellite technology develops, there is a growing interest
in the design of satellites such as the International Space Station (ISS), that are
capable of sustaining human occupation for extended periods. The design requirements
of these occupied satellite systems are complex and depend upon the number of
occupants, the expected duration of occupation (i.e. the number of years an astronaut would
spend on the satellite) and the overarching purpose of the space station.

Each group will examine a different type of space station, which serves different purposes, including
- A habitat for long-term occupation
- One with the optical telescopes or other imagers for disaster-monitoring, persistent Earth observations,
or space-based astronomy
- In-space factory for production of semi-conductors

Students will focus on a single application from the above list and will consider
different levels of human occupants, range from less than 10 to several thousand people.
The specific objectives include determining precise system-level requirements, estimating
costs associated with different possible designs, and developing an Attitude and
Orbit Control System. Students will need to survey available launch vehicles (incl.
SpaceX’s Starship Super Heavy) to develop cost estimates and a mission plan/architecture
for the assembly. The latter will involve developing a high-level concept of operations
needed to assemble the desired space station using either robots or astronauts. Again,
a trade-off analysis is necessary as a precursor that estimates cost, speed, time, risks, etc.
for each assembly style. By the end of the project, students will be expected to conclude with
a recommendation on the station design, the chosen assembly architecture in the ConOps (aka
Concept of Operations) for their given occupancy limit, and orbit/attitude control system simulations.

## Weekly Workshop Philosophy
In line with the [formal assessments (listed below)](http://angadhn.com/online_textbooks/UG_final_year_project/#formal-assessments) but also to prepare you as future leaders in engineering,
our weekly 2-hour workshops are geared primarily towards getting you to developing broader skills than
university might typically prepare you for in the early years. Some examples of skills you will develop
over the coming weeks are listed below (but this is by no means an exhaustive list):
1. **Public Speaking**: elevator pitch style in the early weeks to eventually being able to give rapid updates
in the later weeks.
2. **Writing**: Developing writing skills.
3. **Insight Generation**: Reflecting on technologies[^a] and the underlying
philosophy for their development.

## Informal Assessments
Thus, we have the following two informal assessments:
1. Weekly in-class presentations by each member of every group the entire academic year.
2. 6-page technical report to be submitted in Week 6 of Semester B.

## Formal Assessments

| **Assessment**                                                                                         | **Due Date** |
| ------------------------------------------------------------------------------------------------------ | ------------ |
| **Assessment 1**: Front End Individual Design Report (10%)                                             | [Due Date]   |
| **Assessment 2**: Group Project Proposal/Feasibility Study (10%)                                       | [Due Date]   |
| **Assessment 3**: Peer Evaluation with Self Reflection and Action Plan Sem A (0%, Formative)           | [Due Date]   |
| **Assessment 4**: Peer Evaluation with Self Reflection and Action Plan Sem B (15%)                     | [Due Date]   |
| **Assessment 5**: Individual Detailed Design Report (40%)                                              | [Due Date]   |
| **Assessment 6**: Final Group Presentation and Individual Back-up Evidence (15% Group, 10% Individual) | [Due Date]   |

## Useful Resources:
This list will grow but useful resources at the time of writing are listed below.
### Tools for Writing and Research Managemenent:
1. [$$\LaTeX$$ template on Overleaf](https://www.overleaf.com/latex/templates/qmul-sems-undergraduate-report-template/qdypzhkttgyt)
that I have posted.
2. [Zotero](https://www.zotero.org) is an excellent and free tool for collecting all the papers you use for
your research. These will be used as citations in the Reference section of your report(s). For these
reasons, tools like Zotero are also called reference management tools. Worth downloading and reading/wathcing some
tutorials online.
3. [Google Scholar](https://scholar.google.com) is superb for finding scholarly papers in addition to 
the resources provided on QM+. A browser plugin can also be installed via Zotero that connects to Google
Scholar to quickly import papers that you find interesting; link here for
[Zotero Connector](https://www.zotero.org/download/connectors).
4. [Inkscape](https://inkscape.org) is one example of a useful tool for making high quality images.
[Keynote ](https://www.apple.com/uk/keynote/)and PowerPoint are
also useful tools not only for making presentations but also for quickly making schematics or editing images.

### Some Technical References:
1. Space Systems Engineering Textbooks. The bible for this is typically [SMAD by James Wertz
Some goods one are by Stark and Fortescue](https://www.amazon.com/Space-Mission-Engineering-Technology-Library/dp/1881883159) which is also made available via the
[Internet Archive](https://archive.org/details/spacemissionanal0003edunse). Another is by
[Fortescue et al.](https://www.amazon.com/Spacecraft-Systems-Engineering-Peter-Fortescue/dp/047075012X/ref=sr_1_1?crid=1Q26KNFTZBRSQ&dib=eyJ2IjoiMSJ9.e0d04EB9lgaq4_O9stPoRdmatNHD5PIdX9hZzjEJaZjVglvWUD5JhGJ3eK5mZ7nJqUYuSfL7tKb1kte3X2Ebqmz_mbqegw7XFk98ScwyQvRcQvGKdmAHEonLpOQKcJ6Q.6z31353CMhm9mEjpNLrAcUx1-TDFRUHJSIUju5o05Iw&dib_tag=se&keywords=stark+fortescue&qid=1726750506&s=books&sprefix=stark+foretescu%2Cstripbooks-intl-ship%2C145&sr=1-1)
which QMUL students can access on QM+.
2. If you want to look into how books such as above can inform the development of large space structures, you can
read my paper on how to [robotically assemble 25 metre space telescopes](https://www.angadhn.com/publication/2023-06-01-towards-robotic-on-orbit-assembly)
and another [CalTech/NASA-JPL paper on 80 metre telescopes](https://kiss.caltech.edu/papers/largestructure/papers/architecture.pdf).
3. My blog post on [von Braun's rotating wheel space stations](http://www.angadhn.com/large%20space%20stations/space%20exploration/vonBraunWheels/).

### Footnotes
[^a]: Here, I do not just mean space technolgoies but even those that you use in preparing your reports such as Github and $$\LaTeX$$.
