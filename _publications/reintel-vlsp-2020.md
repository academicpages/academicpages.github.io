---
title: "Exploiting Transfer Learning Models for Reliable Intelligence Identification on Vietnamese Social Network Sites"
collection: publications
permalink: /publication/reintel-vlsp-2020
excerpt: 'The rapid growth of social media and misinformation posed challenges for authorities. As a result, determining the reliability of an article has become a crucial task. After various ablation studies, we propose a multi-input model that can effectively leverage both tabular metadata and post content for the task. Applying state-of-the-art fine-tuning techniques for the pre-trained component and training strategies for our complete model, we have achieved a 0.9462 ROC-score on the VLSP private test set.'
date: 2021-04-09
venue: 'The 7th International Workshop on Vietnamese Language and Speech Processing'
paperurl: 'https://aclanthology.org/2020.vlsp-1.9/'
citation: '@inproceedings{thanh-van-2020-reintel,
    title = "{R}e{INTEL} Challenge 2020: Exploiting Transfer Learning Models for Reliable Intelligence Identification on {V}ietnamese Social Network Sites",
    author = "Thanh, Kim Nguyen Thi  and
      Van, Kiet Nguyen",
    booktitle = "Proceedings of the 7th International Workshop on Vietnamese Language and Speech Processing",
    month = dec,
    year = "2020",
    address = "Hanoi, Vietnam",
    publisher = "Association for Computational Lingustics",
    url = "https://aclanthology.org/2020.vlsp-1.9",
    pages = "45--48",
}'
---
Abstract
======
This paper presents the system that we propose for the Reliable Intelligence Identification on Vietnamese Social Network Sites (ReINTEL) task of the Vietnamese Language and Speech Processing 2020 (VLSP 2020) Shared Task. In this task, the VLSP 2020 provides a dataset with approximately 6,000 training news/posts annotated with reliable or unreliable labels, and a test set consists of 2,000 examples without labels. In this paper, we conduct experiments on different transfer learning models, which are bert4news and PhoBERT fine-tuned to predict whether the news is reliable or not. In our experiments, we achieve the AUC score of 94.52% on the private test set from ReINTEL’s organizers.

Citation
======
> @inproceedings{thanh-van-2020-reintel,
    title = "{R}e{INTEL} Challenge 2020: Exploiting Transfer Learning Models for Reliable Intelligence Identification on {V}ietnamese Social Network Sites",
    author = "Thanh, Kim Nguyen Thi  and
      Van, Kiet Nguyen",
    booktitle = "Proceedings of the 7th International Workshop on Vietnamese Language and Speech Processing",
    month = dec,
    year = "2020",
    address = "Hanoi, Vietnam",
    publisher = "Association for Computational Lingustics",
    url = "https://aclanthology.org/2020.vlsp-1.9",
    pages = "45--48",
}
