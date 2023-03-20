---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---


My research interests encompass healthcare machine learning systems and general artificial intelligence🧠🤖. I envision creating a learning system as efficient and effective as, or surpassing, human capabilities. During my PhD, I conducted extensive research on radiologists' eye-tracking, believing that incorporating the information found in a human expert's reasoning process is crucial for training neural networks.

I am also fascinated by neuroscience, computer graphics, hardware circuit design, and internal combustion engines, I have yet to become an expert in these fields😢.

I am curretnly a PhD candidate at Shanghai Jiao Tong University, supervised by [Prof. Dinggang Shen](http://idea.bme.shanghaitech.edu.cn) and [Prof. Qian Wang](https://qianwang.space). 
Prior to this, I completed my BS degree from Northeastern University (Shenyang, China) and Chinese Academy of Sciences (Shenzhen Institute of Advanced Technology) in 2015. In my free time, I enjoy programming⌨️ (currently ![Github stars](https://img.shields.io/github/stars/jamesqfreeman?style=social) stars🌟), running🏃, swimming🏊, weightlifting🏋️, and motorsports🏁.


CAD with Eye-tracking
======
Our motivation is straightforward: leveraging the eye movements of radiologists to improve computer-aided diagnosis. The collection of this data is a passive and unobtrusive process that captures informative supervision related to the radiologists' diagnostic procedures. First, let me show some cases we collected, This red circle will not show up in the normal collecting, just here for demo.
<div style="text-align: center;">
  <img src="/images/demo-2.gif" alt="Gaze supervision" width="width:50%;" />
</div>

<div style="display: flex; align-items: center;">
  <div style="flex: 1;">
    <img src="/images/Follow_my_eye.png" alt="Gaze supervision" width="width:50%;" />
  </div>

  <div style="flex: 1;">
    <p>1. To make sure the collected gaze are informative, we first use it as a network supervision during training. It is a pilot study that use gaze to improve deep-learning-based CAD sytem and is published at IEEE Trans on Medical Imaging at 2022. </p>
    <p><i>Follow my eye: using gaze to supervise computer-aided diagnosis </i></p>
    <p><b>S Wang</b>, X Ouyang, T Liu, Q Wang, D Shen</p>
  </div>
</div>

<div style="display: flex; align-items: center;">
  <div style="flex: 1;">
    <img src="/images/vitGaze.png" alt="On vision transformer" width="width:50%;" />
  </div>

  <div style="flex: 1;">
    <p>2. After this worked, we apply this to a more complex task (mammography) and architecture (Vision Transformer). This work is submitted in IEEE Trans on Medical Imaging and is currently under major revision. </p>
    <p><i>Eye-gaze-guided Vision Transformer for Rectifying Shortcut Learning</i></p>
    <p>C Ma, L Zhao, Y Chen, L Zhang, Z Xiao, H Dai, D Liu, Z Wu, Z Liu, <b>S Wang</b>, ...</p>
  </div>
</div>

<div style="display: flex; align-items: center;">
  <div style="flex: 1;">
    <img src="/images/focus_contrast.png" alt="Gaze in augmentation" width="width:50%;" />
  </div>

  <div style="flex: 1;">
    <p>3. We extent gaze in the very foundamental part in computer vision, data augmentation. Our brains naturally and constantly augment images (e.g., by slightly shifting our gaze to view the same object from different angles). In our research, we investigated how we could improve current image augmentation techniques by mimicking the way humans use gaze. This work is submitted to IEEE Trans on Neural Networks and Learning Systems (2022.10). </p>
    <p><i>Learning Better Contrastive View from Radiologist’s Gaze</i></p>
    <p><b>S Wang</b>, Z Zhuang, X Ouyang, L Zhang, Z Li, C Ma, T Liu, D Shen, Q Wang</p>
  </div>
</div>

<div style="display: flex; align-items: center;">
  <div style="flex: 1;">
    <img src="/images/McGIP.png" alt="Self-supervision with Gaze" width="width:50%;" />
  </div>

  <div style="flex: 1;">
    <p>4. We propose the idea of training a neural network solely on gaze information, as we believe gaze provides valuable insights for diagnostic tasks. Through our gaze collection process, we have observed that similar lesions often elicit similar gaze patterns. Therefore, we propose constructing a self-supervised system based on gaze similarity. This work is submitted to ICCV 2023.</p>
    <p><i>Mining Gaze for Contrastive Learning toward Computer-Assisted Diagnosis</i></p>
    <p>Z Zhao*, <b>S Wang*</b>, Q Wang, D Shen</p>
  </div>
</div>




<!-- - After this worked, we apply this to a more complex task (mammography) and architecture (Vision Transformer). This work is submitted in IEEE Trans on Medical Imaging and is currently under major revision. [[Paper ] (https://arxiv.org/abs/2205.12466)].
![On vision transformer](/images/vitGaze.png)

Eye-gaze-guided Vision Transformer for Rectifying Shortcut Learning. 

C Ma, L Zhao, Y Chen, L Zhang, Z Xiao, H Dai, D Liu, Z Wu, Z Liu, **S Wang**, ...

- We extent gaze in the very foundamental part in computer vision, data augmentation. Our brains naturally and constantly augment images (e.g., by slightly shifting our gaze to view the same object from different angles). In our research, we investigated how we could improve current image augmentation techniques by mimicking the way humans use gaze. This work is submitted to IEEE Trans on Neural Networks and Learning Systems (2022.10). [[code ](https://jamesqfreeman.github.io/MicEye/contrastive_learning_example/)]
![Gaze in augmentation](/images/focus_contrast.png)

Learning Better Contrastive View from Radiologist’s Gaze. 

**S Wang**, Z Zhuang, X Ouyang, L Zhang, Z Li, C Ma, T Liu, D Shen, Q Wang

- We propose the idea of training a neural network solely on gaze information, as we believe gaze provides valuable insights for diagnostic tasks. Through our gaze collection process, we have observed that similar lesions often elicit similar gaze patterns. Therefore, we propose constructing a self-supervised system based on gaze similarity. This work is submitted to ICCV 2023.
![Self-supervision with Gaze](/images/McGIP.png)

Mining Gaze for Contrastive Learning toward Computer-Assisted Diagnosis.

Z Zhao\*, **S Wang\*,** Q Wang, D Shen -->

Efficient Healthcare Machine Learning System
======
Although with recent progress, neural networks have on par ability compared to human in natural image. Currently, medical expert are more efficient at abstracting things (or say better representation ability). 
My guess is these medical analysis is a harder problem just like GPTs can not deal with mathmatical problem and coding test very well. 

I do think we are at the second research golden age for AI with LARGE transformers and webscale unsupervised pretraining. The first golden age are lead by ImageNet supervised pretrain and CNNs. As a 
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
2. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
3. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
4. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
5. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
6. Check status by going to the repository settings, in the "GitHub pages" section

New age with Foundation Models
======

Activities
------
Reviewer for:
- IEEE Transactions on Medical Imaging, 
- IEEE Transactions on Neural Networks and Learning Systems, 
- IEEE Transactions on Biomedical Engineering, 
- IEEE Journal of Biomedical and Health Informatics,
- Neural Networks,
- Pattern Recognitiion,
- Medical Image Computing and Computer Assisted Interventions (MICCAI).


