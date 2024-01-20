---
title: "[Hierarchical Ensemble-based Feature Selection for Time Series Forecasting](https://arxiv.org/abs/2310.17544)"
layout: single  # Specify the layout template (e.g., 'single', 'post', 'default')
collection: publications
excerpt: 'This paper introduces a novel ensemble approach for feature selection based on hierarchical stacking...'
date: 2024-01-20
venue: 'Machine Learning'
citation: 'A. Tumay, M. E. Aydin, A. T. Koc, S. S. Kozat. &quot; Hierarchical Ensemble-based Feature Selection for Time Series Forecasting.&quot; <i>Machine Learning</i>. Submitted, 2023. (doi:10.48550/arXiv.2310.17544)'
---


This paper is about a novel ensemble approach for feature selection based on hierarchical stacking in cases of non-stationarity and a limited number of samples with a large number of features. Our approach exploits the co-dependency between features using a hierarchical structure. Initially, a machine learning model is trained using a subset of features, and then the model's output is updated using another algorithm with the remaining features to minimize the goal. This hierarchical structure allows for flexible depth and feature selection, resembling post-processing techniques in computer vision. By exploiting feature co-dependency hierarchically, our proposed approach overcomes the limitations of traditional feature selection methods and feature importance scores. The effectiveness of the approach is demonstrated on synthetic and real-world datasets, indicating improved accuracy and stability compared to traditional methods and state-of-the-art approaches. The relatively high performance on different datasets proves the scalability and robustness of the hierarchical ensemble-based approach.


