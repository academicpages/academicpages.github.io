---
title: "A Dynamic Attention Deep Model for Article Recommendation by Learning Human Editors' Demonstration"
collection: publications
permalink: /publications/DADM
venue: "KDD 2017"
date: 2017-06-09
citation: '<b>Lantao Yu</b>*, Xuejian Wang*(equal contribution), Kan Ren, Guanyu Tao, Weinan Zhang, Yong Yu, Jun Wang. <i> The 23rd SIGKDD Conference on Knowledge Discovery and Data Mining. </i> <b>KDD 2017</b>.'
---  
[[PDF]](https://lantaoyu.github.io/files/dadm-kdd.pdf)

## Abstract
As aggregators, online news portals face great challenges in continuously selecting a pool of candidate articles to be shown to their users.
Typically, those candidate articles are recommended manually by platform editors from a much larger pool of articles aggregated from multiple sources. Such a hand-pick process is labor intensive and time-consuming. In this paper, we study the editor article selection behavior and propose a learning by demonstration system to automatically select a subset of articles from the large pool. Our data analysis shows that (i) editors' selection criteria are \emph{non-explicit}, which are less based only on the keywords or topics, but more depend on the quality and attractiveness of the writing from the candidate article, which is hard to capture based on traditional bag-of-words article representation.
And (ii)
editors' article selection behaviors are \emph{dynamic}: articles with different data distribution come into the pool everyday and the editors' preference varies, which are driven by some underlying periodic or occasional patterns.
To address such problems, we propose a meta-attention model across multiple deep neural nets to (i) automatically catch the editors' underlying selection criteria via the automatic representation learning of each article and its interaction with the meta data and (ii) adaptively capture the change of such criteria via a hybrid attention model. The attention model strategically incorporates multiple prediction models, which are trained in previous days.
The system has been deployed in a commercial article feed platform. A 9-day A/B testing has demonstrated the consistent superiority of our proposed model over several strong baselines.
