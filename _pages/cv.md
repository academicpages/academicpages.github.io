---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Work experience
======
* CSIRO, Australian e-Health Research Centre, Brisbane
  * Postdoctoral Research Fellow
  * Search and Natural Language Process for Precision Medicine.
  * Project website: [http://health-search.csiro.au/oscar/](http://health-search.csiro.au/oscar/)
  * Mar 2023 – Current
    
* Microsoft, Beijing, STCA group
  * Research Intern
  * Developing multimodal and multilingual entity retrieval models.
  * May 2022 - Nov 2022
    
* The University of Queensland
  * Casual Research Assistant
  * Assist with the research and development of methods of information retrieval and evaluation based on online learning to rank.
  * Apr 2019 - July 2019
  
Awards
======
* [ICTIR 2021](https://ictir2021.org/awards/) [ <i class="fa fa-trophy" aria-hidden="true"> Best Student Paper Award </i> ]
  * Effective and Privacy-preserving Federated Online Learning to Rank
* [SIGIR 2021 Top10 authors (unofficial)](https://groups.cs.umass.edu/zamani/2021/04/29/sigir-2021-stats/) [ Rank #3 ]
  * Based on normalized full paper count.
* [2021 HUAWEI DIGIX GLOBAL AI CHALLENGE](https://developer.huawei.com/consumer/en/activity/digixActivity/digixWinnersDetail/201621219634131423) [ <b>Champion</b><span role="image" aria-label="🥇" style="font-family:&quot;Apple Color Emoji&quot;,&quot;Segoe UI Emoji&quot;,NotoColorEmoji,&quot;Noto Color Emoji&quot;,&quot;Segoe UI Symbol&quot;,&quot;Android Emoji&quot;,EmojiSymbols;line-height:1em;font-size:1em">🥇</span> ]
  * Search rankings in multimodal and multilingual contexts. 
  * Team leader, US$30,000 prize. 
* [SIGIR 2022](https://sigir.org/sigir2022/program/best-paper-awards/) [ <i class="fa fa-trophy" aria-hidden="true"> Best Paper Honorable Mention Award </i> ]
  * Reduce, Reuse, Recycle: Green Information Retrieval Researchs
* [ADCS 2022](http://adcs-conference.org/2022/index.html) [ <i class="fa fa-trophy" aria-hidden="true"> Best Paper Award </i> ]
  * Robustness of Neural Rankers to Typos: A Comparative Study

Education
======
* Ph.D. Candidate in Computer Science, The University of Queensland, Australia, 2019 - current.
  * Thesis topic: Teaching Pre-trained Language Models to Rank Effectively, Efficiently and Robustly
* Master of Information Technology, The University of Queensland, Australia, 2017 - 2018.
  * GPA: 6.3/7 
* Bachelor of Electrical Engineering, China, Chongqing University of Science and Technology, 2012 - 2016.
  
Teaching
======
<!-- 
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
-->
* The University of Queensland
  * Tutor
  * Tutoring of the INFS7410 (Information Retrieval and Web Search) course. Preparing and delivering course materials, assignments, and exam markings.
  * July 2019 - May 2022

  
Service
======
* PC member: SIGIR-AP2023, GenIR2023, ReNeuIR2023, SIGIR2023, SIGIR2022, SIGIR2021, ADCS2021, ADCS2022, TheWebConf2023, TOIS, ACM Computing Surveys
* Publicity Chair of [CIKM2021](http://www.cikm2021.org/committee)


Publications
======

{%- assign publications = site.publications | sort:"year" | reverse | group_by:"year" -%}
{% for year in publications %}
  {%- for post in year.items -%}
    {% include archive-single.html %}
  {%- endfor -%}
{% endfor %}

<!--   <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul> -->
  
<!-- 
Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>
-->
