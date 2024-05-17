---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

My name is Yu-Sheng (Ethan) Su. I am currently a Research Fellow hosted by [Eric Xing](http://www.cs.cmu.edu/~epxing/) from [CMU](https://www.cmu.edu/) / [MBZUAI](https://mbzuai.ac.ae/) and work on large-scale pre-trained language models (LLMs) now. I completed my Ph.D. in 2023 from the [Department of Computer Science and Technology](http://www.cs.tsinghua.edu.cn/) at [Tsinghua University](https://www.tsinghua.edu.cn/publish/thu2018en/index.html). Throughout my Ph.D. (from 2019 to 2023), I had the privilege of being advised by [Zhiyuan Liu](https://scholar.google.com/citations?user=dT0v5u0AAAAJ&hl=zh-TW) and joining [THUNLP Lab](https://github.com/thunlp) hosted by [Maosong Sun](https://www.cs.tsinghua.edu.cn/csen/info/1180/4033.htm). Besides, I work closely with a start-up team, [ModelBest](https://github.com/OpenBMB). For further details on my academic research and experience, please refer to my [[Google Scholar](https://scholar.google.com/citations?user=xwy6Va4AAAAJ&hl=en)].


<!--You can find my CV [here](/cv/).-->
## On the Job Market
I'm on the job market, looking for academic and industrial research positions related to LLMs. [[Google Schlar](https://scholar.google.com/citations?user=xwy6Va4AAAAJ&hl=en)] 
<!-- [[CV]](https://www.dropbox.com/s/4j059nncu2k6lrf/Yusheng_Su_Resume_2023_05_15.pdf?dl=0) -->
<!-- (in North America) -->


## Research
<!--
I have 4-year experiences in LLMs. My research spans the areas of natural language processing and machine learning. My long-term goal of research is to build a general-purpose machine learning system that can <b>sufficiently learn</b> human-like cognitive capacities (e.g., understanding , reasoning, reflecting, etc.), <b>efficiently adapt</b> to various tasks, and remain <b>interactable and reliable</b> when deployed in real applications. Toward this goal, my previous works spans across:
-->

<!--
* <b>General-purpose Model. (Model Pre-training)</b> Building pre-trained models that possess the more powerful perceptual abilities and cognitive abilities, such as understanding, reasoning, generation abilities etc ([CPM](https://www.sciencedirect.com/science/article/pii/S266665102100019X), [Knowledge Inheritance](https://aclanthology.org/2022.naacl-main.288/)). <small>Besides, I'm also insterested in [scaling science](https://github.com/yushengsu-thu/Scaling-Science) in foundation models. </small>
-->

My research spans the areas of natural language processing and machine learning, specifically focusing on <b>large language models (LLMs)</b>. I am particularly interested in how to better pre-train, fine-tune/instruction-tune, evaluate LLMs, and advance them in real-world scenarios. Thus, my research broadly covers the following topics:
<!--
My goal is to advance LLMs into the next-generation AI system capable of autonomously accomplishing long-horizon tasks according to users' desires. Thus, I am broadly interested in the following topics:
-->
<!-- 
To achieve this goal, LLMs should be *comprehend instructions and efficiently adapt to downstream tasks*, *interact with the external world to devise optimal strategies*, and *reliably execute strategies and accomplish goals autonomously in alignment with human intentions*.
--->

* <b> Retrieval Augmented LLM </b> Equip LLMs with the capability to leverage external retrieval information, thereby enhancing their understanding and increasing their trustworthiness. ([CokeBERT](https://arxiv.org/abs/2009.13964), [CSS-LM](https://arxiv.org/abs/2102.03752)) [[Talk20230723](https://drive.google.com/file/d/1lKARwrVFpoTh2E7W8K7B8R6AWncKrDGw/view?usp=sharing)]

* <b>(Fine-tune/Instruction-tune) Computational Efficiency Tuning </b> Develop theories, tools, and algorithms to tune LLMs, enabling them to better understand human's instruction and efficiently adapt to downstream tasks in a computation-friendly manner. (e.g., parameter-efficient tuning methods, instruction tuning). ([Prompt Transferability](https://aclanthology.org/2022.naacl-main.290/), [IPT](https://arxiv.org/abs/2110.07867), [Parameter-efficient Fine-tuning Survey](https://arxiv.org/abs/2203.06904), [APET](https://openreview.net/forum?id=3CIQIYNGlp)) [[Talk20230723](https://drive.google.com/file/d/1lKARwrVFpoTh2E7W8K7B8R6AWncKrDGw/view?usp=sharing), [Talk20240307](https://drive.google.com/file/d/1zo5aGkeOw16PoUYPxjW_2xllAValW_1x/view?usp=sharing)]

<!--Recently, I more focus on <b>interactable and reliable</b> part:-->

Recently, I am more focus on:


* <b>Autonomous Agent </b> Developing agents (based on LLMs) that can autonomously interact with the external environment (or humans) to self-improve and drive long-horizon decision-making, thereby accomplishing more complex tasks in the real world ([AgentVerse](https://arxiv.org/abs/2308.10848), [XAgent](https://blog.x-agent.net/about/), [Tool Leaning](https://arxiv.org/abs/2304.08354), [ChatDev](https://arxiv.org/abs/2307.07924)) <small> Note that: Currently, I am exploring ways to transform an assistant agent into an autonomous agent. </small> [[Talk20240228](https://drive.google.com/file/d/12M7O3cq8cJX7XXxUMG4IkkwuYP5s8nAh/view?usp=sharing), [Talk20240307](https://drive.google.com/file/d/1zo5aGkeOw16PoUYPxjW_2xllAValW_1x/view?usp=sharing)]


<!-- 
* <b>AI Alignment - weaker supervision </b> Aligning AI models to act in accordance with human values is challenging: these values are taught by humans who make mistakes, harbor biases, and have a complex that is hard to completely specify. AI models often learn to exploit even minor imperfections in the specified objective, a tendency known as reward hacking. To achieve the alignment goal, a core open problem is a scalable oversight. Thus, I study how to explain, understand, and evaluate ways to better control how AI models extend  our supervision over tasks that are beyond our direct oversight, thereby improving alignment and their ability to generalize. ([Model Emotion](https://arxiv.org/abs/2302.09582), [Chateval](https://arxiv.org/abs/2308.07201)) 
-->

* <b>AI Alignment</b> Interpretability - [Model Emotion](https://arxiv.org/abs/2302.09582), Scale-oversight - [Chateval](https://arxiv.org/abs/2308.07201)


<!--and train/guide another AI system that smarter than human.-->

  <!--
  <small> Note that: At the present stage, I am exploring how to fine-tune a large language model (LLM) that can autonomously (without human-provided prompts) initiate chain-of-thought and self-reflection processes, akin to human-like machines, in order to perform long-horizon reasoning and achieve better generalization. </small>
  -->








## News
<!-- 
* [Mar. 2022] Got one paper accepted at ACL 2022. 
* [Aug. 2021] Got one paper accepted at IEEE/TASLP 2021. 
* [Feb. 2021] Got one paper accepted at WWW 2021. 
* [Aug. 2020] Got one paper accepted at EMNLP 2020. 
</font> -->
* [May. 2024] Thrilled to announce that [ChatDev](https://arxiv.org/abs/2307.07924) was accepted by ACL 2024.
* [May. 2024] I will attend ICLR (Vienna, Austria) conference. Let's grab a coffee. Welcome DM me via [Twitter]
* [Mar. 2024] Invited Research Talk at [Microsoft Research - AI Frontiers](https://www.microsoft.com/en-us/research/lab/ai-frontiers/) hosted by [Guoqing Zheng](https://www.microsoft.com/en-us/research/people/zheng/). Topic: Efficient Tuning of Large-scale Pre-trained Language Models (LLMs) [[slide](https://drive.google.com/file/d/1zo5aGkeOw16PoUYPxjW_2xllAValW_1x/view?usp=sharing)]
* [Feb. 2024] Invited Research Talk at [Microsoft Research - Semantic Machines](https://www.microsoft.com/en-us/research/group/semantic-machines/) hosted by [Ben Van Durme](https://www.microsoft.com/en-us/research/people/bevandur/). Topic: Next-Generation Co-pilot: From Assistant Agent to Autonomy Agent [[slide](https://drive.google.com/file/d/12M7O3cq8cJX7XXxUMG4IkkwuYP5s8nAh/view?usp=sharing)]
* [Jan. 2024] Thrilled to announce that [AgentVerse](https://openreview.net/forum?id=EHg5GDnyq1) and [ChatEval](https://openreview.net/forum?id=FQepisCUWu) were accepted by ICLR 2024.
* [Jan. 2024] Invited Research Talk at [Alibaba DAMO Academy](https://www.alibabagroup.com/en-US/about-alibaba). Topic: From Assistant Agents (Co-pilots) to Autonomous Agents [[slide](https://drive.google.com/file/d/12M7O3cq8cJX7XXxUMG4IkkwuYP5s8nAh/view?usp=sharing)].
* [Dec. 2023] I will attend EMNLP (Singapore) and NeurIPS (New Orleans, U.S.A) conference. Welcome DM me via [Twitter](https://twitter.com/thu_yushengsu) / <yushengsu.thu@gmail.com> and say "HI" to me.
* [Oct. 2023] Thrilled to announce that [Exploring the Impact of Model Scaling on Parameter-efficient Tuning Methods](https://openreview.net/forum?id=3CIQIYNGlp) was accepted by EMNLP 2023 as the main conference paper.
* [Oct. 2023] Thrilled to announce that we propose a next-generation AI agent, [X Agent](https://blog.x-agent.net/about/), that can accomplish more challenging tasks in the world.
* [Aug. 2023] I got my Ph.D.! Thanks to all those who trust me and support me.
* [Jul. 2023] Invited Research Talk at [CMU](https://www.cmu.edu/)/[MBZUAI](https://mbzuai.ac.ae/) hosted by [Eric P. Xing](http://www.cs.cmu.edu/~epxing/). Topic: Efficient Adaptation of Large-scale Pre-trained Language Models [[slide](https://drive.google.com/file/d/1ow2Q-YUOk-Hyvou3VAH88yvGlQzS7SFN/view?usp=sharing)].
* [May. 2023] [AgentVerse](https://github.com/OpenBMB/AgentVerse) was published. It provides a flexible framework that simplifies the process of building LLM-based agents to accomplish various tasks in the real world.
* [Apr. 2023] [Tool Learning](https://arxiv.org/pdf/2304.08354.pdf) survey was published. It demonstrates how recently proposed LLMs leverage the emerging ability to comprehend, create, and manipulate tools, thereby assisting humans in accomplishing their intended objectives.
* [Jan. 2023] [Parameter-efficient Fine-tuning of Large-scale Pre-trained Language Models](https://www.nature.com/articles/s42256-023-00626-4) was accepted by [Natural Machine Intelligence](https://www.nature.com/natmachintell/) (Cover Article).
* [Sep. 2022] Advancement of Foundation Models. Invited Talk (on-line) @ [SAP - AI Research](https://www.sap.com/products/artificial-intelligence.html), Headquarters, Germany.
* [Jul. 2022] Will orally present our 2 accepted works at [NAACL 2022](https://2022.naacl.org/) (Seattle, USA). Welcome DM me via [Twitter](https://twitter.com/thu_yushengsu) / <yushengsu.thu@gmail.com> and say "HI" to me.
* [Apr. 2022] [Transferability of Prompt Tuning](https://aclanthology.org/2022.naacl-main.290/) and [Knowledge Inheritance](https://aclanthology.org/2022.naacl-main.288/) are accepted to [NAACL 2022](https://2022.naacl.org/).

<!-- <font color="gray"> </font> -->




## Publications

* <b>Communicative agents for software development</b>\
*Chen Qian, Xin Cong, Cheng Yang, Weize Chen, <b>Yusheng Su</b>, Juyuan Xu, Zhiyuan Liu, Maosong Sun*\
ACL 2024. [[pdf](https://arxiv.org/abs/2307.07924)] [[code](https://github.com/openbmb/chatdev)]

* <b>AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors in Agents</b>\
*<b>Yusheng Su</b><sup><big>*</big></sup>, Weize Chen<sup><big>*</big></sup>, Jingwei Zuo, Cheng Yang, Chenfei Yuan, Chen Qian, Chi-Min Chan, Yujia Qin, Yaxi Lu, Ruobing Xie, Zhiyuan Liu, Maosong Sun, Jie Zhou* (&nbsp;<sup><big>*</big></sup> indicates equal contribution)\
ICLR 2024. [[pdf](https://arxiv.org/abs/2308.10848)] [[code](https://github.com/openbmb/agentverse)]

* <b>ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate</b>\
*Chi-Min Chan, Weize Chen, <b>Yusheng Su</b>, Jianxuan Yu, Wei Xue, Shanghang Zhang, Jie Fu, Zhiyuan Liu*\
ICLR 2024. [[pdf](https://arxiv.org/abs/2308.07201)] [[code](https://github.com/thunlp/ChatEval)]

* <b>Exploring the Impact of Model Scaling on Parameter-efficient Tuning Methods</b>\
*<b>Yusheng Su</b>, Chi-Min Chan, Jiali Cheng, Yujia Qin, Yankai Lin, Shengding Hu, Zonghan Yang, Ning Ding, Xingzhi Sun, Guotong Xie, Zhiyuan Liu, Maosong Sun*\
EMNLP 2023. [[pdf](https://openreview.net/forum?id=3CIQIYNGlp)] [[code](https://github.com/yushengsu-thu/PET_Scaling)]

* <b>Parameter-efficient Fine-tuning of Large-scale Pre-trained Language Models</b>\
*Ning Ding, Yujia Qin, Guang Yang, Fuchao Wei, Zonghan Yang, <b>Yusheng Su</b>, Shengding Hu, Yulin Chen, Chi-Min Chan, Weize Chen, Jing Yi, Weilin Zhao, Xiaozhi Wang, Zhiyuan Liu, Hai-Tao Zheng, Jianfei Chen, Yang Liu, Jie Tang, Juanzi Li, Maosong Sun.*\
Nature Machine Intelligence 2023 (<b>Cover Article</b>). [[pdf](https://www.nature.com/articles/s42256-023-00626-4)] [[code](https://github.com/thunlp/OpenDelta)]

* <b>On Transferability of Prompt Tuning for Natural Language Processing</b>\
*<b>Yusheng Su</b>, Xiaozhi Wang, Yujia Qin, Chi-Min Chan, Yankai Lin, Zhiyuan Liu, Peng Li, Juanzi Li, Lei Hou, Maosong Sun, Jie Zhou*\
NAACL 2022 (<b>Oral</b>). [[pdf]](https://aclanthology.org/2022.naacl-main.290/) [[code]](https://github.com/thunlp/Prompt-Transferability) [[BibTex](https://aclanthology.org/2022.naacl-main.290.bib)] [[slide](https://drive.google.com/file/d/1OSmU3s7DOv-Gux5JcjuY0w79MzRRJuiA/view?usp=sharing)] [[video](https://www.youtube.com/watch?v=KVgmtgMQ3ig)]

* <b>Knowledge Inheritance for Pre-trained Language Models</b>\
*Yujia Qin, Yankai Lin, Jing Yi, Jiajie Zhang, Xu Han, Zhengyan Zhang, <b>Yusheng Su</b>, Zhiyuan Liu, Peng Li, Maosong Sun, Jie Zhou*\
NAACL 2022 (<b>Oral</b>). [[pdf](https://aclanthology.org/2022.naacl-main.288/)] [[code](https://github.com/thunlp/Knowledge-Inheritance)]

* <b>Exploring Low-dimensional Intrinsic Task Subspace via Prompt Tuning</b>\
*Yujia Qin, Xiaozhi Wang, <b>Yusheng Su</b>, Yankai Lin, Ning Ding, Zhiyuan Liu, Juanzi Li, Lei Hou, Peng Li, Maosong Sun, Jie Zhou*\
ACL 2022 Findings. [[pdf](https://arxiv.org/abs/2110.07867)] [[code](https://github.com/thunlp/Intrinsic-Prompt-Tuning)]

* <b>CPM: A large-scale Generative Chinese Pre-trained Language Model</b>\
*Zhengyan Zhang, Xu Han, Hao Zhou, Pei Ke, Yuxian Gu, Deming Ye, Yujia Qin, <b>Yusheng Su</b>, Haozhe Ji, Jian Guan, Fanchao Qi, Xiaozhi Wang, Yanan Zheng, Guoyang Zeng, Huanqi Cao, Shengqi Chen, Daixuan Li, Zhenbo Sun, Zhiyuan Liu, Minlie Huang, Wentao Han, Jie Tang, Juanzi Li, Xiaoyan Zhu, Maosong Sun*\
AI OPEN 2021. [[pdf](https://www.sciencedirect.com/science/article/pii/S266665102100019X)] [[code](https://github.com/TsinghuaAI/CPM)]

* <b>CSS-LM: A Contrastive Framework for Semi-supervised Fine-tuning of Pre-trained Language Models</b>\
*<b>Yusheng Su</b>, Xu Han, Yankai Lin, Zhengyan Zhang, Zhiyuan Liu, Peng Li, Maosong Sun*\
[WWW 2021 Workshop](https://www.aminer.cn/ssl_www2021), IEEE/TASLP 2021. [[pdf](https://arxiv.org/abs/2102.03752)] [[code](https://github.com/thunlp/CSS-LM)] [[slide](https://drive.google.com/file/d/1TqAnFYL5CBwWhrDamB83akqQniVd2B9o/view?usp=sharing)]

* <b>CokeBERT: Contextual Knowledge Selection and Embedding Towards Enhanced Pre-Trained Language Models</b>\
*<b>Yusheng Su</b>, Xu Han, Zhengyan Zhang, Peng Li, Zhiyuan Liu, Yankai Lin, Jie Zhou, Maosong Sun*\
EMNLP 2020 Findings, AI OPEN 2021. [[pdf](https://arxiv.org/abs/2009.13964)] [[pdf](https://www.sciencedirect.com/science/article/pii/S2666651021000188)] [[code](https://github.com/thunlp/CokeBERT)]



## Under Review or Preprint Version <!-- Submitted for Publications-->

* <b>Human Emotion Knowledge Representation Emerges in Large Language Models and Supports Discrete Emotion Inference</b>\
*<b>Yusheng Su</b><sup><big>*</big></sup>, Ming Li<sup><big>*</big></sup>, Hsiu-Yuan Huang, Jiali Cheng, Xin Hu, Xinmiao Zhang, Huadong Wang, Yujia Qin, Xiaozhi Wang, Zhiyuan Liu, Dan Zhang* (&nbsp;<sup><big>*</big></sup> indicates equal contribution)\
(Submitted to Nature Human Behaviour 2023). [[pdf](https://arxiv.org/abs/2302.09582)] [[code](https://github.com/thunlp/OpenNeuron)] <small>(Refactoring - User friendly toolkit coming soon)</small>

* <b>Tool Learning with Foundation Models</b>\
*Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen, Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang, Chaojun Xiao, Chi Han, Yi Ren Fung, <b>Yusheng Su</b>, Huadong Wang, Cheng Qian, Runchu Tian, Kunlun Zhu, Shihao Liang, Xingyu Shen, Bokai Xu, Zhen Zhang, Yining Ye, Bowen Li, Ziwei Tang, Jing Yi, Yuzhang Zhu, Zhenning Dai, Lan Yan, Xin Cong, Yaxi Lu, Weilin Zhao, Yuxiang Huang, Junxi Yan, Xu Han, Xian Sun, Dahai Li, Jason Phang, Cheng Yang, Tongshuang Wu, Heng Ji, Zhiyuan Liu, Maosong Sun*\
ArXiv 2023. [[pdf](https://arxiv.org/abs/2304.08354)] [[code](https://github.com/OpenBMB/BMTools)] 





<!--
* <b>Removing Backdoors in Pre-trained Models by Regularized Continual Pre-training</b>\
*Biru Zhu, Ganqu Cui, Yangyi Chen, Yujia Qin, <b>Yusheng Su</b>, Lifan Yuan, Chong Fu, Yangdong Deng, Zhiyuan Liu, Maosong Sun, Ming Gu.*\
(Submitted to TACL). [[pdf]](https://www.dropbox.com/s/0yuudhokyyomkup/Removing_Backdoors_in_Pre-trained_Models_by_Regularized_Continual_Pretraining.pdf?dl=0) 
-->


## Efficient Training Projects

* (Leader/Co-leader) <b>Prompt Transferability</b>. This system assists users in building a prompt bank, allowing them to save well-trained prompts. It also enables swift access and reuse of these prompts whenever the user requires them on unseen tasks and heterogeneous models.

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=thunlp&repo=Prompt-Transferability)](https://github.com/thunlp/Prompt-Transferability)


## Agents Projects

* (Leader/Co-leader) <b>AgentVerse</b>. AgentVerse provides a framework that streamlines the process of developing custom multi-agent systems using LLMs in user-defined environments. This facilitates the design of more efficient multi-agent systems that can be applied to real-world applications. [[Youtube1](https://www.youtube.com/watch?v=37vcapVCcbM)], [[Youtube2](https://www.youtube.com/watch?v=cbqE6PC9fGQ&t=512s)]

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=OpenBMB&repo=AgentVerse)](https://github.com/OpenBMB/AgentVerse)


* (Member) <b>XAgent</b>. XAgent makes more effective decisions and execute efficient actions to accomplish tasks with an unprecedented degree of autonomy. [[Youtube1](https://www.youtube.com/watch?v=X6dna0O6pCw)], [[Youtube2](https://www.youtube.com/watch?v=LOLRYnQSyC4)]

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=OpenBMB&repo=XAgent)](https://github.com/OpenBMB/XAgent)


* (Member) <b>ChatDev</b>. ChatDev creates customized software using natural language idea through LLM-powered multi-agent collaboration. [[Youtube1](https://www.youtube.com/watch?v=yoAWsIfEzCw)], [[Youtube2](https://www.youtube.com/watch?v=QPBmsgGufXE)] [[Andrew Ng's talk](https://www.youtube.com/watch?v=sal78ACtGTc&t=559s)]

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=OpenBMB&repo=ChatDev)](https://github.com/OpenBMB/ChatDev)


* (Member) <b>Tool Learning</b>. Tool learning for LLMs, open-source solutions of ChatGPT-Plugins.
  
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=OpenBMB&repo=BMTools)](https://github.com/OpenBMB/BMTools)


## LLM Pre-training Projects
* (Member) <b> CPM</b>-X. The first chinese-version large-scale pre-trained project and released a series of LLMs in 2020-2021.
  
[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=TsinghuaAI&repo=CPM)](https://github.com/TsinghuaAI/CPM)

<!--
## Teaching
* [Jul. 2022] Tsinghu University - NLP Big Model Course (Summer) [link](https://www.bilibili.com/video/BV1UG411p7zv?p=1&unique_k=OwC3PgP)
-->

## Talks
* [Mar. 2024] Invited Research Talk at [Microsoft Research - AI Frontiers](https://www.microsoft.com/en-us/research/lab/ai-frontiers/) hosted by [Guoqing Zheng](https://www.microsoft.com/en-us/research/people/zheng/). Topic: Efficient Tuning of Large-scale Pre-trained Language Models (LLMs) [[slide](https://drive.google.com/file/d/1zo5aGkeOw16PoUYPxjW_2xllAValW_1x/view?usp=sharing)]
* [Feb. 2024] Invited Research Talk at [Microsoft Research - Semantic Machines](https://www.alibabagroup.com/en-US/about-alibaba) hosted by [Ben Van Durme](https://www.microsoft.com/en-us/research/people/bevandur/). Topic: Next-Generation Co-pilot: From Assistant Agent to Autonomy Agent [[slide](https://drive.google.com/file/d/12M7O3cq8cJX7XXxUMG4IkkwuYP5s8nAh/view?usp=sharing)]
* [Jan. 2024] Invited Research Talk at [Alibaba DAMO Academy](https://www.alibabagroup.com/en-US/about-alibaba)]. Topic: From Assistant Agents (Co-pilots) to Autonomous Agents [[slide](https://drive.google.com/file/d/12M7O3cq8cJX7XXxUMG4IkkwuYP5s8nAh/view?usp=sharing)]
* [Jul. 2023] Invited Research Talk at [CMU](https://www.cmu.edu/)/[MBZUAI](https://mbzuai.ac.ae/) hosted by [Eric P. Xing](http://www.cs.cmu.edu/~epxing/). Topic: Efficient Adaptation of Large-scale Pre-trained Language Models [[slide](https://drive.google.com/file/d/1ow2Q-YUOk-Hyvou3VAH88yvGlQzS7SFN/view?usp=sharing)].
* [Sep. 2022] Invited Talk (on-line) @ [SAP - AI Research](https://www.sap.com/products/artificial-intelligence.html), Headquarter, Germany
* [Jul. 2022] Oral Talk @ NAACL 2022, [[slide](https://drive.google.com/file/d/1OSmU3s7DOv-Gux5JcjuY0w79MzRRJuiA/view?usp=sharing)] [[video](https://www.youtube.com/watch?v=KVgmtgMQ3ig)]
* [Apr. 2021] Spotlight Talks (on-line) @ WWW 2021 (Self-Supervised Learning Workshop)



## Professional Services
<!--
* Reviewer: COLING 2022
* Review Committee Member: EMNLP 2022
* Reviewer: ICML 2022
* Reviewer: ACL Rolling 2022
* Reviewer: ACL Rolling 2021
* Reviewer: EMNLP/ACL/IEEE-TASLP 2021
-->
Reviewer (Since 2021): ACL, NAACL, AACL, ACL Roling, EMNLP, COLING, ICLR, ICML, IJCAI, AAAI



## Work Experiences

### Tsinghua University - NLP Lab. (Beijing) 2019 - 2023
* Ph.D. NLP Group (hosted by [Maosong Sun](https://www.cs.tsinghua.edu.cn/csen/info/1180/4033.htm)), AI, Computer Science Department 
* Advised by [Zhiyuan Liu](http://nlp.csai.tsinghua.edu.cn/~lzy/).

### MediaTek. (Taiwan) 2018 - 2019
* Deep/Machine Learning Engineer Intern
* Advised by Jing-Han Wang.

### Microsoft. (Taiwan) 2015 - 2016
* Research and Development Intern
* Advised by [Kuang-Chao Yeh](https://www.linkedin.com/in/kuang-chao-yeh/) and [Gordon Chang](https://www.linkedin.com/in/gordonwinnow).

## Pre-doctoral Student Mentoring
* (Since 2021-2023) [Chi-Min Chan](https://scholar.google.com/citations?user=5U4P54wAAAAJ&oi=ao): Tsinghua University (BS) -> Hong Kong University of Science and Technology (HKUST) (MS) 
* (Since 2022-2023) Jiali Cheng: University of North Carolina (MS->PhD)  
* (Since 2022-2023) Yu Xia: Peking University (MS) -> Tsinghua University (PhD)  
* (Since 2022-2023) Xiuyuan Huang: University of Science and Technology Beijing (BS) -> Peking University (MS) 
