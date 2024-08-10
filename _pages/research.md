---
layout: single
title: "Research Interests"
permalink: /research/
author_profile: true
---
My research focuses on **AI Chip and System**, with the following directions:
* [Computing-in-Memory Architecture for Emerging AI Applications](#computing-in-memory-architecture-for-emerging-ai-applications)
* [Reconfigurable AI Chip Architecture](#reconfigurable-ai-chip-architecture)
* [Agile Development for AI Chips](#agile-development-for-ai-chips) 

I have an AI chip-related paper collection at [Neural Networks on Silicon](https://github.com/fengbintu/Neural-Networks-on-Silicon), which is helpful for students to learn the history and SOTA of AI chip and system research.

## Computing-in-Memory Architecture for Emerging AI Applications
[Apr. 2024] **ISSCC'24 Insights for Emerging AI Computing.**
- I was invited by JOS to review the research highlights on machine learning accelerators in ISSCC'24. We observed four research trends toward efficient generative AI (ML Chips for Generative AI, and CIM Innovation from Circuits to Systems) and beyond-AI computing (DSA for Embedded Vision Processors, and DSA for Solver Accelerators). We believe these remarkable trends will lead to more AI software and hardware innovations from academia and industry in the near future.
- [Towards Efficient Generative AI and Beyond-AI Computing: New Trends on ISSCC 2024 Machine Learning Accelerators](http://www.jos.ac.cn/en/article/doi/10.1088/1674-4926/45/4/040204) (**JOS'24, Invited Paper**)

[Feb. 2023] **Scaling-out CIM for Large-scale AI and Beyond-AI Applications.**
- I designed two 28nm chips that scale out the AI capability based on Reconfigurable Digital CIM. TensorCIM is the first CIM processor for tensor computing in a Multi-Chip-Module system. MulTCIM is the first CIM accelerator for the emerging multimodal Transformer models, which leverages attention-token-bit hybrid sparsity to improve energy efficiency.
- [TensorCIM: A 28nm 3.7nJ/Gather and 8.3TFLOPS/W FP32 Digital-CIM Tensor Processor for MCM-CIM-based Beyond-NN Acceleration](https://ieeexplore.ieee.org/abstract/document/10067285) (**ISSCC'23**, extended to [**JSSC'24**](https://ieeexplore.ieee.org/document/10555118))
- [MulTCIM: A 28nm 2.24uJ/Token Attention-Token-Bit Hybrid Sparse Digital CIM-based Accelerator for Multimodal Transformers](https://ieeexplore.ieee.org/abstract/document/10067842) (**ISSCC'23**, extended to [**JSSC'24**](https://ieeexplore.ieee.org/document/10226612))

[Feb. 2022] **Reconfigurable Digital Computing-in-Memory (CIM) AI Chip.**
- I designed an innovative AI chip architecture, Reconfigurable Digital CIM. The architecture fuses the philosophy of reconfigurable computing and digital CIM, balancing efficiency, accuracy, and flexibility for emerging AI chips. I designed two 28nm chips based on the new architecture, Reconfigurable Digital CIM (ReDCIM) and Transformer CIM (TranCIM). ReDCIM (pronounced as "red-CIM") is the first CIM chip for cloud AI with flexible FP/INT support, which was covered by [Synced](https://mp.weixin.qq.com/s/v82Bt99l43S6Kegf83_q6A). TranCIM is the first CIM chip for Transformer models, which tackles the memory and computation challenges raised by Transformer's attention mechanism.
- ReDCIM: [A 28nm 29.2TFLOPS/W BF16 and 36.5TOPS/W INT8 Reconfigurable Digital CIM Processor with Unified FP/INT Pipeline and Bitwise in-Memory Booth Multiplication for Cloud Deep Learning Acceleration](https://ieeexplore.ieee.org/document/9731762) (**ISSCC'22**, extended to [**JSSC'23**](https://ieeexplore.ieee.org/document/9968289))
  - ReDCIM was awarded the [2023 Top-10 Research Advances in China Semiconductors](https://mp.weixin.qq.com/s?__biz=MzA4OTY2Njc1Nw==&mid=2650731796&idx=1&sn=20715157349e7b05c33a499bfb3ff49b&chksm=881d30bebf6ab9a891cc54bc66f95126fbaf295b2df5121a91b8fe95029ecde29237719e9ac8&mpshare=1&scene=2&srcid=0205egurWwnMVy5QKhWrR1d3&sharer_shareinfo=0a5e68f5bd8e867fbaa555ede0957cef&sharer_shareinfo_first=9d0438640e200e56fc5ef6d3473b320a#rd), which was featured by [ACCESS](https://www.linkedin.com/posts/inno-accesshk_access-hkust-access-activity-7161248635551125505-VcrD/?utm_source=share&utm_medium=member_desktop) and [HKUST SENG News](https://seng.hkust.edu.hk/news/20240228/reconfigurable-digital-computing-memory-ai-chip-ece-professors-selected-chinas-2023-top-10-research-advances-semiconductors).
- TranCIM: [A 28nm 15.59uJ/Token Full-Digital Bitline-Transpose CIM-based Sparse Transformer Accelerator with Pipeline/Parallel Reconfigurable Modes](https://ieeexplore.ieee.org/document/9731645) (**ISSCC'22**, extended to [**JSSC'23**](https://ieeexplore.ieee.org/document/9931922))

## Reconfigurable AI Chip Architecture
[Aug. 2020] **Evolver, Evolvable AI Chip.**
- I designed a 28nm evolvable AI chip (Evolver) with DNN training and reinforcement learning capabilities, to enable intelligence evolution during the chip's long lifetime. This work demonstrates a lifelong learning example of on-device quantization-voltage-frequency (QVF) tuning. Compared with conventional QVF tuning that determines policies offline, Evolver makes optimal customizations for varying local user scenarios. 
- [Evolver: A Deep Learning Processor with On-Device Quantization-Voltage-Frequency Tuning](https://ieeexplore.ieee.org/document/9209075) (**JSSC'21**)
  - Evolver won the [Nomination Award for 2021 Top-10 Research Advances in China Semiconductors](https://mp.weixin.qq.com/s/Sad4Kc9lP8XW9vebdt7KaA).

[Jun. 2018] **RANA, Software-Hardware Co-design for AI Chip Memory Optimization.**
- I designed a retention-aware neural acceleration (RANA) framework, which strengthens AI chips with high-density eDRAM, while eliminating eDRAM refresh operations to improve system energy efficiency.
- [RANA: Towards Efficient Neural Acceleration with Refresh-Optimized Embedded DRAM](https://ieeexplore.ieee.org/document/8416839/) (**ISCA'18**)   
  - RANA was the **only** work first-authored by a Chinese research team in ISCA'18, which was covered by [Tsinghua University News](https://www.tsinghua.edu.cn/info/1175/19449.htm) and [AI Tech Talk](https://www.leiphone.com/news/201806/wFQ2Sc52Utikcl8D.html).

[Apr. 2017] **Thinker and DNA, Reconfigurable AI Chip.**
- I designed a deep convolutional neural network accelerator (DNA) targeting flexible and efficient CNN acceleration. This is the first work to assign Input/Output/Weight Reuse to different layers of a CNN, which optimizes system-level energy consumption based on different CONV parameters. Based on the DNA architecture, We designed a 65nm reconfigurable multi-modal neural network processor (Thinker) supporting CNN, RNN, and FCN. 
- DNA: [Deep Convolutional Neural Network Architecture with Reconfigurable Computation Patterns](http://ieeexplore.ieee.org/document/7898402/) (**TVLSI No.5/2/6/8/8/9 Downloaded Manuscripts in 2017~2022, 6 Times Monthly No.1 Popular Article**)  
- Thinker: [A High Energy Efficient Reconfigurable Hybrid Neural Network Processor for Deep Learning Applications](http://ieeexplore.ieee.org/document/8207783/) (**JSSC'18**)   
  - Thinker was exhibited at the [2016 National Mass Innovation and Entrepreneurship Week](https://www.tsinghua.edu.cn/info/1173/18061.htm), as a representative work from Tsinghua University. The Thinker chip was highly praised by Chinese Premier Li Keqiang, and featured by Yang Lan One on One, [AI Tech Talk](https://www.leiphone.com/news/201705/8sB0WHz6D70J7NAy.html) and [MIT Technology Review](https://www.technologyreview.com/s/609954/china-wants-to-make-the-chips-that-will-add-ai-to-any-gadget/?from=timeline&isappinstalled=0). It won the [ISLPED'17 Design Contest Award](http://islped.org/2017/index.php), which was [the first time that a China Mainland team won this contest](https://www.tsinghua.edu.cn/info/1175/19744.htm).

[Oct. 2014] **RNA, Reconfigurable Architecture for Neural Approximation.**
- I designed a reconfigurable neural accelerator (RNA) to process multi-layer perceptron (MLP) for neural approximation. By approximating the core kernels in a program with MLP, RNA achieves higher performance and efficiency with negligible accuracy loss.
- RNA: [Reconfigurable Architecture for Neural Approximation in Multimedia Computing](http://ieeexplore.ieee.org/document/8307081/) (**TCSVT'19**)
     
## Agile Development for AI Chips
[Jul. 2023] **AutoDCIM, Automated Digital CIM Macro Compiler.**
- I worked with ACCESS and developed AutoDCIM, the first automated digital CIM (DCIM) macro compiler. AutoDCIM takes the user specifications as inputs and generates a DCIM macro architecture with an optimized layout. With the growing interest in the DCIM field, AutoDCIM will play an important role in agile DCIM implementation and developing an ecosystem for DCIM-based AI computing.
- [AutoDCIM: An Automated Digital CIM Compiler](https://ieeexplore.ieee.org/document/10247976) (**DAC'23**)
