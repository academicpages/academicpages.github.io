---
title: 'Project: How are we getting along with reverse-engineering the brain?'
date: 2022-05-18
permalink: /posts/2022/05/reversing-the-brain/
tags:
  - q-bio.nc
  - q-bio
  - reverse-engineering-the-brain
  - progress-studies
---

> "If you wish to make an apple pie from scratch, you must first invent the universe." - Carl Sagan

# Idea
I will reach out to biologists to understand the status, progress and experimental methods regarding all areas relevant to [mind uploading](https://en.wikipedia.org/wiki/Mind_uploading) and reproducing a human brain's algorithm in a computer.

# More details
A basic goal of neuroscience is to understand a human brain's development and activity well enough that one could, in principle, reproduce its abilities in a computer. On an atomic scale, the brain is described by known quantum-mechanical principles - so with the computing power found in thought experiments, such a simulation is possible if we have a sufficiently accurate description of [^10]

1. a human zygote, and
2. the environment in which that zygote develops into an adult human, inside and outside the womb.

I argue that, most likely, the greatest part of both of these "sufficiently accurate descriptions" exist today - and that a smartphone has enough memory to store them.

1. By the data on [human genome size](https://en.wikipedia.org/wiki/Human_genome), one can describe human DNA using less than 700 Megabytes. In fact, it is generally believed that not more than about 10 % of this DNA contains relevant information - the rest, called _junk DNA_, doesn't have a positive or negative effect on the organism's fitness. [^20] It is not clear how much relevant data is encoded differently (e.g. in the [epigenome](https://en.wikipedia.org/wiki/Epigenome), but it's fair to assume it's not a higher order of magnitude than the DNA).
2. Similarly, a human hears a few hundred Megabytes worth of spoken language (as text) before they turn 25 (and one would assume most of this doesn't change their mind); a few Megabytes are enough to encode the study material for a college degree. [^30] I think it's fair to assume that this is the order of magnitude of training data a human receives  total amount of data needed to train a human brain to intelligence is not manyStoring the raw visual data arriving in a brain over that time period would require more disk space - but congenitally blind people don't receive these, and end up with brains [just as impressive](https://research.gold.ac.uk/id/eprint/5415/1/Pring_&_Tadic_CBMPD_VI_Nassr.pdf) as those of anyone else when it comes to non-visual tasks. And of course, So while I am less confident of this than the other claim, I'd argue that megabyes _revelant


# Breaking down the problem: The omes
This concerns essentially all [arXiv quantitative biology subcategories](https://arxiv.org/archive/q-bio).

Consider a fresh zygote in a womb, about to develop into a human with a brain. What happens, and what do we need to understand?
1. _Gene expression_ and protein folding: Some part of the DNA encodes. We need to understand, and describes how it reacts to new . of the DNA encodes proteins. These need to be q-bio.BM
- protein expression and formation of biochemical pathways,
  - neural differentiation - which types of neurons exist, and how stem cells decide which one to become,
  - arborization - how neurons decide how to branch out and connect to each other,
  - neuron-level activity - how to model 
  - synaptic plasticity,
  - and overarching design principles.
The goal of the talk is not to explain all of neuroscience and microbiology - it is to give, for each level, a rough understanding of
  - the amount of yet-unknown data and insight versus the capabilities of current experimental methods,
  - how fast and (Moore-like) predictably we can expect these methods to improve,
  - and pointers to recent literature.

# Whom to ask?

# What to ask?

My plan is to ask people

[^10]: The algorithm is typically described as having a random component - nevertheless, a simulation must typically return a working human brain if a typical embryo develops into a brain as well. We are only interested in gathering enough data that one would typically obtain a working brain when replacing the remainder by randomness.

[^20]: According to [Wikipedia](https://en.wikipedia.org/wiki/Non-coding_DNA), less that 2 % of human DNA is _coding_, i.e. describes the amino acid sequences comprising proteins. Another 2-14 % seems to have some other functional role: This is evidenced by the fact that it mutates slower than the rest of the DNA, from which the conclusion is drawn that a mutation in these spots must typically have a negative effect on fitness. See [here](https://academic.oup.com/gbe/article/5/3/578/583411) for details. The rest is known as _junk DNA_.

[^30]: A college student taking 32 courses over the course of their degree, each of which is based on a 500-page book containing 250 words per page, studies 4 000 000 words in total. The original [word gap](https://en.wikipedia.org/wiki/Word_gap) studies resulted in 11.5 million words per year overheard by "an average child in a professional family", which would correspond to 290 million words over 25 years. A raw King James Bible, compressed with lzip, occupies 1.35 bytes/word of disk space.
