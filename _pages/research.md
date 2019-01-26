---
#layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

My research is motivated by my interest in harnessing large, untargeted biological data to better understand, predict, and monitor human disease.
More broadly, I'm interested in using **personalized medicine approaches for public health**.

My main project so far has been a large **[meta-analysis of case-control gut microbiome studies](https://www.nature.com/articles/s41467-017-01973-8)**.
We found generalizable insights about patterns of microbiome shifts and showed that most disease-associated bacteria found in individual studies are not specific to the disease under study.
You can check out the [paper](https://www.nature.com/articles/s41467-017-01973-8) or a more colloquial summary on my Nature Microbiology [behind the paper blog](https://naturemicrobiologycommunity.nature.com/users/70264-claire-duvallet/posts/22494-beyond-dysbiosis-disease-specific-and-shared-microbiome-responses-to-disease blog).

I'm proud to have used this project as an opportunity to practice **reproducible, open science**: every analysis in the paper can be re-made with the code on my [github](http://github.com/cduvallet/microbiomeHD), and we put the data on [Zenodo](https://zenodo.org/record/840333#.WbdUMtOGPBI).

I've also been working with a clinical collaborator at Boston Children's Hospital to analyze a large dataset of **lung, stomach, and throat microbiomes** of over 200 pediatric patients.
We found that lung and stomach microbiomes are driven more by the individual person than the body site and that patients with swallowing dysfunction have more similar lung and throat microbiomes than those who swallow normally.
This has exciting clinical implications for how we treat kids with these disorders, and I hope that the paper will be out soon!

Over the past 3 years, I've worked on the [Underworlds](http://underworlds.mit.edu/) project in our lab, **mining sewage for useful public health information**.
Soon we'll be starting to look at antibiotics and antibiotic resistance genes in sewage to better understand how they spread in the environment and how humans affect that spread.
I also want to mine untargeted metabolomics data from multiple cities' sewage to identify metabolites that could serve as biomarkers for known behavioral or health differences between locations.

Along the way, I've developed an interest in **tool development**. 
I've contributed significantly to a method to [correct for batch effects](https://doi.org/10.1371/journal.pcbi.1006102) across case-control microbiome studies, the re-implementation of [distribution-based OTU clustering](https://doi.org/10.1371/journal.pone.0176335), and our in-house [16S processing pipeline](http://github.com/thomasgurry/amplicon_sequencing_pipeline).

I'm also starting to implement some the [methods](http://almlab.mit.edu/software.html) developed by the Alm lab into [QIIME 2](https://qiime2.org/), a suite of tools broadly used in microbiome research.
I've written two QIIME 2 plugins so far (our [percentile normalization method](https://github.com/cduvallet/q2-perc-norm) and [Sarah Preheim](https://engineering.jhu.edu/ehe/faculty/sarah-preheim/)'s [distribution-based OTU clustering](https://github.com/cduvallet/q2-dbotu) method).
Hopefully I can make cool tools more useful to more people, and perhaps [learn some things](/posts/2018/03/qiime2-plugin) along the way too!
