---
title: 'What Attention Dose Not Look At Is All You Need'
date: 2021-07-23

permalink: /frequency-is-all-that-matters/

---
Abstract
======
* This post proposes a hypothesis about how BERT learns syntactic representations, mainly based on an analysis about BERT's attention ([Clark et al., 2019](https://nlp.stanford.edu/pubs/clark2019what.pdf)). Inspired by the attention distribution, we suppose there are three phases of heads focus on different representations. 
* For a better understanding, we first discuss about what makes tokens special. 
* Then we present solid results from the analysis as well as our explanations to them in each phase.
* Finally, we suggest our hypothesis can probably explain redundancy in BERT's attention heads.

Inspiration
======

* Attention heads often focus on special tokens: early heads attend to \[CLS], middle heads attend to \[SEP], and deep heads attend to periods and commas, as shown in Figure 1. 

<img src="https://gjwubyron.github.io/images/heads.JPG" >
<em>Figure 1: The average attention a particular BERT attention head puts toward a token type (Clark et al., 2019). </em>

Special Tokens
======
* High token frequency makes learning easier and earlier, which separates frequent tokens from the others.    
* Then, constant-relation frequency differentiate frequent tokens into outsiders and insiders: 
  * Insiders (e.g., "the", "be","to") often have simple and constant relations. For example, articles (a/an/the) are often related to the immediately following word. Thus, they often have narrow attention.
  * Outdiers (\[CLS], \[SEP], periods, commmas, and \[MASK]) can hardly have constant relations with other tokens.
* When looking into the outsiders, we find they can be seperated into three types:
  * \[CLS] is a hunter, since it has broad attention due to the Next Sentence Prediction (NSP) task. 
  * \[SEP] locates in the end of sentences, which makes it a haven for tokens that need to lie low. Details in phase two.
  * Typical, the "sentences" referred to by BERT are much longer than single sentences. Periods and commas are separators for traditional sentences inside the "sentences".They locate in flexible positions like drifters.
  * \[MASK] is also a drifter, because it shares the same charactristics with periods and commas. 

<img src="https://gjwubyron.github.io/images/relation.JPG" >
<em>Figure 2: Relationship of tokens in Venn diagram.</em>




Phase One
======
* **Hypothesis: We suppose early heads focus on the usage of tokens, especially insiders.** 
* Solid Results:
  1. In lower layers, some attention heads have broad attention. 
  2. Meawhile, attention to \[CLS] is relativly higher than to others.
* Explanations:
  1. Attention heads attend broadly to get information of tokens. Probably, insiders will stand out amoung all tokens.
  2. \[CLS] is often attended, because it is a hunter. The heads attend to it for imformation about other tokens instead of the hunter itself.
  
  
Phase Two
======
* **Hypothsis: We suppose attention from insiders is the main concern for middle heads**
* Solid Results:
  1. Attention to \[SEP] becomes high in layer 5-10 as shown in Figure 1. Meanwhile, importance of it becomes very low as shown in Figure 3. 
  2. While no single attention head performs well at syntax "overall", attention heads specialize to specific dependency relation (e.g., pobj, det, and dobj), especially for heads from layer 4-9.  
  3. It is often the case that the dependent attends to head word rather than the other way around. 
* Explanations:
  1. Since insiders often have narrow attention, other tokens need to attend as far as possible to highlight attention from insiders. \[SEP] at the end of sentences becomes a haven for those tokens to lie low. 
  2. Because insiders' relations are usually specific, attention heads will specialize to specific dependency relation, . 
  3. Since insiders are often dependents, it is more often the dependent attends to head word than the other way around

<img src="https://gjwubyron.github.io/images/importance.JPG" >
<em>Figure 3: Gradient-based feature importance estimates
for attention to [SEP], periods/commas, and other tokens (Clark et al., 2019).</em>

Phase Three
======
* **Hypothesis: We suppose attention from drifters in the main concern for deep heads**
* Solid Results:
  1. Attention from \[CLS] is obviously broader than the average in the last layer. 
  2. Periods and commas draw over half of attention in the last two layers. 
* Explanations:
  1. Since \[CLS] is used to fulfill NSP task, it attends broadly to aggregate a representation.
  2. Due to Masked LM, attentions from \[MASK] ought to be highlighted. However, it is hard to differentiate \[MASK] from other drifters. Thus, this task motivates attention heads to highlight attention from periods and commas as well. (In BERT's view, it is the randomly selected drifters (\[MASK]) that are responsible for the Masked LM task.) 
   
* By-products:
  1. Predictions of \[MASK] can be more accurate. Because, attention to \[MASK] is mainly from tokens in the heighborhood (the most significant tokens for prediction), while other tokens attend to periods and commas.
  2. The heads will possibly learn finer-grained segment, because tokens attend to periods and commas (traditional seperators) are very likely from the same part of sentences. 

Conclusion
======

