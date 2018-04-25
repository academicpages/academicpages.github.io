---
#layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

My research is motivated by my interest in harnessing large, untargeted biological data to better understand, predict, and monitor human disease.
More broadly, I'm interested in using **personalized medicine approaches for public health**.

My main project so far has been a large **[meta-analysis of case-control gut microbiome datasets](https://www.nature.com/articles/s41467-017-01973-8)** across multiple disease states.
We found generalizable insights about patterns of disease-associated microbiome shifts: it turns out that you can characterize disease-associated microbiome shifts by their extent (how many bacteria are changed) and directionality (whether you have too many "bad" bacteria or not enough "good" bacteria).
Also, we showed that most disease-associated bacteria in individual studies are not specific to one disease.
This means that finding an association in one study really isn't enough to identify putative biomarkers or causal mechanisms, and we'll need to work harder to validate our findings with experiments and further meta-analyses.

I learned a lot about data collection and processing from this project, and have put the raw processed data on [Zenodo](https://zenodo.org/record/840333#.WbdUMtOGPBI).
I also used this project as an opportunity to practice **reproducible, open science**, and I'm proud that every analysis in the paper can be re-made with the code on my [github](http://github.com/cduvallet/microbiomeHD).
I also wrote a blog post talking about my experience writing this paper on Nature Microbiology's [behind the paper](https://naturemicrobiologycommunity.nature.com/users/70264-claire-duvallet/posts/22494-beyond-dysbiosis-disease-specific-and-shared-microbiome-responses-to-disease) blog series, and a related editorial about meta-analysis for translational microbiome research in [Microbial Biotechnology](https://dx.doi.org/10.1111/1751-7915.13047).

I'm also starting to think about how to use **untargeted serum metabolomics to diagnose disease**.
We're hoping to approach untargeted metabolomics with the same "quick, dirty, and good enough" spirit that next-generation sequencing bioinformaticians took to revolutionize genomics.
(Shh... don't tell your analytical chemist friends!)

I also work on some other projects around the lab.
I've done work on the [Underworlds](http://underworlds.mit.edu/) project in our lab, **mining sewage for useful public health information**.
Soon we'll be starting to look at antibiotics and antibiotic resistance genes in sewage to better understand how they spread in the environment and how humans affect that spread.
In collaboration with the [Center for Molecular Dynamics Nepal](http://www.cmdn.org.np/), we'll be sampling in Katmandu and studying how the "resistome" evolves along the river.
I'm also analyzing a clinical collaborator's dataset of **lung, stomach, and throat microbiomes** of over 200 pediatric patients with various aerodigestive conditions.

Finally, I'm interested in **tool development**. 
I've contributed significantly to our in-house [16S processing pipeline](http://github.com/thomasgurry/amplicon_sequencing_pipeline) (yo and check out those [docs](http://amplicon-sequencing-pipeline.readthedocs.io/en/latest/) tho!), to the [re-implementation of distribution-based OTU clustering](https://doi.org/10.1371/journal.pone.0176335), and to a method to [correct for batch effects](https://doi.org/10.1371/journal.pcbi.1006102) across case-control microbiome studies.
I'm also starting to implement some the [methods](http://almlab.mit.edu/software.html) developed by the Alm lab into [QIIME 2](https://qiime2.org/), a suite of tools broadly used in microbiome research.
I've written one QIIME 2 plugin so far (our [percentile normalization method](https://github.com/cduvallet/q2-perc-norm)), and plan to implement a few more before I graduate.
Hopefully I can make cool tools more useful to more people, and perhaps [learn some things](/posts/2018/03/qiime2-plugin) along the way too!
