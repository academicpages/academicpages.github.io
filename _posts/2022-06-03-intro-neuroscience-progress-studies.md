---
title: 'Project: Neuroscience under a quantitative progress studies perspective'
date: 2022-06-03
permalink: /posts/2022/06/intro-neuroscience-progress-studies/
tags:
  - q-bio.nc
  - q-bio
  - reversing-the-brain
  - progress-studies
  - neuroscience
---

## 1. Introduction
Understanding the human brain - to the point of being able to reproduce its abilities, as one could design and build a plane or chair - is hopefully a finite problem for civilization. I think that many aspects of that problem (see section 2 for my attempt at enumeration) can be quantified. Similarly, performance and progress of associated experimental methods can often be quantified and predicted, leading to equivalents of Moore's law famous from computing.

I'd like to attempt just that systematically - create a spreadsheet and accompanying notes discussing the questions in section 3 for the items in section 2, giving numerical answers whenever possible. I'd like to do so by literature review and interviews with experts. This is different - and much simpler - than reviewing all the literature in neuroscience and microbiology: Most of the literature focuses on _what_ scientists know or learned recently, I'd like to focus on _how much_ they did, do, and need to know.

Ideally, this would allow predictions of how far we are from "reverse-engineering" the human brain, and understanding how it works and develops from a human genome in its environment.

## 2. Breaking down the problem: the brain's inner workings by scale
> "If you wish to make an apple pie from scratch, you must first invent the universe." ― Carl Sagan, Cosmos

> “There is a theory which states that if ever anyone discovers exactly what the Universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable. There is another theory which states that this has already happened.” ― Douglas Adams, The Restaurant at the End of the Universe

[As argued](/posts/2022/05/brain-vs-fridge), a description of an adult brain sufficient to reproduce human intelligence would probably take less than 300 megabytes of space - if one considers an adequate lossy compression of the genetic and environmental "input data" and discounts randomness, irrelevant data, and intermediate computations performed during development. The grand challenge of neuroscience is to obtain knowledge and understanding corresponding to that data.

A "brute-force" solution would involve a _whole-cell model_ of human brain and body cells, starting with a fertilized egg. This would be a description of all chemical reactions in the cells, complete and accurate enough to simulate their "algorithm".[^1] The state of the art in whole-cell modeling is quite some way from that[^10] - but crucially, I found in several places that obtaining and processing relevant data becomes exponentially cheaper over the years.

To create a whole-cell model, one is interested in the following questions:

1. How do the cell's proteins fold?
2. What chemical reactions are they involved in, and what are the reaction speeds?
3. Where are proteins and other substances located in a cell?
4. What's the "control logic" in each cell, determining when which proteins get expressed and activated?
5. What chemical and electrical signals do cells exchange for communication?

To understand how human _intelligence_ works in an adult brain, it would suffice to understand the effective behaviour of neurons and other human cells, i.e. answer roughly the following questions:

6. Cell differentation and morphogenesis: What types of cells (in particular, neurons) exist? How are they distributed in a brain?
7. Arborization: How do neurons decide to "branch out" and connect to other neurons?
8. Activity and plasticity: Given a branched-out neuron, how does it respond and change its properties when exposed to electrical and chemical stimuli?

Zooming out further, the question becomes:

9. Collective behaviour: Can we describe collections of neurons without describing each neuron individually? How to map specific abilities to brain regions?

The most important - and, likely, most open-ended - question is:

10. Design principles - what's the point of all these algorithms? Which parts of them are essential for intelligence, and which are artifacts of biology?

