---
title: "Deep Learning Approaches for real-time laser absorption prediction"
excerpt: "The quantification of the amount of absorbed light is essential for understanding laser-material interactions and melt pool dynamics in order to minimize defects in additively manufactured metal components. The geometry of a vapor depression, also known as a keyhole, in melt pools formed during laser melting is closely related to laser absorptivity. This relationship has been observed by the state-of-the-art in situ high speed synchrotron x-ray visualization and integrating sphere radiometry. These two techniques create a temporally resolved dataset consisting of keyhole images and the corresponding laser absorptivity. It is then possible to use deep learning techniques to predict absorption for keyhole x-ray images, reducing dependence on costly direct experimental measurements and multi-physics modeling. <br/><img src='/images/dl_pipelines.png'>"
permalink: /research/dl-absorption/
date: 2023-01-17
collection: research
---

<div style="text-align: justify">
The quantification of the amount of absorbed light is essential for understanding laser-material interactions and melt pool dynamics in order to minimize defects in additively manufactured metal components. The geometry of a vapor depression, also known as a keyhole, in melt pools formed during laser melting is closely related to laser absorptivity. This relationship has been observed by the state-of-the-art in situ high speed synchrotron x-ray visualization and integrating sphere radiometry. These two techniques create a temporally resolved dataset consisting of keyhole images and the corresponding laser absorptivity. It is then possible to use deep learning techniques to predict absorption for keyhole x-ray images, reducing dependence on costly direct experimental measurements and multi-physics modeling.
</div>
<br/>

<figure>
    <img src='/images/exp_setup.png' class="center"> 
    <figcaption> Schematic of combined integrating sphere and high-speed synchrotron x-ray imaging setup at 32-ID-B at the Advanced Photon Source (APS) at Argonne National Laboratory. Figure was adapted from my collaborator Brian Simonds' paper entitled "The causal relationship between melt pool geometry and energy absorption measured in real time during laser-based manufacturing".
    </figcaption>
</figure>


<div style="text-align: justify"> 
In this work, we developed two pipelines for energy absorption prediction: one-stage approach and two-stage approach. The one-stage approach adopts convolutional neural networks (ConvNets) to learn feature kernels automatically via training and directly yields an absorption value for each x-ray image using the fully connected layer and regression layer. The two-stage approach first generates semantic image segmentation for keyholes, then extract the geometric keyhole features, and finally applies regression models. Motivation for the second approach is that many artificial intelligence tasks can be solved by carefully designing the right set of features to extract for the task and then feeding these features to a simple machine learning algorithm. This is especially applicable in this case, where we already have a clear understanding of which features are relevant and should be extracted. On the other hand, the main advantage of one-stage approach to the stage-stage approach is that it automatically detects the important features and make a prediction without any human supervision. It is also a more computationally efficient and straightforward process for users with little machine learning background to pick up as only one model is involved in the entire pipeline. However, the model's interpretability is less than satisfactory. 
</div>
<br/>

<figure>
    <img src='/images/dl_pipelines.png' class="center"> 
    <figcaption> Schematic of the proposed two ML pipelines to predict laser absorption for x-ray keyhole images. The one on top use CNN to extract features automatically and the one at the bottom use engineered geometric keyhole features.
    </figcaption>
</figure>


<div style="text-align: justify">
For the semantic segmentation part in the two-stage approach we created a keyhole segmentation dataset with ground truth masks from four different metallic materials and both stationary and scanning laser conditions to cover large sample space, and experimented with different segmentation models to evaluate the effectiveness to pretrained weights learned on ImageNet and to achieve automatic, robust and accurate keyhole segmentaions. We also compare the two different absorption prediction pipelines in terms of accuracy, interpretability and generalizability on unseen materials.
</div>
<br/>

<figure>
    <img src='/images/new-segmentation-inference.png' class="center"> 
    <figcaption> Segmentation results from test data on different materials and processing conditions.</figcaption>
</figure>

Reference: manuscript under preparation, stay tuned...
