---
permalink: /
title: ''
excerpt: About me
author_profile: true
redirect_from:
  - /about/
  - /about.html
published: true
---

I am a Ph.D. candidate in Computer Science in the [Khoury College of Computer Sciences](https://www.khoury.northeastern.edu) at [Northeastern University](https://www.northeastern.edu). I am working in [The Helping Hands Lab](https://www2.ccs.neu.edu/research/helpinghands/) and [Geometric Learning Lab](http://www.robinwalters.com/index.html), advised by Professor [Robert Platt](https://www.khoury.northeastern.edu/people/robert-platt/) and Professor [Robin Walters](https://www.khoury.northeastern.edu/people/robin-walters/). My research interests include Machine Learning and Robotics. Recently, my research has focused on applying equivariant machine learning methods to robotic manipulation to improve learning efficiency.

Prior to the Ph.D. program, I received my Master's degree in Computer Science from [Northeastern University](https://www.northeastern.edu) and my Bachelor's degree in Computer Science and Technology from [Sichuan University](http://www.scu.edu.cn), Chengdu, China.

Email: wang dot dian at northeastern dot edu. CV: [link](https://pointw.github.io/CV/dian_wang_cv.pdf).

## News
<style>
#myList {
    margin-bottom: 0;
}
#myList li:nth-child(n+6) {
    display: none;
}
#more {
    cursor: pointer;
    color: #52adc8; /* Replace with your desired color */
    margin-left: 1.5em; /* Adjust as needed */
    margin-top: 0;
    display: inline-block;
}
</style>
<script>
document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("more").addEventListener("click", function(){
      var listItems = document.querySelectorAll('#myList li:nth-child(n+6)');
      for(var i=0; i<listItems.length; i++){
        listItems[i].style.display = 'list-item';
      }
      this.style.display = 'none';
  });
});
</script>

<ul id="myList">
  <li>04/2024: I will be returning to the Boston Dynamic AI Institute as a summer intern.</li>
  <li>09/2023: Our paper <a href="https://arxiv.org/pdf/2303.04745.pdf">A General Theory of Correct, Incorrect, and Extrinsic Equivariance</a> is accepted at NeurIPS 2023.</li>
  <li>07/2023: Recording of our <a href="https://sites.google.com/view/rss23-sym">Workshop on Symmetries in Robot Learning</a> is available <a href="https://www.youtube.com/watch?v=E2l16T0biu4">here</a>.</li>
  <li>06/2023: I am honored to receive the <a href="https://www.jpmorgan.com/technology/artificial-intelligence/research-awards/phd-fellowship-2023">2023 JP Morgan Chase PhD Fellowship</a>!</li>
  <li>04/2023: I give a guest lecture, <a href="https://www.youtube.com/watch?v=dx5rDtdv7LM">Equivariant Learning for Robotic Manipulation</a>. The lecture summarizes our latest research, so be sure to check it out!</li>
  <li>03/2023: We are organizing the <a href="https://sites.google.com/view/rss23-sym">Workshop on Symmetries in Robot Learning</a> at RSS 2023.</li>
  <li>02/2023: I will be joining the Boston Dynamic AI Institute as a summer intern.</li>
  <li>01/2023: Our paper <a href="https://arxiv.org/pdf/2211.09231.pdf">The Surprising Effectiveness of Equivariant Models in Domains with Latent Symmetry</a> is accepted at ICLR 2023 as a spotlight presentation.</li>
  <li>01/2023: Two papers are accepted at ICRA 2023.</li>
</ul>
<a id="more" href="javascript:void(0)">more ▾</a>

