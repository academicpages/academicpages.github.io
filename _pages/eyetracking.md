---
layout: archive
title: "CAD with Eye-tracking"
permalink: /eyetracking/
author_profile: true
---

{% include base_path %}

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