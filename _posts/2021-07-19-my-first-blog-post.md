---
title: 'A Hypothesis about Learning Curve of BERT'
date: 2021-07-19

permalink: /posts/2021/07/my-first-post/
tags:
  - cool posts
  - category1
  - category2
---

This post proposes a hypothesis about learning curve of BERT, based on [an analysis about BERT's attention](https://nlp.stanford.edu/pubs/clark2019what.pdf). As mentioned in the analysis, heads often focus on special tokens: early heads attend to \[CLS], middle heads attend to \[SEP], and deep heads attend to periods and commas. Intuitively, we hypothesize there are three rough phases of heads respectively learning three different properties: definition, dependency, and finer-grained Segment. We also suggest that through pre-training the special tokens are systematically defined as special part of speech: \[CLS] as hunter, \[SEP] as separator, periods and commas as loner.

Special Part of Speech
======
For better understanding, we first consider what makes the tokens special. Firstly, high word frequency makes the learning easier and earlier. Secondly, it is hard to relate the special tokens to the others, which makes them outsiders of the sentence. There are many other frequent tokens that are insiders: for example, articles (a/an/the) are often related to immediately following word. In gereral, special tokens are frequent outsiders. When looking into them, we find the different role of each:

* \[CLS] is motivated by the Next Sentence Prediction (NSP) task to attend broadly to aggregate a representation, which makes it a global hunter.
* \[SEP] is a sentence separator and locates at fixed position: the end of sentences. 
* Typical, the "sentences" refered by BERT are much longer than single sentences. Periods and commas are separetors for traditional sentences inside the "sentences". We name them loner for differentiation. Compared to \[SEP], position of loner is more flexible.

Phase One
======
In first phase, the early heads attend broadly to get information of other tokens, which helps define the usage or part of speech of current tokens. Attention to \[CLS] is obviously higher, probably because it is defined as a hunter (i.e., information center). 

Phase Two
======
After clarifying the definition, middle heads focus on dependency parsing. According to the analysis, \[SEP] draw over half of attention in layer 6-10, which is used as a no-op for attention heads. While no single attention head perform well at syntax "overall", attention heads sepcialize to specific dependency relation (e.g., pobj, det, and dobj), especially for heads from layer 4-9. 
