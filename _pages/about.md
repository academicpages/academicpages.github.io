---
permalink: /
title: "ABOUT ME"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

My name is Kia Rahmani and I am a 4<sup>th</sup> year PhD student of computer science at Purdue University. 
I am a member of the [programming languages group](https://purduepl.github.io/), 
working under the supervison of Professor [Suresh Jagannathan](https://www.cs.purdue.edu/homes/suresh/).
The main topics of my reseach interests include formal methods of modeling, analysis and verification of applications. 
I specifically focuse on automated generation of
verifiably correct and scalable distributed (database-backed) applications.




## Projects
### Sound Static Detection of Bugs in Highly Scalable Distributed Applications for Weakly Consistent Databases:
To be written.


### Enforcement of finde-grained consistency guarantees using effect orchestration:
Non-deterministic behaviors arise in weakly consistent data stores which can potentially
violate application correctness, forcing designers to either implement (very complex) ad-hoc
mechanisms to avoid these anomalies, or choose to run applications using stronger levels of
consistency than necessary. In this project, we introduced a lightweight runtime verification
system that relieves developers from having to make such tradeoffs. We leveraged declarative
axiomatic specifications that reflect the necessary constraints any correct implementation
must satisfy to guide a runtime consistency enforcement. Experimental results show that
the performance of our automatically derived mechanisms is better than both specialized
hand-written protocols and common store-offered consistency guarantees.

### Coq Implementation of Quelea:
In this project, I formalized and implemented the
operational semantics used in the PLDI'15 paper, [Declarative Programming
over Eventually Consistent Data Stores](https://dl.acm.org/citation.cfm?id=2737981) in the [Coq proof assistant](https://coq.inria.fr/). Even though the mere
goal of the project was to familiarize myself with proof assistants and formal language definition, I was able to point out numerous previously unknown problems in the paper foe which I offered fixes as well. 
The Coq implementation and the fixes were later used as a supplementary material for
the original paper [(source code)](https://github.com/Kiarahmani/Quelea_Coq_Imp).

## Publications
<ul>
    <li>Fine-grained Distributed Consistency Guarantees with Effect Orchestration
    <br />
    <font size="3">
      (with Gowtham Kaki and Suresh Jagannathan)
    </font>
    <br />
    <font size="2">
    <a href= "https://dl.acm.org/citation.cfm?id=3194267"> 
      [Workshop on the Principles and Practice of Consistency for Distributed Data (Portugal-April 2018)]
    </a >
    <font size="1"> <br /> </font>
   <a href="http://docs.lib.purdue.edu/cstech/1780/">
     [Tech Report]
   </a>
   <a href="/files/papoc-18.pdf">
     [Slides]
   </a>

    
    </font>
    </li>
</ul>





