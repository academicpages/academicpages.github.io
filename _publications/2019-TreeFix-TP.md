---
title: "TreeFix-TP: Phylogenetic Error-Correction for Infectious Disease Transmission Network Inference"
collection: publications
permalink: /publication/2019-TreeFix-TP
date: 2019-10-22
venue: 'Under Review'
paperurl: 'https://www.biorxiv.org/content/10.1101/813931v1'
citation: "S. Sledzieski, C. Zhang, I. Mandoiu, and M.S. Bansal. TreeFix-TP: Phylogenetic Error-Correction for Infectious Disease Transmission Network Inference. bioRxiv 813931; doi: https://doi.org/10.1101/813931"
---

**Background** 
Many existing methods for estimation of infectious disease transmission networks use a phylogeny of the infecting strains as the basis for transmission network inference, and accurate network inference relies on accuracy of this underlying evolutionary history. However, phylogenetic reconstruction can be highly error prone and more sophisticated methods can fail to scale to larger outbreaks, negatively impacting downstream transmission network inference. Additionally, there are no currently available methods which are able to use within-host diversity to improve phylogenetic reconstruction.

**Results**
 We introduce a new method, TreeFix-TP, for accurate and scalable reconstruction of transmission phylogenies based on an error-correction framework. Our method uses intra-host strain diversity and host information to balance a parsimonious evaluation of the implied transmission network with statistical hypothesis testing on sequence data likelihood. The reconstructed tree minimizes the number of required disease transmissions while being as well supported by sequence data as the maximum likelihood phylogeny. We use a simulation framework for viral transmission and evolution to demonstrate that TreeFix-TP improves phylogenetic accuracy and downstream transmission network accuracy. We also use real data from ten HCV outbreaks and demonstrate how error-correction improves source detection.

**Conclusions**
Our results show that using TreeFix-TP can lead to significant improvement in transmission phylogeny inference and that its performance is robust to variations in transmission and evolutionary parameters. Our experiments also demonstrate the importance of sampling multiple strain sequences from each infected host for accurate transmission network inference. TreeFix-TP is freely available open-source from https://compbio.engr.uconn.edu/software/treefix-tp/.

[Download paper here](https://www.biorxiv.org/content/10.1101/813931v1)

**Recommended citation:** "S. Sledzieski, C. Zhang, I. Mandoiu, and M.S. Bansal. TreeFix-TP: Phylogenetic Error-Correction for Infectious Disease Transmission Network Inference. bioRxiv 813931; doi: https://doi.org/10.1101/813931"