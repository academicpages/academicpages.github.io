---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

For full list of publications check [Google Scholar](https://scholar.google.co.uk/citations?user=r8T1-yoAAAAJ&hl=en&oi=ao) 
and [DBLP](https://dblp.org/pid/200/2864.html).

Selected Conference Papers
--------------------------

* _"Abstracting failure-inducing inputs."_
Gopinath, Rahul, Alexander Kampmann, Nikolas Havrikov, _Ezekiel O. Soremekun_, and Andreas Zeller.
In Proceedings of the 29th ACM SIGSOFT international symposium on software testing and analysis, pp. 237-248. 2020.
[link](https://dl.acm.org/doi/abs/10.1145/3395363.3397349)
[preprint](https://rahul.gopinath.org/resources/issta2020/gopinath2020abstracting.pdf)

* _"Debugging Inputs."_
Kirschner, Lukas, _Ezekiel Soremekun_, and Andreas Zeller.
2020 IEEE/ACM 42nd International Conference on Software Engineering (ICSE), 2020, pp. 75-86, doi: 10.1145/3377811.3380329.
[link](https://ieeexplore.ieee.org/abstract/document/9284127)
[preprint](https://publications.cispa.saarland/3060/1/camera-ready-submission.pdf)

* _"When does my program do this? learning circumstances of software behavior."_
Kampmann, Alexander, Nikolas Havrikov, _Ezekiel O. Soremekun_, and Andreas Zeller
In Proceedings of the 28th ACM joint meeting on european software engineering conference and symposium on the foundations of software engineering, pp. 1228-1239. 2020.
[link][https://dl.acm.org/doi/abs/10.1145/3368089.3409687]


* _"Where is the bug and how is it fixed? an experiment with practitioners."_ 
Böhme, Marcel, _Ezekiel O. Soremekun_, Sudipta Chattopadhyay, Emamurho Ugherughe, and Andreas Zeller. 
In Proceedings of the 2017 11th joint meeting on foundations of software engineering, pp. 117-128. 2017.
[link](https://dl.acm.org/doi/abs/10.1145/3106237.3106255)
[preprint)[https://publications.cispa.saarland/1468/1/FSE17.pdf]
[Website](https://dbgbench.github.io)

* _"Detecting information flow by mutating input data."_
Mathis, Björn, Vitalii Avdiienko, _Ezekiel O. Soremekun_, Marcel Böhme, and Andreas Zeller.
In 2017 32nd IEEE/ACM International Conference on Automated Software Engineering (ASE), pp. 263-273. IEEE, 2017.
[link](https://ieeexplore.ieee.org/abstract/document/8115639)
[preprint](https://publications.cispa.saarland/1436/1/ase17-mainp148.pdf)

Selected Journal Papers
------------------------

* _"Inputs from Hell Learning Input Distributions for Grammar-Based Test Generation."_
_Soremekun, Ezekiel_, Esteban Pavese, Nikolas Havrikov, Lars Grunske, and Andreas Zeller. 
IEEE Transactions on Software Engineering (2020)
[link](https://ieeexplore.ieee.org/abstract/document/9154602)
[preprint](https://publications.cispa.saarland/3167/7/inputs-from-hell.pdf)


* _"Astraea: Grammar-based fairness testing."_ 
_Soremekun, Ezekiel_, Sakshi Udeshi, and Sudipta Chattopadhyay. 
IEEE Transactions on Software Engineering (2022)
# (link)[]
[preprint](https://arxiv.org/pdf/2010.02542)


* _"Locating faults with program slicing: an empirical analysis."_
_Soremekun, Ezekiel_, Lukas Kirschner, Marcel Böhme, and Andreas Zeller.
Empirical Software Engineering 26, no. 3 (2021): 1-45. 
[link](https://link.springer.com/article/10.1007/s10664-020-09931-7)
[preprint](https://arxiv.org/pdf/2101.03008)


Thesis
-------
* _"Evidence-driven testing and debugging of software systems."_
_Soremekun, Ezekiel_
PhD Dissertation, Saarland Univerity.
[link](https://publikationen.sulb.uni-saarland.de/handle/20.500.11880/31243)
[preprint](https://publikationen.sulb.uni-saarland.de/bitstream/20.500.11880/31243/1/Phd_thesis_Ezekiel_Soremekun-no-cv.pdf)


#{% if author.googlescholar %}
#  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
#{% endif %}
#
#{% include base_path %}
#
#{% for post in site.publications reversed %}
#  {% include archive-single.html %}
#{% endfor %}
