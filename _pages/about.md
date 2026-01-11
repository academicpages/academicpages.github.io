---
permalink: /
title: "Autonomous&nbsp;Nanophotonics&nbsp;Lab"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
carousel_images:
  - banner/cint-buildings.jpg
  - lumotive_lidar_metasurface.png
  - Lab/Photonic_Ising.png
  - photonic_ising_machine_setup.png
  - Lab/Closed_cycle_He_cryostat.png
  - thermal-enz-antenna-no-pcm.png
  - self_driving_lab_pulses.png

carousel_durations:
  - 12000
  - 4000
  - 4000
  - 4000
  - 4000
  - 4000
  - 4000

carousel_titles:
  - "CINT Facility"
  - "Lumotive Solid-State LiDAR"
  - "Photonic Ising Machine"
  - "Natural Ising Machine"
  - "Structured Quantum Nanophotonics"
  - "Thermally Reconfigurable Antennas"
  - "Self-Driving Lab"
---



{% include carousel.html id="lab-carousel" images=page.carousel_images durations=page.carousel_durations titles=page.carousel_titles interval=4000 %}

## Autonomy of Scientific Discovery

The **Autonomous Nanophotonics Lab** focuses on the development of self-driving experimental platforms that integrate artificial intelligence with nanophotonics. Our goal is to accelerate scientific discovery by automating the design, execution, and analysis of experiments.

We are developing systems where **artificial intelligence drives the experimental process**, navigating parameter spaces to uncover physical principles, optimize material properties, and design photonic systems with enhanced capabilities.

### Our Approach: AI-Driven Experimentation

Our research integrates machine learning with experimental photonics to enable:

* **Autonomous experimentation**: We utilize AI to orchestrate ultrafast spectroscopy, structured light generation, and nanofabrication, allowing for the exploration of light–matter interactions.
* **Interpretable discovery**: We develop algorithms designed to extract physical laws from high-dimensional experimental data, aiming to provide actionable scientific insights.
* **Reconfigurable photonic hardware**: Our work spans quantum emitters, liquid-crystal metasurfaces, and photonic Ising machines, aiming for high-speed computation and energy efficiency.

### Research Areas

Our research contributes to several key areas:

* **Quantum information systems**: Developing deterministic single-photon sources with precise nanoscale control.
* **Ultrafast optical computing**: Implementing optimization and AI inference tasks using photonic hardware.
* **Intelligent LiDAR and imaging**: Utilizing electrically reconfigurable metasurfaces for applications in autonomous vehicles and AR/VR.
* **Self-driving scientific instruments**: Developing tools available to the research community through the *Center for Integrated Nanotechnologies (CINT)*.

### Collaboration Opportunities

We are part of the [Center for Integrated Nanotechnologies (CINT)](https://cint.lanl.gov), a DOE Nanoscale Science Research Center. Researchers interested in using our facilities can [submit a new user proposal here](https://cint.sandia.gov).

We invite collaborations with **prospective students**, **CINT users**, and **industry partners** interested in autonomous scientific tools and nanophotonics.

**We are transitioning scientific discovery into an autonomous era.**

## Highlighted Publications

{% comment %} Assign highlighted papers {% endcomment %}
{% assign autoSci = site.publications | where: "title", "AutoSciLab: A Self-Driving Laboratory For Interpretable Scientific Discovery" | first %}
{% assign autoSciTalk = site.talks | where: "title", "AutoSciLab: A Self-Driving Laboratory For Interpretable Scientific Discovery" | first %}
{% assign beamSteer = site.publications | where: "title", "Sub-picosecond steering of ultrafast incoherent emission from semiconductor metasurfaces" | first %}
{% assign sdl = site.publications | where: "title", "Self-driving lab discovers principles for steering spontaneous emission" | first %}

<div class="publications-cards">
  <div class="publication-card">
    <h3><a href="{{ autoSciTalk.url | relative_url }}">{{ autoSciTalk.title }}</a></h3>
    <p class="archive__item-authors">{{ autoSciTalk.authors }}</p>
    <p><em>{{ autoSciTalk.venue }}</em>, {{ autoSciTalk.date | date: '%Y' }}</p>
  </div>

  <div class="publication-card">
    <h3><a href="{{ beamSteer.url | relative_url }}">{{ beamSteer.title }}</a></h3>
    <p class="archive__item-authors">{{ beamSteer.authors }}</p>
    <p><em>{{ beamSteer.venue }}</em>, {{ beamSteer.date | date: '%Y' }}</p>
  </div>

  <div class="publication-card">
    <h3><a href="{{ sdl.url | relative_url }}">{{ sdl.title }}</a></h3>
    <p class="archive__item-authors">{{ sdl.authors }}</p>
    <p><em>{{ sdl.venue }}</em>, {{ sdl.date | date: '%Y' }}</p>
  </div>
</div>


<div class="lab-news-wrapper">
  {% include lab-news-scroll.html %}
</div>
