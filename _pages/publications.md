---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

## scBONITA: single-cell Boolean Omics Network Invariant Time Analysis

GitHub repository: [https://github.com/mgp13/scBONITA](https://github.com/mgp13/scBONITA)

- uses scRNA-seq data to infer Boolean regulatory rules for topologically characterized networks
- prioritizes genes based on their impact on signaling
- performs pathway analysis, and
- maps sequenced cells to characteristic signaling states of these networks

### Executable models of immune signaling pathways in HIV-associated atherosclerosis

#### Citation: 

***Palshikar, M. G.***, R. Palli, A. Tyrell, S. Maggirwar, G. Schifitto, M. V. Singh and J. Thakar (2022). "Executable models of immune signaling pathways in HIV-associated atherosclerosis." medRxiv: 2022.2003.2007.22271522.

[Download paper here](https://doi.org/10.1101/2022.03.07.22271522)

#### Abstract:
Atherosclerosis (AS)-associated cardiovascular disease is an important cause of mortality in an aging population of people living with HIV (PLWH). This elevated risk has been attributed to viral infection, anti-retroviral therapy, chronic inflammation, and lifestyle factors. However, rates at which PLWH develop AS vary even after controlling for length of infection, treatment duration, and for lifestyle factors. To investigate the molecular signaling underlying this variation, we sequenced 9368 peripheral blood mononuclear cells (PBMCs) from eight PLWH, four of whom have atherosclerosis (AS+). Additionally, a publicly available dataset of PBMCs from persons before and after HIV infection was used to investigate the effect of acute HIV infection. To characterize dysregulation of pathways rather than just measuring enrichment, we developed the single-cell Boolean Omics Network Invariant Time Analysis (scBONITA) algorithm. scBONITA infers executable dynamic pathway models and performs perturbation analysis to identify high impact genes. These dynamic models are used for pathway analysis and to map sequenced cells to characteristic signaling states (attractor analysis). scBONITA revealed that lipid signaling regulates cell migration into the vascular endothelium in AS+ PLWH. Pathways implicated included AGE-RAGE and PI3K-AKT signaling in CD8+ T cells, and glucagon and cAMP signaling pathways in monocytes. Attractor analysis with scBONITA facilitated pathway-based characterization of cellular states in CD8+ T cells and monocytes. In this manner, we identify critical cell-type specific molecular mechanisms underlying HIV-associated atherosclerosis using a novel computational method.

## WikiNetworks: Python package to process pathways from the WikiPathways database into machine-readable network representations

GitHub repository: [https://github.com/mgp13/WikiNetworks](https://github.com/mgp13/WikiNetworks)

#### Citation:

***Palshikar, M. G.***, S. P. Hilchey, M. S. Zand and J. Thakar (2022). "WikiNetworks: translating manually created biological pathways for topological analysis." Bioinformatics 38(3): 869-871.

[Download paper here](https://doi.org/10.1093/bioinformatics/btab699)

#### Abstract:
WikiPathways is a database of 2979 biological pathways across 31 species created using the drawing software PathVisio. Many of these pathways are not directly usable for network-based topological analyses due to differences in curation styles and drawings. We developed the WikiNetworks package to standardize and construct directed networks by combining geometric information and manual annotations from WikiPathways. WikiNetworks performs significantly better than existing tools. This enables the use of high-quality WikiPathways resource for network-based topological analysis of high-throughput data.

