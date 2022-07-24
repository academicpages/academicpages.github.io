---
title: "Point cloud segmentation for improving annotation efficiency"
excerpt: "Point cloud semantic segmentation neural network models for improving annotation efficiency
<br/><img src='/images/semantic segmentation.jpg'>"
collection: portfolio
---


Currently I am working on improving annotation efficiency in the Deepen AI platform. We are developing Deep Learning models for semantic segmentation, object detection, and object tracking in 2D and 3D datasets. Developing AI models to improve annotation poses a unique challenge. When majority of Deep Learning models focuses on metrics like accuracy, mean Intersection over Union (mIoU), mean Average Precision (mAP) etc., they do not directly translate to annotation efficiency. For example, consider 2 models for 2D bounding box detection for cars. One model has an mIOU of 80% and the other has 90%. On first glance, the latter model should be better. However, when used as a precursor to labelling, we need to dive deeper. 

A simple metric to represent annotation efficiency, is time taken by a labeller to annotate a dataset. When using an AI model to boost efficiency, it boils down to the time taken by the labeller to edit/correct the model's predictions. So, even if a model scores lower on a conventional metric (like mIoU), if its predictions are easier to correct to achieve close to ground truth quality, then it is considered a better model. This class of models can be called Off-Board AI models for Annotation.

One way to see if the predictions are easier to correct is to look at the error distribution. Suppose there are a 1000 cars in the dataset. The model with 90% mIoU has a 10% error. If that error is spread across all the 1000 cars in the dataset, then the labeller would have to correct each and every car in the dataset, as annotation needs to achieve ground truth quality. This is a very inefficient process, inspite of the model giving 90% mIoU. On the other hand, if the error for the 80% model is more concentrated in a few cars, then the labeller would need to correct the error only in a few cars, and the rest can be left untouched. This makes the 80% model better than the 90% model for this annotation task.

So I am trying to improve the efficiency of annotation by using off-board AI models.