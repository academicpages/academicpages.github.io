---
title: 'Neuroscience tech tree'
date: 2022-06-25
permalink: /posts/2022/06/neuroscience-tech-tree/
tags:
  - q-bio.nc
  - q-bio
  - quantifying-neuroscience
  - progress-studies
  - neuroscience
---

Neuroscience tech tree
---------------------
Status: Chaotic draft, will hopefully become more coherent within the next 2 months

>The future is already there, it's just not widely distributed yet - attributed to William Gibson

This is part of the ["Neuroscience under a quantitative progress studies perspective"](https://qudent.github.io/posts/2022/06/intro-neuroscience-progress-studies/) project with Kevin Kermani Nejad. An inspiration is the Longevity tech tree in the last page of [this document](https://foresight.org/wp-content/uploads/2021/10/Longevity-Technology.pdf).

In the introduction, we attempted to classify what humanity would like to understand about nervous systems to "reverse-engineer" them. In this post, we attempt the same for possible scientific and engineering advances towards these goals. We try to validate this classification in section XY, where we consider how well past advances in the field would have fit into it.

Apart from the classification itself, another **implied assumption** for it to be useful is that - as in the quote above - progress will come through technologies that are at least conceivable today, and become practically feasible through a rising tide of engineering progress and available experimental data and experience - rather than "one weird trick"-style advances that were hindered by nothing but noone thinking of them before. We will validate this assumption in section XY as well.

These techniques are interrelated. A focus of the current version is on the microscale - i.e. manipulating and understanding cells and lower-level structure. My current guess is that great breakthroughs in understanding nervous systems will rather be achieved by understanding smaller systems very well (than by understanding larger systems a little bit better), though this is the sort of thing to gather more substantiated opinions and evidence about.


This documents lives off interactions with experts and will be updated accordingly.

## 1. How can experimental methods improve?

An experiment is an interaction with a physical system - by which we include a computer or other form of simulator. Assume that, in all cases, the system is supposed to represent something happening in an actual brain. There is variety in which processes we are trying to represent; for any choice, we may improve (by quality/accuracy and/or cost)
1. transfer of data into the system,
2. the system itself
3. transfer of data out of the system.


## 2. Types of systems
This is similar to section 2 in the [introduction post](https://qudent.github.io/posts/2022/06/intro-neuroscience-progress-studies/).
1. proteins/chemicals 
2. (interaction networks in) cells
3. neurons and synapses
4. neural networks
5. nervous systems.

### 1. Proteins/chemicals
We are interested in evaluation - and reversing - the function that maps from a DNA sequence (+whatever further information is necessary) to the protein structure, and the reaction rates - and the reverse function (i.e. given a desired protein function, we'd like to find a DNA sequence).

We'd also like to know where proteins are located in a cell.

"Writing" is comparable to putting DNA into cells and making them express proteins. This is covered by DNA writing progress/the next section. A caveat is that 

Understanding a given protein structure/"reading": The [Protein Data Bank](https://en.wikipedia.org/w/index.php?title=Protein_Data_Bank&oldid=1091514826) is a databank of known protein structures; [](https://en.wikipedia.org/w/index.php?title=Protein_Data_Bank&oldid=1091514826#Contents)this section of the Wikipedia page on the Protein Data Bank) contains a statistic with a list of experimental methods for structure determination.

Reverse problem/"writing": Not yet discussed

### 2. Reaction network inside a cell

- understanding which genes are expressed (by GFP etc.??)
- DNA ticker tapes, ticker tapes getting out/inside of cells...?
	+ writing
		* gene editing:
			- targeted
			- random: observing phenotype changes of randomly induced mutations in population of cells
		* optogenetics/manipulating behaviour/gene by input
		* RF transmitter in cell?

### 3. Whole neurons

* voltage sensitive dyes
* patch clamps
* synthetic extracellular environment neurochemicals to understand cell's behavior
* microscopes+cameras
* calcium imaging (also for "nervous systems")

### 4. Nervous systems
* neuroimaging methods: everything on [this list](https://en.wikipedia.org/w/index.php?title=Neuroimaging&oldid=1094904651#Brain-imaging_techniques). See [here](https://www.frontiersin.org/articles/10.3389/fncom.2013.00137/full) for a review (from 2013) of physical limits of the main methods of the time; according to Milan Cvitkovic, ultrasound methods became more important in the meantime.

- making nervous systems easier to interact with
	+ direct genome manipulation
	+ breeding
	+ metabolism (lower -> waste heat less problematic)
	+ physical space for recording devices
	+ make axons grow towards electrodes themselves
- data from human/animal populations
	+ GWAS
	+ ticker tapes, ticker tapes in bloodstream...
	
- better understanding which information can be abstracted away

- simulation/data processing
- Advances in computing
	+ Moore's law/semiconductor advances
	+ neuromorphic computing
	+ analog computing
	+ biocomputing/laboratories in cells
	+ quantum computing
	+ automated/robot scientists
	+ ML for data-processing/statistical inference more generally
	+ training data generation (as in OpenAI Gym)
- more individualizable semiconductors (so that one-off/small-scale systems improve relative to industrial-scale systems)

## 3. Validation and caveats
todo...
