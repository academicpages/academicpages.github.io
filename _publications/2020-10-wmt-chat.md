---
title: "The University of Edinburgh-Uppsala University’s Submission to the WMT 2020 Chat Translation Task"
collection: publications
venue: Fifth Conference on Machine Translation (WMT 20), EMNLP 2020
permalink: /publications/2020-10-wmt-chat
paperurl:
---
Authors: Nikita Moghe, Christian Hardmeier and Rachel Bawden

**Details coming soon**

This paper describes the joint submission of the University of Edinburgh and Uppsala University to the WMT'20 chat translation task for both language directions (English<->German). 
We use existing state-of-the-art machine translation models trained on news data and fine-tune them on in-domain and pseudo-in-domain web crawled data. 
We also experiment with (i)adaptation using speaker and domain tags and (ii)using different types and amounts of preceding context.
We observe that contrarily to expectations, exploiting context degrades the results (and on analysis the data is not highly contextual). However using domain tags does improve scores according to the automatic evaluation. Our final primary systems use domain tags and are ensembles of 4 models, with noisy channel reranking of outputs. Our en-de system was ranked second  in the shared task while our de-en system outperformed all the other systems.
