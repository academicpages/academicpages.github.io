---
title: "Knowledge Graph Entity Alignment with Graph Convolutional Networks: Lessons Learned"
collection: publications
authors: 'M. Berrendorf, E. Faerman, V. Melnychuk, V. Tresp, T. Seidl'
date: 2020-04-14
excerpt: "![GCN-align](/images/GCN-align.png){: style='float: left; width: 350px'} We focus on the problem of entity alignment in Knowledge Graphs (KG) and report on our experiences when applying a Graph Convolutional Network (GCN) based model for this task. Despite serious efforts, we were not able to fully reproduce the results from the original GCN-Align paper."
venue: 'European Conference on Information Retrieval'
paperurl: 'https://arxiv.org/abs/1911.08342'
---

In this work, we focus on the problem of entity alignment in Knowledge Graphs (KG) and we report on our experiences when applying a Graph Convolutional Network (GCN) based model for this task. Variants of GCN are used in multiple state-of-the-art approaches and therefore it is important to understand the specifics and limitations of GCN-based models. Despite serious efforts, we were not able to fully reproduce the results from the original paper and after a thorough audit of the code provided by authors, we concluded, that their implementation is different from the architecture described in the paper. In addition, several tricks are required to make the model work and some of them are not very intuitive. We provide an extensive ablation study to quantify the effects these tricks and changes of architecture have on final performance. Furthermore, we examine current evaluation approaches and systematize available benchmark datasets. We believe that people interested in KG matching might profit from our work, as well as novices entering the field. [Code](https://github.com/Valentyn1997/kg-alignment-lessons-learned).