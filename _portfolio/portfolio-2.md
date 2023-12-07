---
title: "Distributed Training using PyTorch"
excerpt: "Training a multiclass classifier on MNIST across multiple GCP instances using PyTorch's DistributedDataParallel module<br/><img src='/images/thumbnail_spark.jpg'>"
collection: portfolio
---

# CSE D 514 Project - Distributed Training using PyTorch

In this project, we
- Investigated different functionalities of PyTorch
- Performed NN training on single machine
- Performed NN training on multiple machines (Distributed Training)
- Did performance comparison of single vs multiple machines

## Dataset used
MNIST dataset was used for this project.  

<img src="../images/train_images.png" width="50%"/>

## GCP and PyTorch setup
Please refer to [this document](GCP_PyTorch_setup.pdf) to set up the environment.

## Results

<img src="../images/loss_curve.png" width="50%"/>
<img src="../images/Time%20to%20train%20(1%20epoch)%20vs.%20Number%20of%20machines.png" width="50%"/>

Link to [the code is here](https://github.com/abhishekiitm/CSED_514_Project_Distributed_Training_using_PyTorch).