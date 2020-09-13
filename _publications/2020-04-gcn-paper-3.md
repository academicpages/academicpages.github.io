---
title: "On Incorporating Structural Information to improve Dialogue Response Generation"
collection: publications
venue: 2nd Workshop on Natural Language Processing for Conversational AI, ACL 2020. Extended abstract accepted at EurNLP 2019
permalink: /publications/2020-04-gcn-paper-3
paperurl: https://www.aclweb.org/anthology/2020.nlp4convai-1.2/
---
Authors: Nikita Moghe, Priyesh Vijayan, Balaraman Ravindran and Mitesh M. Khapra

[paper](https://www.aclweb.org/anthology/2020.nlp4convai-1.2/) [code](https://github.com/nikitacs16/horovod_gcn_pointer_generator) [slides](https://docs.google.com/presentation/d/17e6CxD226L2RBSPZnLPMiQmuxXqrjH-4rvgWoR-JIqc/edit?usp=sharing) [video](https://slideslive.com/38929628/on-incorporating-structural-information-to-improve-dialogue-response-generation)


We consider the task of generating dialogue responses from background knowledge comprising of domain specific resources. Specifically, given a conversation around a movie, the task is to generate the next response based on background knowledge about the movie such as the plot, review, Reddit comments etc. This requires capturing structural, sequential and semantic information from the conversation context and the background resources. We propose a new architecture that uses the ability of BERT to capture deep contextualized representations in conjunction with explicit structure and sequence information. More specifically, we use (i) Graph Convolutional Networks (GCNs) to capture structural information, (ii) LSTMs to capture sequential information and (iii) BERT for the deep contextualized representations that capture semantic information. We analyze the proposed architecture extensively. To this end, we propose a plug-and-play Semantics-Sequences-Structures (SSS) framework which allows us to effectively combine such linguistic information. Through a series of experiments we make some interesting observations. First, we observe that the popular adaptation of the GCN model for NLP tasks where structural information (GCNs) was added on top of sequential information (LSTMs) performs poorly on our task. This leads us to explore interesting ways of combining semantic and structural information to improve the performance. Second, we observe that while BERT already outperforms other deep contextualized representations such as ELMo, it still benefits from the additional structural information explicitly added using GCNs. This is a bit surprising given the recent claims that BERT already captures structural information. Lastly, the proposed SSS framework gives an improvement of 7.95% on BLUE score over the baseline.
 