## Publication
<style>
.button {
  background-color: white;
}
.button-4 {
  appearance: none;
  background-color: #FAFBFC;
  border: 1px solid rgba(27, 31, 35, 0.15);
  border-radius: 6px;
  box-shadow: rgba(27, 31, 35, 0.04) 0 1px 0, rgba(255, 255, 255, 0.25) 0 1px 0 inset;
  box-sizing: border-box;
  color: #24292E;
  cursor: pointer;
  display: inline-block;
  font-family: -apple-system, system-ui, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji";
  font-size: 16px;
  font-weight: 500;
  line-height: 20px;
  list-style: none;
  padding: 4px 8px;
  position: relative;
  transition: background-color 0.2s cubic-bezier(0.3, 0, 0.5, 1);
  user-select: none;
  -webkit-user-select: none;
  touch-action: manipulation;
  vertical-align: middle;
  white-space: nowrap;
  word-wrap: break-word;
}

.button-4:hover {
  background-color: #F3F4F6;
  text-decoration: none;
  transition-duration: 0.1s;
}

.button-4:disabled {
  background-color: #FAFBFC;
  border-color: rgba(27, 31, 35, 0.15);
  color: #959DA5;
  cursor: default;
}

.button-4:active {
  background-color: #EDEFF2;
  box-shadow: rgba(225, 228, 232, 0.2) 0 1px 0 inset;
  transition: none 0s;
}

.button-4:focus {
  outline: 1px transparent;
}

.button-4:before {
  display: none;
}

.button-4:-webkit-details-marker {
  display: none;
}
</style>

![](images/equidiff.gif){: .align-right width="200px"}
**Equivariant Diffusion Policy**  
**Dian Wang**, Stephen Hart, David Surovik, Tarik Kelestemur, Haojie Huang, Haibo Zhao, Mark Yeatman, Jiuguang Wang, Robin Walters, Robert Platt  
*Preprint*  
<button class="button-4" onclick="window.open('https://pointw.github.io/equidiff_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2407.01812','_blank')">PDF</button>
<br>

![](images/haojie_imagine.png){: .align-right width="200px"}
**IMAGINATION POLICY: Using Generative Point Cloud Models for Learning Manipulation Policies**  
Haojie Huang, Karl Schmeckpeper\*, **Dian Wang\***, Ondrej Biza\*, Yaoyao Qian, Haotian Liu, Mingxi Jia, Robert Platt, Robin Walters  
*Preprint*  
<button class="button-4" onclick="window.open('https://haojhuang.github.io/imagine_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2406.11740','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=EpYUDb8bUP4','_blank')">Video</button>
<br>

![](images/mingxi_gem.png){: .align-right width="200px"}
**Open-vocabulary Pick and Place via Patch-level Semantic Maps**  
Mingxi Jia, Haojie Huang, Zhewen Zhang, Chenghao Wang, Linfeng Zhao, **Dian Wang**, Jason Xinyu Liu, Robin Walters, Robert Platt, Stefanie Tellex  
*Preprint*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2406.15677','_blank')">PDF</button>
<br>

![](images/arsh_offline.png){: .align-right width="200px"}
**Equivariant Offline Reinforcement Learning**  
Arsh Tangri, Ondrej Biza, **Dian Wang**, David Klee, Owen Howell, Robert Platt  
*Preprint*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2406.13961','_blank')">PDF</button>
<br>

![](images/haojie_iclr24.png){: .align-right width="200px"}
**Fourier Transporter: Bi-Equivariant Robotic Manipulation in 3D**  
Haojie Huang, Owen Lewis Howell\*, **Dian Wang\***, Xupeng Zhu\*, Robert Platt<sup>†</sup>, Robin Walters<sup>†</sup>  
*ICLR 2024, Vienna, Austria*  
<button class="button-4" onclick="window.open('https://haojhuang.github.io/fourtran_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://openreview.net/pdf?id=UulwvAU1W0','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://youtube.com/playlist?list=PLtEvDdcT-Ai8irdlBB7wDsfOuOIZo1ZM2&si=iBD87RsHBr5aIFXt','_blank')">Video</button>
<br>

