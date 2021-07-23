---
title: 'Frequency Is All That Matters: A Hypothesis About How BERT Learn Syntactic Representations'
date: 2021-07-23

permalink: /frequency-is-all-that-matters/

---
Abstract
======
* This post proposes a hypothesis about how BERT learns syntactic representation, mainly based on an analysis about BERT's attention ([Clark et al., 2019](https://nlp.stanford.edu/pubs/clark2019what.pdf)). 
* In the analysis, heads often focus on special tokens: early heads attend to \[CLS], middle heads attend to \[SEP], and deep heads attend to periods and commas, as shown in Figure 1 ([Clark et al., 2019](https://nlp.stanford.edu/pubs/clark2019what.pdf)). 
* Intuitively, we assume there are three rough phases of heads. 
* Following this assumaption, we suppose that special tokens will significantly impact what attention heads learn .
* In this blog, we will desscribe our hypothesis in two parts:
  * What makes tokens special?
  * How special tokens impact attention heads in each phase?

<img src="https://gjwubyron.github.io/images/heads.JPG" >
<em>Figure 1: The average attention a particular BERT attention head puts toward a token type. </em>

Special Tokens
======
* Token frequency makes learning easier and earlier, which separates frequent tokens from the others.    
* Constant-relation frequency differentiate frequent tokens into outsiders and insiders: 
  * Insiders (e.g., "the", "be","to") often have simple and constant relations. For example, articles (a/an/the) are often related to the immediately following word. Thus, they often have narrow attention.
  * Outdiers (\[CLS], \[SEP], periods, commmas, and \[MASK]) can hardly have constant relations with other tokens.
* When looking into the outsiders, we find they can be seperated into three types:
  * \[CLS] is a hunter, since it has broad attention due to the Next Sentence Prediction (NSP) task. 
  * \[SEP] locates in the end of sentences, which makes it a haven for tokens that need to lie low. Details in phase two.
  * Typical, the "sentences" referred to by BERT are much longer than single sentences. Periods and commas are separators for traditional sentences inside the "sentences".They locate in flexible positions like drifters.
  * \[MASK] is also a drifter, because it shares the same charactristics with periods and commas. However, \[MASK] is born to fulfill the Masked LM task. In BERT's view, it is the randomly selected drifters (\[MASK]) that are responsible for the Masked LM task, which means all the drifters will be motivated by this task.
* Attention heads will learn \[CLS] earlier than any other tokens, since it has special charactristic (broad attention) and always locate in the same position. 

<img src="https://gjwubyron.github.io/images/token.JPG" >
<em>Figure 2: Relationship of tokens</em>




Phase One
======
* Solid Results:
  1. In lower layers, some attention heads have broad attention. 
  2. Meawhile, attention to \[CLS] is relativly higher than to others.
* Hypothesis:
  * **Main point: We suppose early heads focus on the usage of tokens, especially insiders.** 
  1. Attention heads attend broadly to get information of tokens. Probably, insiders will stand out amoung all tokens.
  2. \[CLS] are often attended, because it is a hunter. The heads attend to it for imformation about other tokens instead of the hunter itself.
  
  
Phase Two
======
* Solid Results:
  1. \[SEP] draws over half of attention to itself in layer 6-10, which is used as a no-op for attention heads. 
  2. While no single attention head performs well at syntax "overall", attention heads specialize to specific dependency relation (e.g., pobj, det, and dobj), especially for heads from layer 4-9.  
  3. It is often the case that the dependent attends to head word rather than the other way around. 
  4. Attention heads within the same layer have similar attention distributions (redundancy).
* Hypothesis:
  * **Main point: We suppose middle heads focus on specific dependency, especially where insiders should attend to.**
  1. Since insiders often have narrow attention, other tokens need to attend as far as possible to highlight attention from insiders.\[SEP] at the end of sentences becomes a haven for those tokens to lie low. 
  2. Because insiders' relations are usually specific, attention heads will specialize to specific dependency relation, . 
  3. Since insiders are often dependents, it is more often the dependent attends to head word than the other way around
  4. Heads will first focus on the more-frequent insiders, then the less-frequent ones. Thus, heads in the same layer will focus on similar insiders, which leads to redundancy.

Phase Three
======
* Solid Results:
  1. Attention from \[CLS] is obviously broader than the average in the last layer. 
  2. Periods and commas draw over half of attention in the last two layers. 
* Hypothesis:
  * **Main point: We suppose deep heads are significantly impacted by Masked LM and NSP task, and learn finer-grained segment as a by-product.
  * We suppose that since it is hard to differentiate \[MASK], periods, and commas, attention heads will treat them the same. Thus, Masked LM will motivate mutual relations between all the drifters and the other tokens. Since the tokens prefer the drifters (most of them are periods and commas) in the neighborhood, the heads will possibly learn finer-grained segment as a by-product. 
  * Moreover, attention to periods and commas can greatly help the prediction of \[MASK]. Since they attract lots of attentions from other tokens, \[MASK] will be more likely to have relations with tokens close to it, which is exactly the most significant part for prediction.

Conclusion
======
* We hypothesize that frequency is all that matters on BERT's syntactic representation learning. Token frequency positive correlates to the significance of a token. As attention heads gain more experience with the frequent ones, the influence from them becomes stronger (this can probably explain heads redundancy: most heads are influenced by the similar frequent-tokens). 
* When looking into the frequent tokens, constant-relation frequency separates them into two types: insider and outsider. While insiders (e.g., "the") provide clues about specific relations, outsiders (especially \[SEP]) can make the specific relations outstanding by attracting no-op attention. 
* In BERT's view, there are three types of outsiders: hunter, haven, and drifter. Hunter is different from the other two because of broad attention, while haven and drifter is different due to their position. 
