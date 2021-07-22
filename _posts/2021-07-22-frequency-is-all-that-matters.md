---
title: 'Frequency Is All That Matters: A Hypothesis About How BERT Learn Syntactic Representations'
date: 2021-07-19

permalink: /frequency-is-all-that-matters/

---
Abstract
======
* This post proposes a hypothesis about how BERT learns syntactic representation, mainly based on an analysis about BERT's attention ([Clark et al., 2019](https://nlp.stanford.edu/pubs/clark2019what.pdf)). 
* In the analysis, heads often focus on special tokens: early heads attend to \[CLS], middle heads attend to \[SEP], and deep heads attend to periods and commas, as shown in Figure 1 ([Clark et al., 2019](https://nlp.stanford.edu/pubs/clark2019what.pdf)). 
* Intuitively, we hypothesize there are three rough phases of heads respectively learn three different representations: definition, dependency, and finer-grained segment. We also suppose that token frequency and constant-relation frequency make certain tokens special.

<img src="https://gjwubyron.github.io/images/heads.JPG" >
<em>Figure 1: The average attention a particular BERT attention head puts toward a token type. </em>

Special Parts of Speech
======
* Firstly, token frequency separate frequent tokens from the others, since attention heads can gain more experience with them.  
* Secondly, constant-relation frequency diffrensiate outsiders and insiders. While outdiers (\[CLS], \[SEP], periods, commmas, and \[MASK]) can hardly have constant relations with other tokens, insiders often have simple and constant relations. For example, articles (a/an/the) are often related to the immediately following word.
* When looking into the outsiders, we find they can be seperated into three types.
* \[CLS] is born to fulfill the Next Sentence Prediction (NSP) task. It is motivated to attend broadly to aggregate a representation, which makes it a global hunter. 
* \[SEP] is fixed at the end of sentences which makes it a haven for tokens that need to lie low (avoid being related to specific tokens).
* Typical, the "sentences" referred to by BERT are much longer than single sentences. Periods and commas are separators for traditional sentences inside the "sentences".They locate in flexible positions like drifters.
* \[MASK] is also a drifter, because it shares the same charactristics with periods and commas. However, \[MASK] is born to fulfill the Masked LM task. In BERT's view, it is the randomly selected drifters (\[MASK]) that are responsible for the Masked LM task, which means all the drifters will be motivated by this task.

<img src="https://gjwubyron.github.io/images/token.JPG" >
<em>Figure 2: Relationship of tokens</em>




Phase One
======
* In lower layers, some attention heads have broad attention. Meawhile, attention to \[CLS] is relativly higher than to others. 
* We suppose that to define the usage or parts of speech of current tokens, heads attend broadly to get information of other tokens. \[CLS] are often attended, because it is a hunter. The heads attend to it for imformation about other tokens instead of the hunter itself. 


Phase Two
======
* According to the analysis, \[SEP] draws over half of attention to itself in layer 6-10, which is used as a no-op for attention heads. While no single attention head performs well at syntax "overall", attention heads specialize to specific dependency relation (e.g., pobj, det, and dobj), especially for heads from layer 4-9.  
* Moreover, it is often the case that the dependent attends to head word rather than the other way around. We suppose this is probably because the dependents (e.g., "the", "be", and "to") are often the frequent insiders: attention heads are experienced about where they should attend to. 
* Based on these, we suppose that when attention heads specialize in specific relations, the tokens of head words ought to be highlighted while other tokens would better not be functioning (lying low). To lie low, the tokens need to avoid being related to the tokens of the dependents as much as possible. Take dobj relation, tokens in direct object attend to their verbs, while other tokens mostly attend to \[SEP]. 
* A question may be raised: why those tokens choose \[SEP] over other tokens. Probably, it is because \[SEP] have high token frequency and locate in the fixed position, which makes it easier for those tokens to attend. 

Phase Three
======
* Naturally, deep heads will be significantly and directly impacted by the two unsupervised tasks: Masked LM and NSP. Unsurprisingly, attention from \[CLS] is obviously broader than the average in the last layer. Meanwhile, periods and commas draw over half of attention in the last two layers. 
* We suppose that since it is hard to differentiate \[MASK], periods, and commas, attention heads will treat them the same. Thus, Masked LM will motivate mutual relations between all the drifters and the other tokens. Since the tokens prefer the drifters (most of them are periods and commas) in the neighborhood, the heads will possibly learn finer-grained segment as a by-product. 
* Moreover, attention to periods and commas can greatly help the prediction of \[MASK]. Since they attract lots of attentions from other tokens, \[MASK] will be more likely to have relations with tokens close to it, which is exactly the most significant part for prediction.

Conclusion
======
* We hypothesize that frequency is all that matters on BERT's syntactic representation learning. Token frequency positive correlates to the significance of a token. As attention heads gain more experience with the frequent ones, the influence from them becomes stronger (this can probably explain heads redundancy: most heads are influenced by the similar frequent-tokens). 
* When looking into the frequent tokens, constant-relation frequency separates them into two types: insider and outsider. While insiders (e.g., "the") provide clues about specific relations, outsiders (especially \[SEP]) can make the specific relations outstanding by attracting no-op attention. 
* In BERT's view, there are three types of outsiders: hunter, haven, and drifter. Hunter is different from the other two because of broad attention, while haven and drifter is different due to their position. 
