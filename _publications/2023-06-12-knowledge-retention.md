---
title: "The Effect of Masking Strategies on Knowledge Retention by Language Models"
collection: publications
permalink: /publications/2023-06-12-knowledge-retention.md
excerpt: 'We investigate the ability to retain factual information from different pre-training strategies.'
date: 2023-06-12
venue: 'arxiv'
paperurl: 'https://arxiv.org/abs/2306.07185'
citation: 'Wallat, J., Zhang, T., & Anand, A. (2023). The Effect of Masking Strategies on Knowledge Retention by Language Models. ArXiv, abs/2306.07185.'
---
Language models retain a significant amount of world knowledge from their pre-training stage. This allows knowledgeable models to be applied to knowledge-intensive tasks prevalent in information retrieval, such as ranking or question answering. Understanding how and which factual information is acquired by our models is necessary to build responsible models. However, limited work has been done to understand the effect of pre-training tasks on the amount of knowledge captured and forgotten by language models during pre-training. Building a better understanding of knowledge acquisition is the goal of this paper. Therefore, we utilize a selection of pre-training tasks to infuse knowledge into our model. In the following steps, we test the model's knowledge retention by measuring its ability to answer factual questions. Our experiments show that masking entities and principled masking of correlated spans based on pointwise mutual information lead to more factual knowledge being retained than masking random tokens. Our findings demonstrate that, like the ability to perform a task, the (factual) knowledge acquired from being trained on that task is forgotten when a model is trained to perform another task (catastrophic forgetting) and how to prevent this phenomenon. To foster reproducibility, the code, as well as the data used in this paper, are openly available (https://github.com/jwallat/knowledge-acquisition).



Recommended citation: Wallat, J., Zhang, T., & Anand, A. (2023). The Effect of Masking Strategies on Knowledge Retention by Language Models. ArXiv, abs/2306.07185.