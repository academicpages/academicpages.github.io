---
title: "Energy CodeSumption, Leveraging Test Execution for Source Code Energy Consumption Analysis"
collection: publications
category: conferences
permalink: /publication/2025-06-27-paper-energy-codesumption
excerpt:
date: 2025-06-27
venue: 'Proceedings of the 33rd ACM International Conference on the Foundations of Software Engineering (FSE Companion ’25)'
paperurl: 'https://jeromemaquoi.github.io/files/maquoi-2025.pdf'
slideurl: 'https://jeromemaquoi.github.io/files/maquoi-2025-slides.pdf'
citation:
authors: Jérôme Maquoi, Maxime Cauz, Benoît Vanderose, Xavier Devroey
---
[Paper](https://jeromemaquoi.github.io/files/maquoi-2025.pdf),
[DOI](https://doi.org/10.1145/3696630.3728707),
[Replication Package](https://zenodo.org/records/15276280),
[Slides](https://jeromemaquoi.github.io/files/maquoi-2025-slides.pdf)

## Abstract
The software engineering community has increasingly recognized sustainability as a key research area. However, developers often have limited knowledge of effective strategies to reduce software energy consumption. To address this, we analyze energy consumption in software execution, aiming to raise developer awareness by linking energy consumption with each line of code. We rely on unit test executions to identify energy-intensive executions and manually analyze five hot and five cold spots to identify potentially energy-intensive source code constructs. Our findings suggest a link between the energy consumption of the source code and the number of objects’ attributes created within that code. These results lay the groundwork for further analysis of the relationship between object instantiation and energy consumption in Java.