![](images/haojie_ijrr.png){: .align-right width="200px"}
**Leveraging Symmetries in Pick and Place**  
Haojie Huang, **Dian Wang**, Arsh Tangri, Robin Walters<sup>†</sup>, Robert Platt<sup>†</sup>  
*The International Journal of Robotics Research. 2023*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2308.07948.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/HaojHuang/Equivariant-Transporter-Net','_blank')">Code</button>
<br>

![](images/ice_example.png){: .align-right width="200px"}
**A General Theory of Correct, Incorrect, and Extrinsic Equivariance**  
**Dian Wang**, Xupeng Zhu, Jung Yeon Park, Mingxi Jia, Guanang Su, Robert Platt, Robin Walters  
*NeurIPS 2023, New Orleans, Louisiana, USA*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2303.04745.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://youtu.be/snCMcFjuHVI','_blank')">Talk</button>
<button class="button-4" onclick="window.open('https://github.com/pointW/ext_theory','_blank')">Code</button>
<br>

![](images/hai_corl23.png){: .align-right width="200px"}
**Equivariant Reinforcement Learning under Partial Observability**  
Hai Huu Nguyen, Andrea Baisero, David Klee, **Dian Wang**, Robert Platt, Christopher Amato  
*CoRL 2023, Atlanta, Georgia, USA*  
<button class="button-4" onclick="window.open('https://sites.google.com/view/equi-rl-pomdp','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://openreview.net/pdf?id=AnDDMQgM7-','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/hai-h-nguyen/equi-rl-for-pomdps','_blank')">Code</button>
<br>

![](images/xupeng_ar.jpg){: .align-right width="200px"}
**On Robot Grasp Learning Using Equivariant Models**  
Xupeng Zhu, **Dian Wang**, Guanang Su, Ondrej Biza, Robin Walters, Robert Platt  
*Autonomous Robots. 2023*  
<button class="button-4" onclick="window.open('https://zxp-s-works.github.io/equivariant_grasp_site/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://link.springer.com/content/pdf/10.1007/s10514-023-10112-w.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/ZXP-S-works/SE2-equivariant-grasp-learning','_blank')">Code</button>
<br>

![](images/iclr23.gif){: .align-right width="200px"}
**The Surprising Effectiveness of Equivariant Models in Domains with Latent Symmetry**  
**Dian Wang**, Jung Yeon Park, Neel Sortur, Lawson L.S. Wong, Robin Walters<sup>†</sup>, Robert Platt<sup>†</sup>  
*ICLR 2023, Kigali, Rwanda,* ***Spotlight***  
<span style="color:DarkGray"><em>NeurIPS 2023 Workshop on Symmetry and Geometry in Neural Representations</em></span>  
<button class="button-4" onclick="window.open('https://pointw.github.io/extrinsic_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2211.09231.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://openreview.net/forum?id=P4MUGRM4Acu','_blank')">OpenReview</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=US4uWndGx9I','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=QYSb_hueDHI','_blank')">Talk</button>
<button class="button-4" onclick="window.open('https://github.com/pointW/extrinsic_equi','_blank')">Code</button>
<br>

![](images/mingxi_icra23.png){: .align-right width="200px"}
**SEIL: Simulation-augmented Equivariant Imitation Learning**  
Mingxi Jia\*, **Dian Wang\***, Guanang Su, David Klee, Xupeng Zhu, Robin Walters, Robert Platt  
*ICRA 2023, London, UK*  
<span style="color:DarkGray"><em>CoRL 2022 Workshop on Sim-to-Real Robot Learning</em></span>  
<button class="button-4" onclick="window.open('https://saulbatman.github.io/project/seil/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2211.00194.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=UHUmq-cOMh4','_blank')">Video</button>
<br>

![](images/haojie_icra23.png){: .align-right width="200px"}
**Edge Grasp Network: Graph-Based SE(3)-invariant Approach to Grasp Detection**  
Haojie Huang, **Dian Wang**, Xupeng Zhu, Robin Walters, Robert Platt  
*ICRA 2023, London, UK*  
<span style="color:DarkGray"><em>CoRL 2022 Workshop on Sim-to-Real Robot Learning</em></span>  
<span style="color:DarkGray"><em>RSS 2023 Workshop on Symmetries in Robot Learning</em></span>  
<button class="button-4" onclick="window.open('https://haojhuang.github.io/edge_grasp_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2211.00191.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/HaojHuang/Edge-Grasp-Network','_blank')">Code</button>
<br>

