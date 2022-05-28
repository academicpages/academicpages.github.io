---
title: 'Is your brain more complicated than your fridge?'
date: 2022-05-28
permalink: /posts/2022/05/brain-vs-fridge/
tags:
  - q-bio.nc
  - q-bio
  - quantifying-neuroscience
  - neuroscience
  - progress-studies
---
The human brain is often described as "the most complex object in the universe" - justified by the number of synapses it contains or similar. But a glass of water contains lots of molecules and degrees of freedom as well.[^1] While the amount of relevant _computation_ a brain performs during its lifetime may be high,[^2] the amount of _information_ needed to describe it is upper-bounded by how much relevant data the fertilized egg it developed from contained, and how much flowed into it after conception. Even by computing standards of the 1990s, these are modest quantities - what's more, obtaining them is essentially a solved problem:
## How large is a brain's relevant genome?
According to common wisdom, a fertilized egg - containing a human's biological _algorithm_[^3] - is mostly described by its genome.[^4] [With caveats](https://en.wikipedia.org/w/index.php?title=Human_Genome_Project&oldid=1084542142#State_of_completion), a reference human's DNA sequence had been determined by 2003[^9]. It is also believed that at most 10-15% of the genome encodes relevant information,[^5] corresponding to about **[75-115 megabytes](https://en.wikipedia.org/wiki/Human_genome#Information_content)** of uncompressed data.[^6] Of course, some of this (QUESTION: How much?) describes other body parts than the brain.[^7]
## How much data is a brain trained on?
The _data_ a brain receives and develops with comes either from other humans (mostly in the form of language), or from observing and interacting with everyday physics directly. Obtaining it would be as easy as recording actual infants. Estimating the quantities:
1. **150 megabytes** worth of text is on the high end of how much language an American child overhears before age 10 - and according to many parents, much of this information doesn't change its mind. Formal higher education takes even less space: For example, paltry **4 megabytes** suffice to encode a college degree's worth of study material.[^8]
2. The _information_ - as opposed to _computation_ - an infant experimenting in its surroundings benefits from can be generated from sufficiently accurate descriptions of the laws of everyday physics, and the objects the infant interacts with. It seems fair to me to assume that, to the accuracy necessary to develop intelligence, these descriptions are largely contained in what adults talked about while it grew up - particularly considering that [intelligence doesn't require eyesight to develop](https://digital.library.unt.edu/ark:/67531/metadc4318/).

In conclusion, adult human intelligence probably fits into less - and plausibly much less - than 300 megabytes of data mostly available to humanity today - if one doesn't count (pseudo)randomness, redundancy, "character traits" that could be different without changing basic mental functioning, and helpful intermediate computations the brain performed during development.[^10] If you have a smart fridge with an LED screen, it probably runs more code.

Neither are we bottlenecked by our fundamental physics knowledge: To get to a point where physics couldn't predict a brain's behaviour anymore on an atomic scale, one would need to throw it into a black hole or subject it to similarly extreme conditions.

The bottom line is that describing the human brain's algorithm, both before and after training, _can't be that complex_. The question is: How to understand and reproduce the algorithm, not in a thought experiment but in practice?

## Footnotes
[^1]: This problem is not just hypothetical: As of 2016, surrounding water molecules were a major expense in biochemical simulations according to what I heard. I don't know the current status (QUESTION).

[^2]: See [Joseph Carlsmith's report](https://www.openphilanthropy.org/brain-computation-report) for a thorough attempt at estimation. The number of operations needed may be much higher or much lower than the number of spikes occuring in a natural brain. Furthermore, as they become more complex, artificial and natural computation systems tend to become bottle-necked by communication rather than computation - so the "number of operations required" may turn out to be irrelevant. TODO either elaborate, or remove this?

[^3]: Strictly speaking, the distinction between "algorithm" and "data" is blurred in an adult brain, as it changes its algorithm based on what it observed during development.

[^4]: While some more data may be stored in other places, for example the [epigenome](https://en.wikipedia.org/wiki/Epigenome) (QUESTION: more data on that?), it is believed that DNA encodes the bulk.

[^5]: [Less that 2 %](https://en.wikipedia.org/wiki/Non-coding_DNA) of human DNA is _coding_, i.e. describes the amino acid sequences comprising proteins found in humans. According to [Graur et al., 2013](https://academic.oup.com/gbe/article/5/3/578/583411), another 3-13 % changed slower in evolutionary history than the rest, suggesting that mutations in these places typically had a negative effect on the organism's functioning and evolutionary fitness. These regions are known or suspected (QUESTION: What is the status on that?) to encode, for example, "control logic" activating or deactivating protein-coding genes. The remainder is given the title "junk DNA", and assumed to be completely useless.

[^6]: The DNA in a healthy human brain cell contains one sequence per biological parent, but the difference between these sequences is small - the difference between an individual genome and a reference fits into about [4 MB](https://en.wikipedia.org/w/index.php?title=Human_genome&oldid=1085728356#Information_content).

[^7]: It seems plausible to me that a minimal, abstract algorithm reproducing human intelligence takes order of magnitude less space: LATER argue why exactly.

[^8]: A college student taking 32 courses over the course of their degree, each of which is based on a 500-page book containing 250 words per page, studies 4 000 000 words in total. The original [word gap](https://en.wikipedia.org/wiki/Word_gap) study resulted in 11.5 million words per year overheard by "an average child in a professional family", which would correspond to 290 million words over 25 years. A raw King James Bible, compressed with lzip, occupies 1.35 bytes/word of disk space. See [here](https://www.researchgate.net/post/Estimates_of_quantified_human_sensory_system_throughput10) for a discussion of raw sensory throughput.

[^9]: With [more caveats](https://www.genome.gov/sequencingcosts), the hypothetical cost of repeating that feat with modern methods declines exponentially over the years, in analogy to other trends in information processing.

[^10]: Of course, this depends on the exact definitions and cut-off between "computation" and "information" - for example, human-level intelligence may become much simpler to describe if we allowed evolution as part of the algorithm, rather than requiring the algorithm to store evolution's outcome at the moment of conception.
