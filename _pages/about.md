---
permalink: /
title: "About Me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Hi! I am Mehrab, a PhD Candidate (4th year) in CS with a specialization in Artificial Intelligence and Machine Learning. My advisor is [Professor Garrison W. Cottrell](https://cseweb.ucsd.edu/~gary/). My current research focus is on deep generative models, especially debiasing them in different tasks such as attributes to image generation, image-to-image translation tasks, etc. I have also worked on and have research interests in recommender systems and federated learning. To learn more about my projects, please feel free to take a look at my [projects](https://mehrab-tanjim.github.io/#projects) and relevant [publications](https://mehrab-tanjim.github.io/#publications)!

Before joining UCSD, I was a research assistant working with [Dr. Muhammad Abdullah Adnan](https://sites.google.com/site/abdullahadnan/) at my undergraduate university, Bangladesh University of Engineering and Technology (BUET), where I received my bachelor's in CS. There I spent a wonderful time developing scalable machine learning algorithms (e.g. PCA) in the distributed environment (e.g Spark/Hadoop). After joining UCSD, I had the opportunity to work as a Data Science intern at Etsy (Summer 2019), Adobe (Summer 2020, 2021, and 2022). I am grateful to Adobe and The Home Depot for the generous gift funds to my advisor for supporting my research.

<h1>Latest News</h1>

[September 2022] Joined The Home Depot Online Data Science team as a Data Science Intern (part-time, co-op program).

[September 2022] Joint work with Adobe "Discovering and Mitigating Biases in CLIP-based Text-to-Image Generation" accepted as a post at Responsible Computer Vision at ECCV'22.

[August 2022] Joint work with Adobe "Debiasing Image-to-Image Translation Models" accepted in BMVC'22.

[June 2022] Joined Adobe REAL team as a Research Scientist Intern.

[December 2021] Finalist in Adobe Fellowship Program'22.

[September 2021] Submitted my PhD thesis proposal, I am a PhD candidate now!

[July 2021] Joint work with Adobe "Generating and Controlling Diversity in Image Search" has been accepted to WACV'22.

[June 2021] Joined Adobe GILL team as a Computer Vision, Imaging, and Video Intern.

[March 2021] Received my Master's degree in CS (specialization in Machine Learning) from UCSD!

[January 2021] Joint work with BUET "Fast, scalable and geo-distributed PCA for big data analytics" has been accepted to Information Systems'21. 


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
