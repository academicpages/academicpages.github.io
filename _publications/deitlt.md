---
title: "DeiT-LT: Distillation Strikes Back for Vision Transformer Training on Long-Tailed Datasets"
collection: publications
category: manuscripts
permalink: /publication/deitlt
# excerpt: ''
date: 2024-10-01
venue: 'Computer Vision and Patter Recognition'
authors: 'Harsh Rangwani, Pradipto Mondal, Mayank Mishra, Ashish Ramayee Asokan, and R Venkatesh Babu.'
# slidesurl: 'http://academicpages.github.io/files/slides1.pdf'
paperurl: 'https://openaccess.thecvf.com/content/CVPR2024/papers/Rangwani_DeiT-LT_Distillation_Strikes_Back_for_Vision_Transformer_Training_on_Long-Tailed_CVPR_2024_paper.pdf'
code: 'https://github.com/val-iisc/DeiT-LT'
site: 'https://rangwani-harsh.github.io/DeiT-LT/'
---

Vision Transformer (ViT) has emerged as a prominent architecture for various computer vision tasks. In ViT, we divide the input image into patch tokens and process them through a stack of self-attention blocks. However, unlike Convolutional Neural Network (CNN), ViT’s simple architecture has no informative inductive bias (e.g., locality, etc.). Due to this, ViT requires a large amount of data for pre-training. Various data-efficient approaches (DeiT) have been proposed to train ViT on balanced datasets effectively. However, limited literature discusses the use of ViT for datasets with long-tailed imbalances. In this work, we introduce DeiT-LT to tackle the problem of training ViTs from scratch on longtailed datasets. In DeiT-LT, we introduce an efficient and effective way of distillation from CNN via distillation DIST
token by using out-of-distribution images and re-weighting the distillation loss to enhance focus on tail classes. This leads to the learning of local CNN-like features in early ViT blocks, improving generalization for tail classes. Further, to mitigate overfitting, we propose distilling from a flat CNN teacher, which leads to learning low-rank generalizable features for DIST tokens across all ViT blocks. With the proposed DeiT-LT scheme, the distillation DIST token becomes an expert on the tail classes, and the classifier CLS token becomes an expert on the head classes. The experts help to
effectively learn features corresponding to both the majority and minority classes using a distinct set of tokens within the same ViT architecture. We show the effectiveness of DeiT-LT for training ViT from scratch on datasets ranging from smallscale CIFAR-10 LT to large-scale iNaturalist-2018.

