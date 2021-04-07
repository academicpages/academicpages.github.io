---
layout: archive
title: ""
permalink: /research/
author_profile: true
---


{% include base_path %}

# Genetic Interactions

The interplay between genes and environment in human disease remains unclear. We are identifying interactions between genetic factors, lifestyle factors, and medications using massive biobank datasets, with an interest in individualized genetic prediction and modifiable risk factors.

## Statistical methods for discovering interactions

Specialized wearable tracking devices and improvements in biomarker data are being explored, and the hope is that these will deliver a quantum improvement in the availability and accuracy of environmental data. However, gene-environment (GxE) interaction testing suffers from a dimensionality problem when testing for the numerous possible interactions between genome-wide variants and many environmental factors. As a result, efficiently identifying gene-environment (GxE) interactions is an important statistical and computational challenge. 

<p align="center">
<img src='/images/vqtl.png' width='450'>
</p>

To address these difficulties, we are making use of a previously characterized observation that most GxE interactions with large effect size can be revealed as a change in the variance of a quantitative phenotype during a one-SNP-at-a-time genome-wide association study (GWAS). This insight can identify strong GxE interactions associated with a given quantitative trait via a two-step approach. First, we look for genome-wide SNPs that are associated with the variance of the trait, thus identifying what are known as variance quantitative trait loci (vQTLs). Second, we use these vQTLs to screen for potentially strong GxE interactions associated with the same phenotype. Scanning for vQTLs involves just a single test per SNP, so it provides a powerful inroad for discovering genetic interactions by nominating loci as promising candidates for an interaction. 

## Importance of gene-environment interactions in prediction

Polygenic scores are currently based on only marginal additive effects, and our research has identified strong GxE interactions influencing BMI variability. For example, variants in the FTO intron region (the strongest genetic regulators of obesity) are associated with a nearly double BMI increase in low exercise individuals compared to high exercise individuals. Interactions can perturb each individual from the expectation given a single genotype, and the ideal individual prediction would accommodate these interaction effects. An ongoing area is to explore whether polygenic scores that consider interaction effects improve phenotype prediction over polygenic scores that do not consider interaction effects. Simultaneously, we are interested in exploring to what extent polygenic score accuracy varies across sociocultural and lifestyle strata from trait to trait.

## Personalizing treatment regimens for breast cancer prevention

<p align="center">
<img src='/images/medication2.png' width='550'>
</p>

Breast cancer (BC) is the most commonly diagnosed cancer in women, with over 2 million new cases and 600,000 deaths in 2018. While clinical measures for prevention do exist, non-invasive personalized measures for reducing BC risk are limited. Medications are a promising set of modifiable factors, however no previous study has explored whether a range of widely-taken approved drugs modulate BC genetics. Using UK Biobank, we are performing an extensive analysis of the interaction between BC genetic risk factors and medication usage, in an effort to reveal why some medication users experience adverse clinical outcomes or point to potential therapeutic repurposing opportunities for improving “poor” genetic risk.


# Immune infiltration

Infiltrating immune cells are prognostic of cancer progression and a tumor's response to treatment. By using computational approaches in genomic and transcriptomic datasets, we are evaluating immune infiltration across healthy and cancerous tissues in the human body and searching for the major factors that drive individuals' differences.

## An atlas of immune infiltration across healthy human tissues

<p align="center">
<img src='/images/infil.png' width='250'>
</p align="center">

One interesting observation based on histology slides by the GTEx consortium is that healthy tissues harbor infiltrating immune cells, and that there can be large differences in infiltration between samples of a single tissue type. Therefore, in order to understand disease-related infiltration, there is a need to understand the baseline healthy state. By applying cell-type deconvolution algorithms to bulk RNA-seq data in GTEx, we are assessing differences in infiltration across distinct tissues and evaluting the infiltration landscape across the human body. Our results have discovered sex-specific differences and aging-related associations in healthy tissue infiltration.

## Genetic factors associated with infiltration

Genetic determinants are a promising avenue for pinpointing the mechanisms differentiating immune-rich and immune-poor tissues and tumors. By applying genome-wide association study approaches to immune infiltration phenotypes, we aim to identify germline genetic associations, or iQTLs. We have integrated iQTLs with expression QTL and GWAS data to infer the molecular processes driving infiltration, link baseline infiltration to autoimmune disease, and provide insights into potential therapeutic targets for shifting infiltration profiles to something more favorable.

More recently, we are evaluating the role of somatic variation in immune infiltration. After calling somatic mutations from GTEx RNA-seq data, we have found that the total number of somatic mutations (the "burden") correlates in a tissue-specific manner with particular immune cell abundances. Interestingly, there exist several mutations that have stronger associations with infiltration. We are continuing to explore germline-somatic interactions, mutational signatures, and clonal hematopoiesis across healthy and tumor tissues.
