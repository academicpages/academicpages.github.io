---
title: 'Frequency Is All That Matters: A Hypothesis About How BERT Learn Syntactic Representations'
date: 2021-07-19

permalink: /frequency-is-all-that-matters/
tags:
  - cool posts
  - category1
  - category2
---

This post proposes a hypothesis about how BERT learn syntactic representation, mianly based on [an analysis about BERT's attention](https://nlp.stanford.edu/pubs/clark2019what.pdf). In the analysis, heads often focus on special tokens: early heads attend to \[CLS], middle heads attend to \[SEP], and deep heads attend to periods and commas. Intuitively, we hypothesize there are three rough phases of heads respectively learning three different representations: definition, dependency, and finer-grained segment. We also suppose that the difference in token frequency and constant-relation frequency make certain tokens special. For better understanding, we define them as special part of speech: \[CLS] as hunter; \[SEP] as haven; periods, commas, and \[MASK] as drifter.

Special Part of Speech
======
We first consider what makes the tokens (\[CLS], \[SEP], periods and commas, and \[MASK]) special. Firstly, high token frequency makes the learning easier and earlier. Secondly, they are outsiders of the sentence, since they hardly have constant relations with other tokens. While other frequent tokens are insiders with simple and constant relations: for example, articles (a/an/the) are often related to immediately following word. In gereral, special tokens are frequent outsiders, which have high token frequency and low constant-relation frequency. When looking into them, we find they are like the frogs in the wells with different destinies:

* \[CLS] is the frog in the well with a destiny to fulfill the Next Sentence Prediction (NSP) task. Thus it is motivated to attend broadly to aggregate a representation, which makes it a global hunter: the frog is pushed to transform the well into one-way mirror to explore the wide world as an outsider.
* \[SEP] is fixed at the end of sentences like the frog in the fixed well. It is a haven for tokens that need to lie low. We will explain this in detail in phase two.
* Typical, the "sentences" refered by BERT are much longer than single sentences. Periods and commas are separetors for traditional sentences inside the "sentences". Different from \[SEP], position of loner is flexible like the frog in the moving well. Their part of speech is drifter, because they are always moving and seldom have constant relations with other tokens.
* \[MASK] is born with a destiny: fulfilling the Masked LM task. Actually, part of speech of \[MASK] is also drifter, because it shares the same charactristics with periods and commas (high token frequency, low constant-relation frequency, and flexible position). In BERT's view, it is the randomly selected drifter (\[MASK]) that is resiponsible for Masked LM task. Details will be shown in phase three.


Phase One
======
In lower layers, some attention heads have broad attention, meawhile attention to \[CLS] is relativly higher than the others. We suppose that in order to define the usage or part of speech of current tokens, heads attend broadly to get information of other tokens. \[CLS] are more often attended, because it is a hunter. The heads attend to it for imformation about other tokens instead of the hunter itself. 

Phase Two
======
According to the analysis, \[SEP] draws over half of attention to itself in layer 6-10, which is used as a no-op for attention heads. While no single attention head perform well at syntax "overall", attention heads sepcialize to specific dependency relation (e.g., pobj, det, and dobj), especially for heads from layer 4-9. Moreover, it is often the case that the dependent attend to head word rather than the other way around. Based on these findings, we suppose that when attention heads specialize in specific relation, the specific tokens ought to be highlighted while other tokens would better not be functioning (lying low). In order to lie low, the tokens need to avoid being related to the specific tokens as much as possible. Thus, \[SEP] becomes a perfect haven as the frog in the well. Take dobj relation, tokens in direct object attend to their verb, while other tokens mostly attend to \[SEP].  A question may be raised: why not attend to the drifter, since it is also the frog in the well. Probably, the difference of their well is the main reason: it is easier to find the frog in the fixed well instead of the moving one. 

Phase Three
======
Naturally, deep heads will be significantly and directly impacted by the two unsupervised tasks: Masked LM and NSP. Not surprisingly, attention from \[CLS] is obviously broader than the average in last layer. Meanwhile, periods and commas draw over half of attentiion in the last two layers. We suppose that it is hard to differentiate \[MASK], periods, and commas. Attention heads will treat them the same. Thus, Masked LM will motivate mutual relations between all the drifters and the other tokens. Since the tokens prefer the drifters (most of them are periods and commas) in the neighborhood, the heads will possibly learn finer-grained segment as a by-product. Moreover, attention to periods and commas can greatly help the prediction of \[MASK]. Since periods and commas attract lots of attentions from other tokens, \[MASK] will be more likely to have relations with tokens close to it, which is exactly the most significant part for prediction.
