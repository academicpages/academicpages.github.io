---
title: "Refinement and Verification of CBC Casper"
collection: publications
permalink: /publication/2019-06-24-refinement
excerpt: 'Formal verification of CBC Casper in Isabelle/HOL.'
date: 2019-06-24
venue: '2019 Crypto Valley Conference on Blockchain Technology'
paperurl: 'https://eprint.iacr.org/2019/415'
citation: 'Ryuya Nakamura, Takayuki Jimba and Dominik Harz. (2019). &quot;Refinement and Verification of CBC Casper.&quot; <i>CVCBT 2019</i>.'
---

Isabelle proofs are available at [GitHub](https://github.com/LayerXcom/cbc-casper-proof).

Decentralised ledgers are a prime application case for consensus protocols. Changing sets of validators have to agree on a set of transactions in an asynchronous network and in the presence of Byzantine behaviour. Major research efforts focus on creating consensus protocols under such conditions, with proof-of-stake (PoS) representing a promising candidate. PoS aims to reduce the waste of energy inherent to proof-of-work (PoW) consensus protocols. However, a significant challenge is to get PoS protocols "right", i.e. ensure that they are secure w.r.t. safety and liveness. The "Correct-by-Construction" (CBC) Casper approach by the Ethereum project employs pen-and-paper proofs to ensure its security. CBC Casper is a framework to define consensus protocols and aims to prove safety without loss of abstractness. Each member of the CBC Casper family of protocols is defined by five parameters. CBC Casper models the protocol by a state of each validator and messages sent by validators. Each validator can transition its state using messages by other validators that include their current consensus value and a justification (i.e. their previous messages). We extend CBC Casper in three ways. First, we summarise the research of CBC Casper and extend the definitions of safety and liveness properties. To this end, we discuss an instance of CBC Casper called Casper The Friendly GHOST (TFG), a consensus protocol using a variant of the GHOST fork-choice rule. Second, we refine the properties of messages and states in CBC Casper and give a definition of blockchain safety for Casper TFG. Third, we formally verify the CBC Casper framework together with our refined message and state properties as well as our blockchain safety definition in the Isabelle/HOL proof assistant.