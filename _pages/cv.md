---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

Education
======
* B.Tech in Information Technology, Manipal Institute of Technology, 2021

Work experience
====== 

* August 2021 - Present: **Research Engineer @ Carnegie Mellon Univerisity**
  * I work with Dr. Venkat Vishwanathan's group on ML + Material Science 
  * Developing a Julia package for uncertainty quantification in Deep Learning models.
  * Supervisor: Dr. Venkat Vishwanathan
  * [Project Website](https://www.cmu.edu/aced/)

* January 2021 - Present: **Research Intern @ University of Oxford**
  * Oxford Applied and Theoretical ML group
  * I worked with Pascal Notin, Aidan Gomez and Dr. Yarin Gal to understand sparse neural networks
  * Developed an approximate varitional inference technique to speed up neural network training. 
  * Supervisor: Dr.Yarin Gal 

* January 2021 - July 2021: **ML Engineer Intern @ AiXplain**
  * Train large neural networks using distributed training strategies.
  * Deploy ML models on AWS. Worked with AWS Lambda, EC2, S3 Elasticache to build efficient inference pipelines. 
  * [Certificate](https://drive.google.com/file/d/1Rz6UmcSdmmDdznpuBYNaS1nae5rfoVTd/view?usp=sharing), [Recommendation Letter](https://drive.google.com/file/d/1bvKokqcn2rXbk36bDiShVucAdPxf-ok5/view?usp=sharing)
  
* May 2020 - July 2020: **Research Intern @ IBM Research**
  * Built a scalable framework to analyse data augmentation methods for unstructured text data. Worked with large scale language models like BERT, ROBERTA, GPT etc.
  * Designed metrics to quantify the readability, consistency, statistical properties of industry scale datasets.
  * Implemented algorithms to quantify the distribution shift caused due to payload data in online learning settings. [Certificate](https://drive.google.com/file/d/1XqzdX8a3RIIvums3PAvvfsNIWoXcR320/view)

* May 2019 - August 2019: **Software Engineer @ Google Summer of Code**
  * Implemented a multilingual natural language generation framework to verbalise RDF triples, i.e, take in RDF triples represented as graphs and output text describing information they contain.
  * Significantly improved BLEU scores (previous SOTA): Eng -66.21 (55.9), Ger - 53.08 (NA), Rus - 46.86 (NA). Multilingual - 56.04 (NA)
  * Used Encoder-Decoder architecture training with Graph Attention Networks, Transformers, LSTM. [Code](https://github.com/dice-group/NABU)

Skills
======
* **Programming Languages**: Python, C++, Julia 
* **Frameworks**: CUDA, TensorFlow, PyTorch, Keras
* **Technologies**: Docker, Kubernetes, TerraForm, GIT, AWS S3, EC2, Elastic Inference, CloudFormation, ElastiCache
* **Languages**: English, Tamil, Telugu, Hindi

Publications
======
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
<!-- Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul> -->
  
<!-- Teaching
======
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul> -->
  
Service and leadership
======
* 2017-2018: Executive member of IEEE Student Branch, Manipal
