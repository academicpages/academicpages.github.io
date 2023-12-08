---
title: "Interactive Machine Learning"
excerpt: "Implementing and comparing the different Contextual Bandit Algorithms on MNIST dataset<br/><img src='/images/thumbnail_bandit.png'>"
collection: portfolio
---

The algorithms are implemented in Python and tested on the MNIST dataset. The task of predicting the correct label is solved using contextual bandit algorithms. For every image (context), the learner chooses an action among the available class labels and receives a reward 1 if the label is correct and 0 otherwise.

Many real-world tasks such as personalized recommendations, clinical trials, online advertising are well suited to be modeled as contextual bandit problems. The cost of making an incorrect decision can be very high and bandit algorithms minimize the number of examples needed to learn a good policy.

<img src="/images/thumbnail_bandit.png" width="50%"/>

[Link to the code](https://github.com/abhishekiitm/CSE_541_Interactive_Learning)