![](images/rss22.png){: .align-right width="200px"}
**On-Robot Learning With Equivariant Models**  
**Dian Wang**, Mingxi Jia, Xupeng Zhu, Robin Walters, Robert Platt  
*CoRL 2022, Auckland, New Zealand*  
<button class="button-4" onclick="window.open('https://pointw.github.io/equi_robot_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2203.04923.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://openreview.net/forum?id=K8W6ObPZQyh','_blank')">OpenReview</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=NEUDTVXlKeg','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://github.com/pointW/equi_rl','_blank')">Code</button>
<br>

![](images/hai_corl22.png){: .align-right width="200px"}
**Leveraging Fully Observable Policies for Learning under Partial Observability**  
Hai Huu Nguyen, Andrea Baisero, **Dian Wang**, Christopher Amato, Robert Platt  
*CoRL 2022, Auckland, New Zealand*  
<button class="button-4" onclick="window.open('https://sites.google.com/view/cosil-corl22','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://openreview.net/pdf?id=pn-HOPBioUE','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://openreview.net/forum?id=pn-HOPBioUE','_blank')">OpenReview</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=qSm08Q8BlbU','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://github.com/hai-h-nguyen/cosil-corl22','_blank')">Code</button>
<br>

![](images/bulletarm.png){: .align-right width="200px"}
**BulletArm: An Open-Source Robotic Manipulation Benchmark and Learning Framework**  
**Dian Wang\***, Colin Kohler\*, Xupeng Zhu, Mingxi Jia, Robert Platt  
*ISRR 2022, Geneva, Switzerland*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2205.14292.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/ColinKohler/BulletArm','_blank')">Code</button>
<br>

![](images/equi_transporter.png){: .align-right width="200px"}
**Equivariant Transporter Network**  
Haojie Huang, **Dian Wang**, Robin Walters, Robert Platt  
*RSS 2022, New York City, New York, USA*  
<span style="color:DarkGray"><em>RLDM 2022</em></span>  
<span style="color:DarkGray"><em>ICRA 2022 Workshop on Scaling Robot Learning, <strong>Best Paper Award Finalist</strong></em></span>  
<button class="button-4" onclick="window.open('https://haojhuang.github.io/etp_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2202.09400.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/HaojHuang/Equivariant-Transporter-Net','_blank')">Code</button>
<br>

![](images/rss_grasp.jpeg){: .align-right width="200px"}
**Sample Efficient Grasp Learning Using Equivariant Models**  
Xupeng Zhu, **Dian Wang**, Ondrej Biza, Guanang Su, Robin Walters, Robert Platt  
*RSS 2022, New York City, New York, USA*  
<span style="color:DarkGray"><em>ICRA 2022 Workshop on Scaling Robot Learning, Spotlight</em></span>  
<button class="button-4" onclick="window.open('https://zxp-s-works.github.io/equivariant_grasp_site/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2202.09468.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://youtu.be/0jaHpz3KQ7I','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://github.com/ZXP-S-works/SE2-equivariant-grasp-learning','_blank')">Code</button>
<br>

![](images/iclr22_drawer.gif){: .align-right width="200px"}
**SO(2)-Equivariant Reinforcement Learning**  
**Dian Wang**, Robin Walters, Robert Platt  
*ICLR 2022, Virtual,* ***Spotlight***  
<span style="color:DarkGray"><em>RLDM 2022</em></span>  
<span style="color:DarkGray"><em>ICRA 2022 Workshop on Scaling Robot Learning, Spotlight</em></span>  
<button class="button-4" onclick="window.open('https://pointw.github.io/equi_rl_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2203.04439.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://openreview.net/forum?id=7F9cOhdvfk_','_blank')">OpenReview</button>
<button class="button-4" onclick="window.open('https://youtu.be/8Ocwv2nnSKI','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://iclr.cc/virtual/2022/spotlight/6799','_blank')">Talk</button>
<button class="button-4" onclick="window.open('https://github.com/pointW/equi_rl','_blank')">Code</button>
<br>

