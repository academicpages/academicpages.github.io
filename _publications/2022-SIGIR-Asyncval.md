---
title: "Asyncval: A Toolkit for Asynchronously Validating Dense Retriever Checkpoints during Training"
collection: publications
permalink: /publication/SIGIR2022Asyncval
year: 2022
venue: 'Proceedings of the 45th International ACM SIGIR Conference on Research and Development in Information Retrieval (SIGIR ’22)'
authors: <strong>Shengyao Zhuang</strong>, Guido Zuccon
track: Demo paper
---
---

## Abstract
The process of model checkpoint validation refers to the evaluation of the performance of a model checkpoint executed on a held-out portion of the training data while learning the hyperparameters of the model, and is used to avoid over-fitting and determine when the model has converged so as to stop training.A simple and efficient strategy to validate deep learning checkpoints is the addition of validation loops to execute during training. However, the validation of dense retrievers (DR)  checkpoints is not as trivial -- and the addition of validation loops is not efficient. This is because, in order to accurately evaluate the performance of a DR checkpoint, the whole document corpus needs to be encoded into vectors using the current checkpoint before any actual retrieval operation for checkpoint validation can be performed. This corpus encoding process can be very time-consuming if the document corpus contains millions of documents (e.g., 8.8m for MS MARCO and 21m for Natural Questions). Thus, a naive use of validation loops during training will significantly increase training time. To address this issue, in this demo paper, we propose Asyncval: a Python-based toolkit for efficiently validating DR checkpoints during training. Instead of pausing the training loop for validating DR checkpoints, Asyncval decouples the validation loop from the training loop, uses another GPU to automatically validate new DR checkpoints and thus permits to perform validation  asynchronously from training.  Asyncval also implements a range of different corpus subset sampling strategies for validating DR checkpoints; these strategies allow to further speed up the validation process. We provide an investigation of these methods in terms of their impact on validation time and validation fidelity. Asyncval is made available as an open-source project at https://github.com/ielab/asyncval.

[Download paper here](https://arxiv.org/pdf/2202.12510.pdf)

[Code](https://github.com/ielab/asyncval)
