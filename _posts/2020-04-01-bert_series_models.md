---
title: 'Overview of BERT Series Pre-trained Language Models'
date: 2020-04-01
permalink: /posts/2020/04/bert_series_models/
tags:
  - cool posts
  - category1
  - category2
---
This summary provides an overview of the BERT family of models and their subsequent improvements and variants, including RoBERTa, ALBERT, ELECTRA, and DeBERTa. Each model is discussed in terms of its architectural innovations, training objectives, and empirical performance on benchmark NLP tasks. The document also includes lightweight adaptations like TinyBERT and MobileBERT designed for deployment on edge devices. Through this comparative lens, the article illustrates how the BERT framework has evolved to become more robust, efficient, and adaptable to diverse linguistic and computational settings.

# Overview of BERT Series Pre-trained Language Models

## BERT: Bidirectional Encoder Representations from Transformers  
*Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova. NAACL 2019*  
- **Key Points**:
  - Masked Language Modeling (MLM) + Next Sentence Prediction (NSP) for pretraining
  - Bi-directional transformer encoder
- **Results**: Achieved SOTA on 11 NLP tasks including GLUE, SQuAD v1.1/v2.0, and SWAG

---

## RoBERTa: A Robustly Optimized BERT Pretraining Approach  
*Yinhan Liu et al. arXiv 2019*  
- **Improvements over BERT**:
  - Remove NSP
  - Train longer with more data and larger batches
  - Dynamic MLM masking
- **Results**: Outperformed BERT on multiple benchmarks

---

## ERNIE (Baidu): Enhanced Representation through Knowledge Integration  
*Sun et al. 2019*  
- **Innovation**: Incorporate knowledge masking strategies (e.g., phrase, entity masking)
- **Result**: Better semantic representation and SOTA on multiple Chinese NLP tasks

---

## ERNIE (Tsinghua): Continual Pre-training Framework  
*Zhang et al. 2019*  
- **Idea**: Knowledge masking and multi-task learning with continual learning tasks
- **Result**: Competitive results on a wide range of benchmarks

---

## ALBERT: A Lite BERT  
*Zhenzhong Lan et al. ICLR 2020*  
- **Techniques**:
  - Cross-layer parameter sharing
  - Factorized embedding parameterization
  - Sentence Order Prediction (SOP) instead of NSP
- **Result**: Comparable or better accuracy with far fewer parameters

---

## SpanBERT: Improving Pretraining by Representing and Predicting Spans  
*Mandar Joshi et al. ACL 2020*  
- **Contribution**: Span-level prediction task instead of token-level
- **Advantage**: Improves performance on span-based QA tasks

---

## ELECTRA: Efficiently Learning an Encoder that Classifies Token Replacements Accurately  
*Kevin Clark et al. ICLR 2020*  
- **Method**: Replaces MLM with Replaced Token Detection using a small generator and a discriminator
- **Effect**: More efficient training and better downstream performance

---

## TinyBERT: Distilling BERT for NLU  
*Xiaoqi Jiao et al. 2020*  
- **Contribution**: Layer-wise distillation including embeddings, attention, and logits
- **Result**: 7.5× smaller, 9.4× faster, retains 96% performance

---

## MobileBERT: A Compact Task-Agnostic BERT for Resource-Limited Devices  
*Zhiqing Sun et al. ACL 2020*  
- **Architecture**:
  - Bottleneck structure with inverted bottlenecks
  - Teacher-student distillation from fine-tuned BERT
- **Result**: High efficiency with mobile compatibility

---

## DeBERTa: Decoding-enhanced BERT with Disentangled Attention  
*Pengcheng He et al. ICLR 2021*  
- **Innovation**:
  - Disentangled attention (separates content and position)
  - Enhanced position encoding
- **Results**: Outperformed RoBERTa and BERT on various benchmarks

---

## BERT-wwm: Whole Word Masking  
- **Method**: Masks whole words rather than subwords in MLM
- **Benefit**: More consistent semantic modeling, especially for Chinese

---

## MacBERT: MLM as Correction  
*Yuxian Gu et al.*  
- **Idea**: Replace words with similar words instead of [MASK] during MLM training
- **Result**: Closer to actual fine-tuning scenarios, better performance

---

## StructBERT: Incorporating Word and Sentence Structure  
*Weihao Yu et al.*  
- **Innovation**:
  - Word structural objective: token order prediction
  - Sentence structural objective: sentence order prediction
- **Result**: Enhanced representation of syntactic and sentence structures
------