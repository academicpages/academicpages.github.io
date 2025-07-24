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

<head>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
</head>

I am a Postdoctoral researcher at Stanford University working with [Prof. Shuran Song](https://shurans.github.io) and [Prof. Jeannette Bohg](https://web.stanford.edu/~bohg/). I obtained my Ph.D. at Northeastern University with [Prof. Robert Platt](https://www2.ccs.neu.edu/research/helpinghands/people/) and [Prof. Robin Walters](http://www.robinwalters.com/). My research interests include machine learning and robotics, with a focus on improving sample efficiency and generalization of robot learning. 

Email: dianwang at stanford dot edu / [CV](https://pointw.github.io/CV/dian_wang_cv.pdf) / [Research Statement (Dec 2024)](dian_research_statement.pdf) 

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
  <li>07/2025: Super excited to start my postdoc at Stanford with Prof. Shuran Song and Prof. Jeannette Bohg!</li>
  <li>04/2025: Honored to receive <a href="https://academic-honors.provost.northeastern.edu/graduate-awards/graduate-research-awards/">Northeastern Outstanding Ph.D. Student Award in Research</a>!</li>
  <li>03/2025: Invited talk at <a href="https://bostonsymmetry.github.io/">Boston Symmetry Day</a>.</li>
  <li>11/2024: <a href="https://equidiff.github.io/">Equivariant Diffusion Policy</a> is nominated as an Outstanding Paper Award Finalist at CoRL 2024!</li>
  <li>10/2024: Robin and I presented <a href="https://www.youtube.com/watch?v=MU6wpz_8kEA">Pushing the Limits of Equivariant Neural Networks</a> at the <a href="https://www.neurreps.org/speaker-series">NeurReps Speaker Series</a> at MIT.</li>
  <li>09/2024: Three papers are accepted at CoRL 2024, <a href="https://equidiff.github.io/">Equivariant Diffusion Policy</a> is accepted as an oral presentation.</li>
  <li>09/2024: I had a great time visiting the UPenn GRASP lab and presenting at the GRASP SFI seminar. Recording of my talk: <a href="https://www.youtube.com/watch?v=dJG83-6CZMY">link</a>.</li>
  <li>07/2024: We are organizing the <a href="https://sites.google.com/view/gas-rl-rss2024">Workshop on Geometric and Algebraic Structure in Robot Learning</a> at RSS 2024.</li>
  <li>07/2024: Blogpost in GRAM Workshop @ ICML 2024: <a href="https://gram-blogposts.github.io/blog/2024/extrinsic/">Correct, Incorrect and Extrinsic Equivariance</a>.</li>
  <li>06/2024: I am proud to be part of the <a href="https://www.youtube.com/watch?v=B9g2yhHs5Wg">Khoury Story</a>!</li>
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

.project-img-container {
  width: 220px;
  display: flex;
  align-items: center;
  justify-content: center;
  float: right;
  margin-left: 1em;
  margin-bottom: 0.5em;
  background: transparent;
}
.project-img-container img {
  max-width: 100%;
  height: auto;
  display: block;
}

/* Responsive fix for mobile devices */
@media (max-width: 600px) {
  .project-img-container {
    float: none;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 1em;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .project-img-container img {
    width: 90vw;
    max-width: 320px; /* set a sensible maximum */
    height: auto;
  }
}
</style>

<div class="project-img-container" style="width: 220px">
  <img src="images/rel_traj.png" alt="" style="width: 180px; height: auto;">
</div>
<a href="https://arxiv.org/pdf/2505.13431" style="text-decoration: none; color: inherit;"><strong>A Practical Guide for Incorporating Symmetry in Diffusion Policy</strong></a>  
**Dian Wang**, Boce Hu, Shuran Song, Robin Walters, Robert Platt  
*Preprint*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2505.13431','_blank')">PDF</button>
<br><br>

<div class="project-img-container">
  <img src="images/boce_i2s.gif" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://arxiv.org/pdf/2505.16969" style="text-decoration: none; color: inherit;"><strong>3D Equivariant Visuomotor Policy Learning via Spherical Projection</strong></a>  
Boce Hu, **Dian Wang**, David Klee, Heng Tian, Xupeng Zhu, Haojie Huang, Robert Platt, Robin Walters  
*Preprint*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2505.16969','_blank')">PDF</button>
<br>

<div class="project-img-container">
  <img src="images/haibo_hep.png" alt="" style="width: 210px; height: auto;">
</div>
<a href="https://arxiv.org/pdf/2502.05728" style="text-decoration: none; color: inherit;"><strong>Hierarchical Equivariant Policy via Frame Transfer</strong></a>  
Haibo Zhao\*, **Dian Wang\***, Yizhe Zhu, Xupeng Zhu, Owen Howell, Linfeng Zhao, Yaoyao Qian, Robin Walters, Robert Platt  
*ICML 2025*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2502.05728','_blank')">PDF</button>
<br>

<div class="project-img-container">
  <img src="images/mingxi_gem.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://arxiv.org/pdf/2406.15677" style="text-decoration: none; color: inherit;"><strong>Learning Efficient and Robust Language-conditioned Manipulation using Textual-Visual Relevancy and Equivariant Language Mapping</strong></a>  
Mingxi Jia, Haojie Huang, Zhewen Zhang, Chenghao Wang, Linfeng Zhao, **Dian Wang**, Jason Xinyu Liu, Robin Walters, Robert Platt, Stefanie Tellex  
*RAL 2025*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2406.15677','_blank')">PDF</button>
<br>

<div class="project-img-container">
  <img src="images/boce_push_grasp.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://arxiv.org/pdf/2504.03053" style="text-decoration: none; color: inherit;"><strong>Push-Grasp Policy Learning Using Equivariant Models and Grasp Score Optimization</strong></a>  
Boce Hu\*, Heng Tian\*, **Dian Wang**, Haojie Huang, Xupeng Zhu, Robin Walters, Robert Platt  
*Preprint*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2504.03053','_blank')">PDF</button>
<br>

<div class="project-img-container">
  <img src="images/xupeng_c2f.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://arxiv.org/pdf/2502.01773" style="text-decoration: none; color: inherit;"><strong>Coarse-to-Fine 3D Keyframe Transporter</strong></a>  
Xupeng Zhu, David Klee\*, **Dian Wang\***, Boce Hu, Haojie Huang, Arsh Tangri, Robin Walters, Robert Platt  
*Preprint*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2502.01773','_blank')">PDF</button>
<br>

<div class="project-img-container">
  <img src="images/haojie_match.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://haojhuang.github.io/match_page/" style="text-decoration: none; color: inherit;"><strong>MATCH POLICY: A Simple Pipeline from Point Cloud Registration to Manipulation Policies</strong></a>  
Haojie Huang, Haotian Liu, **Dian Wang**, Robin Walter<sup>†</sup>, Robert Platt<sup>†</sup>  
*ICRA 2025*  
<button class="button-4" onclick="window.open('https://haojhuang.github.io/match_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://www.arxiv.org/pdf/2409.15517','_blank')">PDF</button>
<br>

<div class="project-img-container">
  <img src="images/equidiff.gif" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://equidiff.github.io/" style="text-decoration: none; color: inherit;"><strong>Equivariant Diffusion Policy</strong></a>  
**Dian Wang**, Stephen Hart, David Surovik, Tarik Kelestemur, Haojie Huang, Haibo Zhao, Mark Yeatman, Jiuguang Wang, Robin Walters, Robert Platt  
*CoRL 2024, **Outstanding Paper Award Finalist*** 🏆  
<button class="button-4" onclick="window.open('https://equidiff.github.io/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2407.01812','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://youtu.be/xIFSx_NVROU?si=MaxsHmih6AnQKAVy','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=lkNraxnsGCw&t=630s','_blank')">Talk</button>
<button class="button-4" onclick="window.open('https://github.com/pointW/equidiff','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/boce_orbit.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://orbitgrasp.github.io" style="text-decoration: none; color: inherit;"><strong>OrbitGrasp: SE(3)-Equivariant Grasp Learning</strong></a>  
Boce Hu, Xupeng Zhu\*, **Dian Wang\***, Zihao Dong\*, Haojie Huang\*, Chenghao Wang\*, Robin Walters, Robert Platt  
*CoRL 2024*  
<button class="button-4" onclick="window.open('https://orbitgrasp.github.io','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2407.03531','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=Y3UxZMPc0ms','_blank')">Video</button>
<br>

<div class="project-img-container">
  <img src="images/haojie_imagine.png" alt="" style="width: 200px; height: auto;">
</div>
<a href="https://haojhuang.github.io/imagine_page/" style="text-decoration: none; color: inherit;"><strong>IMAGINATION POLICY: Using Generative Point Cloud Models for Learning Manipulation Policies</strong></a>  
Haojie Huang, Karl Schmeckpeper\*, **Dian Wang\***, Ondrej Biza\*, Yaoyao Qian, Haotian Liu, Mingxi Jia, Robert Platt, Robin Walters  
*CoRL 2024*  
<button class="button-4" onclick="window.open('https://haojhuang.github.io/imagine_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2406.11740','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=EpYUDb8bUP4','_blank')">Video</button>
<br>

<div class="project-img-container">
  <img src="images/arsh_offline.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://arxiv.org/pdf/2406.13961" style="text-decoration: none; color: inherit;"><strong>Equivariant Offline Reinforcement Learning</strong></a>  
Arsh Tangri, Ondrej Biza, **Dian Wang**, David Klee, Owen Howell, Robert Platt  
*Preprint*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2406.13961','_blank')">PDF</button>
<br>

<div class="project-img-container">
  <img src="images/haojie_iclr24.png" alt="" style="width: 190px; height: auto;">
</div>
<a href="https://haojhuang.github.io/fourtran_page/" style="text-decoration: none; color: inherit;"><strong>Fourier Transporter: Bi-Equivariant Robotic Manipulation in 3D</strong></a>  
Haojie Huang, Owen Lewis Howell\*, **Dian Wang\***, Xupeng Zhu\*, Robert Platt<sup>†</sup>, Robin Walters<sup>†</sup>  
*ICLR 2024*  
<button class="button-4" onclick="window.open('https://haojhuang.github.io/fourtran_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://openreview.net/pdf?id=UulwvAU1W0','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://youtube.com/playlist?list=PLtEvDdcT-Ai8irdlBB7wDsfOuOIZo1ZM2&si=iBD87RsHBr5aIFXt','_blank')">Video</button>
<br>

<div class="project-img-container">
  <img src="images/haojie_ijrr.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://arxiv.org/pdf/2308.07948.pdf" style="text-decoration: none; color: inherit;"><strong>Leveraging Symmetries in Pick and Place</strong></a>  
Haojie Huang, **Dian Wang**, Arsh Tangri, Robin Walters<sup>†</sup>, Robert Platt<sup>†</sup>  
*The International Journal of Robotics Research. 2024*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2308.07948.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/HaojHuang/Equivariant-Transporter-Net','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/ice_example.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://arxiv.org/pdf/2303.04745.pdf" style="text-decoration: none; color: inherit;"><strong>A General Theory of Correct, Incorrect, and Extrinsic Equivariance</strong></a>  
**Dian Wang**, Xupeng Zhu, Jung Yeon Park, Mingxi Jia, Guanang Su, Robert Platt, Robin Walters  
*NeurIPS 2023*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2303.04745.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://youtu.be/snCMcFjuHVI','_blank')">Talk</button>
<button class="button-4" onclick="window.open('https://github.com/pointW/ext_theory','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/hai_corl23.png" alt="" style="width: 200px; height: auto;">
</div>
<a href="https://sites.google.com/view/equi-rl-pomdp" style="text-decoration: none; color: inherit;"><strong>Equivariant Reinforcement Learning under Partial Observability</strong></a>  
Hai Huu Nguyen, Andrea Baisero, David Klee, **Dian Wang**, Robert Platt, Christopher Amato  
*CoRL 2023*  
<button class="button-4" onclick="window.open('https://sites.google.com/view/equi-rl-pomdp','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://openreview.net/pdf?id=AnDDMQgM7-','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/hai-h-nguyen/equi-rl-for-pomdps','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/xupeng_ar.jpg" alt="" style="width: 200px; height: auto;">
</div>
<a href="https://zxp-s-works.github.io/equivariant_grasp_site/" style="text-decoration: none; color: inherit;"><strong>On Robot Grasp Learning Using Equivariant Models</strong></a>  
Xupeng Zhu, **Dian Wang**, Guanang Su, Ondrej Biza, Robin Walters, Robert Platt  
*Autonomous Robots. 2023*  
<button class="button-4" onclick="window.open('https://zxp-s-works.github.io/equivariant_grasp_site/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://link.springer.com/content/pdf/10.1007/s10514-023-10112-w.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/ZXP-S-works/SE2-equivariant-grasp-learning','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/iclr23.gif" alt="" style="width: 190px; height: auto;">
</div>
<a href="https://pointw.github.io/extrinsic_page/" style="text-decoration: none; color: inherit;"><strong>The Surprising Effectiveness of Equivariant Models in Domains with Latent Symmetry</strong></a>  
**Dian Wang**, Jung Yeon Park, Neel Sortur, Lawson L.S. Wong, Robin Walters<sup>†</sup>, Robert Platt<sup>†</sup>  
*ICLR 2023, **Spotlight***  
<button class="button-4" onclick="window.open('https://pointw.github.io/extrinsic_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2211.09231.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://openreview.net/forum?id=P4MUGRM4Acu','_blank')">OpenReview</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=US4uWndGx9I','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://slideslive.com/38998670/the-surprising-effectiveness-of-equivariant-models-in-domains-with-latent-symmetry','_blank')">Talk</button>
<button class="button-4" onclick="window.open('https://github.com/pointW/extrinsic_equi','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/mingxi_icra23.png" alt="" style="width: 190px; height: auto;">
</div>
<a href="https://saulbatman.github.io/project/seil/" style="text-decoration: none; color: inherit;"><strong>SEIL: Simulation-augmented Equivariant Imitation Learning</strong></a>  
Mingxi Jia\*, **Dian Wang\***, Guanang Su, David Klee, Xupeng Zhu, Robin Walters, Robert Platt  
*ICRA 2023*  
<button class="button-4" onclick="window.open('https://saulbatman.github.io/project/seil/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2211.00194.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=UHUmq-cOMh4','_blank')">Video</button>
<br>

<div class="project-img-container">
  <img src="images/haojie_icra23.png" alt="" style="width: 180px; height: auto;">
</div>
<a href="https://haojhuang.github.io/edge_grasp_page/" style="text-decoration: none; color: inherit;"><strong>Edge Grasp Network: Graph-Based SE(3)-invariant Approach to Grasp Detection</strong></a>  
Haojie Huang, **Dian Wang**, Xupeng Zhu, Robin Walters, Robert Platt  
*ICRA 2023*  
<button class="button-4" onclick="window.open('https://haojhuang.github.io/edge_grasp_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2211.00191.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/HaojHuang/Edge-Grasp-Network','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/rss22.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://pointw.github.io/equi_robot_page/" style="text-decoration: none; color: inherit;"><strong>On-Robot Learning With Equivariant Models</strong></a>  
**Dian Wang**, Mingxi Jia, Xupeng Zhu, Robin Walters, Robert Platt  
*CoRL 2022*  
<button class="button-4" onclick="window.open('https://pointw.github.io/equi_robot_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2203.04923.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://openreview.net/forum?id=K8W6ObPZQyh','_blank')">OpenReview</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=NEUDTVXlKeg','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://github.com/pointW/equi_rl','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/hai_corl22.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://sites.google.com/view/cosil-corl22" style="text-decoration: none; color: inherit;"><strong>Leveraging Fully Observable Policies for Learning under Partial Observability</strong></a>  
Hai Huu Nguyen, Andrea Baisero, **Dian Wang**, Christopher Amato, Robert Platt  
*CoRL 2022*  
<button class="button-4" onclick="window.open('https://sites.google.com/view/cosil-corl22','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://openreview.net/pdf?id=pn-HOPBioUE','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://openreview.net/forum?id=pn-HOPBioUE','_blank')">OpenReview</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=qSm08Q8BlbU','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://github.com/hai-h-nguyen/cosil-corl22','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/bulletarm.png" alt="" style="width: 180px; height: auto;">
</div>
<a href="https://arxiv.org/pdf/2205.14292.pdf" style="text-decoration: none; color: inherit;"><strong>BulletArm: An Open-Source Robotic Manipulation Benchmark and Learning Framework</strong></a>  
**Dian Wang\***, Colin Kohler\*, Xupeng Zhu, Mingxi Jia, Robert Platt  
*ISRR 2022*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2205.14292.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/ColinKohler/BulletArm','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/equi_transporter.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://haojhuang.github.io/etp_page/" style="text-decoration: none; color: inherit;"><strong>Equivariant Transporter Network</strong></a>  
Haojie Huang, **Dian Wang**, Robin Walters, Robert Platt  
*RSS 2022*  
<span style="color:DarkGray"><em>ICRA 2022 Workshop on Scaling Robot Learning, <strong>Best Paper Award Finalist</strong></em></span>  
<button class="button-4" onclick="window.open('https://haojhuang.github.io/etp_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2202.09400.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/HaojHuang/Equivariant-Transporter-Net','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/rss_grasp.jpeg" alt="" style="width: 200px; height: auto;">
</div>
<a href="https://zxp-s-works.github.io/equivariant_grasp_site/" style="text-decoration: none; color: inherit;"><strong>Sample Efficient Grasp Learning Using Equivariant Models</strong></a>  
Xupeng Zhu, **Dian Wang**, Ondrej Biza, Guanang Su, Robin Walters, Robert Platt  
*RSS 2022*  
<button class="button-4" onclick="window.open('https://zxp-s-works.github.io/equivariant_grasp_site/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2202.09468.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://youtu.be/0jaHpz3KQ7I','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://github.com/ZXP-S-works/SE2-equivariant-grasp-learning','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/iclr22_drawer.gif" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://pointw.github.io/equi_rl_page/" style="text-decoration: none; color: inherit;"><strong>SO(2)-Equivariant Reinforcement Learning</strong></a>  
**Dian Wang**, Robin Walters, Robert Platt  
*ICLR 2022, **Spotlight***  
<button class="button-4" onclick="window.open('https://pointw.github.io/equi_rl_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2203.04439.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://openreview.net/forum?id=7F9cOhdvfk_','_blank')">OpenReview</button>
<button class="button-4" onclick="window.open('https://youtu.be/8Ocwv2nnSKI','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://iclr.cc/virtual/2022/spotlight/6799','_blank')">Talk</button>
<button class="button-4" onclick="window.open('https://github.com/pointW/equi_rl','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/corl21.png" alt="" style="width: 190px; height: auto;">
</div>
<a href="https://pointw.github.io/equi_q_page/" style="text-decoration: none; color: inherit;"><strong>Equivariant Q Learning in Spatial Action Spaces</strong></a>  
**Dian Wang**, Robin Walters, Xupeng Zhu, Robert Platt  
*CoRL 2021*  
<button class="button-4" onclick="window.open('https://pointw.github.io/equi_q_page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2110.15443.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://openreview.net/forum?id=IScz42A3iCI','_blank')">OpenReview</button>
<button class="button-4" onclick="window.open('https://openreview.net/attachment?id=IScz42A3iCI&name=poster','_blank')">Poster</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=GtdpvjLHc_Q','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://github.com/pointW/equi_q_corl21','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/Paladyn21.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://www.degruyter.com/document/doi/10.1515/pjbr-2021-0023/html" style="text-decoration: none; color: inherit;"><strong>Design Guidelines for Human-Robot Interaction with Assistive Robot Manipulation Systems</strong></a>  
Alexander Wilkinson, Michael Gonzales, Patrick Hoey, David Kontak, **Dian Wang**, Noah Torname, Amelia Sinclaire, Zhao Han, Jordan Allspaw, Robert Platt, Holly Yanco  
*Paladyn, Journal of Behavioral Robotics. 2021*  
<button class="button-4" onclick="window.open('https://www.degruyter.com/document/doi/10.1515/pjbr-2021-0023/html','_blank')">Paper</button>
<br>

<div class="project-img-container">
  <img src="images/aamas21.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://arxiv.org/pdf/2101.04178.pdf" style="text-decoration: none; color: inherit;"><strong>Action Priors for Large Action Spaces in Robotics</strong></a>  
Ondrej Biza, **Dian Wang**, Robert Platt, Jan-Willem van de Meent, Lawson LS Wong  
*AAMAS 2021*  
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2101.04178.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://github.com/ondrejba/action_priors','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/asrse3.png" alt="" style="width: 190px; height: auto;">
</div>
<a href="https://pointw.github.io/asrse3-page/" style="text-decoration: none; color: inherit;"><strong>Policy learning in SE (3) action spaces</strong></a>  
**Dian Wang**, Colin Kohler, Robert Platt  
*CoRL 2020*  
<button class="button-4" onclick="window.open('https://pointw.github.io/asrse3-page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/2010.02798.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://youtu.be/FiHoIF1oLZs','_blank')">Video</button>
<button class="button-4" onclick="window.open('https://youtu.be/W0UQMntqaog','_blank')">Talk</button>
<button class="button-4" onclick="window.open('https://github.com/pointW/asrse3_corl20','_blank')">Code</button>
<br>

<div class="project-img-container">
  <img src="images/scooter.png" alt="" style="width: 220px; height: auto;">
</div>
<a href="https://pointw.github.io/scooter-page/" style="text-decoration: none; color: inherit;"><strong>Towards Assistive Robotic Pick and Place in Open World Environments</strong></a>  
**Dian Wang**, Colin Kohler, Andreas ten Pas, Alexander Wilkinson, Maozhi Liu, Holly Yanco, Robert Platt  
*ISRR 2019*  
<button class="button-4" onclick="window.open('https://pointw.github.io/scooter-page/','_blank')">Webpage</button>
<button class="button-4" onclick="window.open('https://arxiv.org/pdf/1809.09541.pdf','_blank')">PDF</button>
<button class="button-4" onclick="window.open('https://www.youtube.com/watch?v=ZimZlsJTaTU','_blank')">Video</button>
<br>

\* indicates equal contribution; <sup>†</sup> indicates equal advising.  
<!-- <sup><i class="fa-regular fa-envelope"></i></sup> indicates corresponding author;  -->

## Service
**Organizer:** RSS2023 Workshop on Symmetries in Robot Learning; RSS 2024 Workshop on Geometric and Algebraic Structure in Robot Learning  
**Reviewer:** RSS 2025. IJRR 2024. ICML 2024. ICLR 2023-2025. NeurIPS 2023, 2025. ICRA 2019, 2022-2024. CoRL 2022-2025. IROS
2021, 2023, 2025. RAL 2022-2024. T-RO 2022.

## Education
+ (2020-2025) Ph.D., Computer Science, Northeastern University, Boston, USA
+ (2017-2019) M.S, Computer Science, Northeastern University, Boston, USA
+ (2013-2017) B.Eng, Computer Science & Technology, Sichuan University, Chengdu, China
