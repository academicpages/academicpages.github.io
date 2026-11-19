---
title: "Predator-Swarm-Guide Dynamics: A Hybrid Approach to Crowd Modeling and Guidance in Mass Shooting Scenarios"
collection: publications
category: conferences
permalink: /publication/2024-07-01-acc-predator
excerpt: 'A hybrid approach to crowd modeling and guidance using predator-swarm dynamics.'
date: 2024-07-01
authors: 'A. Darabi, H. Montazeri Hedesh, M. Siami, M. Sznaier'
venue: 'American Control Conference (ACC)'
paperurl: 'https://doi.org/10.23919/ACC60939.2024.10645036'
ieeeurl: 'https://ieeexplore.ieee.org/document/10645036'
codeurl: 'https://github.com/hmon91/PSGModel'
citation: 'A. Darabi, H. Montazeri Hedesh, M. Siami and M. Sznaier. (2024). "Predator-Swarm-Guide Dynamics: A Hybrid Approach to Crowd Modeling and Guidance in Mass Shooting Scenarios," <i>2024 American Control Conference</i>, Toronto, ON, Canada, pp. 4402-4408.'
---

{% include publication-meta.html post=page %}

## In short

A model of how a crowd moves during an active-shooter event: people move away from the shooter and toward a trusted guide, inside a building with walls and zones. The paper uses the model to plan the motion of the people and the guide so that fewer people are hurt, and studies where the crowd settles using a continuum version of the model.

**Topics:** crowd dynamics, evacuation, swarm models, motion optimization.

## Abstract

This paper introduces the “Predator-Swarm-Guide” (PSG) model, a hybrid approach for modeling crowd dynamics by considering pairwise repulsive and attractive interactions among individuals. Extending the predator-swarm model, PSG specifically addresses the behavior of individuals during a shooting event within a zoned environment. It accounts for individuals' simultaneous efforts to evade the shooter while seeking guidance from a trusted agent. The guiding agent's movements during evacuation are influenced by two factors: its orientation towards the safe zone, where individuals are protected from the shooter, and the shooter's location. The PSG model incorporates crucial environmental factors, including impermeable walls, psychological elements leading to significant social friction, and a termination procedure to track casualties. Outputs of the PSG model underscore the significance of coordinated cooperation between individuals and the guiding agent in minimizing casualties during an active shooting scenario. Therefore, the objective is to reduce casualties through a hybrid motion optimization approach for both individuals and the guiding agent. Additionally, an equilibrium analysis, based on the continuum-limit version of the PSG model, is conducted to predict the crowd's equilibrium configuration in specific scenarios.

## BibTeX

{% raw %}
```bibtex
@inproceedings{darabi2024predator,
  author    = {Darabi, Atefe and Montazeri Hedesh, Hamidreza and Siami, Milad and Sznaier, Mario},
  title     = {Predator-Swarm-Guide Dynamics: A Hybrid Approach to Crowd Modeling and Guidance in Mass Shooting Scenarios},
  booktitle = {2024 American Control Conference (ACC)},
  address   = {Toronto, ON, Canada},
  pages     = {4402--4408},
  year      = {2024},
  doi       = {10.23919/ACC60939.2024.10645036}
}
```
{% endraw %}
