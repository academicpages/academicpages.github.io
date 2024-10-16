---
title: "How redundant is the Transformer stack in speech representation models?"
collection: papers/workshops
permalink: /papers/workshops/redundancy
excerpt: ""
date: 2024-12-14
venue: 'Workshop on Efficient Natural Language and Speech Processing (ENLSP) @ NeurIPS, Vancouver, Canada'
# paperurl: 'https://arxiv.org/pdf/2409.16302'
# citation: ' Jacobsen, Albert Kjøller; Højbjerg, Phillip Chavarria; Jacobsen, Aron Djurhuus. (2022). &quot;Visual Question Answering with Knowledge-based Semantics.&quot; <i>DTU Department of Applied Mathematics and Computer Science </i>.'
---

Abstract 
======
Self-supervised speech representation models, particularly those leveraging transformer architectures, have demonstrated remarkable performance on downstream tasks. Recent studies revealed high redundancy of transformer layers, potentially allowing for smaller models and more efficient inference. We perform a detailed analysis of layer similarity in speech models, leveraging three similarity metrics. Our findings reveal a block-like structure of high similarity, suggesting significant redundancy within the blocks along with two main processing steps that are both found to be critical for maintaining performance. We demonstrate the effectiveness of pruning transformer-based speech models without post-training, achieving up to 40% reduction in transformer layers while maintaining 95% of the model’s predictive capacity. Lastly, we show that replacing the transformer stack with a few simple layers can reduce the network size by up to 95% and inference time by up to 87%, significantly reducing the computational footprint with minimal performance loss, revealing the benefits of model simplification for downstream applications.