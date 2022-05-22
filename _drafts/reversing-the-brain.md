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

# Introduction: Is your brain more complicated than your fridge?
The brain is often described as "the most complex object in the universe" - justified by estimating the number of synapses it contains, or similar quantities. But a rock contains lots of atoms and degrees of freedom as well. The amount of _information_ needed to describe a functional brain is upper-bounded by the relevant information that flowed into it since conception, which in turn can be upper-bounded by very modest numbers:

probleme caveats:
epigenome
men+women different genome size
different genome from parents

1. A [human's DNA sequence](https://en.wikipedia.org/wiki/Human_genome#Information_content) contains about 3 billion base pairs - 3 billion choices between 4 different nucleic acids - per parent, and the difference between the parents' sequences is small. At least about 85-90 % of that is so-called _junk DNA_, which is claimed to be irrelevant to human functioning.[^20] While it is not entirely clear whether, or how much, relevant data is encoded differently (e.g. in the [epigenome](https://en.wikipedia.org/wiki/Epigenome)), it seems fair to me to assume it's not of a higher order of magnitude.

Some of the non-junk DNA describes other body parts than the brain,[^25] and there doesn't  . In fact, [the hypothesis exists](https://slatestarcodex.com/blog_images/parasite_study.pdf) that the brain evolved . In conclusion, the _algorithm_ that describes the brain can probably be described in less than ne ends with a bound of 75 megabytes of infomrat
4. Certainly, storing all the raw sensory data impinging upon a human would certainly take me a lot of raw sensory data impinging upon a  human hears a few hundred megabytes worth of language before they turn 25 (and, according to many parents, most of this doesn't change their mind); a few megabytes are enough to encode a college degree's worth of study material. [^30] Their brain also develops Their brain will also develop based on world-modelling they obtain from other senses

Assuming [170](https://www.wolframalpha.com/input?i=%2810*24-%284%2F12*15.5%2B8%2F12*13.5%2B2*12.5%2B3*11.5%2B4*10%29%29*365.25*3600) [million](https://www.sleepfoundation.org/children-and-sleep/how-much-sleep-do-kids-need) waking seconds before age 10, and a rate of change of 1 byte/second, one gets to a similar bound.

So the bulk of the remaining question is how human DNA encodes the brain's algorithm - and how the brain's algorithm turns environmental data into human intelligence, feelings and consciousness.

I claim that, most likely, the bulk of data for both objects has been gathered. This means the 

# Breaking down the problem
1. The cells' DNA and whatever further (e.g. [epigenetic](https://en.wikipedia.org/wiki/Epigenetics)) information needed to describe them to sufficient accuracy,
2. the structure and interaction parameters of the chemicals contained in the cells. In particular, we know not only how the cell's proteins fold, but also what chemical reactions they are involved in, and the reaction speeds,
3. the "control logic" in each cell, determining when which new proteins get expressed and activated.
4. cell differentation and morphogenesis: What types of cells exist, the control logic determining which type a cell in a certain part of the body develops into.
5. Arborization: Neurons, in particular, decide to "branch out" and connect to other neurons according to some algorithm.
6. plasticity: The effective algorithm determining how neuron's connection strength change based on stimuli,
7. neuron-level activity: A sufficient description of a neuron's internal parameters that allow to simulate its electrical and chemical output,
8. larger-scale activity: Understanding to what extent it is possible to average over several neuron's behaviour and preserve the brain's computational power,
9. overarching design principles.

Particularly concerning the first seven points, we have a _basic idea_ what we would need to do. What . Furthermore, to my limited understanding, one can often find that gathering this data becomes exponentially cheaper with time. Just like Moore's law allowed one to predict the development of IT many years in advance, predictions of when science has "solved" some points in the above enumeration may be possible.

But as I understand, the knowledge about the state of each field is quite scattered. So I'd like to find experts for each subfield and interview them regarding these questions - and turn these into short reports, tables, and predictions.

# What to ask?
The basic questions I'd like to understand for all these levels are similar:
  - How much data would we need to gather to "solve" the problem? How sure are we about this quantity?
  - What experimental and computational methods exist, and how expensive is it to gather data with them? How fast - and predictably - do these progress? Can we draw a nice Moore's law-like graph showing exponentially declining costs per unit of information?
  - What is the reason for that progress, i.e. what is changing in the wider world of engineering that allowed the introduction of new methods? What are obstacles to further progress?
  - How many people-hours and USD per year are devoted to the field, and how does this change?
  - Once we understood biology "completely" at this level of abstraction, what computational power do you expect to be necessary to reproduce it with an accuracy sufficient to reproduce the brain's abilities?
  - of course, some space for further remarks.

# Whom to ask?


Understanding this at the various scales corresponds to the :





5. 
6. To bound how much data from observing the world directly is necessary, assume they are (which [usually isn't](https://research.gold.ac.uk/id/eprint/5415/1/Pring_&_Tadic_CBMPD_VI_Nassr.pdf) associated with mental retardation) and experience on the order of [200 million](https://www.sleepfoundation.org/children-and-sleep/how-much-sleep-do-kids-need) waking seconds before age 10.to whatever extent haptical input is necessary to develop world-modelling, it is fair (on the order 200 million waking seconds before age 10

In conclusion, the _algorithm_ that describes the human brain probably fits in a few megabytes at most

# Next: Whom to ask?

# What to ask?

My plan is to ask people

[^10]: The algorithm is typically described as having a random component - nevertheless, a simulation must typically return a working human brain if a typical embryo develops into a brain as well. We are only interested in gathering enough data to almost always obtain a working brain when replacing the remainder by nothing, or randomness.

[^20]: According to [Wikipedia](https://en.wikipedia.org/wiki/Non-coding_DNA), less that 2 % of human DNA is _coding_, i.e. describes the amino acid sequences comprising proteins found in humans. Another 2-14 % seems to have some other functional role: This is evidenced by the fact that it mutates slower than the rest of the DNA, from which the conclusion is drawn that a mutation in these spots must typically have a negative effect on fitness. See [here](https://academic.oup.com/gbe/article/5/3/578/583411) for details.

One objection one might have - and that I want to ask an expert about: What if "junk DNA" is evolutionarily important, but the information it encodes includes redundancy and error corrections, and some amount of mutations will reduce the fitness gradually or not at all?  In that case, one would expect an equilibrium in which there is a significant mutation rate in the "junk DNA", but Leaving out calculations for now - one keyword is the ) of the system - one can calculate that this is not the . This

[^25]: How much is one of the questions I'd like to get an answer to.

[^30]: A college student taking 32 courses over the course of their degree, each of which is based on a 500-page book containing 250 words per page, studies 4 000 000 words in total. The original [word gap](https://en.wikipedia.org/wiki/Word_gap) studies resulted in 11.5 million words per year overheard by "an average child in a professional family", which would correspond to 290 million words over 25 years. A raw King James Bible, compressed with lzip, occupies 1.35 bytes/word of disk space. See [here](https://www.researchgate.net/post/Estimates_of_quantified_human_sensory_system_throughput10) for a more thorough discussion of sensory throughput.
