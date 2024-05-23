---
title: "Alzheimer's Disease classification using spontaneous speech"
excerpt: "Developed a machine learning model for the early detection and classification of Alzheimer's
Disease (AD) using spontaneous speech."
collection: portfolio
---


[![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-blue)](https://github.com/ashishjadhav/AD_classification)
## Project Overview
This GitHub project aims to develop a machine learning model for the early detection and classification of Alzheimer's Disease (AD) using spontaneous speech. Alzheimer's Disease is a progressive neurodegenerative disorder that primarily affects memory and cognitive function. Early diagnosis is crucial for timely intervention and better management of the disease. 



## Key Features
- Data Collection:
  The project utilizes the ADReSS 2020 (Alzheimer's Disease Recognition through Spontaneous Speech) dataset for training and evaluation purpose.
In order to gain access to the ADReSS data, you will need to become a member of DementiaBank (https://dementia.talkbank.org/). 
- Feature Extraction: Extracts features from speech data using the eGeMAPSv02 feature set, including acoustic, prosodic, and spectral features, for use in machine learning models.
- Model Training: Implements machine learning models, including LDA, KNN, Decision Tree, and Random Forest, to classify speech data into Alzheimer's and non-Alzheimer's categories.
- Evaluation: Uses accuracy as the primary metric for assessing the performance of classification models.

## Algorithms Implementation
The following machine learning algorithms have been implemented:

- Linear Discriminant Analysis (LDA):
LDA is used for dimensionality reduction and classification, finding the linear combinations of features that best separate classes.
- k-Nearest Neighbors (KNN):
KNN classifies samples based on the majority class of their k-nearest neighbors in the feature space.
- Decision Tree:
A Decision Tree is employed for classification by recursively partitioning the feature space based on the most informative features.
- Random Forest:
Random Forest is an ensemble of Decision Trees, providing a robust and accurate classification by combining the predictions of multiple trees.

## Limitations
Audio data, especially when represented by features such as eGeMAPSv02, can be high-dimensional. Traditional machine learning algorithms struggle and lead to overfitting. Next version of the project will implement neural architecturs to solve this issue.

## Technology Stack

* [Python 3.11.5](https://anaconda.org/anaconda/python/files?sort=basename&sort_order=desc&version=3.11.5)
* [opensmile](https://audeering.github.io/opensmile-python/)
* [scikit-learn](https://scikit-learn.org/stable/)


## Author

Ashish Shivajirao Jadhav - [@ashishjadhav](https://github.com/ashishjadhav)





