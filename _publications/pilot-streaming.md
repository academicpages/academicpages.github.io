---
title: "Pilot-Streaming: A Stream Processing Framework for High-Performance Computing"
collection: publications
permalink: /publication/pilot-streaming
excerpt: 'This paper is about stream processing  on HPC environments'
date: 2018-01-26
paperurl: 'https://arxiv.org/pdf/1801.08648.pdf'
citation: 'Andre Luckow,  George Chantzialexiou, Shantenu Jha
Pilot-Streaming: A Stream Processing Framework for High-Performance Computing
---

## Abstract:
An increasing number of scientific applications rely on stream processing for generating timely insights from data feeds of scientific instruments, simulations, and Internet-of-Thing (IoT) sensors. The 
development of streaming applications is a complex task and requires the integration of heterogeneous, distributed infrastructure, frameworks, middleware and application components. Different application components are often written in different languages
using different abstractions and frameworks. Often, additional components, such as a message broker (e. g. Kafka), are required to decouple data production and consumptions and avoiding issues,
such as back-pressure. Streaming applications may be extremely dynamic due to factors, such as variable data rates caused by the data source, adaptive sampling techniques or network congestions, variable processing loads caused by usage of different machine 
learning algorithms. As a result application-level resource management that can respond to changes in one of these factors is critical. We propose Pilot- Streaming, a framework for supporting streaming
frameworks, applications and their resource management needs on HPC infrastructure. Pilot-Streaming is based on the Pilot-Job concept and enables developers to manage distributed computing and data resources for complex streaming applications. It enables
applications to dynamically respond to resource requirements by adding/removing resources at runtime. This capability is critical for balancing complex streaming pipelines. To address the complexity
in developing and characterization of streaming applications, we present the Streaming Mini- App framework, which supports different plug-able algorithms for data generation and processing, e. g.,
for reconstructing light source images using different techniques. We utilize the Mini-App framework to conduct an evaluation of the Pilot-Streaming capabilities.
