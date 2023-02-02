---
title: "Knowledge Graph Entity Alignment with Graph Convolutional Networks: Lessons Learned"
collection: publications
authors: 'M. Berrendorf, E. Faerman, <b>V. Melnychuk</b>, V. Tresp, T. Seidl'
date: 2020-04-14
excerpt: "![GCN-align](/images/GCN-align.png){: style='float: left; height: 100px'}"
arxiv: 'https://arxiv.org/abs/1911.08342'
paperurl: 'https://www.dbs.ifi.lmu.de/~tresp/papers/978-3-030-45442-5_Chapter_1.pdf'
code: 'https://github.com/Valentyn1997/kg-alignment-lessons-learned'
---

In this work, we focus on the problem of entity alignment in Knowledge Graphs (KG) and we report on our experiences when applying a Graph Convolutional Network (GCN) based model for this task. Variants of GCN are used in multiple state-of-the-art approaches and therefore it is important to understand the specifics and limitations of GCN-based models. Despite serious efforts, we were not able to fully reproduce the results from the original paper and after a thorough audit of the code provided by authors, we concluded, that their implementation is different from the architecture described in the paper. In addition, several tricks are required to make the model work and some of them are not very intuitive. We provide an extensive ablation study to quantify the effects these tricks and changes of architecture have on final performance. Furthermore, we examine current evaluation approaches and systematize available benchmark datasets. We believe that people interested in KG matching might profit from our work, as well as novices entering the field.

Recommended citation: 
```bibtex
@inproceedings{berrendorf2020knowledge,
  title={Knowledge graph entity alignment with graph convolutional networks: lessons learned},
  author={Berrendorf, Max and Faerman, Evgeniy and Melnychuk, Valentyn and Tresp, Volker and Seidl, Thomas},
  booktitle={European Conference on Information Retrieval},
  year={2020}
}
```