Putting it all together, a _[whole-brain emulation](https://en.wikipedia.org/wiki/Mind_uploading)_ would be a model reproducing a brain in a computer accurately enough that the simulation reproduces its abilities. This has not been achieved even for the simplest real-life neural networks.[^19] A related field is _[neuromorphic engineering](https://en.wikipedia.org/wiki/Neuromorphic_engineering)_, though the emphasis there is on solving concrete engineering problems rather than accurately reproducing an entire brain.

Just like Moore's law allowed to predict developments in IT decades in advance, similar laws concerning the items of this enumeration may allow predictions when, and how, humanity meets those subjects' grand challenges.[^27]
## 3. What questions to ask experts, and the literature?
The basic questions I'd like to understand concerning all these levels are similar:
1. How much data would we need to gather to "solve" the problem? How sure are we about this quantity?
2. What experimental and computational methods exist, and how expensive is it to gather data with them? How fast - and predictably - do these improve? Can we draw a nice Moore's law-like graph showing exponentially declining costs per unit of information?
3. What is the reason for that progress, i.e. what changed in the wider world of engineering that allowed the introduction of new methods? What are obstacles to further progress?
4. How many people-hours and USD per year are devoted to the field? How did that develop historically and how is it projected to develop?
5. How much compute is expected to suffice to simulate that level's effective behaviour so that one reproduces a biological brain's functions? How much is expected to be "essential for intelligence" - i.e. how much could be saved by changing higher-level organization?
6. Further remarks or complications?

## 4. The desired end-state, and how I'd like to get there
I'd like there to exist a reference discussing all combinations of items in the previous two sections in a unified way - naturally, this could be built around a spreadsheet, and notes from interviews and papers organized around the items in section 2. The answers should be quantified and made comparable - i.e. be given in terms of USD, gigabytes, person-hours invested in a certain year etc. With such a reference, drawing plots analogous to those associated with Moore's law would be trivial.

In reality, answers to these questions will have plenty of caveats if they exist at all.[^36] What's more, there will be different opinions in the community regarding whatever points can be made about them.

But as always, a problem having no complete solution doesn't in principle imply that working on it is useless. I think _some_ reference that summarizes relevant information and makes its own limitations clear is feasible. I estimate that one can get there based on interviews with about 2-3 experts per item in section 2, plus preparing and following up by a brief literature review.

In total, I'd expect a fact-sheet of about 1.5 A4 page per item in section 2 - excluding item 10, which is too open-ended.

I hope to have a partial report in 3 months, based on which I can hold a talk.
## 6. Acknowledgments
So far, thanks in particular to Kynan Eng, Jonathan Karr, and Lucia Purcaru for helpful feedback and references on the subject. 
## 7. Footnotes
[^1]: See [this website](https://www.wholecell.org/), and the [list of models](https://www.wholecell.org/models/) therein, for more information - although it doesn't seem to have been updated since 2018.

[^10]: To my understanding, a "complete" whole-cell model has been [obtained](https://doi.org/10.1016/j.cell.2012.05.044) for _[Mycoplasma genitalium](https://en.wikipedia.org/wiki/Mycoplasma_genitalium)_, an STD agent that happens to be among the simplest known bacteria. More recent work focused on [yeast](https://doi.org/10.1016/j.tibtech.2021.06.010). See [here](https://www.karrlab.org/static//doc/papers/Goldberg2018.pdf) for an overview of technological advances needed for human whole-cell modeling - though the focus there is on generic human cells rather than neurons.

[^19]: The [OpenWorm project](https://openworm.org/) attempts to emulate the entire neural network of the _C. Elegans_ worm, but [hasn't succeeded yet](https://en.wikipedia.org/w/index.php?title=OpenWorm&oldid=1088110958#Progress). A crucial problem seems to be that, although we know the worm's neural network's "wiring diagram" - called _connectome_ - we don't have adequate knowledge of connection strengths, and how these change in response to stimuli.
 
[^27]: Of course, there are various approaches to obtain data for each level. For example, the structure of a folded protein could be determined by [cryogenic electron microscopy](https://en.wikipedia.org/w/index.php?title=Cryogenic_electron_microscopy&oldid=1085472775) - which, as I heard, improved greatly since about 2010 - or [by a computer program](https://en.wikipedia.org/w/index.php?title=Protein_structure_prediction&oldid=1077551533), where a deep learning system called AlphaFold  improved the state of the art in 2018-2020. Similarly, an adequate model of neurons and their interactions may be obtained by whole-cell modeling - or by growing neurons in a lab, measuring how they respond to stimuli, and training a machine learning model on the results.

[^36]: That is not too different from the situation in computing; there, all plots of structure sizes or costs per bit, transistor, or floating-point operation by year hide complications and caveats beyond the scope of this text.
