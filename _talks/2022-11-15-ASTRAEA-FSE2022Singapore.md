---
title: "ASTRAEA: Grammar-based Fairness Testing"
collection: talks
type: "Conference Talk"
permalink: /talks/2022-11-15-ASTRAEA-FSE2022Singapore
venue: "ESEC/FSE 2022, NUS U-Town"
date: 2022-11-15
location: "Singapore, Singapore"
---

[More information here](https://2022.esec-fse.org/profile/ezekielsoremekun)

**Abstract:** Software often produces biased outputs. In particular, machine learning (ML) based software is known to produce erroneous predictions when processing discriminatory inputs. Such unfair program behaviour can be caused by societal bias. In the last few years, Amazon, Microsoft and Google have provided software services that produce unfair outputs, mostly due to societal bias (e.g. gender or race). In such events, developers are saddled with the task of conducting fairness testing. Fairness testing is challenging; developers are tasked with generating discriminatory inputs that reveal and explain biases. We propose a grammar-based fairness testing approach (called ASTRAEA) which leverages context-free grammar to generate discriminatory inputs that reveal fairness violations in software systems. Using probabilistic grammar, ASTRAEA also provides fault diagnosis by isolating the cause of observed software bias. ASTRAEAs diagnoses facilitate the improvement of ML fairness. ASTRAEA was evaluated on 18 software systems that provide three major natural language processing (NLP) services. In our evaluation, ASTRAEA generated fairness violations at a rate of about 18%. ASTRAEA generated over 573K discriminatory test cases and found over 102K fairness violations. Furthermore, ASTRAEA improves software fairness by about 76% via model retraining, on average.