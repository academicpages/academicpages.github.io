---
title: "Black-grass Detection with Deep Neural Networks"
<!-- excerpt: "<img src='/images/blackgrass.jpg'>" -->
collection: projects
---

### Introduction
<img src='/images/blackgrass.jpg'>
Blackgrass is a native annual grass weed that can be found all over the United Kingdom, but is most widespread in the cereal-growing areas of southern and eastern England. Blackgrass has become a major headache for many farmers due to its prevalence over autumn-sown arable crops and herbicide resistance. 
The aim of the project is to develop a computer vision-based weed detection system that can reliably detect blackgrass in cereal crops. 

To accomplish this, I have used two machine learning tools so far: Generative Adversarial Networks (GANs) and Convolutional Neural Networks (CNNs). CNNs are well-known image recognition systems that have demonstrated outstanding performance in a variety of applications. 
However, CNNs require large datasets to train, and collecting such a dataset for each field is not practical. To meet this challenge, I trained a [StyleGAN model](https://arxiv.org/abs/1912.04958), which generates synthetic images based on factors, such as growth stage and soil type. 

For further information regarding the project, please refer to this link: [Blackgrass Project](https://agrifoodtech.blogs.lincoln.ac.uk/2020/12/16/black-grass-detection-project/)

### Synthetic Data Generation
Based on the authors' [GitHub repo](https://github.com/NVlabs/stylegan2), I trained a StyleGAN model with our dataset which is collected from cereal fields across the UK. The dataset consists of five channels: red, green, blue, near-infrared, red-edge. Also, each pixel is represented by 16 bits. As a pre-processing step, I combined red, green and near-infrared channels and normalized the pixel values.

The generated synthetic images for the dense blackgrass class are as follows:![!](/images/fakes000481.jpeg)

I trained the network with four Nvidia P100 GPUs for 36 hours to obtain these results. As the original dataset hasn't been published yet, I can only share here some samples of synthetic images. As can be seen from the image, the model performs poorly in the generation of soil texture and high frequency components, such as bushes.

### Binary Classification
The main objective of this project is to detect blackgrass in the field images. Hence, as the next step, I trained a binary classifier with two classes: dense blackgrass and no blackgrass. The dataset consists of four classes, dense, medium, sparse, and no blackgrass, with the class imbalance in favor of no blackgrass. Therefore, I combined medium and dense blackgrass classes and fine-tuned a ResNet50 model. The numbers of training, validation, and test images per class are: 1730, 494, 247.

The tutorial I followed for fine-tuning and transfer learning: [Tensorflow - Transfer learning](https://www.tensorflow.org/tutorials/images/transfer_learning)\
Also, an interesting paper regarding transfer learning: [How transferable are features in deep neural
networks?](https://arxiv.org/pdf/1411.1792.pdf)

Some preliminary results are as follows: 

![!](/images/results_bs_32_img_512_fig2_fine.png)


Also, some metric results for the test dataset:

Confusion matrix: [[206  41], [ 58 189]]

              precision    recall  f1-score   support

     class 0       0.78      0.83      0.81       247
     class 1       0.82      0.77      0.79       247
    accuracy                           0.80       494
