---
title: "S-NLP at SemEval-2021 Task 5: An Analysis of Dual Networks for Sequence Tagging"
collection: publications
permalink: /publication/semeval-2021
excerpt: 'In this paper, we propose a system to resolve the task 5 in The 15th International Workshop on Semantic Evaluation (SemEva 2021): Toxic Spans Detection. Our method utilizes a pre-trained language model in toxic-domain and combines two approaches Self-training and Feature-based Learning to achieve a high F1-score of 70.77. Finally, we provide insights into the failure of the system and the task’s potential falsely-negative annotations issue with careful error analysis.'
date: 2021-03-31
venue: 'The 15th International Workshop on Semantic Evaluation (SemEval 2021)'
paperurl: 'https://aclanthology.org/2021.semeval-1.120/'
citation: '@inproceedings{nguyen-etal-2021-nlp,
    title = "{S}-{NLP} at {S}em{E}val-2021 Task 5: An Analysis of Dual Networks for Sequence Tagging",
    author = "Nguyen, Viet Anh  and
      Nguyen, Tam Minh  and
      Quang Dao, Huy  and
      Huu Pham, Quang",
    booktitle = "Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.semeval-1.120",
    doi = "10.18653/v1/2021.semeval-1.120",
    pages = "888--897",
}'
---
Abstract
======
The SemEval 2021 task 5: Toxic Spans Detection is a task of identifying considered-toxic spans in text, which provides a valuable, automatic tool for moderating online contents. This paper represents the second-place method for the task, an ensemble of two approaches. While one approach relies on combining different embedding methods to extract diverse semantic and syntactic representations of words in context; the other utilizes extra data with a slightly customized Self-training, a semi-supervised learning technique, for sequence tagging problems. Both of our architectures take advantage of a strong language model, which was fine-tuned on a toxic classification task. Although experimental evidence indicates higher effectiveness of the first approach than the second one, combining them leads to our best results of 70.77 F1-score on the test dataset.

Citation
======
> @inproceedings{nguyen-etal-2021-nlp,
    title = "{S}-{NLP} at {S}em{E}val-2021 Task 5: An Analysis of Dual Networks for Sequence Tagging",
    author = "Nguyen, Viet Anh  and
      Nguyen, Tam Minh  and
      Quang Dao, Huy  and
      Huu Pham, Quang",
    booktitle = "Proceedings of the 15th International Workshop on Semantic Evaluation (SemEval-2021)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.semeval-1.120",
    doi = "10.18653/v1/2021.semeval-1.120",
    pages = "888--897",
}