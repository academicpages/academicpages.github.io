---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

## Selected Papers [Google Scholar](https://scholar.google.com/citations?user=JKXOENIAAAAJ&hl=en)

1.	Thomas Reese, Adam Wright, **Siru Liu**, Richard Boyce, Andrew Romero, Guilherme Del Fiol, Kensaku Kawamoto, Daniel Malone. Improving the specificity of drug-drug interaction alerts: Can it be done?, American Journal of Health-System Pharmacy. 2022. doi: 10.1093/ajhp/zxac045
2.	**Siru Liu**, Kensaku Kawamoto, Guilherme Del Fiol, Charlene Weir, Daniel C. Malone, Thomas J. Reese, Keaton Morgan, David ElHalta, Samir Abdelrahman. The Potential for Leveraging Machine Learning to Filter Medication Alerts. J Am Med Inform Assoc. 2022. doi: 10.1093/jamia/ocab292
3.	**Siru Liu**, Jialin Liu. Public Attitudes toward COVID-19 Vaccines on English-language Twitter: A Sentiment Analysis. Vaccine. 2021. doi: 10.1016/j.vaccine.2021.08.058
4.	**Siru Liu**, Thomas J. Reese, Kensaku Kawamoto, Guilherme Del Fiol, Charlene Weir. A Theory-based Meta-regression of Factors Influencing Clinical Decision Support Adoption and Implementation. J Am Med Inform Assoc. 2021. doi: 10.1093/jamia/ocab160
5.	**Siru Liu**, Jili Li, Jialin Liu. Leveraging Transfer Learning to Analyze Opinions, Attitudes, and Behavioral Intentions Toward COVID-19 Vaccines. J Med Internet Res. 2021 Aug 10;23(8):e30251. doi: 10.2196/30251. PubMed PMID: 34254942.
6.	**Siru Liu**, Jialin Liu. Understanding Behavioral Intentions Toward COVID-19 Vaccines: Theory-Based Content Analysis of Tweets. J Med Internet Res. 2021;23(5): e28118. doi.org/10.2196/28118.
7.	**Siru Liu**, Thomas Reese, Guilherme Del Fiol, Kensaku Kawamoto, Charlene Weir. A systematic review of theoretical constructs in CDS literature. BMC Med Inform Decis Mak. 2021;21(1):102. doi:10.1186/s12911-021-01465-2.


{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
