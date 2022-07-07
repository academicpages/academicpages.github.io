---
date: 2022-06-22
tags:
- stream
- nn
title: Encoder-decoder models
---

Encoder decoder is a deep neural network architecture that consists of 2 components:
- Encoder: input -> encoder memory (real-valued vector),
- Decoder: encoder memory -> output.
Input is variable length, encoder memory is fixed length.

![Attachments/Pasted image 20220622113403.png](/files/2022-06-22-Encoder-decoder models.md-Pasted image 20220622113403.png)
[9.6. Encoder-Decoder Architecture — Dive into Deep Learning 0.17.5 documentation](https://d2l.ai/chapter_recurrent-modern/encoder-decoder.html)

The encoder and decoder portions can be swapped out.
Sometimes the encoder is initialized with pretrained weights, for example in [CodeBERT](https://github.com/guoday/CodeBERT/blob/master/CodeBERT/code2nl/run.py#L257-L263).

They are often used for Seq2seq tasks such as Neural Machine Translation (NMT).