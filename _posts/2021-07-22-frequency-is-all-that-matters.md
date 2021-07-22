---
title: 'Frequency Is All That Matters: A Hypothesis About How BERT Learn Syntactic Representations'
date: 2021-07-19

permalink: /frequency-is-all-that-matters/

---

This post proposes a hypothesis about how BERT learns syntactic representation, mainly based on an analysis about BERT's attention ([Clark et al., 2019](https://nlp.stanford.edu/pubs/clark2019what.pdf)). In the analysis, heads often focus on special tokens: early heads attend to \[CLS], middle heads attend to \[SEP], and deep heads attend to periods and commas, as shown in the figure  below ([Clark et al., 2019](https://nlp.stanford.edu/pubs/clark2019what.pdf)). Intuitively, we hypothesize there are three rough phases of heads respectively learn three different representations: definition, dependency, and finer-grained segment. We also suppose that the difference in token frequency and constant-relation frequency make certain tokens special. For better understanding, we define them as special parts of speech: \[CLS] as a hunter; \[SEP] as a haven; periods, commas, and \[MASK] as drifters.

<img src="https://gjwubyron.github.io/images/attention.JPG"/ width=400px height=300px>

Special Parts of Speech
======
We first consider what makes the tokens (\[CLS], \[SEP], periods and commas, and \[MASK]) special. Firstly, high token frequency makes learning easier and earlier: attention heads gain more experience with them. Secondly, they are outsiders of the sentence, since they hardly have constant relations with other tokens. While other frequent tokens are insiders with simple and constant relations. For example, articles (a/an/the) are often related to the immediately following word. In general, special tokens are frequent outsiders, which have high token frequency and low constant-relation frequency. When looking into them, we find they are outsiders with different destinies:

* \[CLS] is born with a destiny to fulfill the Next Sentence Prediction (NSP) task. It is motivated to attend broadly to aggregate a representation, which makes it a global hunter. 
* \[SEP] is fixed at the end of sentences: the outsider stay in the fixed position. It is a haven for tokens that need to lie low. We will explain this in detail in phase two.
* Typical, the "sentences" referred to by BERT are much longer than single sentences. Periods and commas are separators for traditional sentences inside the "sentences". Different from \[SEP], their positions are flexible: the outsiders are always moving. Thus, they are drifters.
* \[MASK] is also born with a destiny: fulfilling the Masked LM task. Actually, \[MASK] is also a drifter, because it shares the same charactristics with periods and commas (high token frequency, low constant-relation frequency, and flexible position). In BERT's view, it is the randomly selected drifters (\[MASK]) that are responsible for the Masked LM task. Details will be shown in phase three.

Relationship of all tokens is presented in the figure below.
<img src="https://gjwubyron.github.io/images/tokens.JPG"/ >


Phase One
======
In lower layers, some attention heads have broad attention. Meawhile, attention to \[CLS] is relativly higher than to others. We suppose that to define the usage or parts of speech of current tokens, heads attend broadly to get information of other tokens. \[CLS] are often attended, because it is a hunter. The heads attend to it for imformation about other tokens instead of the hunter itself. 

Phase Two
======
According to the analysis, \[SEP] draws over half of attention to itself in layer 6-10, which is used as a no-op for attention heads. While no single attention head performs well at syntax "overall", attention heads specialize to specific dependency relation (e.g., pobj, det, and dobj), especially for heads from layer 4-9. Moreover, it is often the case that the dependent attends to head word rather than the other way around. We suppose this is probably because the dependents (e.g., "the", "be", and "to") are often the frequent insiders: attention heads are experienced about where they should attend to. Based on these, we suppose that when attention heads specialize in specific relations, the tokens of head words ought to be highlighted while other tokens would better not be functioning (lying low). To lie low, the tokens need to avoid being related to the tokens of the dependents as much as possible. \[SEP] becomes a perfect haven, because it contains little information about other tokens. Take dobj relation, tokens in direct object attend to their verbs, while other tokens mostly attend to \[SEP].  A question may be raised: why not attend to the drifters. Probably, the difference in their positions is the main reason: it is easier to find the outsiders in the fixed position instead of the moving one. 

Phase Three
======
Naturally, deep heads will be significantly and directly impacted by the two unsupervised tasks: Masked LM and NSP. Unsurprisingly, attention from \[CLS] is obviously broader than the average in the last layer. Meanwhile, periods and commas draw over half of attention in the last two layers. We suppose that since it is hard to differentiate \[MASK], periods, and commas, attention heads will treat them the same. Thus, Masked LM will motivate mutual relations between all the drifters and the other tokens. Since the tokens prefer the drifters (most of them are periods and commas) in the neighborhood, the heads will possibly learn finer-grained segment as a by-product. Moreover, attention to periods and commas can greatly help the prediction of \[MASK]. Since they attract lots of attentions from other tokens, \[MASK] will be more likely to have relations with tokens close to it, which is exactly the most significant part for prediction.

Conclusion
======
We hypothesize that frequency is all that matters on BERT's syntactic representation learning. Token frequency positive correlates to the significance of a token. As attention heads gain more experience with the frequent ones, the influence from them becomes stronger (this can probably explain heads redundancy: most heads are influenced by the similar frequent-tokens). When looking into the frequent tokens, constant-relation frequency separates them into two types: insider and outsider. While insiders (e.g., "the") provide clues about specific relations, outsiders (especially \[SEP]) can make the specific relations outstanding by attracting no-op attention. In BERT's view, there are three types of outsiders: hunter, haven, and drifter. Hunter is different from the other two because of broad attention, while haven and drifter is different due to their position. 
