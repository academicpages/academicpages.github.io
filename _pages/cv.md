---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Ph.D. student seeking machine learning research internship.
<br>
Research interests are the intersection of machine learning and software engineering.
<br>
Experience in deep learning, machine learning, program analysis, software development.


# Education
{% for position in site.data.cv_education %}
  {% include cv_position.html %}
{% endfor %}


# Professional Experience
{% for position in site.data.cv_positions %}
  {% include cv_position.html %}
{% endfor %}


# Publications
<ul>
{% for post in site.publications reversed %}
  {% assign cv_venues = "conference-paper,preprint,thesis,poster" | split: "," %}
  {% if cv_venues contains post.venue-type %}
    {% include archive-single-cv.html %}
  {% endif %}
{% endfor %}
</ul>


# My Projects

## Primary developer
* [cfactor](https://github.com/bstee615/cfactor): Scalable, policy-driven refactoring for C programs (Python/srcML).
* [tree-climber](https://github.com/bstee615/tree-climber): Scalable program analysis tools for C built on tree-sitter (Python).
* [pal-tools](https://github.com/bstee615/pal-tools): Dynamic analysis and code generation, using Intel Pin (C++) and LLVM (Python).
* [rarl](https://github.com/bstee615/rarl): Reproduction of <a href="https://doi.org/10.48550/arXiv.1703.02702">Robust Adversarial Reinforcement Learning (Pinto et al. 2017)</a> (PyTorch/stable-baselines).

## Team project
* [animal-cognitive](https://github.com/animal-cognitive/AnimalAI-Olympics/tree/feature/whole-cache-agent): Deep reinforcement learning models with embodied animal cognition (PyTorch/rllib).
* [precise-interrupts](https://github.com/isu-cpre581-pangolin/gem5/tree/sleepy): Reproducing a historical interrupt handling paper in ARM architecture (C++/gem5).


# Technical Skills
* Programming Languages: Proficient in Python and C#. Knowledge of C++, Java, JavaScript, SQL.
* Machine Learning & data scraping: PyTorch, rllib, pandas, numpy, Selenium, beautifulsoup.
* Web Development: Vue, ASP.NET Core, .NET Framework, SQL Server, Azure Functions, ACI, VMs, ML Studio.
* Computer architecture and program analysis: Antlr, LLVM, Intel Pin, gem5, abstract interpretation, fuzzing.
* DevOps: Git, Azure DevOps, and CI/CD, Slurm batch processing, Linux server administration.


# Leadership
* Science education outreach at Greenville County Juvenile Detention, Fall 2018/Spring 2019
* Vice president of Phi Beta Chi society, Spring 2018
