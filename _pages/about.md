---
permalink: /
title: "Self-introduction"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<font size=3>I am final-year PhD student at the Chinese University of Hong Kong (CUHK) supervised by Prof.</font> [<font size=3>Soung Chang Liew</font>] (https://www.ie.cuhk.edu.hk/faculty/LIEW-Soung-Chang/). <font size=3>I received my bachelor’s degree in electronic engineering from Peking University (PKU) supervised by Prof.</font> [<font size=3>Yiming Lei</font>](https://ele.pku.edu.cn/dzxxen/info/1023/1115.htm). <font size=3>I am currently a visiting scholar at Prof. Minlan Yu’s group at</font> [<font size=3>Harvard SEAS</font>](https://minlanyu.seas.harvard.edu/index.html). <font size=3>Before starting my PhD at CUHK, I worked as a communication engineer at 2012 Lab, Huawei, where I participated in the development of</font> [<font size=3>Kirin9000 5G SoC</font>](https://www.hisilicon.com/en/products/Kirin/Kirin-flagship-chips/Kirin-9000)<font size=3>, with a focus on 5G modem power efficiency.</font>  

<font size=3>I have a comprehensive research interest, ranging from RF circuit analysis, ultra-reliable low-latency communication (URLLC), and the interdisciplinary research on generative AIs and networking systems. Recently, I am highly interested in the efficient deployment and inference of MoE model at edge.</font>  
<br>
**<font size=3>I am on the job market and looking for research positions in both industry and academia.</font>**

Publications <font size=3>(17 papers, with 16 first/co-first/corresponding authors)</font>
------
**Journals**
* Du, Y., Liew, S.C., "Reliable Packet Detection for Random Access Networks: Analysis, Benchmark, and
Optimization." IEEE Transactions on Vehicular Technology (2025).
* Cui, H.*, Du, Y.*, Yang, Q.*, Shao, Y., Liew, S. C., "LLMind: Orchestrating AI and IoT with LLMs for complex task execution." IEEE Communications Magazine (2024).
* Du, Y., Hao, L., Lei, Y., "Nonlinear Multi-Carrier System with Signal Clipping: Measurement, Analysis, and Optimization." IEEE Systems Journal (2024).
* Du, Y., Liew, S.C., Shao, Y., "Efficient FFT computation in IFDMA transceivers." IEEE Transactions on Wireless Communications (2023).
* Du, Y., Hao, L., Lei, Y., "SER Optimization in OFDM-IM Systems with Nonlinear Power Amplifiers." IEEE Transactions on Vehicular Technology (2023).
* Du, Y., Lei, Y., McGrath, S., "SER optimization in transparent OFDM relay systems in the presence of dual nonlinearity." Digital Signal Processing (2022).
* Du, Y.*, Chen, J.*, Lei, Y., Hao, X., "Performance analysis of nonlinear spatial modulation multiple-input multiple-output systems." Digital Signal Processing (2021).
* Shao, Y., Liew, S.C., Chen, H., Du, Y., "Flow sampling: Network monitoring in large-scale software-defined IoT networks." IEEE Transactions on Communications (2021).

**Conferences**
* Wang, L.*, Du, Y.*, Lin, J*., Chen, K., Liew, S. C. "Rephrase and Contrast: Fine-Tuning Language Models for Enhanced Understanding of Communication and Computer Networks." IEEE ICNC 2025.
* Zhang, F.*, Du, Y.*, Chen, K.*, Shao, Y., Liew, S. C., "Addressing Out-of-Distribution Challenges in Image Semantic Communication Systems with Multi-modal Large Language Models." IEEE/IFIP WiOpt 2024.
* Chen, K.*, Du, Y.*, You, T., Islam, M., Guo, Z., Jin, Y., Chen, G., Heng, P.A. "LLM-Assisted Multi-Teacher Continual Learning for Visual Question Answering in Robotic Surgery." IEEE ICRA 2024.
* Du, Y., Deng, H., Liew, S. C., Chen, K., Shao, Y., Chen, H., "The power of large language models for wireless communication system development: A case study on FPGA platforms." IEEE VTC 2024.
* Du, Y., Hao, L., Lei, Y., "SER Analysis and Joint Optimization in Nonlinear MIMO-OFDM Systems with
Clipping." IEEE VTC 2023.
Du, Y., Hao, L., Liu, Z., Chen, Y., Lei, Y., "Ergodic Rate Performance in Nonlinear Omnidirectional Coding MIMO-OFDM Systems." IEEE UEMCON 2019.

**Preprints**
* Zhang, Y., Chen, X., Chen, K., Du, Y.#, Dang, X., et al, "The Dual-use Dilemma in LLMs: Do Empowering Ethical Capacities Make a Degraded Utility?." arXiv:2501.xxxxx (2025).
* Chen, K., Cao, H., Li, J., Du, Y.#, Guo, M., Zeng, X., et al, "An autonomous large language model agent for chemical literature data mining." arXiv:2402.12993 (2024).
* Chen, K., Li, J., Wang, K., Du, Y.#, Yu, J., Lu, J., et al, " Chemist-X: Large Language Model-empowered Agent for Reaction Condition Recommendation in Chemical Synthesis." arXiv:2311.10776 (2023)


Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

The repository includes [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the Academic Pages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring Academic Pages can be found in [the guide](https://academicpages.github.io/markdown/), the [growing wiki](https://github.com/academicpages/academicpages.github.io/wiki), and you can always [ask a question on GitHub](https://github.com/academicpages/academicpages.github.io/discussions). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
