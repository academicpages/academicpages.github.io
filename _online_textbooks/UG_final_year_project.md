---
title: "Final Year Project: Space Station Design"
excerpt: "An introduction to multibody dynamics and the use of symbolic computation in modelling them."
mathjax: true
url: "https://qmplus.qmul.ac.uk/course/view.php?id=22090"
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
- A site for disaster-monitoring
- Persistent Earth observations
- Space-based astronomy
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
3. **Insight Generation**: Reflecting on technologies {% sidenote '' 'here I do not just mean space technolgoies but 
even those that you use in preparing your reports such as Github and $$\LaTeX$$' %} and the underlying
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
