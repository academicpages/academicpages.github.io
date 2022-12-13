---
permalink: /
title: "Welcome to Ranak's Homepage!"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I’m a PhD Student (4th year) at UCSD Computer Science with a specialization in Data Mining, advised by <a href="https://shangjingbo1226.github.io/" target="_blank">Professor Jingbo Shang</a> and <a href="http://mesl.ucsd.edu/gupta/" target="_blank">Professor Rajesh K. Gupta</a>. I am grateful to Qualcomm and Halıcıoğlu Data Science Institute for their fellowship to support my research.

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

[August 2022] Won the <a href="https://www.qualcomm.com/research/university-relations/innovation-fellowship/2022-north-america" target="_blank">Qualcomm Innovation Fellowship 2023</a> for our proposal on "Robust Machine Learning in IoT Devices"!

[June 2022] Joined Amazon Web Services (AWS) AI as an Applied Scientist II Intern at the Speech Science Group.

[June 2022] Received my Master's degree in CS (specialization in AI & ML) from UCSD!

[June 2022] Presented my Research Exam on <a href="https://drive.google.com/file/d/1-mcb_nuEN8jZE4I5gXwLXdudRiLj_8Sz/view?usp=sharing" target="_blank">Learning Across Irregular and Asynchronous Time Series</a>.

[May 2022] <a href="https://dl.acm.org/doi/10.1145/3534678.3539329" target="_blank">TARNet: Task-Aware Reconstruction for Time-Series Transformer</a> has been accepted to KDD '22.

[October 2021] <a href="https://dl.acm.org/doi/abs/10.1145/3488560.3498461" target="_blank">ESC-GAN: Extending Spatial Coverage of Physical Sensors</a> has been accepted to WSDM '22.

[September 2021] <a href="https://dl.acm.org/doi/10.1145/3485730.3485942" target="_blank">UniTS: Short-Time Fourier Inspired Neural Networks for Sensory Time Series Classification</a> has been accepted to SenSys '21. 

<!--

[June 2021] Joined Nokia Bell Labs as a Data Science Intern at the Statistics and Data Science Group.

[June 2020] Joined Amazon Web Services (AWS) Redshift as a Software Development Engineer Intern.

[November 2019] <a href="https://dl.acm.org/doi/10.1145/3374750" target="_blank">Real Time Principal Component Analysis</a> has been accepted to ACM Transactions on Data Science.

[August 2019] Attended The Cornell, Maryland, Max Planck Pre-doctoral Research School 2019 at Saarbrücken, Germany.

[June 2019] Won the <a href="https://hdsi-web.sdsc.edu/2019/07/" target="_blank">Halıcıoğlu Data Science Institute Graduate Prize Fellowship Award</a>!

[February 2019] <a href="https://ieeexplore.ieee.org/document/8731514" target="_blank">Real Time Principal Component Analysis</a> has been accepted to ICDE '19.

[October 2018] Received my Bachelor's degree in CSE (specialization in AI & ML) from BUET!

[October 2018] Defended my thesis on <a href="https://drive.google.com/file/d/16Sy0VkMstIVt5NQkrUiRKDICIG7rbLDM/view?usp=sharing" target="_blank">Real Time Principal Component Analysis</a>!

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




<div id="work_experience">
<h1>Work Experience</h1>


<h2>Amazon Web Services</h2>
<em>Applied Scientist II Intern </em>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Jun 2022 - Sep 2022

  <ul>
  <li>Built a pre-trained model for accent-robust speech representation that improves performance on several downstream tasks, like Speech Recognition by 20.4% and Speaker Verification by 6.3%, across 12 minority accents with few minutes of training data. Used Domain Adversarial Training with Masked Reconstruction to induce an accent-invariant output and Accent Classification with Contrastive Learning to infuse accent knowledge into the model acoustic space.</li>
  </ul>

</div>





<div id="publications">
<h1>Publications</h1>

