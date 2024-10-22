---
title: "RuMono: Fuzz Driver Synthesis for Rust Generic APIs"
collection: publications
category: manuscripts
permalink: /publication/2023-rumono
excerpt: "Fuzzing is a popular technique for detecting bugs, which can be extended to libraries by constructing executables that call library APIs, known as fuzz drivers. Automated fuzz driver synthesis has been an important research topic in recent years since it can facilitate the library fuzzing process. Nevertheless, existing approaches generally ignore generic APIs or simply treat them as non-generic APIs. As a result, they cannot generate effective fuzz drivers for generic APIs. \nThis paper explores the challenge of automating fuzz driver synthesis for Rust libraries with generic APIs. The problem is essential because Rust prioritizes security and generic APIs are widely employed in Rust libraries. We propose a novel approach and develop a prototype, RuMono, to tackle the problem. Our approach initially infers API reachability from the generic API dependency graph, discovering the reachable and valid monomorphic APIs within the library. Further, we apply a similarity-based filter to eliminate redundant monomorphic APIs. Experimental results from 29 popular open-source libraries demonstrate that RuMono can achieve promising generic API coverage with a low rate of invalid fuzz drivers. Besides, we have identified 23 bugs previously unknown in these libraries, with 18 related to generic APIs."
date: 2023-12-17
venue: Arxiv
slidesurl: 
paperurl: 'https://arxiv.org/abs/2312.10676'
citation: 'Zhang, Yehong, Jun Wu, and Hui Xu. "Fuzz Driver Synthesis for Rust Generic APIs." arXiv preprint arXiv:2312.10676 (2023).'
---

Our tool and bug report are public available at GitHub! You can click the following links to visit:
- [RuMono](https://github.com/Artisan-Lab/RULF/tree/RuMono)
- [Bug Report](https://github.com/Artisan-Lab/RuMono-Bugs)

Fuzzing is a widely-used technique for detecting software vulnerabilities. This technique can be extended for API testing by constructing the API sequence within the tested API. Recently, automated fuzz driver synthesis has gained significant attention due to its potential to streamline and enhance the fuzzing process. Rust is an emerging programming language focusing on efficiency and memory safety. Nevertheless, existing approaches of fuzz driver synthesis offer limited support for generics, a crucial language feature in Rust, resulting in low API coverage for Rust libraries. This is a significant concern given Rust's emphasis on memory safety and generics are widely employed in Rust libraries.

This paper investigates the challenge of fuzz driver synthesis for Rust libraries with generic APIs. To tackle the problem, we propose a novel approach that introduces the generic API dependency graph to model the dependencies among generic APIs. Using the graph, we propose a novel approach to transform generic APIs into multiple monomorphic APIs, involving two algorithms: reachable monomorphic API search and similarity pruning. The reachable monomorphic API search algorithm infers API reachability from the graph and discovers all possible monomorphic APIs that are valid and reachable. To enhance fuzzing efficiency, the similarity pruning algorithm defines similarity by sharing trait implementations between two monomorphic APIs and filter redundant monomorphic APIs by their similarity. 

We have developed a prototype named RuMono and evaluated its performance on 29 popular open-source libraries. Our experimental results demonstrate that RuMono achieves promising generic API coverage and detect bugs hidden in generic APIs. Specifically, we identified 23 previously unknown bugs, 18 of which are related to generic APIs. Additionally, a case study highlights RuMono's capability to detect multiple bugs hidden in a generic API that can only be triggered in different monomorphic APIs derived from it.
