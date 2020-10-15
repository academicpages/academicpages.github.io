---
title: "Rainblock: Faster Transaction Processing in Public Blockchains"
collection: publications
permalink: /publication/2019-09-25-rainblock
excerpt: 'Public blockchains like Ethereum use Merkle trees to verify transactions received from untrusted servers before applying them to
the blockchain. We empirically show that the low throughput of
such blockchains is due to the I/O bottleneck associated with using
Merkle trees for processing transactions. We present RainBlock,
a new architecture for public blockchains that increases throughput without affecting security. RainBlock achieves this by tackling
the I/O bottleneck on two fronts: first, decoupling transaction processing from I/O and removing I/O from the critical path; second,
reducing I/O amplification by customizing storage for blockchains.
RainBlock uses a novel variant of the Merkle tree, the Distributed,
Sharded Merkle Tree (DSM-Tree) to store system state. We evaluate RainBlock using workloads based on public Ethereum traces
(including smart contracts) and show that RainBlock processes
20K transactions per second in a geo-distributed setting with four
regions spread across three continents.'
date: 2019-09-25
venue: 'ArXiv'
paperurl: 'https://arxiv.org/pdf/1909.11590.pdf'
citation: 'Ponnapalli, Soujanya, Aashaka Shah, Amy Tai, Souvik Banerjee, Vijay Chidambaram, Dahlia Malkhi, and Michael Wei. "Rainblock: Faster Transaction Processing in Public Blockchains" arXiv preprint arXiv:1909.11590 (2019).'
---

Public blockchains like Ethereum use Merkle trees to verify transactions received from untrusted servers before applying them to
the blockchain. We empirically show that the low throughput of
such blockchains is due to the I/O bottleneck associated with using
Merkle trees for processing transactions. We present RainBlock,
a new architecture for public blockchains that increases throughput without affecting security. RainBlock achieves this by tackling
the I/O bottleneck on two fronts: first, decoupling transaction processing from I/O and removing I/O from the critical path; second,
reducing I/O amplification by customizing storage for blockchains.
RainBlock uses a novel variant of the Merkle tree, the Distributed,
Sharded Merkle Tree (DSM-Tree) to store system state. We evaluate RainBlock using workloads based on public Ethereum traces
(including smart contracts) and show that RainBlock processes
20K transactions per second in a geo-distributed setting with four
regions spread across three continents.

[Download paper here](https://arxiv.org/pdf/1909.11590.pdf)

Ponnapalli, Soujanya, Aashaka Shah, Amy Tai, Souvik Banerjee, Vijay Chidambaram, Dahlia Malkhi, and Michael Wei. "Rainblock: Faster Transaction Processing in Public Blockchains" arXiv preprint arXiv:1909.11590 (2019).
