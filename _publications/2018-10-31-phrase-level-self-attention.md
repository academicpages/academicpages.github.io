---
title: 'Phrase-level Self-Attention Networks for Universal Sentence Encoding'

collection: publications

category: conferences

permalink: /publication/2018-10-31-phrase-level-self-attention

excerpt: 'PSAN introduces phrase-level self-attention and gated memory to generate universal sentence embeddings with reduced memory cost.'

date: 2018-10-31

venue: 'Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP)'

paperurl: 'http://pku-wuwei.github.io/files/PSAN.pdf'

citation: 'Wei Wu, Houfeng Wang, Tianyu Liu, Shuming Ma. Phrase-level Self-Attention Networks for Universal Sentence Encoding. In EMNLP, 2018.'

---
Phrase-level Self-Attention Networks (PSAN) tackle the inefficiency of sentence-level attention by performing self-attention within syntactic phrases extracted from constituency parse trees. The model further uses gated memory updates to hierarchically refine representations across levels. Final sentence vectors are computed via a multi-dimensional attention mechanism. PSAN outperforms existing sentence encoders on multiple transfer tasks while offering better scalability by reducing quadratic memory overhead.