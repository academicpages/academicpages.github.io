---
title: 'Types of stochasticity and errors brains need to deal with/ways in which proteins in water are suboptimal for computation'
date: 2022-06-11
permalink: /posts/2022/06/neuro-stochasticity/
tags:
  - listicle
  - q-bio
  - neuroscience
---
Together, these may add orders of magnitude to the complexity and resources a brain has to use to accomplish tasks.
- mutations in evolutionary history - preferable to have a brain structure surviving some mutations
- diffusion times of neurotransmitters
- stochasticity of reactions facilitated by proteins
- protein folding: to implement the equivalent of a logic gate, one needs to invent some protein that folds in just the right way to facilitate a computation. That doesn't sound easy at all, may introduce overhead
- leakage (of current through axon/neuron walls)
- stochasticity of neuronal growth and arborization?
- Energy:
  - using too much energy is a much bigger concern for animals than for computers, so it is plausible that there are tradeoffs towards using less energy vs. better performance
  - relatedly: Mitochondrial volume limits energy inflow into brain; power density of biomatter is much lower than achievable in e.g. microchips
  - warm-blooded brain temperature can't rise more than a few K before damage, limiting sustained energy expenditure. Can't cool with liquid nitrogen either...
- Evolution: There must have been a continuous evolutionary path from a bacterium to the human, or any other, brain. This probably doesn't mix well with many "brittle" algorithms typical in CS, like cryptography, compression, maybe error correction...
- because proteins and neurons are so incredibly slow compared to transistors, algorithms that can't be parallelized well may not even be worth it
- Indeed, there is little evidence for the sort of algorithms computer scientists devise (as in cryptography, compression, ...) in biology. The most involved algorithm I heard of is the use of ["modified Bloom filters" in flies remembering odors](https://en.wikipedia.org/w/index.php?title=Bloom_filter&oldid=1087877900#Examples).
- [Parasites](https://slatestarcodex.com/blog_images/parasite_study.pdf)

Finally:
- Size and suboptimality: According to ["Principles of Neural Design"](https://mitpress.mit.edu/books/principles-neural-design) (PoND) by Sterling and Laughlin (a repeat appearance here), information-processing systems' impressiveness appears to be strongly sublinear in complexity and physical size (because of higher communication overhead). Therefore, the increase in necessary brain matter to implement some function is probably superlinear in the overhead introduced by the factors above.

(Possible) evidence
--------
- "The Knowledge" - [BBC coverage](https://mitpress.mit.edu/books/principles-neural-design), [scientific article](https://www.cell.com/current-biology/fulltext/S0960-9822(11)01267-X): As of 2011, to become a registered taxi driver in London, one needs to learn a lot of London geography by heart (apparently, students work about full-time for ~3 years - see table 2 in the article). Scientists determined changes in/enlargements of parts of the students' brains structure - see figure 3 there. This may give a data point what a certain amount of factual knowledge (quantifiable in bits) corresponds to in terms of brain matter (and how many orders of magnitude this is above information-theoretic bounds one would obtain from the connectome). But considering [this article](https://www.nytimes.com/2014/11/10/t-magazine/london-taxi-test-knowledge.html) about what The Knowledge entails, it seems to have a significant component beyond street information as well.
   - did someone try this with people who learn the Quran by heart?...
- From everyday experience, we know that we have a hard time multiplying 3-digit number in our heads, or estimating times/distances, when compared to a computer. Seems plausible to me that this can be directly traced back to imprecision/stochasticity in the brain. One possible way of evidence-gathering I wonder about:
    - Birds (e.g. ravens) seem to be unusually intelligent for their body/brain size (see [here](https://slatestarcodex.com/2019/03/25/neurons-and-intelligence-a-birdbrained-perspective/) for a brief discussion of the issue, particularly [this survey](https://aiimpacts.org/investigation-into-the-relationship-between-neuron-count-and-intelligence-across-differing-cortical-architectures/)). One attempted explanation is that they have very small neurons - and therefore, both a higher neuron count and a better-connected brain compared to larger animals. [This](https://arstechnica.com/science/2016/06/bird-brains-are-densewith-neurons/) source states that "the brains of parrots and songbirds contain on average twice as many neurons as primate brains of the same mass, indicating that avian brains have higher neuron packing densities than mammalian brains." - although I didn't look into whether these neurons may be more simple on average than primate ones. Why do mammals have bigger neurons then? One hypothesis:
    - The expected drawback of small neurons is that they are supposed to be more stochastic/noisy than larger ones (read this somewhere, can't find a source/calculation now). To the extent bird neural tissue is "fundamentally more stochastic" than primate, one would expect that birds make larger errors on quantitative estimates than humans/primates (e.g. they would suck at throwing a spear). In conclusion:
    - Maybe this has been/can be tested? If yes, a big reason for animal neuron size (leading to friction from interconnections) may be just be a need for accurate quantitative estimation - and "logical/qualitative" reasoning we associate with higher intelligence would work with smaller neurons as well.
- according to [PoND](https://mitpress.mit.edu/books/principles-neural-design), neurons are only spiking (rather than analogous/with continuous-valued activations) if they are longer than about 1 mm - so apparently, this is an energy-conservation measure/workaround because of leakage. Also means that spiking neurons in the human brai
- PoND: axon diameter is linear in avg (?) spike rate, but axon volume, energy rises as diameter squared (as I understand: available power ~ mitochondrial volume ~ diameter^2, so 2x axon diameter -> 4x mit. volume, 2x -> capacitance of membrane/energy needed to charge membrane/energy per spike -> 2x possible spike rate - page xix in that book)
- from this, we can see that encoding of some senses are terrible compared to what computer engineers could do, case study: [vestibular system](https://en.wikipedia.org/wiki/Vestibular_system) (sense of balance) -
    - axons of vestibular system (carrying sense of balance) are thickest in the human body (see fig. 10.2.), firing at about 100 Hz and requiring the most energy per spike
    - encoding: rate coding: spikes occur at random times, average frequency encodes pressure from fluid in semicircular canals to sensing cells
    - need to be so thick because body wants to know position with high accuracy (few degrees)
    - but a computer engineer would encode 2^N possibilities in N spikes even if only 1 bit per spike, the rate coding only encodes order of sqrt(N) possibilites (considering stochasticity - not 100 % sure about whether it is stochastic though)
    - Conclusion: At a point where we actually understand what's going on in the nervous system, we find it's woefully inferior to what humans could design with silicon (and maybe with biological/chemical circuits as well). No reason to believe it wouldn't be that way in other parts of the brain.

- There seems to be [no inherent evolutionary selection](https://en.wikipedia.org/w/index.php?title=Genome_size&oldid=1076325456#Variation_in_genome_size_and_gene_content) to keep the genome small; the same may be true for biochemical signalling pathways and effective algorithms.

- infants improve world-modeling by experimenting with toys, driving students improve by driving, people learning calculus improve by calculating on sheets of paper. In all of these examples, apparently having an external memory/data-processing system is very helpful for the brain, even though the amount of computation it performs/data it stores is very low compared to # synapses
