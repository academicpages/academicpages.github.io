---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---


{% include base_path %}

# Genetic Interactions

The interplay between genes and environment in human disease remains unclear. I am identifying interactions between genetic factors, lifestyle factors, and medications using massive biobank datasets, with an interest in individualized genetic prediction and modifiable risk factors.

## Statistical methods for discovering interactions

Efficiently identifying gene-environment (GxE) interactions remains an important statistical and computational challenge. Specialized wearable tracking devices and improvements in biomarker data are being explored, and the hope is that these will deliver a quantum improvement in the availability and accuracy of environmental data. However, GxE interaction testing suffers from a dimensionality problem when testing for the numerous interactions between genome-wide variants and many environmental factors.

<img src='/images/vqtl.png' height='250'>

To address these difficulties, we make use of a previously characterized observation that most GxE interactions with large effect size can be revealed as a change in the variance of a quantitative phenotype during a one-SNP-at-a-time genome-wide association study (GWAS). This insight lets us identify strong GxE interactions associated with a given quantitative trait via a two-step approach. First, we look for genome-wide SNPs that are associated with the variance of the trait, thus identifying what are known as variance quantitative trait loci (vQTLs). Second, we use these vQTLs to screen for potentially strong GxE interactions associated with the same phenotype. Scanning for vQTLs involves just a single test per SNP, so it provides a powerful inroad for discovering genetic interactions by nominating loci as promising candidates for an interaction. 

## Importance of gene-environment interactions in prediction

Polygenic scores are currently based on only marginal additive effects, and our research has identified strong GxE interactions influencing BMI variability. For example, variants in the FTO intron region (the strongest genetic regulators of obesity) are associated with a nearly double BMI increase in low exercise individuals compared to high exercise individuals. Interactions can perturb each individual from the expectation given a single genotype, and the ideal individual prediction would accommodate these interaction effects. An ongoing area is to explore whether polygenic scores that consider interaction effects improve phenotype prediction over polygenic scores that do not consider interaction effects. Simultaneously, we are interested in exploring to what extent polygenic score accuracy varies across sociocultural and lifestyle strata from trait to trait.

## Personalizing treatment regimens for breast cancer prevention

<img src='/images/medication2.png' width='550'>

Breast cancer (BC) is the most commonly diagnosed cancer in women, with over 2 million new cases and 600,000 deaths in 2018. An individual’s genetics can considerably predispose individuals to be at high BC risk. While clinical measures for prevention do exist, non-invasive personalized measures for reducing BC risk are limited. Medications are a promising set of modifiable factors, however no previous study has explored whether a range of widely-taken approved drugs modulate BC genetics. Using UK Biobank, we are performing an extensive analysis of the interaction between BC genetic risk factors and medication usage, in an effort to reveal why some medication users experience adverse clinical outcomes or point to potential therapeutic repurposing opportunities for improving “poor” genetic risk.


# Immune infiltration

Infiltrating immune cells are prognostic of cancer progression and a tumor's response to treatment. By using computational approaches in genomic and transcriptomic datasets, I am evaluating immune infiltration across healthy and cancerous tissues in the human body and searching for the major factors that drive individuals' differences.

## An atlas of immune infiltration across healthy human tissues

<img src='/images/infil.png' width='250'>"

## Genetic factors associated with infiltration

Bang.

## Role of somatic variation in immune infiltration

Bang.
