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
* Mar 2022 - Present: Jr. Machine Learning Engineer @ [Novit AI](https://novit.ai)
  * Machine/deep learning pipelines with PyTorch
  * Containerization with Docker and Docker Compose
  * REST APIs with FastAPI on AWS cloud servers
  * Embedded work (Raspberry Pi & Jetson devices)

* Oct 2020 - Mar 2022: Research Assistant @ [METU Heart Research Laboratory](https://hrl.eee.metu.edu.tr)
  * Worked with Assoc. Prof. Yeşim Serinağaoğlu on her TUBITAK funded projects:
    * Application of Bayesian Estimation Methods to Electrocardiographic Imaging: Prior Model Selection and Reduction of Noise Effects
    * Performance Evaluation of Noninvasive Electrocardiographic Imaging for the Localization of Premature Ventricular Contractions from Clinical Data

* Summer 2019: Machine Learning Engineer Intern @ [Darkblue Telecommunications](https://www.linkedin.com/company/darkblue-telecommunication-systems/)
  * Became familiar with convolutional neural networks.
  * Trained a road detecting model and tested it on videos from a drone.

* Summer 2019: Electronics Engineer Intern @ [Aircar Corp](https://www.aircar.aero/)
  * Did research on battery management systems.
  * Worked on the safety of electronic components.

* Summer 2018: Electrical Engineer Intern @ [ELTEMTEK](https://www.eltemtek.com.tr/)
  * Designed and modeled new electric distribution networks for several districts in Turkey.
  * Worked with the future construction plans of the cities to decide on suitable locations for the new transformers and underground cables.
  * Modeled the said networks in the CYME software.

Education
======
* B.S. in [METU EE](https://eee.metu.edu.tr), 2020
* M.Sc. in [METU EE](https://eee.metu.edu.tr), 2023
  
Skills
======
* Python
* Docker & Docker Compose
* CI/CD (GitHub Actions)
* AWS
  * EC2, ECR, Lambda, DynamoDB, Lightsail
* Trivial React & Vue

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
