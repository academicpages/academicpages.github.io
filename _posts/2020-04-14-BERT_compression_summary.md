---
title: 'BERT Model Compression Methods'
date: 2020-04-14
permalink: /posts/2020/04/BERT_compression_summary/
tags:
  - Model Compression
  - Quantization
  - Pruning
---

This document explores various strategies for compressing BERT models to make them more efficient and deployable in resource-constrained environments. It categorizes compression techniques into pruning, quantization, parameter sharing, and knowledge distillation. Each method is reviewed through representative research works such as Q-BERT, ALBERT, DistilBERT, and TinyBERT, highlighting their technical innovations, effectiveness in reducing model size, and trade-offs in performance. The compilation serves as a comprehensive summary of efforts to balance model compactness with high accuracy in natural language understanding tasks.

# BERT Model Compression Methods

## Pruning

Remove less important parameters from the model.

## Quantization

Use fewer bits to represent model parameters (hardware support required).

### Q-BERT: Hessian Based Ultra Low Precision Quantization of BERT  
*Sheng Shen, Zhen Dong, Jiayu Ye, Linjian Ma, Zhewei Yao, Amir Gholami, Michael W. Mahoney, Kurt Keutzer. Preprint.*  
**[pdf]**

- **Contribution**: Mixed-precision quantization and grouped quantization for BERT.
- **Effectiveness**: Achieves a 13× compression rate with only 2% accuracy loss.

### Q8BERT: Quantized 8Bit BERT  
*Ofir Zafrir, Guy Boudoukh, Peter Izsak, Moshe Wasserblat. Preprint.*  
**[pdf]**

- **Contributions**:
  - Symmetric linear quantization
  - Quantization-Aware Training
- **Effectiveness**: Reduces from FP32 to FP8, achieving 4× compression and only 1% accuracy loss.

## Parameter Sharing

Similar model units can share parameters.

### ALBERT: A Lite BERT for Self-supervised Learning of Language Representations  
*Zhenzhong Lan, Mingda Chen, Sebastian Goodman, Kevin Gimpel, Piyush Sharma, Radu Soricut. ICLR 2020.*  
**[pdf] [code & model]**

#### Problem:
- Pre-trained language models are too large:
  - **Memory limitation**: Existing hardware may not fit the model.
  - **Communication overhead**: Too many parameters need to be transmitted during distributed training.
  - **Model degradation**: Increasing hidden size may hurt performance.

#### Contribution:
- Techniques to reduce parameter count:
  - 18× model compression
  - 1.7× acceleration
  - Improved generalization

#### Methods:
- **Factorized embedding parameterization**:  
  Contextual information outweighs the importance of individual tokens, hence H ≫ E. Factorize the embedding matrix (V×H) into two smaller matrices (V×E, E×H).
- **Cross-layer parameter sharing**:  
  Share all parameters (FFN, attention) across layers.
- **Alternative to NSP loss**:  
  Use Sentence Order Prediction (SOP), where adjacent sentence pairs are classified as ordered or reversed.

#### Effectiveness:
Achieves better and deeper BERT variants with fewer parameters, achieving SOTA on RACE, SQUAD, and GLUE.

## Distillation

Train a smaller **student model** to mimic the outputs of a **teacher model**.

### Distilling Task-Specific Knowledge from BERT into Simple Neural Networks  
*Raphael Tang, Yao Lu, Linqing Liu, Lili Mou, Olga Vechtomova, Jimmy Lin. Preprint.*  
**[pdf]**

- **Contribution**:  
  Transfers fine-tuned BERT to a single-layer BiLSTM.
- **Effectiveness**:  
  Performance drops 3–15% (similar to ELMo), but:
  - 100× fewer parameters
  - 15× faster inference

- **Approach**:
  - Teacher: Fine-tuned BERT + classification layer
  - Student: One-layer BiLSTM + softmax
  - Distillation loss:  
    MSE between teacher and student logits + Cross-entropy with ground truth
  - Uses heuristics for data augmentation due to limited labeled data

### Patient Knowledge Distillation for BERT Model Compression  
*Siqi Sun, Yu Cheng, Zhe Gan, Jingjing Liu. EMNLP 2019.*  
**[pdf] [code]**

- **Contribution**:  
  Distillation loss includes teacher’s intermediate outputs.
- **Two strategies**:
  - **PKD-Last**: Learn from the last k layers of teacher
  - **PKD-Skip**: Learn from every k-th layer of teacher

- **Implementation**:
  - Cross-entropy between student prediction and ground truth
  - Cross-entropy between teacher and student distributions
  - MSE for intermediate CLS tokens

- **Findings**:
  - PKD-Skip outperforms PKD-Last
  - 6-layer student is 2× faster; 3-layer is 3.7× faster than the 12-layer teacher

### DistilBERT: A Distilled Version of BERT  
*Victor Sanh, Lysandre Debut, Julien Chaumond, Thomas Wolf. Preprint.*  
**[pdf]**

- **Contribution**:  
  Distills a smaller general-purpose BERT during pretraining
- **Loss components**:
  - MLM loss between student and ground truth
  - Distillation loss (cross-entropy between logits)
  - Cosine distance between hidden states

- **Approach**:
  - Halve the number of layers
  - Layer-wise initialization from teacher

- **Effectiveness**:  
  - 40% fewer parameters
  - 60% faster inference
  - Retains 97% of the performance

### TinyBERT: Distilling BERT for Natural Language Understanding  
*Xiaoqi Jiao, Yichun Yin, Lifeng Shang, Xin Jiang, Xiao Chen, Linlin Li, Fang Wang, Qun Liu. Preprint.*  
**[pdf] [code & model]**

- **Contribution**:
  - **Transformer distillation**: Match BERT outputs at:
    - Embedding layer
    - Hidden states and attention matrices
    - Output logits

- **Two-stage framework**:
  - General distillation: Teacher = pre-trained BERT
  - Task-specific distillation: Teacher = fine-tuned BERT  
    Augments data and then applies loss functions

- **Layer Mapping Strategies**:
  - **Uniform**: Pick n evenly spaced teacher layers → Best performance
  - **Top**: Top n layers
  - **Bottom**: Bottom n layers

- **Effectiveness**:  
  - 7.5× parameter reduction
  - 9.4× speedup
  - Retains 96% of original performance

### Model Compression with Multi-Task Knowledge Distillation for Web-scale QA  
*Ze Yang, Linjun Shou, Ming Gong, Wutao Lin, Daxin Jiang. Preprint.*  
**[pdf]**

- **Contribution**:  
  Multiple teachers → single student
- **Method**:
  - Parallel heads for each teacher output logits
  - Each head learns to match its respective teacher
  - Final prediction: weighted sum of all logits during inference
------