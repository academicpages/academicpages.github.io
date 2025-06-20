---
title: 'Question Condensing Networks for Answer Selection in Community Question Answering'
collection: publications
category: conferences
permalink: /publication/2018-07-15-question-condensing-networks
excerpt: 'This paper introduces Question Condensing Networks (QCN), a model that leverages the subject-body structure of community questions for improved answer selection.'
date: 2018-07-15
venue: 'Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL)'
paperurl: 'http://pku-wuwei.github.io/files/QCN.pdf'
citation: 'Wei Wu, Xu Sun, Houfeng Wang. Question Condensing Networks for Answer Selection in Community Question Answering. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (ACL), 2018.'
---
QCN tackles the challenge of redundancy and noise in community question answering (CQA) by recognizing the distinction between the question subject and body. Instead of concatenating them, QCN treats the subject as the primary representation and uses orthogonal decomposition to aggregate complementary information from the body based on similarity and disparity with the subject. It further aligns question-answer pairs using multi-dimensional attention to better capture semantic interactions. Experiments on two SemEval datasets demonstrate that QCN significantly outperforms prior models, setting a new state-of-the-art for CQA answer selection.