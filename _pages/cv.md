---
layout: archive
title: "Hi! This is my resume"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

[pdf version available here](http://WeiCheng14159.github.io/files/resume/resume.pdf)

## Education

* Ph.D. in Electrical and Computer Engineering, Duke University, 2023 - Now
* M.S. in Computer Science and Information Engineering, National Cheng Kung University, 2022
* B.E. in Computer Engineering, University of Hong Kong, 2018

## Research experiences
* Feb 2021 - Jul 2023: Research Assistant, [Institute of Information Science, Academia Sinica](https://www.iis.sinica.edu.tw/)
  * Supervisor: [Prof. Yuan-Hao Chang](https://www.iis.sinica.edu.tw/~johnson/)
  * Graph processing on dual-addressing memory [ICCAD'22]
* Sep 2020 - Jun 2022: Research Assistant, [Computer Architecture & IC Design Lab, NCKU](http://caid.csie.ncku.edu.tw/index.php)
  * Supervisor: [Prof. Ing-Chao Lin](http://caid.csie.ncku.edu.tw/index.php?e=home.professor)
  * CNN accelerator with CLIP-Q network quantization on FPGA [TCAS-I]
* Summer 2016: Intership, [TCL Corporate Research (HK) Co., Ltd](https://www.linkedin.com/company/tcl-corporate-research-hk-co-ltd/)
  * Assist researchers on Structure from Motion, SLAM algorithms

## Publications
  <ul>{% for post in site.publications %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
<!-- Talks
======
  <ul>{% for post in site.talks %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul> -->

## Teaching
  <ul>{% for post in site.teaching %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

## Honors & Awards
* 2022: IEEE Tainan Section Best Master Thesis Award
  * Thesis Title: A Dual-Addressing Graph Processing Accelerator with Vertex Coalescing
* 2014 - 2018: HKU Foundation Scholarship for International Students (240k HKD in total)
* 2016 - 2017: Reaching Out Award scholarship from HKSAR gov.
* 2018: IEEE (Hong Kong) Final Year Project Merit Award
  * Project Title: The performance optimization on TensorFlow framework on Mobile GPU devices using OpenCL

## Projects
* A complete SW/HW co-design system for mask detection SoC 
  * SoC consists of: pipelined RV32I core, I-cache/D-cache, AXI bus, DMA, DRAM/ROM controller, Interrupt manager, and CNN acceleration unit.
  * Apply network compression and quantization on mask detection NN model.
  * Inference the compressed model on a SoC with HW acceleration.
  * SoC handles the booting sequence, data movements, the control of acceleration unit, and system interrupts.
  * Github: [https://github.com/WeiCheng14159/VSD_CNN_accelerator](https://github.com/WeiCheng14159/VSD_CNN_accelerator)
* Contribute to ria-jit (an open source RISC-V to x86 binary translator)
  * Find and fix a divide by zero bug with RISC-V compliance tests.
  * Details: [https://hackmd.io/@WeiCheng14159/BJuwQJy_s](https://hackmd.io/@WeiCheng14159/BJuwQJy_s)
* Contribute to srv32 (an open source 3-stage pipeline RV32IM core)
  * Verify and contribute RV32C instructions to the existing implementation.
  * Details: [https://hackmd.io/@WeiCheng14159/ryh1iJ1_o](https://hackmd.io/@WeiCheng14159/ryh1iJ1_o)

## Other Experiences
* Cell-based Digital IC tapeout, [Taiwan Semiconductor Research Institute](https://www.tsri.org.tw/en/index.jsp)
  * Participate in the design, tapeout, and verification of an UMC 0.18 um process digital IC
* Service as the class representative for CE major students in academic year 2015-2016, 2017-2018

## Skills
* Programming: Python, C++/C, Verilog/SystemVerilog
* AI Frameworks: Pytorch, TensorFlow
* EDA tools: NC Verilog, Design Compiler, IC Compiler/Innovus
* Miscellaneous: Linux, Shell, Latex, Markdown, Git
* Other Skills: Qi-gong (A Chinese system of physical exercises and breathing control)

## Languages
* Native Mandarian, Taiwanese
* Fluent English, Cantonese