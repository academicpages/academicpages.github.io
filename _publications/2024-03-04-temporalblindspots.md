---
title: "Temporal Blind Spots in LLMs"
collection: publications
permalink: /publications/2024-03-04-temporalblindspots.md
excerpt: 'In this paper, we investigate the underlying limitations of general-purpose LLMs when deployed for tasks that require a temporal understanding.'
date: 2024-03-04
venue: 'WSDM 2024'
paperurl: 'https://dl.acm.org/doi/abs/10.1145/3616855.3635818'
citation: 'Jonas Wallat, Adam Jatowt, and Avishek Anand. 2024. Temporal Blind Spots in Large Language Models. In Proceedings of the 17th ACM International Conference on Web Search and Data Mining (WSDM '24). Association for Computing Machinery, New York, NY, USA, 683–692. https://doi.org/10.1145/3616855.3635818'
---
Large language models (LLMs) have recently gained significant attention due to their unparalleled zero-shot performance on various natural language processing tasks. However, the pre-training data utilized in LLMs is often confined to a specific corpus, resulting in inherent freshness and temporal scope limitations. Consequently, this raises concerns regarding the effectiveness of LLMs for tasks involving temporal intents. In this study, we aim to investigate the underlying limitations of general-purpose LLMs when deployed for tasks that require a temporal understanding. We pay particular attention to handling factual temporal knowledge through three popular temporal QA datasets. Specifically, we observe low performance on detailed questions about the past and, surprisingly, for rather new information. In manual and automatic testing, we find multiple temporal errors and characterize the conditions under which QA performance deteriorates. Our analysis contributes to understanding LLM limitations and offers valuable insights into developing future models that can better cater to the demands of temporally-oriented tasks. The code is available https://github.com/jwallat/temporalblindspots.



Recommended citation: Jonas Wallat, Adam Jatowt, and Avishek Anand. 2024. Temporal Blind Spots in Large Language Models. In Proceedings of the 17th ACM International Conference on Web Search and Data Mining (WSDM '24). Association for Computing Machinery, New York, NY, USA, 683–692. https://doi.org/10.1145/3616855.3635818