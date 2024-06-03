---
title: "DATA INCREMENTAL LEARNING IN DEEP ARCHITECTURES"
collection: publications
permalink: /publication/2022-09-01-continual-ssl
excerpt: 'This paper is about self supervised learning model as continual learners'
date: 2022-09-01
venue: '-'
slidesurl: 'https://drive.google.com/file/d/1rjVr4SDBvtEyMtcAR5rX2qq-036I3gAh/view?usp=sharing'
paperurl: 'https://drive.google.com/file/d/1rjVr4SDBvtEyMtcAR5rX2qq-036I3gAh/view?usp=sharing'
citation: 'Alex Kameni, 2022'
---
Without relying on human annotations, self-supervised learning aims to learn useful representations of input data. When trained offline with enormous amounts of unlabelled data, self-supervised models have been found to provide visual representations that are equivalent to or better than supervised models. However, in continual learning (CL) circumstances, when data is fed to the model sequentially, its efficacy is drastically diminished. Numerous ongoing learning techniques have recently been presented for a variety of computer vision problems. In this study, by utilizing distillation and proofreading, we tackle the extremely challenging problem of continuously learning a usable representation in which input data arrives sequentially. We can prevent severe forgetfulness and continue to train our models by adding a prediction layer that forces the current representations vectors to precisely match the frozen learned representations and an effective selection memory for proofreading previous data. This makes it possible for us to design a framework for continual self-supervised learning of visual representations that (i) greatly enhances the quality of the learned representations, (ii) is suitable for a number of state-of-art self-supervised objectives, and (iii) requires little to no hyperparameter tuning. The code of this paper is made available here [cssl-dsdm](https://github.com/ensea-internship-2022/cassle-dsdm)
