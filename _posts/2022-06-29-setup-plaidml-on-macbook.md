---
title: 'Setup PlaidML on macbook'
date: 2022-06-29
permalink: /posts/2022/06/setup-plaidml-on-macbook
tags:
  - ml
  - macbook
  - tutorial
---

PlaidML은 nvidia GPU를 사용할 수 없을때 deep learning neural network를 빠르게 훈련시키고 추론하는데 사용하는 라이브러리이다. 최근 뉴스로는 macbook m1 chip에서 pytorch, tensorflow등이 GPU로 바로 작동한다고 하는데, 그 이전에 AMD GPU나 Intel GPU등에서 사용할 수 있는 라이브러리이다. 단점으로는 예전 버전의 kera에 연동되어 있는데, 기본적인 공부를 하는데에는 무리없이 사용할 수 있을 것 같다. keras가 처음 머신러닝이 입문하는데 가장 편한 라이브러리 인 것 같다. 

# Installation

```{sh}
pyenv global 2.7.18 3.8.10
pip3 install virtualenv
virtualenv plaidml
source plaidml/bin/activate
pip3 install plaidml-keras plaidbench
plaidml-setup
```

# Benchmarking 

## Using llvm_cpu.0

```{sh}
> plaidbench keras mobilenet

Running 1024 examples with mobilenet, batch size 1, on backend plaid
INFO:plaidml:Opening device "llvm_cpu.0"
Compiling network... Warming up... Running...
Example finished, elapsed: 3.536s (compile), 126.724s (execution)

-----------------------------------------------------------------------------------------
Network Name         Inference Latency         Time / FPS
-----------------------------------------------------------------------------------------
mobilenet            123.75 ms                 120.58 ms / 8.29 fps
Correctness: PASS, max_error: 1.7640328223933466e-05, max_abs_error: 7.040798664093018e-07, fail_ratio: 0.0
```

## Using metal_intel_iris_pro_graphics.0

```{sh}
> plaidbench keras mobilenet

Running 1024 examples with mobilenet, batch size 1, on backend plaid
INFO:plaidml:Opening device "metal_intel_iris_pro_graphics.0"
Compiling network... Warming up... Running...
Example finished, elapsed: 1.878s (compile), 79.834s (execution)

-----------------------------------------------------------------------------------------
Network Name         Inference Latency         Time / FPS
-----------------------------------------------------------------------------------------
mobilenet            77.96 ms                  0.00 ms / 1000000000.00 fps
Correctness: PASS, max_error: 7.6248343248153105e-06, max_abs_error: 2.8312206268310547e-07, fail_ratio: 0.0
```