---
title: "Code Defect Detection using Pre-trained Language Models with Encoder-Decoder via Line-Level Defect Localization"
collection: publications
permalink: /publication/2024-05-22-Code-Defect-Detection-using-Pre-trained-Language-Models-with-Encoder-Decoder-via-Line-Level-Defect-Localization
date: 2024-05-22
venue: 'LREC-Coling'
---

[paper](http://academicpages.github.io/files/paper1.pdf)

### Abstract
Recently, code Pre-trained Language Models (PLMs) trained on large amounts of code and comment, have shown great success in code defect detection tasks. However, most PLMs simply treated the code as a single sequence and only used the encoder of PLMs to determine if there exist defects in the entire code. For a more analyzable and explainable approach, it is crucial to identify which lines contain defects. In this paper, we propose a novel method for code defect detection that integrates line-level defect localization into a unified training process. To identify code defects at the line-level, we convert the code into a sequence separated by lines using a special token. Then, to utilize the characteristic that both the encoder and decoder of PLMs process information differently, we leverage both the encoder and decoder for line-level defect localization. By learning code defect detection and line-level defect localization tasks in a unified manner, our proposed method promotes knowledge sharing between the two tasks. We demonstrate that our proposed method significantly improves performance on four benchmark datasets for code defect detection. Additionally, we show that our method can be easily integrated with ChatGPT.
