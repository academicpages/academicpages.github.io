---
title: 'SGM: Sequence Generation Model for Multi-Label Classification'

collection: publications

category: conferences

permalink: /publication/2018-08-20-sgm-sequence-generation

excerpt: 'SGM models multi-label classification as a sequence generation task, capturing label dependencies and contextual relevance through a novel decoder.'

date: 2018-08-20

venue: 'Proceedings of the 27th International Conference on Computational Linguistics (COLING)'

paperurl: 'http://pku-wuwei.github.io/files/sgm.pdf'

citation: 'Pengcheng Yang, Xu Sun, Wei Li, Shuming Ma, Wei Wu, Houfeng Wang. SGM: Sequence Generation Model for Multi-Label Classification. In COLING, 2018.'

---
This paper proposes the Sequence Generation Model (SGM), a novel approach to multi-label classification (MLC) that treats label prediction as a sequential process. Traditional MLC approaches struggle with modeling inter-label dependencies and often ignore the variable contribution of different text components. SGM introduces a label-wise decoder with attention to capture dependencies among labels and focus on relevant text segments dynamically. A global embedding mechanism is further introduced to preserve overall label information across steps. Extensive experiments show SGM achieves significant improvements over prior methods on standard MLC benchmarks, highlighting its ability to model label co-occurrence and text-label interactions effectively.