---
title: "causalAssembly: Generating Realistic Production Data for Benchmarking Causal Discovery

"
collection: publications
permalink: /publication/causalassembly
excerpt: 'Algorithms for causal discovery have recently undergone rapid advances and increasingly draw on flexible nonparametric methods to process complex data. With these advances comes a need for adequate empirical validation of the causal relationships learned by different algorithms. However, for most real and complex data sources true causal relations remain unknown. This issue is further compounded by privacy concerns surrounding the release of suitable high-quality data. To tackle these challenges, we introduce causalAssembly
, a semisynthetic data generator designed to facilitate the benchmarking of causal discovery methods. The tool is built using a complex real-world dataset comprised of measurements collected along an assembly line in a manufacturing setting. For these measurements, we establish a partial set of ground truth causal relationships through a detailed study of the physics underlying the processes carried out in the assembly line. The partial ground truth is sufficiently informative to allow for estimation of a full causal graph by mere nonparametric regression. To overcome potential confounding and privacy concerns, we use distributional random forests to estimate and represent conditional distributions implied by the ground truth causal graph. These conditionals are combined into a joint distribution that strictly adheres to a causal model over the observed variables. Sampling from this distribution, causalAssembly
 generates data that are guaranteed to be Markovian with respect to the ground truth. Using our tool, we showcase how to benchmark several well-known causal discovery algorithms.'
date: 2024-04-01
venue: Proceedings of Machine Learning Research (PMLR)
paperurl: 'https://proceedings.mlr.press/v236/gobler24a.html'
citation: 'Göbler, K., Windisch, T., Drton, M., Pychynski, T., Roth, M. &amp; Sonntag, S.. (2024). causalAssembly: Generating Realistic Production Data for Benchmarking Causal Discovery. <i>Proceedings of the Third Conference on Causal Learning and Reasoning</i>, in <i>Proceedings of Machine Learning Research</i> 236:609-642 Available from https://proceedings.mlr.press/v236/gobler24a.html.'
---
