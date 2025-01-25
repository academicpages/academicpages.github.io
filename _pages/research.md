---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
header:
---

My current research focuses on modeling biochemical particle systems by stochastic processes and ODEs/PDEs, make inference for the key parameters in such reaction-diffusion particle system by statists and machine learning, and implemented efficient numerical simulation for such large-scale system. 

In my first project, we developed a novel particle-based Reactive Langevin Dynamics (RLD) model, focusing on deriving reactive interaction kernels that satisfy the physical constraint of detailed balance for reactive fluxes at equilibrium. We demonstrated that, to leading order, the overdamped limit of the resulting RLD model corresponds to the volume reactivity PBSRD model, with the well-known Doi model emerging as a special case. This work represents a step toward systematically deriving PBSRD models from more microscopic reaction frameworks and highlights potential constraints on the latter to ensure consistency across physical scales. To validate our theory, we implemented an efficient numerical simulation to confirm the agreement between the two physical scales.

<nbsp>

{% include base_path %}

{% assign ordered_pages = site.research | sort:"order_number" %}

{% for post in ordered_pages %}
  {% include archive-single.html type="grid" %}
{% endfor %}