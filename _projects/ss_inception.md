---
title: "Semantic Segmentation using Inception"
collection: projects
permalink: /projects/ss_inception
authors: 'Hsuan-lin Her, Ashish Farande, Prabhav Gaur'
excerpt: 'Developed an architecture inspired from UNet and Inception to segment images for Unstructured Driving Scenarios from TAS500 Dataset. The model was able to perform approx 5% better than the UNet, with 50% lesser parameters'
# date: 2009-10-01
# venue: 'Journal 1'
# paperurl: 'http://academicpages.github.io/files/ss_inception_report.pdf'
# citation: 'Hsuan-lin Her, Ashish Farande, Prabhav Gaur'
---
In this project, we perform the task of semantic segmentation on TAS500 dataset. We develop Convolutional Neural Network (CNN) so as to train and predict the segmentation masks of the images. We experiment with various CNN architectures and also several data augmentation methods that are state of the art. We also implement or own architecture named HAPNet. We then evaluate the performance of these structures using parameters such as loss, accuracy and Jaccard index (IoU). We also visualize the segmented output for the first image in the test set. An IoU accuracy of 51% was achieved with the Baseline Model. This was increased to 56% using the data augmentation and weighted loss, which address the issue of real world data. Further, a well known model for image segmentation was implemented and compared with the baseline model, which yielded approximately 56% IoU accuracy. In addition, we make use of ResNet in order to transfer the learning and train a model for our dataset, which yields a better accuracy (62% IoU). At the end, we design and present a new model which is inspired from the models which performed better at ImageNet and our understanding of different Models. This model was able to yield 63% validation IoU accuracy.

[Download report here](/files/ss_inception_report.pdf)

<!-- Recommended citation: Your Name, You. (2009). "Paper Title Number 1." <i>Journal 1</i>. 1(1). -->