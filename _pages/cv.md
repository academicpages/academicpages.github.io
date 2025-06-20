---
layout: archive
title: CV
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}


Work experience
======
## TikTok Inc., San Jose  
**Tech Lead, TikTok AI Search** — *07/2024 – Present*  
- **LLM Pretraining**: Developed Thoth, a 7B-parameter LLM. Introduced KV cache reduction, improving throughput 32× over baseline 7B models. Extended context length to 128k.  
- **LLM Alignment**: Led alignment using enhanced knowledge distillation and RLHF. Achieved top multilingual benchmark scores among 7B models.  
- **Search RAG Development**: Managed training for summary generation. Introduced answer-planning-based datasets. Boosted top-result CTR and card dwell time.

## Bytedance, Beijing  
**Generative AI Researcher, Seed Alignment** — *04/2020 – 07/2024*  
- Built process reward models for math and reasoning. 
- Developed reward merging strategies to mitigate reward hacking.  

**Machine Learning Engineer, Search**  
- **Douyin Visual Search**: Developed early recall models and led fine-ranking, enhancing user precision.  
- **Toutiao Search**: Designed a funnel transformer for long query-doc interactions in Precise QA. Unified 23 models via multi-task distillation.  
- **TikTok Search**: Built the first multilingual Search BERT, deployed for ranking, recall, and query suggestion in all regions (except P0 countries).

## ShannonAI, Beijing  
**Machine Learning Engineer** — *07/2019 – 02/2020*  
- Pretrained a financial-domain Chinese BERT model on TPU Pods.  
- Built an end-to-end financial information extractor for document mining.


Education
======
**Peking University**, Beijing  
M.S.E. in Computer Science — *09/2016 – 07/2019*  
Advisor: Prof. Houfeng Wang  
Focus: Answer Selection and Sentence Representation

**Nanjing University**, Nanjing  
B.E. in Microelectronics — *09/2012 – 07/2016*  
Advisor: Prof. Chenglei Peng


Honors & Awards
======
- Special Academic Scholarship, Peking University — *2017, 2018*  
- First Prize, Innovation & Entrepreneurship Program — *2015*  
- First Prize, National Undergraduate Electronics Design Contest (Jiangsu) — *2014*

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>
  
