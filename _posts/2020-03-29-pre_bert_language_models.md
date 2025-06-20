---
title: 'Evolution of Pre-trained Language Models Before BERT'
date: 2020-03-29
permalink: /posts/2020/03/pre_bert_language_models/
tags:
  - cool posts
  - category1
  - category2
---
This article traces the developmental trajectory of pre-trained language models prior to the emergence of BERT, showcasing how foundational works such as ELMo, ULMFiT, and GPT laid the groundwork for modern NLP advancements. By analyzing the limitations of early RNN-based models and the progressive adoption of contextual embeddings, transfer learning, and transformer architectures, the document highlights the gradual shift toward more generalized and scalable pretraining paradigms. This retrospective provides valuable context for understanding BERT’s breakthrough and its predecessors’ contributions to the field.

# Evolution of Pre-trained Language Models Before BERT

## Semi-supervised Sequence Learning  
*Andrew M. Dai, Quoc V. Le. NIPS 2015* [pdf]  
- **Key Idea**: First to propose pretraining on large-scale unsupervised tasks and fine-tuning on downstream supervised tasks.  
- **Model**: Unidirectional LSTM. Two pretraining tasks (language modeling and auto-encoding) both prove effective.

---

## context2vec: Learning Generic Context Embedding with Bidirectional LSTM  
*Oren Melamud, Jacob Goldberger, Ido Dagan. CoNLL 2016* [pdf] [project]  
- **Key Idea**: Emphasizes contextual information in word representation.  
- **Model**: Builds upon CBOW in word2vec but replaces averaging with BiLSTM to create contextual embeddings. Produces SOTA results in word sense disambiguation and cloze tasks.

---

## Unsupervised Pretraining for Sequence to Sequence Learning  
*Prajit Ramachandran, Peter J. Liu, Quoc V. Le. EMNLP 2017* [pdf]  
- **Problem**: Seq2seq models overfit with small supervised datasets.  
- **Solution**: Prove effectiveness of pretraining with large unsupervised data, then fine-tuning. Suggests joint training with LM and seq2seq objectives.  
- **Model**: Initialize encoder and decoder using two language models. Joint loss for fine-tuning.

---

## ELMo: Deep Contextualized Word Representations  
*Matthew E. Peters et al. NAACL 2018* [pdf] [project]  
- **Key Idea**: Pretrained bidirectional language models outperform unidirectional; multilayer better than single-layer.  
- **Model**: Embeddings from a pretrained BiLSTM. Each word’s vector is a weighted sum of internal layer outputs.  
- **Results**: Boosts performance on many NLP tasks including QA, NLI, SRL, NER, sentiment classification.

---

## ULMFiT: Universal Language Model Fine-tuning for Text Classification  
*Jeremy Howard, Sebastian Ruder. ACL 2018* [pdf] [project]  
- **Pipeline**:  
  1. General-domain LM pretraining  
  2. Target-domain LM fine-tuning  
  3. Task-specific fine-tuning  
- **Tricks**:
  - Vary learning rates across layers (lower in bottom layers)
  - Dynamic LR schedule (fast warm-up then gradual annealing)
  - Sentence representation = last hidden + mean + max pooling
  - Gradual layer unfreezing during fine-tuning
- **Extra Tips**:  
  - Multi-task fine-tuning improves robustness  
  - Combine last few layers' mean/max/concat  
  - For long texts, splice beginning and end instead of truncating to 512 tokens

---

## GPT: Improving Language Understanding by Generative Pre-Training  
*Alec Radford et al. Preprint* [pdf] [project]  
- **Innovation**: Reformulates input format to enable general-purpose pretraining. Breakthrough SOTA in multiple tasks.  
- **Model**:
  - Transformer backbone (better at long-range dependency modeling than RNNs)
  - BPE-based subword vocabulary
  - Joint loss in task training improves generalization, reduces catastrophic forgetting

---

## GPT-2: Language Models are Unsupervised Multitask Learners  
*Alec Radford et al. Preprint* [pdf] [code]  
- **Innovation**: Scaling up model/data enables zero-shot QA, translation, summarization. Fluent and coherent generations.  
- **Model Improvements**:
  - Trained on 40GB filtered text from 45M web links
  - Improved BPE merges to reduce noise
  - Layer norm moved to input; final block adds extra layer norm
  - Hyperparameters:
    - Vocab size +10K
    - Max sequence length: 512 → 1024
    - Batch size: 512

---

## Grover: Defending Against Neural Fake News  
*Rowan Zellers et al. NeurIPS 2019* [pdf] [project]  
- **Contribution**: Unified model for generating and detecting fake news via controllable generation.  
- **Method**:
  - **Generation**: Same structure as GPT-2.  
    Article = fields (domain, date, authors, headline, body), wrapped in special tokens. Pretraining predicts missing fields from known ones.  
    Uses nucleus sampling (top-p = 0.96) instead of beam search.
  - **Detection**:  
    Binary classification (human vs. machine generated).  
    Semi-supervised: many human articles, 10K machine articles.  
    Appends [CLS] at end; corresponding hidden used for classification.
- **Results**:
  - High-quality fake news (rated better than human by humans!)
  - Grover excels at detecting its own fakes
    - Due to exposure bias: trained on human, tested on machine inputs
------