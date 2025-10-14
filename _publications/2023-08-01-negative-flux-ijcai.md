---
title: "Negative Flux Aggregation to Estimate Feature Attributions"
collection: publications
category: conferences
permalink: /publication/2023-08-01-negative-flux-ijcai
excerpt: 'This paper proposes negative flux aggregation for estimating feature attributions in neural networks.'
date: 2023-08-01
venue: 'Proceedings of the 32nd International Joint Conference on Artificial Intelligence (IJCAI-23)'
authors: 'Li, X., Pan, D., Li, C., Qiang, Y., and Zhu, D.'
paperurl: 'https://www.ijcai.org/proceedings/2023/0050.pdf'
citation: 'Li, X., Pan, D., Li, C., Qiang, Y. and Zhu, D. (2023). &quot;Negative Flux Aggregation to Estimate Feature Attributions.&quot; <i>In the Proceedings of 32nd International Joint Conference on Artificial Intelligence (IJCAI-23)</i>, Macao, China.'
---

**Abstract:**
There are increasing demands for understanding deep neural networks' (DNNs) behavior spurred by growing security and/or transparency concerns. Due to multi-layer nonlinearity of the deep neural network architectures, explaining DNN predictions still remains as an open problem, preventing us from gaining a deeper understanding of the mechanisms. To enhance the explainability of DNNs, we estimate the input feature's attributions to the prediction task using divergence and flux. Inspired by the divergence theorem in vector analysis, we develop a novel Negative Flux Aggregation (NeFLAG) formulation and an efficient approximation algorithm to estimate attribution map. Unlike the previous techniques, ours doesn't rely on fitting a surrogate model nor need any path integration of gradients. Both qualitative and quantitative experiments demonstrate a superior performance of NeFLAG in generating more faithful attribution maps than the competing methods. Our code is available at [GitHub](https://github.com/xinli0928/NeFLAG)
