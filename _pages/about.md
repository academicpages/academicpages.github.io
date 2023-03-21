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
Prior to this, I completed my BS degree from Northeastern University (Shenyang, China) and Chinese Academy of Sciences (Shenzhen Institute of Advanced Technology) in 2015. In my free time, I enjoy programming⌨️ (currently ![Github stars](https://img.shields.io/github/stars/jamesqfreeman?style=social) stars🌟), running🏃, swimming🏊, weightlifting🏋️, motorsports🏁 and cooking🍳.


CAD with Eye-tracking
======
<div style="display: flex; align-items: center;">
  <div style="flex: 1;">
    <p>Our motivation is straightforward: leveraging the eye movements of radiologists to improve computer-aided diagnosis. The collection of this data is a passive and unobtrusive process that captures informative supervision related to the radiologists' diagnostic procedures. First, let me show some cases we collected, This red circle will not show up in the normal collecting, just here for demo.</p>
  </div>
  <div style="flex: 1;">
    <img src="/images/demo-2.gif" alt="" width="width:30%;" />
  </div>
</div>

<br>


<br>

<div style="display: flex; align-items: center;">
  <div style="flex: 1;">
    <p>1. To make sure the collected gaze are informative, we first use it as a network supervision during training. It is a pilot study that use gaze to improve deep-learning-based CAD sytem and is published at IEEE Trans on Medical Imaging at 2022.01 </p>
    <p><i>Follow my eye: using gaze to supervise computer-aided diagnosis </i></p>
    <p><b>S Wang</b>, X Ouyang, T Liu, Q Wang, D Shen</p>
  </div>

  <div style="flex: 1;">
    <img src="/images/Follow_my_eye.png" alt="Gaze supervision" width="width:50%;" />
  </div>
</div>

<br>



<div style="display: flex; align-items: center;">
  <div style="flex: 1;">
    <p>2. We extent gaze in the very foundamental part in computer vision, data augmentation. Our brains naturally and constantly augment images (e.g., by slightly shifting our gaze to view the same object from different angles). In our research, we investigated how we could improve current image augmentation techniques by mimicking the way humans use gaze. This work is submitted to IEEE Trans on Neural Networks and Learning Systems (2022.10). </p>
    <p><i>Learning Better Contrastive View from Radiologist’s Gaze</i></p>
    <p><b>S Wang</b>, Z Zhuang, X Ouyang, L Zhang, Z Li, C Ma, T Liu, D Shen, Q Wang</p>
  </div>
  <div style="flex: 1;">
    <img src="/images/focus_contrast.png" alt="Gaze in augmentation" width="width:50%;" />
  </div>
</div>

<br>

<div style="display: flex; align-items: center;">
  <div style="flex: 1;">
    <p>3. We propose the idea of training a neural network solely on gaze information, as we believe gaze provides valuable insights for diagnostic tasks. Through our gaze collection process, we have observed that similar lesions often elicit similar gaze patterns. Therefore, we propose constructing a self-supervised system based on gaze similarity. This work is submitted to ICCV 2023.</p>
    <p><i>Mining Gaze for Contrastive Learning toward Computer-Assisted Diagnosis</i></p>
    <p>Z Zhao*, <b>S Wang*</b>, Q Wang, D Shen</p>
  </div>
  <div style="flex: 1;">
    <img src="/images/McGIP.png" alt="Self-supervision with Gaze" width="width:50%;" />
  </div>
</div>


<div style="display: flex; align-items: center;">
  <div style="flex: 1;">
    <p>4. After this worked, we apply this to a more complex task (mammography) and architecture (Vision Transformer). This work is submitted in IEEE Trans on Medical Imaging and is currently under major revision. </p>
    <p><i>Eye-gaze-guided Vision Transformer for Rectifying Shortcut Learning</i></p>
    <p>C Ma, L Zhao, Y Chen, L Zhang, Z Xiao, H Dai, D Liu, Z Wu, Z Liu, <b>S Wang</b>, ...</p>
  </div>
  <div style="flex: 1;">
    <img src="/images/vitGaze.png" alt="On vision transformer" width="width:50%;" />
  </div>
</div>

<br>

New age with Foundation Models
======
I believe we are currently experiencing the second golden age of AI research, driven by the emergence of LARGE transformers and webscale unsupervised pretraining. The first golden age was led by ImageNet supervised pretraining and CNNs. In light of this, I am motivated to work on projects that have the potential to become the cornerstone of this exciting new era in AI research.

1. We propose ChatCAD, that use trained CAD networks and use ChatGPT (or other LLMs) to merge them. To make the result more truthy, we are adding a healthcare retriever into this framework (like New Bing)
![](/images/ChatCAD.png)
*ChatCAD: Interactive Computer-Aided Diagnosis on Medical Image using Large Language Models*
**S Wang**, Z Zhao, X Ouyang, Q Wang, D Shen

2. We are also working on MeLo, a medical image low-rank adaptation scheme that is to replace finetuning in medical image analysis. This is a work I really enjoy doing as a programmer and engineer. More information coming soon.


Efficient Learning System for Voxel Images
======
Although with recent progress, neural networks have on par ability compared to human in natural image. Currently, medical expert are more efficient at abstracting things (or say better representation ability), especially for voxel images. We have done several things to improve that:

1. We believe voxel image should be represent in a continuous form instead of a discrete one (see NeRF). This idea is verified in a super-resolution setting. Submitted to MedIA.
![](/images/2022-SAINR.png)
*Spatial Attention-based Implicit Neural Representation for Arbitrary Reduction of MRI Slice Spacing* 
X Wang\*, **S Wang\***, H Xiong, K Xuan, Z Zhuang, M Liu, Z Shen, X
Zhao, L Zhang, Q Wang

2. We recontruct vessel with its centerline, representing vessel with graph. Accepted by TMI, 2023 
![](/images/2023-TaG-Net.png)
*TaG-Net: Topology-aware Graph Network for Centerline-based Vessel Labeling*
L Yao, F Shi, **S Wang**, X Zhang, Z Xue, X Cao, Y Zhan, L Chen, Y Chen, B Song, Q Wang, D Shen


3. We recontruct knee with its surface, representing the joint structure with graph. Accepted by TMI 2022 and MICCAI 2022.
![](/images/2022-LGF.png)
*Local Graph Fusion of Multi-view MR Images for Knee Osteoarthritis Diagnosis* (MICCAI 2022)
Z Zhuang, **S Wang**, L Si, K Xuan, Z Xue, D Shen, L Zhang, W Yao, Q Wang
*Knee cartilage defect assessment by graph representation and surface convolution* (TMI 2022)
Z Zhuang, L Si, **S Wang**, K Xuan, X Ouyang, Y Zhan, Z Xue, L Zhang, D Shen, W Yao, Q Wang

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


