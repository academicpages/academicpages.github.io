---
layout: single
title: "Sensitivity analysis on reﬂex parameters
of a bio-inspired locomotion controller
and mimetism based optimisation"
excerpt: "Study of the stability of a bio-inspired human locomotion model and development of an optimisation framework to reproduce pathological gaits<br/><img src='/images/biorob_cover.jpg'>"
category: student-project
---




<!-- Introduction of the project -->
This project was a student project at the EPFL Biorob lab, aiming to tune a bio-inspired bipedal locomotion [model](https://pubmed.ncbi.nlm.nih.gov/20378480/) controlled by muscle reflexes.

<!-- Problematic -->
<!-- <figure> -->
<img src="/images/geyer-2.png" alt="Geyer reflex model" style="float:left;width:300px;height:300px;">
<!-- <figcaption></figcaption> -->
<!-- </figure> -->
The first goal of this project was to study the impact of each of the 25 model parameters of the gait stability, and then to tune it in order to reproduce pathological gaits.
The complexity of this model comes from the interactions between the antagonist and agonist muscles, making it hard to study parameters independently.

<!-- My approach -->

In order to evaluate the relations with the model's parameter and the generated gait, I started by doing a sensitivity analysis. This study was made by varying each parameter independently, while the others were set to tuned values. For that matter, I established stability and gait quality metrics, for example the energy/distance ratio. I then  optimised the simulation execution and logging, and adapted it so that evaluations could be done in parallel on a cluster.

Once these tools were developed, I proposed a formulation of the pathological gait reproduction as an multi-objective optimisation problem. As I had access to clinical measures of [idiopathic toe walking](https://orthoinfo.aaos.org/en/diseases--conditions/toe-walking/) gaits, with the joint angles for hip, knee and heel along a full stride, I set the model's parameters as degrees of freedom, with the objective of mimicking the joint angles from the patients.
I then performed a litterature review on multi-objective optimisation, and wrote my implementation of the NSGA-II algorithm.

 <video width="640" height="480" controls>
  <source src="/files/demo_toewalking.mp4" type="video/mp4">
    <figcaption>Resulting gait after optimisation</figcaption>
</video>

<!-- Challenges -->

This resulted in a good proof of concept, with the model adopting a "toe walking" like gait after optimisation, with a larger stimulation of the soleus and gastrocnemius muscles than in a normal stride.

<!-- Results -->