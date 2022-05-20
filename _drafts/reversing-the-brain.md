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
Human neuroscience is concerned with understanding how a human's brain develops and works. Various parts of this task quite closely to [arXiv quantitative biology subcategories](https://arxiv.org/archive/q-bio):

1. The brain starts out being a zygote in a womb; we need to determine its DNA and all other data relevant to simulating it (i.e. which proteins surround that DNA).
2. Some part of the DNA - [less than 2 % in humans](https://en.wikipedia.org/wiki/Human_genome) - encodes proteins. In as far as they are relevant to the brain, we need to understand how the finished proteins look like, what chemical reactions they are involved in, and the reaction rates.
3. This is enough for 
- protein expression and formation of biochemical pathways,
  - neural differentiation - which types of neurons exist, and how stem cells decide which one to become,
  - arborization - how neurons decide how to branch out and connect to each other,


  - neuron-level activity - how to model 
  - synaptic plasticity,


  - and overarching design principles.

All of these
The goal of the talk is not to explain all of neuroscience and microbiology - it is to give, for each level, a rough understanding of
  - the amount of yet-unknown data and insight versus the capabilities of current experimental methods,
  - how fast and (Moore-like) predictably we can expect these methods to improve,
  - and pointers to recent literature.


Understanding this at the various scales corresponds to the :



# It can't be that hard, or... can it?
On an atomic scale, the brain is described by known quantum-mechanical principles - so with the computing power found in thought experiments, such a simulation is possible if we have a sufficiently accurate description of [^10]

1. a human zygote, and
2. the environment in which that zygote develops into an adult human, inside and outside the womb.

The amount of information in these "sufficiently accurate descriptions" upper-bounds the information needed to describe a functional adult human brain (when ignoring pseudorandom character traits). I argue that obtaining them is mostly a solved problem today, and the quantity

1. By the data on [human genome size](https://en.wikipedia.org/wiki/Human_genome), storing the human genome requires less than 700 megabytes. In fact, it is generally believed that not more than about 10 % of this DNA contains relevant information - the rest, called _junk DNA_, doesn't have a positive or negative effect on the organism's fitness. [^20] It is not clear how much relevant data is encoded differently (e.g. in the [epigenome](https://en.wikipedia.org/wiki/Epigenome), but it seems fair to me to assume it's not a higher order of magnitude than the DNA.
3. Similarly, a human hears a few hundred megabytes worth of language before they turn 25 (and, according to many parents, most of this doesn't change their mind); a few megabytes are enough to encode a college degree's worth of study material. [^30] Their brain also develops Their brain will also develop based on world-modelling they obtain from other senses

Assuming [170](https://www.wolframalpha.com/input?i=%2810*24-%284%2F12*15.5%2B8%2F12*13.5%2B2*12.5%2B3*11.5%2B4*10%29%29*365.25*3600) [million](https://www.sleepfoundation.org/children-and-sleep/how-much-sleep-do-kids-need) waking seconds before age 10, and a rate of change of 1 byte/second, one gets to a similar bound.


5. 
6. To bound how much data from observing the world directly is necessary, assume they are (which [usually isn't](https://research.gold.ac.uk/id/eprint/5415/1/Pring_&_Tadic_CBMPD_VI_Nassr.pdf) associated with mental retardation) and experience on the order of [200 million](https://www.sleepfoundation.org/children-and-sleep/how-much-sleep-do-kids-need) waking seconds before age 10.to whatever extent haptical input is necessary to develop world-modelling, it is fair (on the order 200 million waking seconds before age 10

In conclusion, the _algorithm_ that describes the human brain probably fits in a few megabytes at most

# Whom to ask?

# What to ask?

My plan is to ask people

[^10]: The algorithm is typically described as having a random component - nevertheless, a simulation must typically return a working human brain if a typical embryo develops into a brain as well. We are only interested in gathering enough data to almost always obtain a working brain when replacing the remainder by nothing, or randomness.

[^20]: According to [Wikipedia](https://en.wikipedia.org/wiki/Non-coding_DNA), less that 2 % of human DNA is _coding_, i.e. describes the amino acid sequences comprising proteins. Another 2-14 % seems to have some other functional role: This is evidenced by the fact that it mutates slower than the rest of the DNA, from which the conclusion is drawn that a mutation in these spots must typically have a negative effect on fitness. See [here](https://academic.oup.com/gbe/article/5/3/578/583411) for details. The rest is known as _junk DNA_.

[^30]: A college student taking 32 courses over the course of their degree, each of which is based on a 500-page book containing 250 words per page, studies 4 000 000 words in total. The original [word gap](https://en.wikipedia.org/wiki/Word_gap) studies resulted in 11.5 million words per year overheard by "an average child in a professional family", which would correspond to 290 million words over 25 years. A raw King James Bible, compressed with lzip, occupies 1.35 bytes/word of disk space. See [here](https://www.researchgate.net/post/Estimates_of_quantified_human_sensory_system_throughput10) for a more thorough discussion of sensory throughput.
