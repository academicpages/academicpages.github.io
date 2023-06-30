---
title: "Augmented SBERT: Data Augmentation Method for Improving Bi-Encoders for Pairwise Sentence Scoring Tasks"
collection: publications
permalink: /publication/2021-04-12-augsbert-naacl
excerpt: 'A simple yet efficient data augmentation strategy using the cross-encoder to label training data for training the bi-encoder for pairwise sentence scoring tasks.'
date: 2021-04-12
venue: 'Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)'
paperurl: 'https://aclanthology.org/2021.naacl-main.28/'
citation: ''
authors: '<strong> Nandan Thakur </strong>, Nils Reimers, Johannes Daxenberger, Iryna Gurevych'
image: 'images/augbsert.png'
code: 'https://www.sbert.net/examples/training/data_augmentation/README.html'
---


Recommended citation:
```
@inproceedings{thakur-etal-2021-augmented,
    title = "Augmented {SBERT}: Data Augmentation Method for Improving Bi-Encoders for Pairwise Sentence Scoring Tasks",
    author = "Thakur, Nandan  and
      Reimers, Nils  and
      Daxenberger, Johannes  and
      Gurevych, Iryna",
    booktitle = "Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.naacl-main.28",
    doi = "10.18653/v1/2021.naacl-main.28",
    pages = "296--310",
    abstract = "There are two approaches for pairwise sentence scoring: Cross-encoders, which perform full-attention over the input pair, and Bi-encoders, which map each input independently to a dense vector space. While cross-encoders often achieve higher performance, they are too slow for many practical use cases. Bi-encoders, on the other hand, require substantial training data and fine-tuning over the target task to achieve competitive performance. We present a simple yet efficient data augmentation strategy called Augmented SBERT, where we use the cross-encoder to label a larger set of input pairs to augment the training data for the bi-encoder. We show that, in this process, selecting the sentence pairs is non-trivial and crucial for the success of the method. We evaluate our approach on multiple tasks (in-domain) as well as on a domain adaptation task. Augmented SBERT achieves an improvement of up to 6 points for in-domain and of up to 37 points for domain adaptation tasks compared to the original bi-encoder performance.",
}
```