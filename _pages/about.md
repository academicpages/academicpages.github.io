---
permalink: /
title: "Welcome!"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I'm Hannah-Marie Martiny and currently I am currently a PhD student in Bioinformatics at the Technical University of Denmark in the <a href='https://www.food.dtu.dk/english/research/genomic-epidemiology' targeT="_blank"> Research Group for Genomic Epidemiology at DTU Food</a>. My project is about dong large-scale metagenomic analysis to analyze the global distribution of antimicrobial resistance.

Feel free to reach out to me, if you have any inquries! 

You can also check out <a href="/cv/" targeT="_blank">my CV here</a>.

Publications:
{% for post in site.publications reversed %} {% include archive-single-cv.html %} {% endfor %}

In case you came looking for the documentation on the 214K metagenomic data collection, which we shared on Zenodo, go here:
https://hmmartiny.github.io/mARG/