![](images/corl21.png){: .align-right width="200px"}
**Equivariant Q Learning in Spatial Action Spaces**  
**Dian Wang**, Robin Walters, Xupeng Zhu, Robert Platt  
*CoRL 2021, London, UK*  
<span style="color:DarkGray"><em>RSS 2022 Workshop on Scaling Robot Learning, Spotlight</em></span>  
<button class="button-4" onclick="window.open('https://pointw.github.io/equi_q_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2110.15443.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://openreview.net/forum?id=IScz42A3iCI','_blank')">OpenReview</button>
<button class="button-4" onclick="window.open('https://openreview.net/attachment?id=IScz42A3iCI&name=poster','_blank')">Poster</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=GtdpvjLHc_Q','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://github.com/pointW/equi_q_corl21','_blank')">Code</button>
<br>

![](images/Paladyn21.png){: .align-right width="200px"}
**Design Guidelines for Human-Robot Interaction with Assistive Robot Manipulation Systems**  
Alexander Wilkinson, Michael Gonzales, Patrick Hoey, David Kontak, **Dian Wang**, Noah Torname, Amelia Sinclaire, Zhao Han, Jordan Allspaw, Robert Platt, Holly Yanco  
*Paladyn, Journal of Behavioral Robotics. 2021*  
<button class="button-4" onclick="window.open('https://www.degruyter.com/document/doi/10.1515/pjbr-2021-0023/html','_blank')">Paper</button>
<br>

![](images/aamas21.png){: .align-right width="200px"}
**Action Priors for Large Action Spaces in Robotics**  
Ondrej Biza, **Dian Wang**, Robert Platt, Jan-Willem van de Meent, Lawson LS Wong  
*AAMAS 2021, London, UK*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2101.04178.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/ondrejba/action_priors','_blank')">Code</button>
<br>

![](images/asrse3.png){: .align-right width="200px"}
**Policy learning in SE (3) action spaces**  
**Dian Wang**, Colin Kohler, Robert Platt  
*CoRL 2020, Boston, Massachusetts, USA*  
<button class="button-4" onclick="window.open('https://pointw.github.io/asrse3-page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2010.02798.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://youtu.be/FiHoIF1oLZs','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://youtu.be/W0UQMntqaog','_blank')">Talk</button>
<button class="button-4" onclick="window.open('https://github.com/pointW/asrse3_corl20','_blank')">Code</button>
<br>

![](images/scooter.png){: .align-right width="200px"}
**Towards Assistive Robotic Pick and Place in Open World Environments**  
**Dian Wang**, Colin Kohler, Andreas ten Pas, Alexander Wilkinson, Maozhi Liu, Holly Yanco, Robert Platt  
*ISRR 2019, Hanoi, Vietnam*  
<button class="button-4" onclick="window.open('https://pointw.github.io/scooter-page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/1809.09541.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=ZimZlsJTaTU','_blank')">Video</button>
<br>

\* indicates equal contribution; <sup>†</sup> indicates equal advising.  

## Service
Organizer: RSS2023 Workshop on Symmetries in Robot Learning  
Reviewer: ICML 2024. ICLR 2023-2024. NeurIPS 2023. ICRA 2019, 2022-2024. CoRL 2022-2023. IROS 2021, 2023. RAL 2022-2024. T-RO 2022.

## Education
+ (2020-Present) PhD student, Computer Science, Northeastern University, Boston, USA
+ (2017-2019) M.S, Computer Science, Northeastern University, Boston, USA
+ (2013-2017) B.Eng, Computer Science & Technology, Sichuan University, Chengdu, China
