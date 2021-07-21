---
title: 'Frequency Is All That Matters: A Hypothesis About How BERT Learn Syntactic Representations'
date: 2021-07-19

permalink: /frequency-is-all-that-matters/
tags:
  - cool posts
  - category1
  - category2
---

This post proposes a hypothesis about how BERT learn syntactic representation, mianly based on [an analysis about BERT's attention](https://nlp.stanford.edu/pubs/clark2019what.pdf). In the analysis, heads often focus on special tokens: early heads attend to \[CLS], middle heads attend to \[SEP], and deep heads attend to periods and commas. Intuitively, we hypothesize there are three rough phases of heads respectively learning three different representations: definition, dependency, and finer-grained segment. We also suppose that the difference in token frequency and constant-relation frequency make certain tokens special. For better understanding, we define them as special part of speech: \[CLS] as hunter, \[SEP] as haven, periods and commas as drifters.

Special Part of Speech
======
We first consider what makes the tokens (\[CLS], \[SEP], periods and commas, and \[MASK]) special. Firstly, high token frequency makes the learning easier and earlier. Secondly, they are outsiders of the sentence, since it is hard to find constant relations between the special tokens and the others. While other frequent tokens are insiders with simple and constant relations: for example, articles (a/an/the) are often related to immediately following word. In gereral, special tokens are frequent outsiders, which have high token frequency and low constant-relation frequency. When looking into them, we find they are like the frogs in different wells:

* \[CLS] is motivated by the Next Sentence Prediction (NSP) task to attend broadly to aggregate a representation, which makes it a global hunter: the frog is pushed to transform the well into one-way mirror to explore the wide world as an outsider.
* \[SEP] is fixed at the end of sentences like the frog in the fixed well. It is a haven for tokens that need to lie low. We will explain this in detail in phase two.
* Typical, the "sentences" refered by BERT are much longer than single sentences. Periods and commas are separetors for traditional sentences inside the "sentences". Different from \[SEP], position of loner is flexible like the frog in the moving well. Thus, we name them drifters.
* Actually, \[MASK] is also the frog in the moving well. However, it is born with a destiny: fulfill the Masked LM task. Since this mission is a gloabl concern, it will push \[MASK] to leave the well and encourage mutual relations between \[MASK] and the others. However, drifters are easily mistook for \[MASK]. Since the tokens would prefer the ones in the neighborhood, \[MASK] can only mingle with the tokens near it (drifters steal its thunder). Accidentally, this mistake helps the \[MASK] to fulfill the mission better, since relations with close tokens are exacly what it needs the most.

Phase One
======
In lower layers, some attention heads have broad attention, meawhile attention to \[CLS] is relativly higher than the others. We suppose that in order to define the usage or part of speech of current tokens, heads attend broadly to get information of other tokens. \[CLS] are more often attended, because it is a hunter: the heads attend to it for imformation about other tokens instead of the hunter itself. 

Phase Two
======
According to the analysis, \[SEP] draws over half of attention to itself in layer 6-10, which is used as a no-op for attention heads. While no single attention head perform well at syntax "overall", attention heads sepcialize to specific dependency relation (e.g., pobj, det, and dobj), especially for heads from layer 4-9. Based on these findings, we suppose that \[SEP] is used as a relation separator which separate specific relation from the others: for example, when certain heads specialize in direct object (dobj), the relation between verb and object ought to be outstanding while relations between other tokens would better not be functioning (no-op). \[SEP] provides a suitable place for these no-op tokens, since \[SEP] is hardly related to other tokens like the frog in the well: relations . With high potential, a question may be raised: why not attend to loner (periods and commas), since loner is also the frog in the well. Probably, the difference of their well is the main reason: it is easier to find the frog in the fixed well instead of the moving one. 

Phase Three
======
Naturally, deep heads will be significantly and directly impacted by the two unsupervised tasks: Masked LM and NSP. Not surprisingly, attention from \[CLS] is obviously broader than the average in last layer. Meanwhile, loners draw over half of attentiion in the last two layers. We suppose that Masked LM will motivate heads to encourage mutual relations between \[MASK] and the others. However, the deep heads will mistake loners for \[MASK], since they share the same characteristics. Possibly, the heads will learn finer-grained segment as a by-product, because it is convenient for tokens in the same part to attend to the traditional seperators (loners) close to them. Moreover, this mistake can greatly help the prediction of \[MASK]. Since loners attract lots attention from other tokens, \[MASK] will only be able to build relations with tokens close to it which is exacly the most significant part for the prediction.
