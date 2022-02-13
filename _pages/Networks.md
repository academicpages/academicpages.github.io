---
permalink: /networks/
title: "Networks"
author_profile: true
---

<p float="middle">
    <video autoplay="autoplay" src="../images/NetworksFast.mp4" controls="controls" width="100%" />
</p>


## Overview
We design a real-time dense local semantic mapping algorithm, MotionSC as a benchmark of semantic scene completion on the CarlaSC dataset. Besides, we also run the state-of-the-art semantic scene completion solutions such as SSCNet, SSCNet-Full, LMSCNet and JS3CNet. You can find our implementation of SSCNet, SSCNet-Full and LMSCNet on the [3DMapping repository](https://github.com/UMich-CURLY/3DMapping). Our implementation of [JS3CNet](https://github.com/yanx27/JS3C-Net) can be found on our [forked JS3CNet](https://github.com/Song-Jingyu/JS3C-Net). The video of running the four different models are shown above. We will also include the introduction on MotionSC and some training logs in this page.

## MotionSC
![MotionSC-structure](../images/MotionSC.png)
Proposed MotionSC network. A Spatio-Temporal Pooling Network backbone performs SSC using temporal information in real-time. The shrinking dimension of the rectangular prism indicates the temporal axis being squeezed from size T to size 1 through max pooling in the temporal pooling (TP) layer. Consecutive occupancy grids are maintained in a temporal stack, so there is no additional computational overhead from maintaining additional data across time. 

The MotionSC network achieved both accurate and real-time performance compared with other state-of-the-art algorithms. More details can be found in the figure below and in our paper.
![acc-latency](../images/accuracy_latency.png)

## Training Logs
We also use the [TensorBoard](https://www.tensorflow.org/tensorboard) to record the training process. You can check how to use the TensorBoard [here](https://pytorch.org/tutorials/recipes/recipes/tensorboard_with_pytorch.html). You can access and download the logs [here](https://drive.google.com/drive/folders/1GglMWcAe4r7-BjsIRVWikl5xA0GjyLqz?usp=sharing). To illustrate, `MotionSC_11` is the training log of MotionSC model using reduced-label setting. And `MotionSC_23` is the training log using all-label setting.

<!-- ## Visualization -->
