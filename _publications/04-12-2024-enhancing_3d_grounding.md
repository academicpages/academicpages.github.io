---
title: "Enhancing 3D Referential Grounding by Learning Coarse Spatial Relationships"
collection: publications
category: conferences
permalink: /publication/04-12-2024-enhancing_3d_grounding
excerpt: 'Work on pre-training 3D Referential Grounding Models.'
date: 2024-12-04
venue: 'International Conference on Pattern Recognition (ICPR)'
paperurl: 'https://link.springer.com/chapter/10.1007/978-3-031-78113-1_28'
citation: # 'Your Name, You. (2024). &quot;Paper Title Number 3.&quot; <i>GitHub Journal of Bugs</i>. 1(3).'
---

Large-scale pre-training is commonly used in 2D referential grounding tasks owing to the easy availability of a large number of image-text pairs with corresponding bounding box annotations. However, for 3D referential grounding, the unavailability of high-quality 3D scene-text pairs with annotations poses a significant challenge. To address this issue, we leverage the large corpus of 3D scenes with bounding box annotations of object instances and design an automated strategy to synthesize scene-text data for pre-training by utilising the coarse spatial relationships between the objects in the scene without any human supervision. The proposed strategy first clusters the 3D bounding boxes and then uses these clusters to create pairwise and triplet relations between the objects in the 3D scene. We achieved improved results consistently across various top-performing methods in 3D referential grounding, when the proposed pre-training strategy is deployed. In addition to pre-training with the samples containing coarse spatial relations, we also encode semantic relationships between the bounding boxes conditioned on the language utterance, using a compatibility measure between the box features and the language utterance. To evaluate the performance of our proposed techniques, we conduct experiments on large-scale publicly available datasets, namely ScanRefer and ReferIt3D (SR3D and NR3D). Our proposed techniques can be seamlessly integrated with any off-the-shelf 3D referential grounding method. Specifically, when integrated with BUTD-DETR, we observed notable improvements of 2.2% and 1% in performance on the SR3D and NR3D datasets, respectively.
