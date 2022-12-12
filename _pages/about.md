---
permalink: /
title: "Welcome to Ranak's Homepage!"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I’m a PhD Student (4th year) at UCSD Computer Science with a specialization in Data Mining, advised by <a href="https://shangjingbo1226.github.io/" target="_blank">Professor Jingbo Shang</a>............................ [Professor Jingbo Shang](https://shangjingbo1226.github.io/) and [Professor Rajesh K. Gupta](http://mesl.ucsd.edu/gupta/). I am grateful to Qualcomm and Halıcıoğlu Data Science Institute for their fellowship to support my research.

I spent several wonderful summers working as an Applied Scientist II Intern at AWS AI, a Data Science Intern at Bell Labs, and a Software Development Engineer Intern at AWS Redshift. 


<h2>Research Interests</h2>

I'm broadly interested in Data Mining Applications in Human-Centric AI:
- Human Motion Understanding
- Health Analytics
- Speech Processing

My projects focus on self-supervised learning to build data-efficient and robust algorithms from sensor-based time-series (PPG, ECG, EEG, IMU, clinical/medical data, wearable sensors). To learn more about my projects, please look into my [projects](https://ranakroychowdhury.github.io/#projects) and relevant [publications](https://ranakroychowdhury.github.io/#publications)!




<h1>Latest News</h1>

Will be attending AAAI '23 at Washington D.C. from Feb 7 - 14, 2023. Come and say hi!

[November 2022] "PrimeNet: Pre-Training for Irregular Multivariate Time Series" has been accepted to AAAI '23.

[August 2022] Won the [Qualcomm Innovation Fellowship 2023](https://www.qualcomm.com/research/university-relations/innovation-fellowship/2022-north-america) for our proposal on "Robust Machine Learning in IoT Devices"!

[June 2022] Joined Amazon Web Services (AWS) AI as an Applied Scientist II Intern at the Speech Science Group.

[June 2022] Received my Master's degree in CS (specialization in AI & ML) from UCSD!

[June 2022] Presented my Research Exam on [Learning Across Irregular and Asynchronous Time Series](https://drive.google.com/file/d/1AK1edhKizIZRbj3evpcFlPt_l40r4HLL/view?usp=sharing).

[May 2022] [TARNet: Task-Aware Reconstruction for Time-Series Transformer](https://dl.acm.org/doi/10.1145/3534678.3539329) has been accepted to KDD '22.

[October 2021] [ESC-GAN: Extending Spatial Coverage of Physical Sensors](https://dl.acm.org/doi/abs/10.1145/3488560.3498461) has been accepted to WSDM '22.

[September 2021] [UniTS: Short-Time Fourier Inspired Neural Networks for Sensory Time Series Classification](https://dl.acm.org/doi/10.1145/3485730.3485942) has been accepted to SenSys '21. 

<!--

[June 2021] Joined Nokia Bell Labs as a Data Science Intern at the Statistics and Data Science Group.

[June 2020] Joined Amazon Web Services (AWS) Redshift as a Software Development Engineer Intern.

[November 2019] [Real Time Principal Component Analysis](https://dl.acm.org/doi/10.1145/3374750) has been accepted to ACM Transactions on Data Science.

[August 2019] Attended The Cornell, Maryland, Max Planck Pre-doctoral Research School 2019 at Saarbrücken, Germany.

[June 2019] Won the [Halıcıoğlu Data Science Institute Graduate Prize Fellowship Award](https://hdsi-web.sdsc.edu/2019/07/)!

[February 2019] [Real Time Principal Component Analysis](https://ieeexplore.ieee.org/document/8731514) has been accepted to ICDE '19.

[October 2018] Received my Bachelor's degree in CSE (specialization in AI & ML) from BUET!

[October 2018] Defended my thesis on [Real Time Principal Component Analysis](https://drive.google.com/file/d/1ffzSaEF7o3vuWtz9dVNXdd9EcZWUaqny/view?usp=sharing)!

-->




<div id="projects">
<h1>Projects</h1>

<h2>Debiasing Generative Models</h2>

<div class="archive__proj__row">
  <div class="archive__proj__right">
    <p>
    <b><a href="https://drive.google.com/file/d/1uDgAPfl3bA4wbWtpOPdPdiQq0wzTiAOl/view">Discovering and Mitigating Biases in CLIP-based Text-to-Image Generation</a></b>
    <br>Discovered the queries for which the popular CLIP model biases the generated images in the text-to-image synthesis task and proposed several ways to mitigate the biases without retraining CLIP or the underlying generative model. <br> Tech Stack: Pytorch
    </p>
  </div>
  <div class="archive__proj__left">
    <div>
        <img  src="https://mehrab-tanjim.github.io/images/debiasing_clip.png"> 
    </div>
  </div>
</div>
  
<div class="archive__proj__row">
  <div class="archive__proj__right">
    <p>
    <b><a href="https://bmvc2022.org/programme/papers/">Debiasing Image-to-Image Translation Models</a></b>
    <br>Pretrained StyleGAN2 based networks show various biases in different image-to-image translation tasks (such as super-resolution, sketch-to-image, etc.). Mitigated this bias issue using contrastive learning and uniform sampling of minority attributes.  <br> Tech Stack: Pytorch
    </p>
  </div>
  <div class="archive__proj__left">
    <div>
        <img  src="https://mehrab-tanjim.github.io/images/debiasing_i2i.png"> 
    </div>
  </div>
</div>

<div class="archive__proj__row">
  <div class="archive__proj__right">
    <p>
    <b><a href="https://openaccess.thecvf.com/content/WACV2022/html/Tanjim_Generating_and_Controlling_Diversity_in_Image_Search_WACV_2022_paper.html">Bias Detection in Image Search and Mitigation</a></b>
    <br>Identified the bias issue in the image results for search queries, proposed a way to audit. In addition, proposed an attribute-controlled style-based generator to create new content to mitigate such biases and enrich user experience. <br> Tech Stack: Pytorch, Tensorflow
    </p>
  </div>
  <div class="archive__proj__left">
    <div>
        <img  src="https://mehrab-tanjim.github.io/images/introduction_alternative_smaller.png"> 
    </div>
  </div>
</div>

<h2>Recommender Systems</h2> 
<div class="archive__proj__row">
  <div class="archive__proj__right">
    <p>
      <b><a href="https://cseweb.ucsd.edu/~gary/pubs/mehrab-cikm-2020.pdf">Dynamic Convolution</a></b>
    <br>Built an adaptive convolution network which changes its kernel dynamically depending on the current input (~10% better recommendations). <br> Tech Stack: Pytorch
    </p>
  </div>
  <div class="archive__proj__left">
    <div>
        <img  src="https://mehrab-tanjim.github.io/images/dynamic_convolution.png"> 
    </div>
  </div>
</div>


<div class="archive__proj__row">
  <div class="archive__proj__right">
    <p>
    <b><a href="https://cseweb.ucsd.edu/~jmcauley/pdfs/www20.pdf">Intent Detection for Recommendation</a></b>
    <br>Captured users’ hidden intents (i.e. explore, purchase) from their interactions by designing a hierarchical Transformer model. It first discovers these intents and then pays attention to them for next item prediction (improved personalized recommendations by 5%). <br> Tech Stack: Tensorflow
    </p>
  </div>
  <div class="archive__proj__left">
     <div>
        <img src="https://mehrab-tanjim.github.io/images/asli.png"> 
    </div>
  </div>
</div>
  
<div class="archive__proj__row">
  <div class="archive__proj__right">
    <p>
    <b><a href="https://github.com/Mehrab-Tanjim/ConvRec/blob/master/ConvRec%20A%20simple%20lightweight%20convolutional.pdf">Lightweight Convolutional Network for Recommendation</a></b>
    <br>Improved the scalability of sequential recommender methods by modelling a scalable depth-wise separable 1D convolution neural network (requires ~30% less memory). <br> Tech Stack: Tensorflow
    </p>
  </div>
  <div class="archive__proj__left">
     <div>
        <img src="https://mehrab-tanjim.github.io/images/lightweight_convolutoin.png"> 
    </div>
  </div>
</div>
  
  
<h2>Multi-modal Learning</h2>
  
<div class="archive__proj__row">
<div class="archive__proj__right">
  

<p>
<b><a href="https://arxiv.org/pdf/1910.11124.pdf">Visual Commonsense Reasoning</a></b>.
<br>Enforced reasoning for ans. prediction on VCR by building a differentiable module which jointly trains ans. and rationale prediction (performed better in leaderboard). <br> Tech Stack: Pytorch
</p>
  
</div>
<div class="archive__proj__left">
   <div>
      <img src="https://mehrab-tanjim.github.io/images/enforcing_common_sense.png"> 
  </div>
</div>
</div>
  
<div class="archive__proj__row">
<div class="archive__proj__right">
  
<p>
<b><a href="https://arxiv.org/pdf/2004.02032.pdf">Rationale Generation</a></b>
<br>Tasked state-of-the-art Visual Question Answering model (ViLBERT) with  rationale generation (using GPT-2) to interpret/justify answer prediction. It improves accuracy by 1.5% as well. <br> Tech Stack: Pytorch
</p>
  
</div>
<div class="archive__proj__left">
   <div>
      <img src="https://mehrab-tanjim.github.io/images/rationale_generation.png"> 
  </div>
</div>
</div>
  
  
<h2>Scalable Machine Learning</h2>

<div class="archive__proj__row">
  <div class="archive__proj__right">
    <p>
    <b>Scalable Video Fingerprinting</b>
    <br>Built a scalable, end-to-end pipeline using FAISS library that can trace a manipulated video in less than a second from a trusted database with millions of corpuses. <br> Tech Stack: Tensorflow
    </p>
  </div>
  <div class="archive__proj__left">
    <div>
        <img  src="https://mehrab-tanjim.github.io/images/scalable_video_fingerprinting.png"> 
    </div>
  </div>
</div>
  
<div class="archive__proj__row">
<div class="archive__proj__right">
  
<p>
  <b><a href="https://github.com/Mehrab-Tanjim/geo-spark-hadoop">Distributed Algorithm Design</a></b>
<br>Extended both Spark and Hadoop for creating  geo-distributed clusters in AWS and designed geo-distributed algorithms for higher dimension data. <br> Tech Stack: Java, Spark, Hadoop
</p>
 
</div>
<div class="archive__proj__left">
   <div>
      <img src="https://mehrab-tanjim.github.io/images/TallnWide.png"> 
  </div>
</div>
</div>
  

<div class="archive__proj__row">
<div class="archive__proj__right">
  

<p>
  <b><a href="https://dl.acm.org/doi/abs/10.1145/3159652.3159736">Scalable Principal Component Analysis</a></b>.
<br>Improved the scalability of PCA for large datasets (up to 83× better 
performance) using sketching technique. <br> Tech Stack: Java, Scala, Spark
</p>
  
</div>
<div class="archive__proj__left">
   <div>
      <img src="https://mehrab-tanjim.github.io/images/ssketch.png"> 
  </div>
</div>
</div>

<h2>Miscellaneous</h2>

  
<div class="archive__proj__row">
  <div class="archive__proj__right">
    <p>
    <b><a href="https://github.com/Mehrab-Tanjim/Image-Colorization-using-Cycle-GAN">Image Colorization using Cycle Consistency Loss</a></b>
    <br>Explored the potential of using Cycle Consistency Loss between grey and colored images in Generative Adversarial Networks for generating true and vivid colors for black & white images. <br> Tech Stack: Pytorch
    </p>
  </div>
  <div class="archive__proj__left">
     <div>
        <img src="https://mehrab-tanjim.github.io/images/cycle_gan.png"> 
    </div>
  </div>
</div>

<div class="archive__proj__row">
  <div class="archive__proj__right">
    <p>
    <b><a href="https://github.com/Mehrab-Tanjim/pragmaticPPCA">Pragmatic Probabilistic Principal Component Analysis</a></b>
    <br> Using sketching techniques, derived a warm initialization for Expectation Maximization (EM) algorithm of Probabilistic PCA (PPCA). This speeds up convergence up to 2.25×.  <br> Tech Stack: Java, Spark
    </p>
  </div>
  <div class="archive__proj__left">
     <div>
        <img src="https://mehrab-tanjim.github.io/images/pragmatic_ppca.png"> 
    </div>
  </div>
</div>
  
<div class="archive__proj__row">
  <div class="archive__proj__right">
    <p>
    <b><a href="https://github.com/Mehrab-Tanjim/Digitor">Digitor: A Digital Circuit Simulator</a></b>
    <br>Developed a digital circuit simulator app where one can draw digital circuits and simulate its behavior. It can automatically derive the boolean expression from the circuit and minimize it (using Quine–McCluskey algorithm) to suggest a simplified implementation.<br> Tech Stack: Java
    </p>
  </div>
  <div class="archive__proj__left">
     <div>
        <img src="https://mehrab-tanjim.github.io/images/digitor.gif"> 
    </div>
  </div>
</div>

  
</div>


<div id="publications">
<h2>Publications</h2>

<div>
For latest publications, please visit <u><a href="https://scholar.google.com/citations?user=IPr2JZYAAAAJ&hl=en">my Google Scholar profile</a>.</u>
<br><br>
</div>
 
<div class="archive__pub__row">
  <div class="archive__pub__left">
    <p>
    <b>Discovering and Mitigating Biases in CLIP-based Text-to-Image Generation.</b>
    <br>Md Mehrab Tanjim, Krishna Kumar Singh, Kushal Kafle, Ritwik Sinha, Garrison W. Cottrell
    <br>Responsible Computer Vision at ECCV (RCV@ECCV), 2022
    <br><a href="https://drive.google.com/file/d/1uDgAPfl3bA4wbWtpOPdPdiQq0wzTiAOl/view">pdf</a>
    </p>
  </div>
  <div class="archive__pub__right">
    <div class="square">
        <img  src="https://mehrab-tanjim.github.io/images/adobe_logo_scaled.png"> 
    </div>
  </div>
  <div class="archive__pub__left">
    <p>
    <b>Debiasing Image-to-Image Translation Models.</b>
    <br>Md Mehrab Tanjim, Krishna Kumar Singh, Kushal Kafle, Ritwik Sinha, Garrison W. Cottrell
    <br>British Machine Vision Conference (BMVC), 2022
<!--     <br><a href="https://openaccess.thecvf.com/content/WACV2022/html/Tanjim_Generating_and_Controlling_Diversity_in_Image_Search_WACV_2022_paper.html">pdf</a> -->
    </p>
  </div>
  <div class="archive__pub__right">
    <div class="square">
        <img  src="https://mehrab-tanjim.github.io/images/adobe_logo_scaled.png"> 
    </div>
  </div>
  <div class="archive__pub__left">
    <p>
    <b>Generating and Controlling Diversity in Image Search.</b>
    <br>Md Mehrab Tanjim, Ritwik Sinha, Krishna Kumar Singh, Sridhar Mahadevan, David Arbour, Moumita Sinha, Garrison W. Cottrell
    <br>Winter Conference on Applications of Computer Vision (WACV), 2022
    <br><a href="https://openaccess.thecvf.com/content/WACV2022/html/Tanjim_Generating_and_Controlling_Diversity_in_Image_Search_WACV_2022_paper.html">pdf</a>
    </p>
  </div>
  <div class="archive__pub__right">
    <div class="square">
        <img  src="https://mehrab-tanjim.github.io/images/adobe_logo_scaled.png"> 
    </div>
  </div>
</div>

<p>
<b>Fast, scalable and geo-distributed PCA for big data analytics</b>
<br>TM Tariq Adnan, Md Mehrab Tanjim, Mummad Abdullah Adnan
<br>Information Systems, Elsevier, 2021
<br><a href="https://www.sciencedirect.com/science/article/abs/pii/S0306437920301526?dgcid=rss_sd_all">pdf</a> | <a href="https://github.com/Mehrab-Tanjim/TallnWide">code</a>
</p>

<p>
<b>DynamicRec: A Dynamic Convolutional Network for Next Item Recommendation</b>
<br>Md Mehrab Tanjim, Hammad A. Ayyubi, Garrison W. Cottrell
<br>Conference on Information and Knowledge Management (CIKM), 2020
<br><a href="https://cseweb.ucsd.edu/~gary/pubs/mehrab-cikm-2020.pdf">pdf</a> | <a href="https://github.com/Mehrab-Tanjim/DynamicRec">code</a>
</p>

<div class="archive__pub__row">
  <div class="archive__pub__left">
    <p>
    <b>Attentive sequential models of latent intent for next item recommendation</b>
    <br>Md Mehrab Tanjim, Congzhe Su, Ethan Benjamin, Dian Hu, Liangjie Hong, Julian McAuley
    <br>World Wide Web (WWW), 2020
    <br><a href="https://cseweb.ucsd.edu/~jmcauley/pdfs/www20.pdf">pdf</a>
    </p>
  </div>
  <div class="archive__pub__right">
     <div class="square">
        <img src="https://mehrab-tanjim.github.io/images/etsy_logo_scaled.png"> 
    </div>
  </div>
</div>

<!-- <p>
<b>Generating Rationales in Visual Question Answering</b>
<br>Hammad A. Ayyubi*, Md Mehrab Tanjim*, Julian McAuley, Garrison W. Cottrell
<br>Computing Research Repository (CoRR), 2020
<br><a href="https://arxiv.org/pdf/2004.02032.pdf">pdf</a>
</p>

<p>
<b>Enforcing Reasoning in Visual Commonsense Reasoning</b>.
<br>Hammad A. Ayyubi, Md Mehrab Tanjim, David Kriegman
<br>Computing Research Repository (CoRR), 2019
<br><a href="https://arxiv.org/pdf/1910.11124.pdf">pdf</a> | <a href="https://github.com/Mehrab-Tanjim/r2c">code</a>
</p> -->


<p>
<b>sSketch: A scalable sketching technique for PCA in the cloud</b>.
<br>Md Mehrab Tanjim, Muhammad Abdullah Adnan
<br>Web Search & Data Mining (WSDM), 2018
<br><a href="https://dl.acm.org/doi/abs/10.1145/3159652.3159736">pdf</a> | <a href="https://github.com/Mehrab-Tanjim/sSketch">code</a>
</p>

</div>