<div>
For latest publications, please visit <u><a href="https://scholar.google.com/citations?user=kVPqPVUAAAAJ&hl=en&oi=ao" target="_blank">my Google Scholar profile</a>.</u>
<br><br>
</div>
 
  
<div>
  <p>
  <b>PrimeNet: Pre-training for Irregular Multivariate Time-Series</b>
  <br><em>Ranak Roy Chowdhury</em>, Jiacheng Li, Xiyuan Zhang, Dezhi Hong, Rajesh K. Gupta, Jingbo Shang
  <br>AAAI Conference on Artificial Intelligence (AAAI), 2023
  <br><a href="https://github.com/ranakroychowdhury/PrimeNet" target="_blank">code</a>
  </p>
  
  <p>
  <b>ESC-GAN: Extending Spatial Coverage of Physical Sensors</b>
  <br>Xiyuan Zhang, <em>Ranak Roy Chowdhury</em>, Jingbo Shang, Rajesh Gupta, Dezhi Hong
  <br>Web Search and Data Mining (WSDM), 2022
  <br><a href="https://dl.acm.org/doi/abs/10.1145/3488560.3498461" target="_blank">paper</a> | 
  <a href="https://github.com/xiyuanzh/ESC-GAN" target="_blank">code</a> | 
  <a href="https://drive.google.com/file/d/1M37W1tHasqmc5pyuc6I7pdBzPVwzWOvW/view?usp=sharing" target="_blank">poster</a> |         
  <a href="https://drive.google.com/file/d/1_AcKGJ2cpn548K81HEegvyED2eQHI5iu/view?usp=sharing" target="_blank">presentation</a>
  </p>
  
  <p>
  <b>TARNet: Task-Aware Reconstruction for Time-Series Transformer</b>
  <br><em>Ranak Roy Chowdhury</em>, Xiyuan Zhang, Jingbo Shang, Rajesh K. Gupta, Dezhi Hong
  <br>SIGKDD Conference On Knowledge Discovery and Data Mining (KDD), 2022. [<em>Travel Grant</em>]
  <br><a href="https://dl.acm.org/doi/10.1145/3534678.3539329" target="_blank">paper</a> | 
  <a href="https://github.com/ranakroychowdhury/TARNet" target="_blank">code</a> | 
  <a href="https://drive.google.com/file/d/13XrHTsPf6bhXiue0h1SunMhjYCtYRtLI/view?usp=sharing" target="_blank">poster</a> |         
  <a href="https://drive.google.com/file/d/1APhSv_TxToGm-oHLz6TqA_0FQXqLjZCL/view?usp=sharing" target="_blank">presentation</a>
  </p>
  
  <p>
  <b>UniTS: Short-Time Fourier Inspired Neural Networks for Sensory Time Series Classification</b>
  <br>Shuheng Li, <em>Ranak Roy Chowdhury</em>, Jingbo Shang, Rajesh K. Gupta, Dezhi Hong
  <br>Conference on Embedded Networked Sensor Systems (SenSys), 2021
  <br><a href="https://dl.acm.org/doi/abs/10.1145/3485730.3485942" target="_blank">paper</a> | 
  <a href="https://github.com/Shuheng-Li/UniTS-Sensory-Time-Series-Classification" target="_blank">code</a> |        
  <a href="https://drive.google.com/file/d/1MCIS23MGLbOy0Wlhu2dZy_9U7FExa_9m/view?usp=sharing" target="_blank">presentation</a>
  </p>
  
  <p>
  <b>Real-Time Principal Component Analysis</b>
  <br><em>Ranak Roy Chowdhury</em>, Muhammad Abdullah Adnan, Rajesh K. Gupta
  <br>Transactions on Data Science (TDS), Volume 1, Issue 2
  <br><a href="https://dl.acm.org/doi/10.1145/3374750" target="_blank">paper</a>
  </p>
  
  <p>
  <b>Real-Time Principal Component Analysis</b>
  <br><em>Ranak Roy Chowdhury</em>, Muhammad Abdullah Adnan, Rajesh K. Gupta
  <br>International Conference on Data Engineering (ICDE), 2019
  <br><a href="https://ieeexplore.ieee.org/document/8731514" target="_blank">paper</a> | 
  <a href="https://drive.google.com/file/d/1ZQQJShafy8qpFDXrQLBY6ZYQwKFDjG_M/view?usp=sharing" target="_blank">poster</a> |        
  <a href="https://drive.google.com/file/d/1gOqrRIKggmPr0Uz3UTrXs9j_3KQhE5QA/view?usp=sharing" target="_blank">presentation</a>
  </p>
  
  <p>
  <b>Enhancing Human Activity Recognition via Label Name Modeling</b>
  <br>Xiyuan Zhang, <em>Ranak Roy Chowdhury</em>, Dezhi Hong, Rajesh Gupta, Jingbo Shang
  <br><em>[under submission]</em>
  </p>
  
  <p>
  <b>RIoT: Towards Robust Learning for Internet-of-Things</b>
  <br><em>Ranak Roy Chowdhury</em>, Dezhi Hong, Rajesh Gupta, Jingbo Shang
  <br><em>[under submission]</em>
  </p>
  
  <p>
  <b>Towards Diverse and Coherent Augmentation for Time-Series Forecasting</b>
  <br>Xiyuan Zhang, <em>Ranak Roy Chowdhury</em>, Dezhi Hong, Rajesh Gupta, Jingbo Shang
  <br><em>[under submission]</em>
  </p>

</div>
	
	

<div id="education">
<h1>Education</h1>
	
<div>
	
</div>
	
	

<div id="awards">
<h1>Honors and Awards</h1>
	
<div>
	
</div>
	
	
	
<div id="skills">
<h1>Skills</h1>
	
<div>
	
</div>
