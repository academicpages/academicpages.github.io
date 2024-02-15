---
permalink: /
title: "Haozhe Ji 计昊哲"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---


I am Haozhe Ji, a penultimate-year Ph.D. student from [CoAI Group](http://coai.cs.tsinghua.edu.cn/) in the Dept. of Computer Science and Technology, Tsinghua University, advised by [Prof. Minlie Huang](http://coai.cs.tsinghua.edu.cn/hml/). Before that, I received my B.Eng. degree from the Dept. of Electronic Engineering, Tsinghua University in July, 2020. Please find my **CV here** [[English](files/cv_haozhe_en.pdf)].


My current research interests are focused on the **theoretical foundations** and **scalable algorithms** for generative language models, aiming to develop *verifiable*, *consistent* and *robust* AI systems capable of generating natural language indistinguishable from that of humans.

Specifically, my research is theoretically motivated to advance language models beyond the inherent limitations of **Auto-Regressive (AR) modeling** and **Maximum Likelihood Estimation (MLE) objective** by providing practical and scalable solutions.

- To overcome the capacity limitation of AR models, my research delves into a broader spectrum of expressive model families, including semi-parametric models {% glossary grf, display: 8%}, memory-augmented models {% glossary lamemo, display: 5%}, latent variable models {% glossary discodvt, display: 6%} and energy-based models {% glossary Daemon, display: 2%}.

- To tackle the biases inherent in the conventional MLE objective, my research introduces theoretically grounded and practically accessible training objectives {% glossary EXO, display: 1%}{% glossary TaiLr, display: 3%} and decoding frameworks {% glossary Daemon, display: 2%}, aiming to achieve better alignment with human language.



## Publications

*\* indicates equal contribution.*

1. **Haozhe Ji**, Cheng Lu, Yilin Niu, Pei Ke, Hongning Wang, Jun Zhu, Jie Tang, Minlie Huang. <br>
**Towards Efficient and Exact Optimization of Language Model Alignment**.
<br> 
<u>arXiv:2402.00856.</u> <br>
[[paper]](https://arxiv.org/abs/2402.00856) [[repo]](https://github.com/haozheji/exact-optimization)

2. **Haozhe Ji**, Pei Ke, Hongning Wang, Minlie Huang. <br>
**Language Model Decoding as Direct Metrics Optimization**. <br>
<u>The Twelfth International Conference on Learning Representations, <em>ICLR 2024</em>.</u> <br>
[[paper]](https://arxiv.org/abs/2310.01041)

3. **Haozhe Ji**, Pei Ke, Zhipeng Hu, Rongsheng Zhang, Minlie Huang. <br>
**Tailoring Language Generation Models under Total Variation Distance**. <br>
<u>The Eleventh International Conference on Learning Representations, <em>ICLR 2023</em>. <br> <strong><font color=red bold>(Notable top 5%)</font></strong></u> <br>
[[paper]](https://openreview.net/forum?id=VELL0PlWfc) [[repo]](https://github.com/thu-coai/TaiLr)

4. Pei Ke, **Haozhe Ji**, Zhenyu Yang, Yi Huang, Junlan Feng, Xiaoyan Zhu, Minlie Huang. <br>
**Curriculum-Based Self-Training Makes Better Few-Shot Learners for Data-to-Text Generation** <br>
<u>Proceedings of the Thirty-First International Joint Conference on Artificial Intelligence, <em>IJCAI 2022</em>.</u> <br>
[[paper]](https://arxiv.org/abs/2206.02712)

5. **Haozhe Ji**, Rongsheng Zhang, Zhenyu Yang, Zhipeng Hu, Minlie Huang. <br>
**LaMemo: Language modeling with look-ahead memory** <br>
<u>Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics, <em>NAACL 2022</em>. <strong><font color=red bold>(Oral)</font></strong></u> <br>
[[paper]](https://aclanthology.org/2022.naacl-main.422/) [[repo]](https://github.com/thu-coai/lamemo)

6. **Haozhe Ji**, Minlie Huang.
<br>
**DiscoDVT: Generating Long Text with Discourse-Aware Discrete Variational Transformer**
<br>
<u>Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing, <em>EMNLP 2021</em>. <strong><font color=red bold>(Oral)</font></strong></u> <br>
[[paper]](https://aclanthology.org/2021.emnlp-main.347/) [[repo]](https://github.com/haozheji/DiscoDVT)

7. Pei Ke, **Haozhe Ji**, Yu Ran, Xin Cui, Liwei Wang, Linfeng Song, Xiaoyan Zhu, Minlie Huang. <br>
**Jointgt: Graph-text joint representation learning for text generation from knowledge graphs** <br>
<u>Findings of the Association for Computational Linguistics, <em>Findings of ACL 2021</em>.</u> <br>
[[paper]](https://aclanthology.org/2021.findings-acl.223/) [[repo]](https://github.com/thu-coai/JointGT)

8. Zhengyan Zhang, Xu Han, Hao Zhou, Pei Ke, Yuxian Gu, Deming Ye, Yujia Qin, Yusheng Su, **Haozhe Ji**, Jian Guan, Fanchao Qi, Xiaozhi Wang, Yanan Zheng, Guoyang Zeng, Huanqi Cao, Shengqi Chen, Daixuan Li, Zhenbo Sun, Zhiyuan Liu, Minlie Huang, Wentao Han, Jie Tang, Juanzi Li, Xiaoyan Zhu, Maosong Sun. <br>
**CPM: A large-scale generative Chinese pre-trained language model** <br>
<u>AI Open.</u> <br>
[[paper]](https://www.sciencedirect.com/science/article/pii/S266665102100019X)

8. **Haozhe Ji**, Pei Ke, Shaohan Huang, Furu Wei, Xiaoyan Zhu, Minlie Huang. <br>
**Language generation with multi-hop reasoning on commonsense knowledge graph** <br>
<u>Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing, <em>EMNLP 2020</em>. <strong><font color=red bold>(Oral)</font></strong></u> <br>
[[paper]](https://aclanthology.org/2020.emnlp-main.54/) [[repo]](https://github.com/haozheji/multigen)

9. Pei Ke\*, **Haozhe Ji\***, Siyang Liu, Xiaoyan Zhu, Minlie Huang. <br>
**Sentilare: Linguistic knowledge enhanced language representation for sentiment analysis** <br>
<u>Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing, <em>EMNLP 2020</em>.</u> <br>
[[paper]](https://aclanthology.org/2020.emnlp-main.567/) [[repo]](https://github.com/thu-coai/SentiLARE)

10. **Haozhe Ji**, Pei Ke, Shaohan Huang, Furu Wei, Minlie Huang. <br>
**Generating commonsense explanation by extracting bridge concepts from reasoning paths** <br>
<u>Proceedings of the 1st Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics, <em>AACL 2020</em>.</u> <br>
[[paper]](https://aclanthology.org/2020.aacl-main.28/)

11. Yankai Lin, **Haozhe Ji**, Zhiyuan Liu, Maosong Sun. <br>
**Denoising Distantly Supervised Open-Domain Question Answering** <br>
<u>Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics, <em>ACL 2018</em>.</u> <br>
[[paper]](https://aclanthology.org/P18-1161/) [[repo]](https://github.com/thunlp/OpenQA)


## Honors & Awards

- **Tang Junyuan (唐君远) Scholarship**, Tsinghua University, 2023
- **Sohu Scholarship**, Tsinghua University, 2022
- **Yang Huiyan (杨惠妍) Scholarship**, Tsinghua University, 2021
- **Comprehensive Merit Scholarship**, Tsinghua University, 2017/2019
- **Gold Medal**, 32nd China Physics Olympiads (CPhO), 2015 
- **Honor Roll of Distinction (Top 1%)**, American Mathematics Contest 12 (AMC12), 2015

## Education

- September, 2020 - present. Ph.D. student in [CoAI Group](http://coai.cs.tsinghua.edu.cn/), Dept. of Computer Science and Technology, Tsinghua University. Advisor: [Prof. Minlie Huang](http://coai.cs.tsinghua.edu.cn/hml/)
- September, 2016 - July, 2020. B.Eng. in Electronic Engineering, [Tsinghua University](https://www.tsinghua.edu.cn/). 

## Services

Reviewer/Program Committee: ACL, EMNLP, NAACL, ARR

## Teaching

I was a Head TA in the undergraduate course **Artificial Neural Network**, instructed by [Minlie Huang](https://coai.cs.tsinghua.edu.cn/hml) (2021 Fall, 2022 Fall, 2023 Fall).

## Personal

I am a cellist :violin: in the Tsinghua University Symphony Orchestra (TUSO). Check out our performance of [Symphony No. 8](https://www.bilibili.com/video/BV1Yh4y1g7t7) by [Antonín Dvořák](https://en.wikipedia.org/wiki/Anton%C3%ADn_Dvo%C5%99%C3%A1k). I also like playing guitar :guitar: in daily life. I love music!


