---
layout:     post
title:      "Eventual Serializability (1)"
subtitle:   "A critique of the application-level notions of correctness"
date:       2018-04-15 12:00:00
author:     "Kia Rahmani"
header-img: "img/post-bg-10.jpg"
---
##### [In this post I am going to challenge the current direction in the literature on the appropriate *notion of correctness* for distributed applications]


-----
### Prologue
Programmers have historically been interested in developing their programs assuming
fully isolated executions and single copies of (non-shared) data.
This (intuitive) tendency has been carried on through the decades, even after
multiprocessing and distributed systems became prominent, the strong notions
of consistency and isolation (e.g. linearizability and serializability) were
used extensively despite their relatively high costs.


However, in about a decade ago developers realized that things cannot stay the same way anymore:
providing such strong guarantees was simply not feasible, considering the unprecedented requirements of web-scale applications. Following the 2007 Amazon's DynameDB, a plethora of eventually consistent data stores emerged that completely stripped off almost all
concurrency control mechanisms
in favor of low latency and high availability, which  initially created a massive wave of excitement in the 
database users community: (at least some) people were convinced that they have
finally found the final ansewr to their scalability problem. However, this honeymoon phase didn't last long and posts like this started to appear on Hacker news:

![cise1](https://github.com/Kiarahmani/kiarahmani.github.io/raw/master/_posts/figures/hacker1.png
"CISE - EXAMPLE")



The community of system developers ([queit painfully](http://hackingdistributed.com/2014/04/06/another-one-bites-the-dust-flexcoin/))
realized that they have entered the wrong neighborhood and things (once again),
cannot stay like this any longer. This  was the beginning of a new movement in distributed systems research to offer
*additional* concurrency control mechanisms on top of these databases to keep
them still attractive while making the lives of the developers easier (e.g. [CRDT](https://arxiv.org/abs/0907.0929) and 
[HAT](https://dl.acm.org/citation.cfm?id=2735509)).

Although, the whole story sounds like people were just running around a circle,
the process was (is) taking place smartly; on one side system researchers are
designing well-engineered protocols offering *new notions of
fine-grained add-on concurrency control mechanisms* without fully sacrificing the performance, and on the other side, the PL community is using
program analysis techniques to *inject* these additional fine-grained guarantees as sparingly as possible: targeted concurrency control mechanisms must only be injected minimally until the programming semantics is lifted up enough for developers to be able to comfortably
write correct applications.

What follows is my understanding of the direction
that the second group of researchers took and my questions on if it was not the best one
possible. 


---
### Application-level integrity invariants
One of the currently prominent ideas in the literature on how the concurrency mechanisms injection should take place, is to decouple the task
of  program design and the task of assigning correct meaning to those
programs. The idea is to allow developers write their applications assuming a standard
semantics and (**then**)  specify their expectations from the program. Developers can then use program analysis tools to verify their programs correct *under
a particular choice of concurrency mechanisms* (mechanisms that are being *separately* developed by the first group
of researchers, which I think is a problem and I will write about it later).




**Cause I’m Strong Enough:
Reasoning about Consistency Choices in Distributed Systems [(POPL'16)](https://dl.acm.org/citation.cfm?id=2837625)**
<br> This work presents a modular reasoning framework to establish preservation of
high-level application invariants on a replicated eventually consistent system model under a 
particular choice of consistency guarantees assigned on a per-operation basis.

In the introduction, the paper uses the following example to argue that **certain**
anomalous behaviors in the applications are not problematic and the mean of separating 
the acceptable behaviors from the non-acceptable ones, is the notion of application level "integrity
invariants".

---
![cise1](https://github.com/Kiarahmani/kiarahmani.github.io/raw/master/_posts/figures/cise1.png
"CISE - EXAMPLE")
`"Alice and Bob concurrently make posts at r1 and r2. Carol, connected to r3 initially sees Alice’s post, but not Bob’s, and Dave, connected to r4, sees Bob’s post, but not Alice’s. This outcome cannot be obtained by executing the operations in any total order and, hence, deviates from strong consistency"`

However, it then continues:

`"Such anomalies related to the ordering of actions are often acceptable for
applications."`

They conclude from the above example that understanding such acceptable and
unacceptable cases (e.g. the concurrent withdrawals from a bank account) is far from being trivial that's why we have to equip
users with a language to specify their requirements such as "the account
balance to be always non-negative". <br>
However, they do not explain why they think writing application invariants 
in this way is an easy task; finding **all** sanity checks for  real-world
applications, at least to me, seems to be far from trivial. Forget about toy examples like bank account; 
can anybody specify what are **all** the application-level integrity requirements for TPC-C (besides the 12 
that are given in the spec)?


---
**Alone Together: Compositional Reasoning and Inference for Weak Isolation [(POPL'18)](https://dl.acm.org/citation.cfm?id=3158115)**
<br>
This paper uses a non-trivial proof technique to address the "challenging problem of verifying high-level correctness properties in weakly isolated environments".
Here, the main argument is that proving correctness of the applications assuming
serializable transactions is easy but it is non-trivial for weaker forms of
transactions.

As an example, authors present how a high-level consistency condition is preserved when running
the *new_order* transaction (from TPC-C) in [SI transactions](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/snapshot-isolation-in-sql-server), but is
violated under weaker forms of isolation and also how their tool can be useful to automatically generate formal proves
of such assertions.

However, one might ask the same question as before: what if a user misses some of the necessary high-level
invariants and by using this tool concludes that their implementation is correct under a certain isolation guarantee
and is good to be deployed?
Luckily, the question is answered toward the end of this paper:

` 
"Alternatively, a weakly isolated transaction T can be verified against a generic
serializability condition, eliminating the need for guarantee annotations."
`

This means that their annotation language is able to capture the high-level notion of generic serializability 
(i.e. equivalence of all interleaved execution to some serial execution) 
and verify it over different isolation guarantees. Now, this seems reasonable; we should certainly
use the weakest underlying transactional isolation guarantees if we are confident that no additional behavior will emerge compared to the strongly isolated case.

Unfortunately, the paper does not provide any evidence of the practical usability of their 
invariant specification language compared to this particuar notion of
correctness (generic serializability condition). All of their examples show that in order to preserve any intuitive high-level 
invariant, generic notion of serializability must also be satisfied and vice versa.

Now, the question that naturally follows is:
what is the point of performing all the intricate analysis techniques if at the end of
the day, in order to be certain about the correctness of our application, we
have to feed the tool with the classic notion of generic serializability? 
Couldn't you come up with a much easier proof technique, if you knew the input to your tool
is the good old notion of serializability? I don't know the ansewr; maybe not. Maybe there is no easier targeted proof technique to achieve the same only for serializability.

---
In the next blog post, I will present some insights on the above observations.











