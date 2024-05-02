---
title: "High resolution landslide susceptibility mapping using ensemble machine learning and geospatial big data"
collection: publications
permalink: /publication/ILSM
date: 2023-10-01
venue: Catena
---
<b>This paper is Published in Catena</b>

![ILSM](/images/ILSM.jpg){: width="900" }  


<b>Abstract</b>  
Landslide susceptibility represents the potential of slope failure for given geo-environmental conditions. The existing landslide susceptibility maps suffer from several limitations, such as being based on limited data, heuristic methodologies, low spatial resolution, and small areas of interest. In this study, we overcome all these limitations by developing a probabilistic framework that combines imbalance handling and ensemble machine learning for landslide susceptibility mapping. We employ a combination of One -Sided Selection and Support Vector Machine Synthetic Minority Oversampling Technique (SVMSMOTE) to eliminate class imbalance and develop smaller representative data from big data for model training. A blending ensemble approach using hyperparameter tuned Artificial Neural Networks, Random Forests, and Support Vector Machine, is employed to reduce the uncertainty associated with a single model. The methodology provides the landslide susceptibility probability and a landslide susceptibility class. A thorough evaluation of the framework is performed using receiver operating characteristic curves, confusion matrices, and the derivatives of confusion matrices. This framework is used to develop India's first national-scale machine learning based landslide susceptibility map. The landslide database is carefully curated from global and local inventories, and the landslide conditioning factors are selected from a multitude of geophysical and climatological variables. The Indian Landslide Susceptibility Map (ILSM) is developed at a resolution of 0.001o (~100 m) and is classified into five classes: very low, low, medium, high, and very high. We report an accuracy of 95.73%, sensitivity of 97.08%, and matthews correlation coefficient (MCC) of 0.915 on test data, demonstrating the accuracy, robustness, and generalizability of the framework for landslide identification. The model classified 4.75% area in India as very highly susceptible to landslides and detected new landslide susceptible zones in the Eastern Ghats, hitherto unreported in the government landslide records. The ILSM is expected to aid policymaking in disaster risk reduction and developing landslide prediction models.  

[Github codebase](https://github.com/der-knight/ILSM)   
[Interactive App](https://hydrosense.users.earthengine.app/view/ml-cascade)
