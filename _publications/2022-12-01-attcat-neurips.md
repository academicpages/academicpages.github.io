---
title: "AttCAT: Explaining Transformers via Attentive Class Activation Tokens"
collection: publications
category: conferences
permalink: /publication/2022-12-01-attcat-neurips
excerpt: 'This paper presents AttCAT, a method for explaining transformer models using attentive class activation tokens.'
date: 2022-12-01
venue: 'Proceedings of the Thirty-sixth Conference on Neural Information Processing Systems (NeurIPS-22)'
authors: 'Qiang, Y., Pan, D., Li, C., Li, X., Jang, R., and Zhu, D.'
paperurl: 'https://proceedings.neurips.cc/paper_files/paper/2022/hash/20e45668fefa793bd9f2edf19be12c4b-Abstract-Conference.html'
citation: 'Qiang, Y., Pan, D., Li, C., Li, X., Jang, R., and Zhu, D. (2022). &quot;AttCAT: Explaining Transformers via Attentive Class Activation Tokens.&quot; <i>In the Proceedings of Thirty-sixth Conference on Neural Information Processing Systems (NeurIPS-22)</i>.'
---

**Abstract:**
Transformers have improved the state-of-the-art in various natural language processing and computer vision tasks. However, the success of the Transformer model has not yet been duly explained. Current explanation techniques, which dissect either the self-attention mechanism or gradient-based attribution, do not necessarily provide a faithful explanation of the inner workings of Transformers due to the following reasons: first, attention weights alone without considering the magnitudes of feature values are not adequate to reveal the self-attention mechanism; second, whereas most Transformer explanation techniques utilize self-attention module, the skip-connection module, contributing a significant portion of information flows in Transformers, has not yet been sufficiently exploited in explanation; third, the gradient-based attribution of individual feature does not incorporate interaction among features in explaining the model's output. In order to tackle the above problems, we propose a novel Transformer explanation technique via attentive class activation tokens, aka, AttCAT, leveraging encoded features, their gradients, and their attention weights to generate a faithful and confident explanation for Transformer's output. Extensive experiments are conducted to demonstrate the superior performance of AttCAT, which generalizes well to different Transformer architectures, evaluation metrics, datasets, and tasks, to the baseline methods. Our code is available at: https://github. com/qiangyao1988/AttCAT.
