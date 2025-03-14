---
title: "Re-Thinking Text Clustering for Images with Text"
collection: publications
category: conferences
permalink: /publication/19-08-2023-text_clustering
excerpt: 'Work on text clustering in Text-VQA.'
date: 2023-08-19
venue: 'International Conference on Document Analysis and Recognition (ICDAR)'
slidesurl: # ''
paperurl: 'https://link.springer.com/chapter/10.1007/978-3-031-41679-8_16'
citation: # 'Mishra, S.K., Joshi, S., Gopalakrishnan, V. (2023). Re-Thinking Text Clustering for Images with Text. In: Fink, G.A., Jain, R., Kise, K., Zanibbi, R. (eds) Document Analysis and Recognition - ICDAR 2023. ICDAR 2023. Lecture Notes in Computer Science, vol 14188. Springer, Cham. https://doi.org/10.1007/978-3-031-41679-8_16'
---

Text-VQA refers to the set of problems that reason about the text present in an image to answer specific questions regarding the image content. Previous works in text-VQA have largely followed the common strategy of feeding various input modalities (OCR, Objects, Question) to an attention-based learning framework. Such approaches treat the OCR tokens as independent entities and ignore the fact that these tokens often come correlated in an image representing a larger ‘meaningful’ entity. The ‘meaningful’ entity potentially represented by a group of OCR tokens could be primarily discerned by the layout of the text in the image along with the broader context it appears. In the proposed work, we aim to cluster the OCR tokens using a novel spatially-aware and knowledge-enabled clustering technique that uses an external knowledge graph to improve the answer prediction accuracy of the text-VQA problem. Our proposed algorithm is generic enough to be applied to any multi-modal transformer architecture used for text-VQA training. We showcase the objective and subjective effectiveness of the proposed approach by improving the performance of the M4C model on the Text-VQA datasets. 